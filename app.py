import random

guessesTaken = 0

print('Привіт! Як тебе звати?')

myName = input()

number = random.randint(1, 20)

print('Ок, ' + myName + ', Я загадав число від 1 до 20. Маєш 6 спроб')

while guessesTaken < 6:
    print('Давай вгадуй') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Твоє число занадто мале') # There are eight spaces in front of print.

    if guess > number:
        print('Твоє число занадто велике')

    if guess == number:
        break

if guess == number:
        guessesTaken = str(guessesTaken)
        print('Гарна інтуїція, ' + myName + '! ти вгадав моє число ' + guessesTaken + ' спроб!')

if guess != number:
        number = str(number)
        print('Нажаль не розгадано. Число було ' + number)
