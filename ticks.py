#!/usr/bin/env python3

##########################################
#                                        #
#               Imports                  #
#                                        #
##########################################

import mysql.connector

##########################################
#                                        #
#                Functions               #
#                                        #
##########################################

def update_ticks():

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

    mycursor.execute("SELECT * FROM Quantity")

    result = mycursor.fetchone()

    #####################################
    #    Checking if the row is empty   #
    #####################################

    if (result is None):

        ###############
        #    Fridge   #
        ###############

        print('\nEnter 0 if you not have the appliance')

        while True:
            try:
                fridge_Q = int(input('\nPlease insert the number of Fridge you own: '))
                break
            except:
                print('\nPlease enter only whole numbers\n')

        #####################################
        #         User owns a fridge        #
        #####################################

        if (fridge_Q > 0):

            ###############################################
            #    Loop till user enter the correct range   #
            ###############################################

            while (1 == 1):

                while True:
                    try:
                        fridge_T = int(input('\nEnter your Ticks: '))
                        break
                    except:
                        print('\nPlease enter only whole numbers\n')

                ###################################################
                #   Ensuring that user enters the correct range   #
                ###################################################

                if(fridge_T < 0 or fridge_T > 5):
                    print('\nPlease enter the number from 0-5 only')

                else: 

                    while (1 == 1):

                        while True:
                            try:
                                fridge_E = float(input('\nEnter your Energy Consumption: '))
                                break
                            except:
                                print('\nPlease enter only numbers\n')

                        if(fridge_E > 0):
                            #####################################
                            #          INSERT STATEMENT         #
                            #####################################

                            sql = "INSERT INTO Quantity (fridgeQ, fridgeT, fridgeE) VALUES (%s, %s, %s)"
                            val = (fridge_Q, fridge_T, fridge_E)
                            mycursor.execute(sql, val)

                            cnx.commit()
                            break
                        else:
                            print('\nPlease enter a value greater than 0')
                    break

        #####################################
        #    User doesn't owns a fridge     #
        #####################################

        else: 

            #####################################
            #          INSERT STATEMENT         #
            #####################################

            sql = "INSERT INTO Quantity (fridgeQ, fridgeT, fridgeE) VALUES (%s, %s, %s)"
            val = (0, 0, 0)
            mycursor.execute(sql, val)

            cnx.commit()

        ###################
        #    Television   #
        ###################

        print('\nEnter 0 if you not have the appliance')

        while True:
            try:
                tv_Q = int(input('\nPlease insert the number of Television you own: '))
                break
            except:
                print('\nPlease enter only whole numbers\n')

        #####################################
        #      User owns a Television       #
        #####################################

        if (tv_Q > 0):

            ###############################################
            #    Loop till user enter the correct range   #
            ###############################################

            while (1 == 1):

                while True:
                    try:
                        tv_T = int(input('\nPlease insert the number of Ticks your Television have: '))
                        break
                    except:
                        print('\nPlease enter only whole numbers\n')

                ###################################################
                #   Ensuring that user enters the correct range   #
                ###################################################

                if(tv_T < 0 or tv_T > 5):

                    print('\nPlease enter the number from 0-5 only')

                else: 

                    while (1 == 1):
                        while True:
                            try:
                                tv_E = float(input('\nPlease insert your Television Energy Consumption (kW): '))
                                break
                            except:
                                print('\nPlease enter only numbers\n')

                        if(tv_E > 0):

                            #####################################
                            #          UPDATE STATEMENT         #
                            #####################################

                            sql = "UPDATE Quantity SET tvQ = %s, tvT = %s, tvE = %s WHERE id = %s"
                            val = (tv_Q, tv_T, tv_E, 1)
                            mycursor.execute(sql, val)

                            cnx.commit()
                            break
                        else:
                            print('\nPlease enter a value greater than 0')
                    break 
                

        ######################################
        #    User doesn't owns a Television  #
        ######################################
        else:

            #####################################
            #          UPDATE STATEMENT         #
            #####################################

            sql = "UPDATE Quantity SET tvQ = %s, tvT = %s, tvE = %s WHERE id = %s"
            val = (0, 0, 0, 1)
            mycursor.execute(sql, val)

            cnx.commit()

        ########################
        #    Washing Machine   #
        ########################

        print('\nEnter 0 if you not have the appliance')

        while True:
            try:
                washing_Q = int(input('\nPlease insert the number of Washing Machine you own: '))
                break
            except:
                print('\nPlease enter whole numbers only\n')

        #####################################
        #    User owns a Washing Machine    #
        #####################################

        if (washing_Q > 0):

            ###############################################
            #    Loop till user enter the correct range   #
            ###############################################

            while (1 == 1):

                while True:
                    try:
                        washing_T = int(input('\nPlease insert the number of ticks your Washing Machine have: '))
                        break
                    except:
                        print('\nPlease enter whole numbers only\n')

                ###################################################
                #   Ensuring that user enters the correct range   #
                ###################################################

                if(washing_T < 0 or washing_T > 5):

                    print('\nPlease enter the number from 0-5 only')

                else: 

                    while (1 == 1):
                        while True:
                            try:
                                washing_E = float(input('\nPlease insert your Washing Machine Energy Consumption (kW): '))
                                break
                            except:
                                print('\nPlease enter numbers only\n')

                        if(washing_E > 0):

                            #####################################
                            #          UPDATE STATEMENT         #
                            #####################################

                            sql = "UPDATE Quantity SET washingQ = %s, washingT = %s, washingE = %s WHERE id = %s"
                            val = (washing_Q, washing_T, washing_E, 1)
                            mycursor.execute(sql, val)

                            cnx.commit()
                            break
                        else:
                            print('\nPlease enter a value greater than 0')
                    break 

        #############################################
        #    User doesn't owns a Washing Machine    #
        ############################################# 

        else:

            #####################################
            #          UPDATE STATEMENT         #
            #####################################

            sql = "UPDATE Quantity SET washingQ = %s, washingT = %s, washingE = %s WHERE id = %s"
            val = (0, 0, 0, 1)
            mycursor.execute(sql, val)

            cnx.commit()   

        ######################
        #   Air Conditioner  #
        ######################

        print('\nEnter 0 if you not have the appliance')

        while True:
            try:
                aircon_Q = int(input('\nPlease insert the number of Air Conditioner you own: '))
                break
            except:
                print('\nPlease enter only whole numbers\n')

        if (aircon_Q > 0):

            ###############################################
            #    Loop till user enter the correct range   #
            ###############################################

            while (1 == 1):

                while True:
                    try:
                        aircon_T = int(input('\nPlease insert the number of Ticks your Air Conditioner have: '))
                        break
                    except:
                        print('\nPlease enter whole numbers only\n')


                ###################################################
                #   Ensuring that user enters the correct range   #
                ###################################################

                if(aircon_T < 0 or aircon_T > 5):

                    print('\nPlease enter the number from 0-5 only')

                else: 

                    while (1 == 1):
                        while True:
                            try:
                                aircon_E = float(input('\nPlease insert your Air Conditioner Energy Consumption (kW): '))
                                break
                            except:
                                print('\nPlease enter numbers only\n')

                        if(aircon_E > 0):

                            #####################################
                            #          UPDATE STATEMENT         #
                            #####################################

                            sql = "UPDATE Quantity SET airconQ = %s, airconT = %s, airconE = %s WHERE id = %s"
                            val = (aircon_Q, aircon_T, aircon_E, 1)
                            mycursor.execute(sql, val)

                            cnx.commit()
                            break
                        else:
                            print('\nPlease enter a value greater than 0\n')
                    break 
                

        else:

            #####################################
            #          UPDATE STATEMENT         #
            #####################################

            sql = "UPDATE Quantity SET airconQ = %s, airconT = %s, airconE = %s WHERE id = %s"
            val = (0, 0, 0, 1)
            mycursor.execute(sql, val)

            cnx.commit() 

        print('\nYour details have been updated\n')

    #####################################
    #           Row is not empty        #
    #####################################

    else:

        ####################
        #  Fridge Quantity #
        ####################   

        print('\nEnter -1 to remain same Quantity\n')

        print('You currently own ' + result[1] + ' Fridge\n')
 
        while (1 == 1):

            while True:
                try:
                    fridge_Q = int(input('\nEnter your new Quantity: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            #####################################
            #      Remain Fridge Quantity       #
            #####################################

            if (fridge_Q == -1):
                break

            #####################################
            #     Updating Fridge Quantity      #
            #####################################  

            elif (fridge_Q >= 0):
                sql = "UPDATE Quantity SET fridgeQ = %s WHERE id = %s"
                val = (fridge_Q, 1)
                mycursor.execute(sql, val)

                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount greater than 0\n')


        #################
        #  Fridge Ticks #
        #################   

        print('\nEnter -1 to remain same Ticks\n')

        print('Your Fridge currently have ' + result[2] + ' Ticks\n')
 
        while (1 == 1):

            while True:
                try:
                    fridge_T = int(input('\nEnter your new Ticks: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            ##################################
            #     Updating Fridge Ticks      #
            ##################################  

            if (fridge_T >= 0 and fridge_T < 6):
                sql = "UPDATE Quantity SET fridgeT = %s WHERE id = %s"
                val = (fridge_T, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break

            #################################
            #      Remain Fridge Ticks      #
            #################################

            elif (fridge_T == -1):
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount from 1 - 5\n')


        ##############################
        #  Fridge Energy Consumption #
        ##############################   

        print('\nEnter -1 to remain same Energy Consumption\n')

        print('Currently, your Fridge Energy Consumption is ' + result[3] + ' \n')
 
        while (1 == 1):

            while True:
                try:
                    fridge_E = float(input('\nEnter your new Energy Consumption: '))
                    break
                except:
                    print('\nPlease enter only numbers\n')

            ############################################
            #      Remain Fridge Energy Consumption    #
            ############################################

            if (fridge_E == -1):
                break

            ############################################
            #     Updating Fridge Energy Consumption   #
            ############################################  

            elif (fridge_E > 0):
                sql = "UPDATE Quantity SET fridgeE = %s WHERE id = %s"
                val = (fridge_E, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nEnter amount greater than 0\n')

        ########################
        #  Television Quantity #
        ########################   

        print('\nEnter -1 to remain same Quantity\n')

        print('You currently own ' + result[4] + ' Television\n')
 
        while (1 == 1):

            while True:
                try:
                    tv_Q = int(input('\nEnter your new Quantity: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            #####################################
            #    Remain Television Quantity     #
            #####################################

            if (tv_Q == -1):
                break

            #####################################
            #   Updating Television Quantity    #
            #####################################  

            elif (tv_Q >= 0):
                sql = "UPDATE Quantity SET tvQ = %s WHERE id = %s"
                val = (tv_Q, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount greater than 0\n')


        #####################
        #  Television Ticks #
        #####################   

        print('\nEnter -1 to remain same Ticks\n')

        print('Your Television currently have ' + result[5] + ' Ticks\n')

 
        while (1 == 1):

            while True:
                try:
                    tv_T = int(input('\nEnter your new Ticks: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            ##################################
            #   Updating Television Ticks    #
            ##################################  

            if (tv_T >= 0 and tv_T < 6):
                sql = "UPDATE Quantity SET tvT = %s WHERE id = %s"
                val = (tv_T, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break

            ##################################
            #     Remain Television Ticks    #
            ##################################

            elif (tv_T == -1):
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount from 1 - 5\n')


        ##################################
        #  Television Energy Consumption #
        ##################################   

        print('\nEnter -1 to remain same Energy Consumption\n')

        print('Currently, your Television Energy Consumption is ' + result[6] + ' \n')
 
        while (1 == 1):

            while True:
                try:
                    tv_E = float(input('\nEnter your new Energy Consumption: '))
                    break
                except:
                    print('\nPlease enter only numbers\n')

            ############################################
            #   Remain Television Energy Consumption   #
            ############################################

            if (tv_E == -1):
                break

            ################################################
            #     Updating Television Energy Consumption   #
            ################################################  

            elif (tv_E > 0):
                sql = "UPDATE Quantity SET tvE = %s WHERE id = %s"
                val = (tv_E, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nEnter amount greater than 0\n')

        #############################
        #  Washing Machine Quantity #
        #############################   

        print('\nEnter -1 to remain same Quantity\n')

        print('You currently own ' + result[7] + ' Washing Machine\n')
 
        while (1 == 1):

            while True:
                try:
                    washing_Q = int(input('\nEnter your new Quantity: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            #####################################
            #  Remain Washing Machine Quantity  #
            #####################################

            if (washing_Q == -1):
                break

            #####################################
            # Updating Washing Machine Quantity #
            #####################################  

            elif (washing_Q >= 0):
                sql = "UPDATE Quantity SET washingQ = %s WHERE id = %s"
                val = (washing_Q, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount greater than 0\n')


        ##########################
        #  Washing Machine Ticks #
        ##########################   

        print('\nEnter -1 to remain same Ticks\n')

        print('Your Washing Machine currently have ' + result[8] + ' Ticks\n')
 
        while (1 == 1):

            while True:
                try:
                    washing_T = int(input('\nEnter your new Ticks: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            ####################################
            #  Updating Washing Machine Ticks  #
            ####################################  

            if (washing_T >= 0 and washing_T < 6):
                sql = "UPDATE Quantity SET washingT = %s WHERE id = %s"
                val = (washing_T, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break

            #####################################
            #    Remain Washing Machine Ticks   #
            #####################################

            elif (washing_T == -1):
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount from 1 - 5\n')


        #######################################
        #  Washing Machine Energy Consumption #
        #######################################   

        print('\nEnter -1 to remain same Energy Consumption\n')

        print('Currently, your Washing Machine Energy Consumption is ' + result[9] + ' \n')
 
        while (1 == 1):

            while True:
                try:
                    washing_E = float(input('\nEnter your new Energy Consumption: '))
                    break
                except:
                    print('\nPlease enter only numbers\n')

            ##################################################
            #   Remain Washing Machine Energy Consumption    #
            ##################################################

            if (washing_E == -1):
                break            

            #####################################################
            #     Updating Washing Machine Energy Consumption   #
            #####################################################  

            elif (washing_E > 0):
                sql = "UPDATE Quantity SET washingE = %s WHERE id = %s"
                val = (washing_E, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nEnter amount greater than 0\n')

        #############################
        #  Air Conditioner Quantity #
        #############################   

        print('\nEnter -1 to remain same Quantity\n')

        print('You currently own ' + result[10] + ' Air Conditioner\n')
 
        while (1 == 1):

            while True:
                try:
                    aircon_Q = int(input('\nEnter your new Quantity: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            #####################################
            #  Remain Air Conditioner Quantity  #
            #####################################

            if (aircon_Q == -1):
                break

            #####################################
            #     Updating Fridge Quantity      #
            #####################################  

            elif (aircon_Q >= 0):
                sql = "UPDATE Quantity SET airconQ = %s WHERE id = %s"
                val = (aircon_Q, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount greater than 0\n')


        ##########################
        #  Air Conditioner Ticks #
        ##########################   

        print('\nEnter -1 to remain same Ticks\n')

        print('Your Air Conditioner currently have ' + result[11] + ' Ticks\n')
 
        while (1 == 1):

            while True:
                try:
                    aircon_T = int(input('\nEnter your new Ticks: '))
                    break
                except:
                    print('\nPlease enter only whole numbers\n')

            ##################################
            # Updating Air Conditioner Ticks #
            ##################################  

            if (aircon_T >= 0 and aircon_T < 6):
                sql = "UPDATE Quantity SET airconT = %s WHERE id = %s"
                val = (aircon_T, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break

            #####################################
            #   Remain Air Conditioner Ticks    #
            #####################################

            elif (aircon_T == -1):
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nPlease enter amount from 1 - 5\n')


        #######################################
        #  Air Conditioner Energy Consumption #
        #######################################   

        print('\nEnter -1 to remain same Energy Consumption\n')

        print('Currently, your Air Conditioner Energy Consumption is ' + result[12] + ' \n')
 
        while (1 == 1):

            while True:
                try:
                    aircon_E = float(input('\nEnter your new Energy Consumption: '))
                    break
                except:
                    print('\nPlease enter only numbers\n')

            ##############################################
            #  Remain Air Conditioner Energy Consumption #
            ##############################################

            if (aircon_E == -1):
                break

            ################################################
            #  Updating Air Conditioner Energy Consumption #
            ################################################  

            elif (aircon_E > 0):
                sql = "UPDATE Quantity SET airconE = %s WHERE id = %s"
                val = (aircon_E, 1)
                mycursor.execute(sql, val)
                cnx.commit()
                break
            
            ######################
            #    Error Checking  #
            ######################

            else:
                print('\nEnter amount greater than 0\n')

        print('\nYour Details have been updated\n')

    #####################################
    #         Connection Closed         #
    #####################################
    
    mycursor.close()
    cnx.close()
