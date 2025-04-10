#User input 
#list 
#if else statement 
#while loop 
#def function 
#function call 
#Parameters

#fix this into a game where it has difficulty and levels 
#maybe 
#add a thing that adds to the sum everytime they get a question right so that at the end it can say you got this many out of ten

import time
import sys

lev = ['easy', 'hard']
lst = ['Who is the current papa in Ghost as of 2025?', 'Who is the keyboardist in Rammstein', 'What is the top hit by My Chemical Romance?', 'What is the name of the lead singer in Slipknot?', 'True or False. In PAIN Peter Tägtgren recruited his son to play drums for the band.', 'Who is the drummer for Korn?', 'What country did Three Days Grace originate from? ', 'What is the most popular album by Matallica', 'what Set It Off song contains the lyrics " Look out, theyre closing in on you now"' ]
ans1 = ['papa v']
ans2 = ['flake lorenz']
ans3 = ['welcome to the black parade']
ans4 = ['corey taylor']
ans5 = ['true']
ans6 = ['ray luzier']
ans7 = ['canada']
ans8 = ['the black album']
ans9 = ['killer in the mirror']
ans10 = ['']

def leave_prog():
    print("Leaving the program. Goodbye....")
    time.sleep(2)
    sys.exit(0)

def score():
    print("Calculating score")
    time.sleep(2)
    # print("You scored " + thesum + "/10")
#create a program called thesum to calculate the score

me = True



def prog():
    numb = True
    while me == True:
        print("Do you think you know metal/punk bands? Let's test your knowlegde! Here are a few bands that might show up on the quiz. ")
        print('')
        time.sleep(2)
        print('PAIN', 'Ghost', 'Metallica', 'Three Days Grace', 'Foo Fighters', 'My Chemical Romance', 'Korn', 'Slipknot', 'Set It Off', 'Rammstein','System Of A Down', sep=', ')
        time.sleep(2)
        print('')
        print("Pick Your Difficulty")
        print(*lev , sep = '\n' )
        user_level = input("Level:")
        if user_level.lower() in lev:
            if user_level.lower() == 'easy':
                print("")
                print("You choose Easy correct?")
                print("1. Yes")
                print("2. No")
                user_correct = input('Option:')
                yes = ('1')
                no = ('2')
                if user_correct.lower() in (yes,no):
                    if user_correct == '1':
                        while numb == True:
                            print("")
                            print("Are you ready?")
                            print("1. Yes")
                            print("2. No")
                            user_int = input("Option:")
                            if user_int.lower() in (yes,no):
                                if user_int == '1':
                                    print("")
                                    print("Perfect! Lets start!")
                                    time.sleep(1)
                                    print("Loading questions...")
                                    time.sleep(2)
                                    print("")
                                    print("Question 1/10")
                                    print(lst[0]) 
                                    user_opti = input("Answer:")
                                    if user_opti.lower() in ans1:
                                        print("Correct!")
                                        time.sleep(1)
                                        print("")
                                        print("Question 2/10")
                                        print(lst[1])
                                        user_opti2 = input("Answer:")
                                        if user_opti2.lower() in ans2:
                                            print("Correct!")
                                            time.sleep(1)
                                            print("")
                                            print("Question 3/10")
                                            print(lst[2])
                                            user_opti3 = input("Answer:")
                                            if user_opti3.lower() in ans3:
                                                print("Correct!")
                                                time.sleep(2)
                                                print("")
                                                print("Question 4/10")
                                                print(lst[3])
                                                user_opti4 = input("Answer:")
                                                if user_opti4.lower() in ans4:
                                                    print("Correct!")
                                                    time.sleep(2)
                                                    print("")
                                                    print("Question 5/10")
                                                    print(lst[4])
                                                    user_opti5 = input("Answer:")
                                                    if user_opti5.lower() in ans5:
                                                        print("Correct!")
                                                        time.sleep(2)
                                                        print("")
                                                        print("Question 6/10")
                                                        print(lst[5])
                                                        user_opti6 = input("Answer:")
                                                        if user_opti6.lower() in ans6:
                                                            print("Correct!")
                                                            time.sleep(2)
                                                            print("")
                                                            print("Question 7/10")
                                                            print(lst[6])
                                                            user_opti7 = input('Answer:')
                                                            if user_opti7.lower() in ans7:
                                                                print("Correct!")
                                                                time.sleep(2)
                                                                print("")
                                                                print("Question 8/10")
                                                                print(lst[7])
                                                                user_opti8 = input("Answer:")
                                                                if user_opti8.lower() in ans8:
                                                                    print("Correct!")
                                                                    time.sleep(2)
                                                                    print("")
                                                                    print("Question 9/10")
                                                                    print(lst[8])
                                                                    user_opti9 = input("Answer:")
                                                                    if user_opti9 in ans9:
                                                                        print("Correct!")
                                                                        time.sleep(2)
                                                                        print("")
                                                                        print("Question 10/10")
                                                                        print(lst[9])
                                                                        user_opti10 = input("Answer")
                                                                        if user_opti10 in ans10:
                                                                            print("Correct!")
                                                                            score()


                                        else:
                                            print("Sorry, incorrect.")
                                            time.sleep(2)
                                            print("")
                                            print("Question 3/10")
                                            print(lst[3])
                                            user_opti4 = input("Answer:")
                                            if user_opti4 in ans4:
                                                print("Correct!")
                                    else:
                                        print("Sorry, incorrect.")
                                        time.sleep(2)
                                        print("")
                                        print("Question 2/10")
                                        print(lst[1])
                                        user_opti2 = input("Answer:")
                                        if user_opti2.lower in ans2:
                                            print("Correct!")
                                            time.sleep(1)
                                            print("Question 3/10")
                                            print(lst[2])
                                            user_opti3 = input("Answer:")
                                            if user_opti3.lower() in ans3:
                                                print("Correct!")
                                                time.sleep(2)
                                                print("Question")

                                        
                                    time.sleep(1)
                                if user_int == '2':
                                    print("Oh.... okay? Well, come back at any time!")
                                    time.sleep(1)
                                    leave_prog()
                            else:
                                print("Sorry that was not an option! Try again!")
                                print("")
                                time.sleep(1)
                                continue #fit this else statement (i think it works now?)
                    if user_correct == '2':
                        print("Oh, well you can choose a different difficulty then ")
                        time.sleep(2)
                        continue 
                else:
                    print("That wasn't an option, sorry!")
                    time.sleep(2)
                    continue
            if user_level.lower() == 'hard':
                print("")
                print("You choose Hard correct?")
                print("1. Yes")
                print("2. No")
                user_correct = input('Option:')
                yes = ('1')
                no = ('2')
                if user_correct.lower() in (yes,no):
                    if user_correct == '1':
                        while numb == True:
                            print("")
                            print("Are you ready?")
                            print("1. Yes")
                            print("2. No")
                            user_int = input("Option:")
                            if user_int.lower() in (yes,no):
                                if user_int == '1':
                                    print("")
                                    print("Perfect! Lets start!")
                                    time.sleep(1)
                                    print("Loading questions...")
                                    time.sleep(2)
                                    print("")
                                    print("Question 1/10")
            else:
                print("Sorry, that wasn't an option!")
                time.sleep(1)
                continue



prog()





