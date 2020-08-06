def fizzBuzz(num):
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(str(i))

def customFB():
    while True:
        print('how many?')
        value = input()
        try:
            value = int(value)
        except ValueError:
            print('please enter a number, using digits')
            continue
        if value < 1:
            print('gonna need a positive number here')
            continue
        break
    fizzBuzz(value)

customFB()
