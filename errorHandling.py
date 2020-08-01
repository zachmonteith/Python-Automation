def divide(numer, denomer):
    try:
        return numer / denomer
    except ZeroDivisionError:
        return 'Dawg, you can\'t divide by zero!'
    except TypeError:
        return 'Dawg, this is math.  please use numbers.'

#good for input validation!

def inputValidation():
    print('please input a number greater than 7')
    value = input()
    try:
        if int(value) > 7:
            return 'thank you, you are very compliant'
        else:
            return 'um, ' + value + ' is not greater than 7!'
    except ValueError:
        return 'that\'s not even a number man!'
