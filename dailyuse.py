#!/usr/bin/env python3

##########################################
#                                        #
#               Imports                  #
#                                        #
##########################################

import mysql.connector
from datetime import datetime

##########################################
#                                        #
#                Functions               #
#                                        #
##########################################

def update_usage():

    #####################################
    #       Connection to Database      #
    #####################################

    cnx = mysql.connector.connect(user='root', password='test',
                              host='127.0.0.1',
                              database='track')
    mycursor = cnx.cursor()

    #####################################
    #          SELECT STATEMENT         #
    #####################################

    mycursor.execute("SELECT * FROM Unit")

    resultU = mycursor.fetchone()

    mycursor.execute("SELECT * FROM Quantity")

    resultQ = mycursor.fetchone()

    #######################################
    # Checking if the Unit Price is empty #
    #######################################

    if (resultU is None):

        print('\nPlease enter your Unit Price (1) first')

    ####################################
    # Checking if the Details is empty #
    ####################################

    elif (resultQ is None):
        print('\nPlease enter your Details of Application (2) first')

    else:

        now = datetime.now()  
        formatted_date = now.strftime("%Y-%m-%d")

        #####################################
        #          SELECT STATEMENT         #
        #####################################

        sql = "SELECT * FROM Dailyuse WHERE date = %s"
        val = (formatted_date)

        mycursor.execute(sql,(val,))

        row = mycursor.fetchone()

        ################################
        #    Checking if Entry exist   #
        ################################

        if(row == None):

            #############################
            #    Entry does not exist   #
            #############################

            print('\nEnter Total Daily Usage in Minutes\n')

            while ( 1 == 1):

                while True:
                    try:
                        washing_m = int(input('\nEnter your total amount of minutes that your Washing Machine taken today: '))
                        break
                    except:
                        print('\nPlease enter only whole numbers\n')

                if (washing_m >= 0):
                    break
                else:
                    print('\nPlease Enter amount greater than or equal to 0\n')

            while ( 1 == 1):

                while True:
                    try:
                        aircon_m = int(input('\nEnter your total amount of minutes spent turning on your Air Condition today: '))
                        break
                    except:
                        print('\nPlease enter only whole numbers\n')

                if (aircon_m >= 0):
                    break
                else:
                    print('\nPlease Enter amount greater than or equal to 0\n')

            while ( 1 == 1):

                while True:
                    try:
                        tv_m = int(input('\nEnter your total amount of minutes spent watching the Television today: '))
                        break
                    except:
                        print('\nPlease enter only whole numbers\n')

                if (tv_m >= 0):
                    break
                else:
                    print('\nPlease Enter amount greater than or equal to 0\n')

            #####################################
            #          Price Calculation        #
            #####################################

            fridge_p = float(resultU[1]) * float(resultQ[3]) * (1440/60) * int(resultQ[1])
            fridge_fp = str(round(fridge_p,2))
            fridge_e = float(resultQ[3]) * (1440/60) * int(resultQ[1])
            fridge_fe = str(round(fridge_e,2))


            tv_p = float(resultU[1]) * float(resultQ[6]) * (float(tv_m) / 60) * int(resultQ[4])
            tv_fp = str(round(tv_p,2))
            tv_e = float(resultQ[6]) * (float(tv_m) / 60) * int(resultQ[4])
            tv_fe = str(round(tv_e,2))

            washing_p = float(resultU[1]) * float(resultQ[9]) * (float(washing_m) / 60) * int(resultQ[7])
            washing_fp = str(round(washing_p,2))
            washing_e = float(resultQ[9]) * (float(washing_m) / 60) * int(resultQ[7])
            washing_fe = str(round(washing_e,2))

            aircon_p = float(resultU[1]) * float(resultQ[12]) * (float(aircon_m) / 60)  * int(resultQ[11])
            aircon_fp = str(round(aircon_p,2))
            aircon_e = float(resultQ[12]) * (float(aircon_m) / 60) * int(resultQ[11])
            aircon_fe = str(round(aircon_e,2))

            total_p = float(fridge_fp) + float(tv_fp) + float(washing_fp) + float(aircon_fp)
            total_fp = str(round(total_p,2)) 

            total_e = float(fridge_fe) + float(tv_fe) + float(washing_fe) + float(aircon_fe)
            total_fe = str(round(total_e,2)) 

            #####################################
            #       Getting Date of Entry       #
            #####################################  
             
            now = datetime.now()  
            formatted_date = now.strftime("%Y-%m-%d")

            #####################################
            #          INSERT STATEMENT         #
            #####################################

            sql = "INSERT INTO Dailyuse (date, fridgeM, fridgeP, tvM, tvP, washingM, washingP, airconM, airconP, totalP, totalE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (formatted_date, 1440, fridge_fp, tv_m, tv_fp, washing_m, washing_fp, aircon_m, aircon_fp, total_fp, total_fe)
            mycursor.execute(sql, val)

            cnx.commit()

            #####################################
            #          SELECT STATEMENT         #
            #####################################

            sql = "SELECT * FROM Dailyuse WHERE date = %s"
            val = (formatted_date)

            mycursor.execute(sql,(val,))

            selected_display_row = mycursor.fetchone()

            #####################################
            #          Printing Summary         #
            #####################################

            print('\n-----------------------------')
            print('Summary for your first Usage')
            print('-----------------------------\n')

            print('Appliances\t\tDuration\t\tEnergy Used(kW)\t\tPrice')
            print('------------------------------------------------------------------------------')

            print('\nFridge\t\t\t ' + selected_display_row[2] + ' Mins\t\t\t' + resultQ[3] +'kW\t\t$'+ selected_display_row[3] +'\n')

            print('\nTelevision\t\t '+ selected_display_row[4] +' Mins\t\t\t' + resultQ[6] + 'kW\t\t$' + selected_display_row[5] +'\n')

            print('\nWashing Machine\t\t ' + selected_display_row[6] + ' Mins\t\t\t' + resultQ[9] + 'kW\t\t$' + selected_display_row[7] + '\n')

            print('\nAir Condition\t\t ' + selected_display_row[8] + ' Mins\t\t\t' + resultQ[12] + 'kW\t\t$' + selected_display_row[9] + '\n')

            print('------------------------------------------------------------------------------\n')

            print('\t\t\t\t\t\t  Subtotal\t\t $' + selected_display_row[10])

            print('------------------------------------------------------------------------------\n')

        #######################
        #     Entry Exist     #
        #######################

        else:

            print('\nYou have already enter your usage today\n')

            while ( 1 == 1):

                while True:
                    try:
                        choice = int(input('\nPlease enter 0 if you wish to edit your entry or enter 1 to go back to menu: '))
                        break
                    except:
                        print('\nPlease enter only whole numbers\n')

                if (choice == 0 or choice == 1):
                    break
                else:
                    print('\nPlease Enter either 0 or 1 only\n')

            if (choice == 0):

                #####################################
                #          SELECT STATEMENT         #
                #####################################

                sql = "SELECT * FROM Dailyuse WHERE date = %s"
                val = (formatted_date)

                mycursor.execute(sql,(val,))

                selected_row = mycursor.fetchone()

                ##################################
                #     Editing existing entry     #
                ##################################

                print('\nCurrently your total time taken for your Washing Machine is ' + selected_row[6] + ' mins\n')

                while ( 1 == 1):

                    while True:
                        try:
                            washing_m = int(input('\nEnter your total amount of minutes that your Washing Machine taken today: '))
                            break
                        except:
                            print('\nPlease enter only whole numbers\n')

                    if (washing_m >= 0):
                        break
                    else:
                        print('\nPlease Enter amount greater than or equal to 0\n')

                print('\nCurrently your total time taken for your Air Conditioner is ' + selected_row[8] + ' mins\n')

                while ( 1 == 1):

                    while True:
                        try:
                            aircon_m = int(input('\nEnter your total amount of minutes spent turning on your Air Condition today: '))
                            break
                        except:
                            print('\nPlease enter only whole numbers\n')

                    if (aircon_m >= 0):
                        break
                    else:
                        print('\nPlease Enter amount greater than or equal to 0\n')

                print('\nCurrently your total time taken for your Television is ' + selected_row[4] + ' mins\n')   

                while ( 1 == 1):

                    while True:
                        try:
                            tv_m = int(input('\nEnter your total amount of minutes spent watching the Television today: '))
                            break
                        except:
                            print('\nPlease enter only whole numbers\n')

                    if (tv_m >= 0):
                        break
                    else:
                        print('\nPlease Enter amount greater than or equal to 0\n') 

                #####################################
                #          Price Calculation        #
                #####################################

                fridge_p = float(resultU[1]) * float(resultQ[3]) * (1440/60) * int(resultQ[1])
                fridge_fp = str(round(fridge_p,2))
                fridge_e = float(resultQ[3]) * (1440/60) * int(resultQ[1])
                fridge_fe = str(round(fridge_e,2))

                tv_p = float(resultU[1]) * float(resultQ[6]) * (float(tv_m) / 60) * int(resultQ[4])
                tv_fp = str(round(tv_p,2))
                tv_e = float(resultQ[6]) * (float(tv_m) / 60) * int(resultQ[4])
                tv_fe = str(round(tv_e,2))

                washing_p = float(resultU[1]) * float(resultQ[9]) * (float(washing_m) / 60) * int(resultQ[7])
                washing_fp = str(round(washing_p,2))
                washing_e = float(resultQ[9]) * (float(washing_m) / 60) * int(resultQ[7])
                washing_fe = str(round(washing_e,2))

                aircon_p = float(resultU[1]) * float(resultQ[12]) * (float(aircon_m) / 60)  * int(resultQ[11])
                aircon_fp = str(round(aircon_p,2))
                aircon_e = float(resultQ[12]) * (float(aircon_m) / 60) * int(resultQ[11])
                aircon_fe = str(round(aircon_e,2))

                total_p = float(fridge_fp) + float(tv_fp) + float(washing_fp) + float(aircon_fp)
                total_fp = str(round(total_p,2)) 

                total_e = float(fridge_fe) + float(tv_fe) + float(washing_fe) + float(aircon_fe)
                total_fe = str(round(total_e,2)) 

                #####################################
                #          UPDATE STATEMENT         #
                #####################################

                sql = "UPDATE Dailyuse SET fridgeM = %s, fridgeP = %s, tvM = %s, tvP = %s, washingM =%s, washingP = %s, airconM = %s, airconP = %s, totalP = %s, totalE = %s WHERE date = %s"
                val = (1440, fridge_fp, tv_m, tv_fp, washing_m, washing_fp, aircon_m, aircon_fp, total_fp, total_fe ,formatted_date)
                mycursor.execute(sql, val)

                cnx.commit()

                #####################################
                #          SELECT STATEMENT         #
                #####################################

                sql = "SELECT * FROM Dailyuse WHERE date = %s"
                val = (formatted_date)

                mycursor.execute(sql,(val,))

                selected_display_row = mycursor.fetchone()

                #####################################
                #          Printing Summary         #
                #####################################

                print('\n-----------------------')
                print('Summary for your Usage')
                print('------------------------\n')

                print('Appliances\t\tDuration\t\tEnergy Used(kW)\t\tPrice')
                print('------------------------------------------------------------------------------')

                print('\nFridge\t\t\t ' + selected_display_row[2] + ' Mins\t\t\t' + resultQ[3] +'kW\t\t$'+ selected_display_row[3] +'\n')

                print('\nTelevision\t\t '+ selected_display_row[4] +' Mins\t\t\t' + resultQ[6] + 'kW\t\t$' + selected_display_row[5] +'\n')

                print('\nWashing Machine\t\t ' + selected_display_row[6] + ' Mins\t\t\t' + resultQ[9] + 'kW\t\t$' + selected_display_row[7] + '\n')

                print('\nAir Condition\t\t ' + selected_display_row[8] + ' Mins\t\t\t' + resultQ[12] + 'kW\t\t$' + selected_display_row[9] + '\n')

                print('------------------------------------------------------------------------------\n')

                print('\t\t\t\t\t\t  Subtotal\t\t $' + selected_display_row[10])

                print('------------------------------------------------------------------------------\n')

    #####################################
    #         Connection Closed         #
    #####################################
    
    mycursor.close()
    cnx.close()