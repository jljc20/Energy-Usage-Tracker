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

def update_desiredSavings():

    this_month_price = 0.0
    this_month_energy = 0.0
    last_month_energy = 0.0
    last_month_price = 0.0


    #####################################
    #       Connection to Database      #
    #####################################

    cnx = mysql.connector.connect(user='root', password='test',
                              host='127.0.0.1',
                              database='track')
    mycursor = cnx.cursor()

    while ( 1 == 1):

        while True:
            try:
                dsavings = int(input('\nEnter your Desired Amount of Savings: $'))
                break
            except:
                print('\nPlease enter only whole numbers\n')

        if (dsavings > 0):
            break
        else:
            print('\nPlease Enter amount greater than 0\n')

    print('\nComparison between your selected month and previous month ...\n')

    while( 1 == 1 ):

        while True:
            try:
                currentYear = int(input('\nEnter the Year that you want to view (>= 2000): '))
                break
            except:
                print('\nPlease enter only whole numbers\n')

        if (currentYear >= 2000):

            while(1 == 1):

                while True:
                    try:
                        currentMonth = int(input('\nEnter the Month that you want to view (1-12): '))
                        break
                    except:
                        print('\nPlease enter only whole numbers\n')

                if (currentMonth <= 0 or currentMonth > 12):
                    print('\nPlease enter Month from 1 - 12')                    

                else:
                    ###############################
                    #    Calculating the months   #
                    ###############################   

                    lastMonth = int(currentMonth) - 1
                    lastMonth_year = currentYear

                    if (lastMonth == 0):
                        lastMonth = 12
                        lastMonth_year = int(currentYear) - 1

                    ####################################
                    #    Retrieving this month usage   #
                    ####################################    

                    sql = ("SELECT totalP, totalE FROM Dailyuse WHERE MONTH(date) = %s and YEAR(date) = %s")
                    val = (currentMonth, currentYear)

                    mycursor.execute(sql, val)

                    resultT = mycursor.fetchall()

                    for i in resultT:
                        this_month_price = this_month_price + float(i[0])
                        this_month_energy = this_month_energy + float(i[1])

                    ####################################
                    #    Retrieving last month usage   #
                    ####################################  

                    sql = ("SELECT totalP, totalE FROM Dailyuse WHERE MONTH(date) = %s and YEAR(date) = %s")
                    val = (lastMonth, lastMonth_year)

                    mycursor.execute(sql, val)

                    resultL = mycursor.fetchall()

                    for i in resultL:
                        last_month_price = last_month_price + float(i[0])
                        last_month_energy = last_month_energy + float(i[1])

                    ####################
                    #    Get savings   #
                    ####################      

                    saving_p = float(last_month_price) - float(this_month_price)
                    saving_fp = str(round(saving_p,2))
                    saving_e = float(last_month_energy) - float(this_month_energy)
                    saving_fe = float(round(saving_e,2))

                    ##########################################
                    #    Retrieving user's Desired Savings   #
                    ##########################################  

                    #####################################
                    #          Printing Summary         #
                    #####################################

                    print('\n-----------------------------')
                    print('Monthly Summary')
                    print('-----------------------------\n')

                    print('Last Month\t\tThis Month\t\tEnergy Saved(kW)\t\tSavings')
                    print('--------------------------------------------------------------------------------------')

                    print('\n' + str(lastMonth) + '/' + str(lastMonth_year) + '\t\t\t ' + str(currentMonth) + '/' + str(currentYear) + '\t\t\t' + str(saving_fe) +'kWH\t\t\t$'+ str(saving_fp) +'\n')

                    print('-------------------------------------------------------------------------------------\n')

                    break

            break
        else:
            print('\nPlease enter Year from 2000 onwards\n')

    #####################################
    #         Connection Closed         #
    #####################################
    
    mycursor.close()
    cnx.close()

