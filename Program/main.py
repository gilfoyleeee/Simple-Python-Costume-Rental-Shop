# importing all necessary packages and function python file
import function
import time
from tqdm import tqdm
  
# loading bar from tqdm module  
for i in tqdm (range (100), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
print("Done.")

# calling intro function
function.intro()
# calling menuOptions function
function.menuOptions()
while True:
   print()
   time.sleep(2)
   try: 
      # creating variable to assign option choosed by user
      userOption = int(input("Please choose any option >>> "))
      if userOption == 1:
         # calling displayCostume functionn
         function.displayCostume()
         function.menuOptions()
      elif userOption == 2:
          # calling rentCostume function
         function.rentCostume()
      elif userOption == 3:
          # calling returnCostume function
         function.returnCostume()
      elif userOption == 4:
         print('*'*43,"Thank you for visiting us ! Have a great day !",'*'*43)
         break
      else:
          print("Sorry, you choose incorrect option !")
   except :
      print()
      print('>'*5,"Sorry, You choose invalid option !", '<'*5)
      print("Please Enter Again !")
