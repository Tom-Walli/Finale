#User input -
#list -
#if else statement -
#while loop -
#def function -
#function call -
#Parameters

#so there are things that i absolutely need for the project create task but im not sure if i have all of them and my while loops are just being funky.
# help :(


import time
import sys


lst = ['weezer', 'pain', 'ghost', 'metallica', 'three days grace', 'foo fighters', 'my chemical romance', 'korn', 'slipknot', 'set it off', 'rammstein', 'system of a down',]
oth = ['other']


def leave_prog():
    print("Leaving the program. Goodbye....")
    time.sleep(2)
    sys.exit(0)


me = True
numb = True


def prog():
    while me == True:
        print("What is your favorite Metal/Rock Band? Here are some options")
        time.sleep(2)
        print('PAIN', 'Ghost', 'Metallica', 'Three Days Grace', 'Foo Fighters', 'My Chemical Romance', 'Korn', 'Slipknot', 'Set It Off', 'Rammstein','System Of A Down', 'Other', sep="\n")
        user_int = input("Option:")
        if user_int.lower() in lst:
            print("You chose " + user_int + ". Solid Choice")
            time.sleep(2)
            print("My Favorite is Ghost! \n It was nice talking with you!")
            time.sleep(1)
            me == False
            sys.exit(0)
        if user_int.lower() in oth:
            print("What band?")
            user_prop = input("Band Name:")
            print(user_prop + "? Are they a metal or rock band?")
            print("1. Yes \n 2. No")
            user_yn = input("Option:")
            yes = ('1')
            no = ('2')
            while numb == True:
                if user_yn.lower() in (yes,no):
                    if user_yn == '1':
                        print("Oh cool! I'll check them out! It was nice talking to you!")
                        time.sleep(2)
                        numb = False
                        sys.exit(0)
                    if user_yn == '2':
                        print("Oh! I was asking for metal or rock. Do you want to try again?")
                        print("1. Yes \n 2. No")
                        user_ans = input("Option:")
                        if user_ans == '1':
                            print("Great! Sending you back!")
                            break
                        if user_ans == '2':
                            print("Okay, That's fine. It was nice talking to you!")
                            time.sleep(2)
                            numb = False
                            sys.exit(0)
                        else:
                            print("That wasn't an option. Try again!")
                            time.sleep(2)
                    else:
                        print("Can you please choose Yes or No?")
                        numb = True
        else:
            print("That wasn't an option. Try again!")
            time.sleep(2)
            me == True

prog()





