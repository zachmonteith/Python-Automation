#this is a lil guess the number game
import random, time

def intputVal(prompt, name='User'):
    while True:
        print(prompt)
        value = input()
        try:
            value = int(value)
        except ValueError:
            print(name + ', please enter a number, using digits')
            continue
        if value < 1:
            print('gonna need a positive number here, ' + name)
            continue
        break
    return value

def tooHigh():
    responses = ['oof, too high!', "yeah...no, thats too high.", "cmon now, thats a big ol number", "gaaaaah too high too high", "try smaller!", "guess again big shot thats too big"]
    responseNum = random.randint(0,5)
    return responses[responseNum]

def tooLow():
    responses = ['its larger than that', 'try again, too low', 'thats a tiny guess, go bigger', 'cmon now, thats a teensy number', "try higher!", "guess again lil friend thats too smol"]
    responseNum = random.randint(0,5)
    return responses[responseNum]

def guessingGame():
    print('Greetings, please tell me your name')
    name = input()
    print('It\'s lovely to meet you, ' + name + "!!")
    maximum = intputVal('what range you want to guess in? from 1 to...?', name)
    attempts = intputVal('ok and how many attempts should I give you?', name) + 1
    secretNumber = random.randint(1, maximum)

    for guessesMade in range (1, attempts):
        time.sleep(random.randint(2,5)/4)
        guess = intputVal('now, what u think is the number?', name)
        if guess < secretNumber:
            if guess < secretNumber/2:
                print('that\'s less than half of the target!')
            else:
                print(tooLow())
        elif guess > secretNumber:
            if guess > secretNumber*2:
                print('that\'s more than double the target!')
            else:
                print(tooHigh())
        else:
            break #win condition

    if guess == secretNumber:
        print('oh snap ' + name + '!! thats correct!')
        print('the number was indeed ' + str(secretNumber))
        time.sleep(random.randint(2,5)/4)
        print('you got it in ' + str(guessesMade) + ' tries :)')
    else:
        print('oof, u had ' + str(guessesMade) + ' tries and you never got it!')
        time.sleep(random.randint(2,5)/4)
        print('it was ' + str(secretNumber))
    time.sleep(random.randint(2,5)/4)
    print('thank you for playing, I hope you have a lovely day!')

guessingGame()
