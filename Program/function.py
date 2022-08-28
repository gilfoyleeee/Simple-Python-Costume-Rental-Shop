#importing all necessary packages of python library
from tabulate import tabulate
from datetime import date
from datetime import datetime
from random import gammavariate
import time
from tqdm import tqdm
#variable currentdate is created for invoice name uniqueness
currentDate = time.strftime("%Y%m%d-%H%M%S")
#delayProgram variable is created to delay the program 
delayProgram = time.sleep(1.5)

#Function intro is created for introduction part of Costume Rental Shop
def intro():
    print()
    print('*'*135)
    print('*'*49,"Welcome to my Costume Rental Shop !", '*'*49)
    print('*'*135)
    
#Function menuOptions is created for providing the options after intro
def menuOptions():
    print(""" 
        Here are the options available for you !
        1) Display available custome
        2)Rent Costume
        3)Return Costume
        4)Exit
        
        >>>Hope you have a good time !<<< 
    """)

#Function displayCostume is created to display the data of costumeFile text file with table format
def displayCostume():
    costumeFileRead = open('costumeFile.txt','r').readlines()
    print()
    print()
    print('>'*18,"List of Costume Details", '<'*18)
    print()

    costumeList = []
    tableDatas = []
    for i in costumeFileRead:
        costumeDetails = i.rstrip('\n').split(',')
        costumeList.append(costumeDetails)
    for j in range(len(costumeList)):
        idOfItem = j + 1
        customerName = costumeList[j][0]
        costumecostumeBrand = costumeList[j][1]
        costumePrice = costumeList[j][2]
        costumeQuantity = costumeList[j][3]
        
        insideData = [idOfItem,customerName,costumecostumeBrand,costumePrice,costumeQuantity]
        tableDatas.append(insideData)
        nameOfHeaders = ['ID','costume name','costume Brand','custome price',' custome quantity']
        #Using tabulate for displaying the costumes//
    table = tabulate(tableDatas,headers=nameOfHeaders,tablefmt='pipe',showindex=False)
    print(table)
    print()
    print()
    

