# coding=utf-8
import random, easygui

secret = random.randint(1, 100)
guess = 0
tries = 0

while guess != secret and tries < 6 :
    guess = easygui.integerbox("""
        AHOY I'm the Dread Pirate Roberts, and I gave a secret!
        It is a number from 1 to 99 , I'll give you 6 tries.
    """)
    if not guess: break
    if guess < secret :
        easygui.msgbox('Too low')
    elif guess > secret :
        easygui.msgbox('Too high')
    tries = tries + 1

if guess == secret :
    easygui.msgbox('Ye hot it!')
else :
    easygui.msgbox('No more guesses')

# while guess != secret and tries < 6 :
#     guess = input("What's yer guess? ")
#     if guess < secret :
#         print "Too low"
#     elif guess > secret :
#         print "Too high"
#     tries = tries + 1

# if guess == secret :
#     print "Ye got it!"
# else:
#     print "No more guesses"