print("Rock PaperScissors Game")
user1=input("User1 enter name:")
user2=input("User2 enter name:")
user1_favfood=input("Enter User1 favourite food and  eat:")
user2_favfood=input("Enter User2 favourite food and  eat:")
while True:
  print("food items are:")
  print("1.Burger")
  print("2.Pizza")
  print("3.Cake")
  print("4.Custurd")
  print("5.Pasta")
 
  print("Game start")
  user1_turn=input("user1 enter rock,paper,scissor:")
  user2_turn=input("user2 enter rock,paper,scissor:")
  if user1_turn=="rock"and user2_turn=="Scissor":
    print(user1,"wins and eats",user1_favfood)
  elif user1_turn=="paper"and user2_turn=="rock":
    print(user1,"wins and eats",user1_favfood)
  elif user1_turn=="scissor"and user2_turn=="paper":
    print(user1,"wins and eats",user1_favfood)
  elif user_turn=="rock"and user2_turn=="paper":
    print(user2,"wins and eats",user2_favfood)
  elif user1_turn=="paper"and user2_turn=="Scissor":
    print(user2,"wins and eats",user2_favfood)
  elif user1_turn=="scissor"and user2_turn=="rock":
    print(user2,"wins and eats",user2_favfood)
  elif user1_turn==user2_turn:
    print("Draw")
    continue 
  else:
  print("Invalid choice")
    continue 
break
  
  