#Function rentcostume is created to rent out the available costume
def rentCostume():
    # making variable assigning the current date 
    costumeFileRead = open('costumeFile.txt','r').readlines()
    costumeIDlist = []
    costumeList = []
    for line in costumeFileRead:
        list = line.rstrip('\n').split(',')
        costumeList.append(list)  
    for i in range(1,len(costumeList)+1):
        costumeIDlist.append(i) 
    #creating while loop for renting
    nameLoop = True
    while nameLoop: 
        print()
        # loading bar from tqdm module  
        for i in tqdm (range (100), 
                       desc="Entering in Renting Panel…", 
                       ascii=False, ncols=75):
            time.sleep(0.01)
        print()
        print('>'*15,"Welcome to Renting panel",'<'*15)
        print()
        customerName = input("Enter Your Name>>> ")
        #Exception handling using try and catch for CostumeID
        try:
            idLoop = True
            while idLoop:
                while True:
                    displayCostume()
                    print()
                    costumeID = int(input('Enter the costumeID of your chosen custome: '))
                    if costumeID not in costumeIDlist:
                        print()
                        print("Hell Noo ! You input the invalid CostumeID\n")
                    else:
                        print()
                        break
                a = True      
                while a:
                        #Exception handling for Quantity of the costume
                        try:
                            quantityLoop = True
                            while quantityLoop:
                                
                                costumeQuantity = int(input('Enter the quantity of the custome >>> '))
                                if costumeQuantity <=0:
                                    print()
                                    print('Costume Quantity must be greater than 0 !')
                                    print()
                                else:
                                    quantityLoop = False
                            for i in range(len(costumeList)): 
                                costumeName = costumeList[i][0]
                                costumeBrand = costumeList[i][1]
                                costumePrice = costumeList[i][2]
                                strPrice = str(costumePrice)
                                priceInFloat = float(strPrice.strip('$ '))
                                costumeQuantityAvailable = int(costumeList[i][3])
                                delayProgram
                                #using if clause for costumeID
                                if costumeID == i+1 :
                                    #using if clause for checking the availability of costume quantity
                                    if costumeQuantityAvailable < costumeQuantity: 
                                        print()
                                        print('>'*5, "Unfortunately, your chosen costume quantity isn't available recently !", '<'*5)
                                        print()
                                    else:
                                        remCostumeQuantity = costumeQuantityAvailable-costumeQuantity 
                                        print()
                                        # creating a function for generating invoice for renting costumes
                                        def rentInvoice(noOfCostumes):
                                            shopName = "Kushal Costume Rental Shop"
                                            shopAddress = "Belbari-03, Morang"
                                            shopEmail = "kusCostumeRental@gmail.com"
                                            message = "Thanks for visiting us"
                                            #Generating new file for invoice of Rented costume
                                            with open('rentInvoice\\'+customerName+'_Rent_Invoice_'+currentDate+'.txt','w') as rentInvoiceFile:
                                                rentInvoiceFile.write(f""" 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Rent Invoice for {customerName}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        
       Shop Name: {shopName}         Email Address : {shopEmail}                                  
       Shop Address: {shopAddress}              Date of Rent : {date.today()}                     
                                                                                                  
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Customer and Costume Details<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
                                                                                                  
                Costumer's Name             : {customerName}                                       
                Costume                     : {costumeName}                                       
                costumeBrand                : {costumeBrand}                                      
                Total Renting Days          : 5 days                                              
                Total no. of costume rented : {noOfCostumes}                                      
                Total Price                 : ${noOfCostumes*priceInFloat}                        
                                                                                                  
                Note : $100 will be extra fine charge if you delay the returning of Costume.      
                                                                                                  
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{message}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                """)
                                                rentInvoiceFile.close()
                
                                            print()
                                            # loading bar from tqdm module  
                                            for i in tqdm (range (100), 
                                                           desc="Renting your Costume…", 
                                                           ascii=False, ncols=75):
                                                time.sleep(0.01)
                                            print()
                                            print("Costume successfully rented ! Please check your invoice for details !")
                                            print()
                                        # calling rentInvoice for generating INvoice
                                        rentInvoice(costumeQuantity)
                                        # calling alterCostumeQuantity function to alter the quantity in costume costumeFileRead
                                        alterCostumeQuantity(costumeID,remCostumeQuantity) 
                                
                                        delayProgram
                                        # asking user if they want to rent more
                                        rentMoreLoop = True
                                        while rentMoreLoop:
                                            rentMore = input('Do you want to rent more ? ( y/n ) : \n>>>')
                                            print()
                                            if rentMore == 'y' or rentMore == 'Y' :
                                                x = True
                                                while x:
                                                    # exception handling for quantity of costume when renting more
                                                    try:
                                                            delayProgram
                                                            quantityLoop2 = True
                                                            while quantityLoop2:
                                                                cosQuanForRentMore = int(input('Enter the quantity of costume >>> '))
                                                                if cosQuanForRentMore <= 0:
                                                                    print('Costume quantity must be greater than 0')
                                                                else:
                                                                    quantityLoop2 = False
                                                            print()
                                                            #checking the availability of quantity of costume
                                                            if cosQuanForRentMore > remCostumeQuantity:
                                                                if remCostumeQuantity == 0:
                                                                    delayProgram
                                                                    print('>'*8,'Sorry, your chosen custome is unavilable recently !','<'*8)
                                                                    print()
                                                                    delayProgram
                                                                    print()

                                                                    # calling Function menuOptions
                                                                    menuOptions()
                                                                    x = False
                                                                    a = False
                                                                    idLoop = False
                                                                    nameLoop = False
                                                                else:
                                                                    delayProgram
                                                                    print('>'*8,f'Sorry, we only have {remCostumeQuantity} available of your chosen costume recently !','<'*8)
                                                                    print()
                                                            else:
                                                                print()
                                                                costumeQuantity2 = costumeQuantity + cosQuanForRentMore
                                                                # calling rentInvoice function and passing parameter "costumeQuantity2"
                                                                rentInvoice(costumeQuantity2)
                                                                costumeQuantityAvailable2 = costumeQuantityAvailable-costumeQuantity2
                                                                delayProgram
                                                                # calling Function menuOptions
                                                                menuOptions()
                                                                #calling Function alterCostumeQuantity to change the quantity of costume in text file
                                                                alterCostumeQuantity(costumeID,costumeQuantityAvailable2)
                                                                l = False
                                                                x = False
                                                                a = False
                                                                idLoop = False
                                                                nameLoop = False
                                                    except:
                                                        print()
                                                        delayProgram
                                                        print('Invalid quantity of Costume !')
                                                        print()
                                                rentMoreLoop = False       
                                            elif rentMore == 'n' or rentMore =='N':
                                                delayProgram
                                                menuOptions()  
                                                a = False
                                                rentMoreLoop = False
                                                idLoop = False
                                                nameLoop = False
                                            else :
                                                delayProgram
                                                print('Invalid answer ! ')
                                                print()
                                                x = False

                        except:
                            print()
                            delayProgram
                            print('Invalid Costume Quantity !')
                            print()
                            break
        
        except:
            print()
            delayProgram
            print('Please enter the valid Costume ID !')
            print()
    
