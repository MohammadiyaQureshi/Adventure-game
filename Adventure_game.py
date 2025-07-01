name=input("Enter your name: ")
print("Welcome",name,"to *Python Adventure Game*")
 
answer = input ("You are on dirt road and it has come to an end, you can go 'left' or 'right'. Which way do you like to go. ").lower()
if answer=="left":
  answer=input("You are on a river ,you can walk around it or swim across it.Type 'walk' to walk around it and 'swim' to swim across it. ")

  if answer=="swim":
   print("You swam across and were eaten by alligator...You lose!")
  elif answer=="walk":
   print("You walked for many miles,ran out of water and you lost the game")
  else:
   print("Not valid! U lose")


elif answer=="right":
 answer=input("You come to a bridge ,it looks woblly,do u want to cross or head back('cross' or 'back')?")
 if answer=="back":
  print("You go back and lose!") 
 elif answer=="cross":
  answer=input("You crossed the bridge and meet a stranger. Do you want to talk him (yes /no)?")

  if answer=="yes":
   print("You talk him and he give you a Gold.")
   print("U WIN")
  elif answer=="no":
   print("You ignored the stranger,he offended ...and U Lose!")
  else:
   print ("Not valid! U lose")

 else:
  print("Not valid! U lose")

else:
      print("Not valid! U lose")  
print("Thanks for trying",name) 