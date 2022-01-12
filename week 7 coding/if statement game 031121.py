import random
name = input('Whats your Name: ')
ans = input('Would You like to play a guessing game? ')
if ans == 'yes'
number = random.randint(1,10)
print(number)

while True:    
    guess = int(input('Enter a number between one and ten: '))
    if guess >= 11 or guess <= 0:
        print('Its between 1 and 10')

    if guess == number:
        print('You are correct!!!')
        break
    elif guess < number:
        print('Too low')
    elif 10 >= guess > number:
        print('Too High')
    else:
        print('incorrect')


#print('Goodbye')