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

def update_unit():

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

    result = mycursor.fetchone()

    #####################################
    #    Checking if the row is empty   #
    #####################################

    if (result is None):

        while True:
            try:
                electricity_unit = float(input('\nPlease insert your Electricity Unit Price: $'))
                break
            except:
                print('\nPlease enter only numbers\n')

        #####################################
        #          INSERT STATEMENT         #
        #####################################

        sql = "INSERT INTO Unit (electricity) VALUES (%s)"
        val = (electricity_unit)
        mycursor.execute(sql, (val,))

        cnx.commit()

        print('\nYour Electricity Unit Price have been updated')

    else:

        print('\nEnter 0 to remain the current price\n')

        print('Your current Electricity Unit Price is $' + result[1] + '\n')

        #####################################
        #          UPDATE STATEMENT         #
        #####################################
        while (1 == 1):
            
            while True:
                try:
                    electricity_unit = float(input('\nPlease insert your Electricity Unit Price: $'))
                    break
                except:
                    print('\nPlease enter only numbers\n')

            if (electricity_unit > 0):
                sql = "UPDATE Unit SET electricity = %s WHERE id = %s"
                val = [electricity_unit,1]

                mycursor.execute(sql,val)

                cnx.commit()
                print('\nYour Electricity Unit Price have been updated\n')
                break
            elif (electricity_unit == 0):
                print('\nNothing is changed\n')
                break
            else:
                print('\nPlease enter number above 0')

    #####################################
    #         Connection Closed         #
    #####################################
    
    mycursor.close()
    cnx.close()
