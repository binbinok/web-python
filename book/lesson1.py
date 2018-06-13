import random

secret = random.randint(1, 100)
guess = 0
tries = 0

print "AHOY I'm the Dread Pirate Roberts, and I gave a secret!"
print "It is a number from 1 to 99 , I'll give you 6 tries."

while guess != secret and tries < 6 :
    guess = input("What's yer guess? ")
    if guess < secret :
        print "Too low"
    elif guess > secret :
        print "Too high"
    tries = tries + 1

if guess == secret :
    print "Ye got it!"
else:
    print "No more guesses"