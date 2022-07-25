#!/usr/bin/env python3

##########################################
#                                        #
#            Initialization              #
#                                        #
##########################################

check = 0

##########################################
#                                        #
#                Imports                 #
#                                        #
##########################################

from unit import update_unit
from ticks import update_ticks
from dailyuse import update_usage
from desiredsavings import update_desiredSavings
from exit import exit

##########################################
#                                        #
#      While loop until user exit (7)    #
#                                        #
##########################################

while (1 == 1):

    #####################################
    #    Check when user press 'exit'   #
    #####################################

    if (check == 1):
        break

    #############
    #    Menu   #
    #############
    
    print('\n------------------------------------------------------------------------')
    print('1. Enter/Update your Eletricity Unit Price')
    print('2. Enter/Update your Details of your Appliances (Ticks, Quantity and Energy [kW])')
    print('3. Enter/Update your Daily usage')
    print('4. Enter/Update/View Electricity & savings')
    print('5. Exit Program')
    print('------------------------------------------------------------------------\n')

    #####################################
    #    while loop to ensure 1-5 only  #
    #####################################

    while(1 == 1):

        option = input('Select your number: ')

        if (option == '1'):
            update_unit()
            break
        elif (option == '2'):
            update_ticks()
            break
        elif (option == '3'):
            update_usage()
            break
        elif (option == '4'):
            update_desiredSavings()
            break
        elif (option == '5'):
            exit()
            check = 1
            break
        else: 
            print("\nPlease enter number 1-5 only\n")