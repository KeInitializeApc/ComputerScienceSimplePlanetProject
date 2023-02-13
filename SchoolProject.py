import os
import math
from time import sleep

#Mercury - Weight on earth * 0.38
#Venus - Weight on earth * 0.91
#Mars - Weight on earth * 0.38
#Jupiter - Weight on earth * 2.53
#Saturn - Weight on earth * 1.07
#Uranus - Weight on earth * 0.89
#Neptune - Weight on earth * 1.10


print("THE POINT OF THIS PROGRAM IS TO CONVERT A WEIGHT IN LBS FROM EARTH TO ANOTHER PLANET IN OUR SOLAR SYSTEM! \n\n ANYWAYS LETS CONTINUE!\n\n")

##TAKES AN INPUT TO SELECT AN OPTION
option = input(" [1] Convert Weight From Earth To A Single Planet \n\n [2] Convert Weight From Earth To All Planets In Solar System \n\nInput >")

## GETS THE OPTION VARIABLE AND CHECKS IF ITS EQUAL TO THE SELECTION OF ONE
if (option == "1"):

    ## CALCULATES ONLY THE PLANET SELECTED!
    planet_selection = input("Please select a planet in our solar system >")

    if (planet_selection == "Mercury" or planet_selection == "mercury"):
      Mercury_Input = float(input("\n\n" + "Please Enter Your Weight On Earth > "))
      print("\n\n Mercury > ", Mercury_Input * 0.38, " LBS \n")
      print("\n\n CLOSING PROGRAM IN 30 SECONDS")
      sleep(30)

    elif (planet_selection == "Venus" or planet_selection == "venus"):
        Venus_Input = float(input("\n\n" + "Please Enter Your Weight On Earth > "))
        print("\n\n Venus > ", Venus_Input * 0.91, " LBS \n")
        print("\n\n CLOSING PROGRAM IN 30 SECONDS")
        sleep(30)
   
    elif (planet_selection == "Mars" or planet_selection == "mars"):
        Mars_Input  = float(input("\n\n" + "Please Enter Your Weight On Earth > "))
        print("\n\n Mars > ", Mars_Input * 0.38, " LBS \n")
        print("\n\n CLOSING PROGRAM IN 30 SECONDS")
        sleep(30)

    elif (planet_selection == "Jupiter" or planet_selection == "jupiter"):
        Jupiter_Input  = float(input("\n\n" + "Please Enter Your Weight On Earth > "))
        print("\n\n Jupiter > ", Jupiter_Input * 2.53, " LBS \n")
        print("\n\n CLOSING PROGRAM IN 30 SECONDS")
        sleep(30)

    elif (planet_selection == "Saturn" or planet_selection == "saturn"):
        Saturn_Input  = float(input("\n\n" + "Please Enter Your Weight On Earth > "))
        print("\n\n Saturn > ", Saturn_Input * 1.07, " LBS \n") 
        print("\n\n CLOSING PROGRAM IN 30 SECONDS")
        sleep(30)

    elif (planet_selection == "Uranus" or planet_selection == "uranus"):
        Uranus_Input  = float(input("\n\n" + "Please Enter Your Weight On Earth > "))
        print("\n\n Uranus > ", Uranus_Input * 0.89, " LBS \n") 
        print("\n\n CLOSING PROGRAM IN 30 SECONDS")
        sleep(30)

    elif (planet_selection == "Neptune" or planet_selection == "neptune"):
        Neptune_Input = float(input("\n\n" + "Please Enter Your Weight On Earth > "))
        print("\n\n Neptune > ", Neptune_Input * 1.10, " LBS \n")
        print("\n\n CLOSING PROGRAM IN 30 SECONDS")
        sleep(30)
    else:
         print("Invalid Selection Please Try Again!")
         ## GETS THE OPTION VARIABLE AND CHECKS IF ITS EQUAL TO THE SELECTION OF TWO
elif (option == "2"):
    ##TAKES AN INPUT
    All_Input  = float(input("\n\n Please Enter Your Weight On Earth >"))
    print("\n\n Calculating Weight On All Planets...\n\n")
    sleep(2)
         #ALL THESE PRINTS BELOW ARE CALCULATING FROM LBS ON EARTH TO ANOTHER PLANET IN OUR SOLAR SYSTEM!

    print("EARTH'S WEIGHT > ", All_Input, "\n\n\n")
    print("PLANET   |  WEIGHT")
    print("===============================")
    print("Mercury > ", All_Input * 0.38, " LBS \n")## Earth To Mercury Weight Conversion In LBS | Mercury
    print("Venus > ",All_Input * 0.91, " LBS \n")## Earth To Venus Weight Conversion In LBS   | Venus
    print("Mars > ",All_Input * 0.38, " LBS \n")## Earth To Mars Weight Conversion In LBS    | Mars
    print("Jupiter > ",All_Input * 2.53, " LBS \n")## Earth To Jupiter Weight Conversion In LBS | Jupiter
    print("Saturn > ",All_Input * 1.07, " LBS \n") ## Earth To Saturn Weight Conversion In LBS | Saturn
    print("Uranus > ",All_Input * 0.89, " LBS \n") ## Earth To Uranus Weight Conversion In LBS | Uranus
    print("Neptune > ",All_Input * 1.10, " LBS \n\n\n\n\n")## Earth To Neptune Weight Conversion In LBS| Neptune
    print("\n\n CLOSING PROGRAM IN 30 SECONDS")
    sleep(30)
else:
    print("Invalid selection please restart the program and try again!")
    print("\n\n CLOSING PROGRAM IN 5 SECONDS")
    sleep(5)

