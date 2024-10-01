import random
import math
#taking inputs from user
lower = int(input("Enter the Lowest number: "))
upper = int(input("Enter the highest Number: "))

#Generating the number between the lowest and highest numbers
x = random.randint(lower, upper)
print("\n\tYou have only", round(math.log(upper - lower + 1, 2)), "chances to guess the Number!\n")

#initializing the of guesses
count = 0;
#calculation of the minimum number of guesses depending on the range

while count < math.log(upper - lower + 1, 2):
    count += 1
    #taking the guessed number as the input
    guess = int(input("Guess the Number: "))

    #testing condition
    if x == guess:
        print("Conratulation. You did it in ", count, " trials")
    elif x > guess:
        print("Sorry. you guessed a lower number.")    
    elif x < guess:
        print("Sorry. you guessed a higher number.")

#if the guessed counts are more than required, show this output.
if count >=math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\nTry again Later!")