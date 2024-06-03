import random
num = random.randint(1, 20)

try_num = 5

key = True

print(f'I am thinking of a number between 1 to 20. Can you guess it? You have {try_num} Chances')

while key:
    try_num = try_num - 1
    
    answer = int(input('Guess the Number :'))

    if try_num == 0 and answer != num:
        key = False
        print('Oops!! You lost , ran out of your chances.')

        again = input('yes or no :').lower()

        if again == 'yes':
            key = True
            try_num = 5
        elif again == 'no':
            key = False

    elif answer == num:
        print('you won')
        key = False

        again = input('yes or no :').lower()

        if again == 'yes':
            key = True
            try_num = 5
        elif again == 'no':
            key = False

    elif answer > num:
        print(f'YOU HAVE {try_num} CHANCES LEFT')
        print('Hint : Choose a Lower Number')

    elif answer < num:
        print(f'YOU HAVE {try_num} CHANCES LEFT')
        print('Hint : Choose a Higher Number')
    



