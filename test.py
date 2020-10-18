import random
from datetime import datetime
import requests

def greet():
    response = [
        "Welcome, I am chatbot.Your name please",
        "Hey hello! I am your bot who helps you to do calculations.May I know your name?"
    ]
    print(random.choice(response))
greet()

def get_greeting_time():
    time = datetime.now()
    greeting_time = "Good Morning"
    if(time.hour > 12 and time.hour <= 17):
        greeting_time = "Good Afternoon"
    elif(time.hour > 17 and time.hour < 22):
        greeting_time = "Good Evening"
    elif(time.hour >= 22):
        greeting_time = "Hi, Its late"
    return greeting_time

def welcome(name):
    message = [
        "Nice to meet you",
        "Lets work together"
    ]
    print(f"{get_greeting_time()}, {random.choice(message)}")
name = input("Enter your name : ")
welcome(name)
def temp1():
    print("Which of the following apply to you?")
    choice=menu2()
    if '3' in choice:
        print("Thank you! For your patience there isn't anything you should be worried about now, get this test done again when you dont feel well")
    elif '1' not in choice and '2' not in choice and '3' not in choice:
        print()
        print("Please enter a valid choice")
        print()
        temp1()
    else:
         print("we recommand you to get tested for covid-19 near your local hospital!,Please put on a mask!Thank you!")

def temp(a):
    l=[int(i) for i in a.split(',')]
    if 3 in l or 4 in l:
        print("Have you ever had any of the following:")
        choice = menu1()
        if '6' in choice:
            print("Have you traveled anywhere internationally in the last 28-45 days?")
            print("if yes we recommend you to stay home for a couple of weeks,ThankYou!")
        elif '1' not in choice and '2' not in choice and '3' not in choice and '4' not in choice and '5' not in choice and '6' not in choice:
            print()
            print("Please enter a valid choice")
            print()
            temp(a)
        else:
            temp1()
    if 2 in l or 1 in l:
        print("May be its just climate change ,we recommend you to stay at home for a couple of days and get this sample test done again,Thankyou!")
def menu2():
    print("1. I have recently interacted or lived with someone who has tested covid-19 positive ")
    print("2. I am a Healthcare Worker and I examined a covid-19 confirmed case without protective gear")
    print("3. None of the above")
    print("__________________________________")
    try:
        n=input("Enter your choice ,if you have more than one symptoms please enter all of your choices with a ',' : ")
        return n
    except:
        print("Out of menu")
        return 0
    
def menu1():
    print("1. Diabetes")
    print("2. Hypertension")
    print("3. Lung disease")
    print("4. Heart Diesease")
    print("5. Kidney Disorder")
    print("6. None of the above")
    print("__________________________________")
    try:
        n=input("Enter your choice ,if you have more than one symptoms please enter all of your choices with a ',' : ")
        return n
    except:
        print("Out of menu")
        return 0
    
def menu():
    print("1. Cough")
    print("2. Fever")
    print("3. Difficulty in breathing")
    print("4. Loss of senses of smell and taste")
    print("5. None of the above")
    print("__________________________________")
    try:
        n=input("Enter your choice ,if you have more than one symptoms please enter all of your choices with a ',' : ")
        return n
    except:
        print("Out of menu")
        return 0
def bot():
    choice = menu()
    if  '5' in choice:
        print("There isn't anything you should be worried about ,just stay home and safe")
    if '1' not in choice and '2' not in choice and '3' not in choice and '4' not in choice and '5' not in choice:
        print()
        print("Please enter a valid choice")
        print()
        bot()
    else:
        temp(choice)
bot()