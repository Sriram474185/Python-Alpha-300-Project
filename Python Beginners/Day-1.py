import random
print("Hello, World!")
print("Welcome to Day 1 of Python programming.")
def get_choices():
    plyer_choice=input("Enter a choice (rock, paper, scissors): ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player": plyer_choice,"computer": computer_choice }
    return choices
choices=get_choices()
print(choices)

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player==computer:
        return "It's a tie!"
def greeting():
    return "Hi, how are you "

result=greeting()
print(result)

dict={"name":"John", "age":30, "messg":result}

print(dict["name"])

#Library
import random

#list

food=["pizza","burger","pasta","sushi"]
dinner=random.choice(food)
print("Tonight's dinner is:", dinner)

# if elif else 
age=int(input(("Enter your age:")))
if  age >=18:
    print("Your an adult");
elif age >12 and age <18:
    print("Your a teenager");
elif age >3 and age <12:
    print("Your a child");
else:
    print("Your a toddler");

