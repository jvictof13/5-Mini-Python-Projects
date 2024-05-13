name = input("Type your name: ")
print("Welcome", name, "to this adventure! ")

answser = input("You are on a dirty road, it has come to an end and you can go left or right which way would you like to go? ").lower()

if answser == "left":
   answser = input("You've reached a river, and you can walk around it or swim accross! Type walk to walk around it or type swim to swim accross it: ")
   if answser == "swim":
     print("You've swam accross and got eaten by an alligator! You've lost")
   elif answser == "walk":
     print("You've walk for many miles and ran out of water! You've lost")
   else:
     print("Not a valid option, you lose! ")

elif answser == "right":
   answser = input("You've come to a bridge and it looks kinda wobbly. Would you like to cross, or head back?  ")
   if answser == "head back":
     print("You were heading back to the river and got lost!")
   elif answser == "cross":
     answser = input("You've crossed the bridge and met a stranger. Would you like to talk to him or run away?  ")
     if answser == "talk to him":
      print("The stranger smiles at you and gave you a diamond. Congratulations you've won!")
     elif answser == "run away":
      print("You've ran away and fell off a cliff. You've lost!")
     else:
      print("Not a valid option, you lose! ")

   else:
     print("Not a valid option, you lose! ")
else:
 print("Not a valid option, you lose! ")

print("Thank you for playing", name, "!")