#Creating function returnCostume for returning the costume available in the shop
def returnCostume():
    #Reading text file to store costume and costume id in seperate lists
    costumeFileRead = open('costumeFile.txt','r').readlines()
    costumeIDlist = []
    costumeList = []
    for line in costumeFileRead:
        list = line.rstrip('\n').split(',')
        costumeList.append(list)  
    for i in range(1,len(costumeList)+1):
        costumeIDlist.append(i) 
    
    print()
    # loading bar from tqdm module  
    for i in tqdm (range (100), 
                   desc="Entering in Returning Panel…", 
                   ascii=False, ncols=75):
        time.sleep(0.01)
    print()
    print('>'*8,"Welcome to Returning Panel",'<'*8)
    print()
    customerName = input("Please enter your Name >>> ")
    print()
    dateOfRent = input('Enter Date of Rent in form of Y-M-D >>> ')
    print()
    dateOfReturn = date.today()
    costumeDetail = []
    with open("costumeFile.txt", 'r') as costumeFileRead:
        costumeDetails = costumeFileRead.read().splitlines()
        for i in range(len(costumeDetails)):
            costumeDetail = costumeDetail + [costumeDetails[i].split(", ")]
        costumeDetails = costumeFileRead.readlines()
    costumeFileRead.close()

    #exception handling for Costume ID
    try:
        displayCostume()
        customeID = int(input("Enter the costumeID of the costume  >>> "))
        print()
        if customeID not in costumeIDlist:
            print('Costume ID is invalid !')
            return returnCostume()
        else:
            #Exception handling for quantity of the costume
            try:
                returnLoop = True
                while returnLoop:
                    
                    customeQuantity = int(input("Enter the quantity of the Costume >>> "))
                    print()
                    if customeQuantity <= 0 :
                        print()
                        print('Costume quantity must be greater than 0 !')
                    else:
                        returnLoop = False
                splittedDOR = dateOfRent.split('-')
                dateOfRent2 = date(int(splittedDOR[0]),int(splittedDOR[1]),int(splittedDOR[2]))
                rentingDays = (dateOfReturn - dateOfRent2).days
                fine = checkingDays(rentingDays)
                if dateOfRent2>dateOfReturn :
                    print()
                    print('Please enter valid date !')
                    return returnCostume
                else:
                    for i in range(len(costumeList)): 
                            costumeName = costumeList[i][0]
                            costumeBrand = costumeList[i][1]
                            costumePrice = costumeList[i][2]
                            strPrice = str(costumePrice)
                            priceInFloat = float(strPrice.strip('$ '))
                            costumeQuantityAvailable = int(costumeList[i][3])
                            delayProgram
                            if customeID == i+1 :
                                newCustomeQuantity = costumeQuantityAvailable+customeQuantity
                                print()
                                # creating a function for generating invoice for renting costumes
                                def returnInvoice(noOfCostumes):
                                    amount = str((customeQuantity*priceInFloat)+ fine)
                                    shopName = "Kushal Costume Rental Shop"
                                    shopAddress = "Belbari-03, Morang"
                                    shopEmail = "kusCostumeRental@gmai.com"
                                    message = "Thanks for visiting us"
                                    with open('returnInvoice\\'+customerName+'_Return_Invoice_'+currentDate+'.txt','w') as returnInvoiceFile:
                                        returnInvoiceFile.write(f""" 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Return Invoice for {customerName}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

   Shop Name: {shopName}           Shop Email: {shopEmail}
   Shop Address: {shopAddress}               Date of Rent: {date.today()}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Customer and Costume Details<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        Costumer's Name             : {customerName} 
        Costume                     : {costumeName}
        costumeBrand                : {costumeBrand}
        Total renting Days          : {rentingDays}
        Total costume returned      : {noOfCostumes}
        Total Price                 : ${amount}

        Note : $100 will be extra fine charge if you delay the returning of Costume.
        
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{message}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                        """)
                                        returnInvoiceFile.close()
        
                                    print()
                                    delayProgram
                                    # loading bar from tqdm module  
                                    for i in tqdm (range (100), 
                                                   desc="Returning the Costume…", 
                                                   ascii=False, ncols=75):
                                        time.sleep(0.01)
                                    print()
                                    print("Costume successfully returned ! Please check your invoice for details !.")
                                    
                                # calling rentInvoice for generating INvoice
                                returnInvoice(customeQuantity)
                                # calling alterCostumeQuantity function to alter the quantity in costume costumeFileRead
                                alterCostumeQuantity(customeID,newCustomeQuantity) 
                                menuOptions()
    
                    
    
            except :
                print("Please input the valid customeQuantity number again !")
                return returnCostume()



    except :
        print("You type invalid customeID, type correct again")
        return returnCostume()

#function created to change the quantity of costume in costumefile text file
def alterCostumeQuantity(costumeID,finalCostumeQuantity):
    costumeFileRead = open('costumeFile.txt','r').readlines() 
    costumeList = []
    for line in costumeFileRead:
        list = line.rstrip('\n').split(',')
        costumeList.append(list)
    for i in range(len(costumeList)):
        costumeFileRead[costumeID-1] = costumeFileRead[costumeID-1].replace(costumeList[i][3],str(f' {finalCostumeQuantity}'))
        file4 = open('costumeFile.txt','w')
        file4.writelines(costumeFileRead)
        file4.close()
#FUnction created to check the days when returning the costume if it is delay or not     
def checkingDays(days):
    fine = 0
    if days> 5:
        fine = int(100)
    else:
        fine = 0
    return fine
