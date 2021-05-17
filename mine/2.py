import random
num = random.randint(0, 100)
text = -1
while (text != num):
    text = int(input("Guess a number between 0 and 100: "))
    if (text > num):
        print("Sorry but {} is HIGHER than the number".format(text))
    elif (text < num):
        print("Sorry but {} is LOWER than the number".format(text))
print("YES! You've got it! The number is {}".format(text))
