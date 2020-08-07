def baseConvert(num, base=2):
    exp = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    while base**exp <= num:
        exp += 1
    # print("number of digits will be:", exp) #for debug
    for i in range(exp):
        thisDig = base**(exp-(i+1))
        if num - thisDig >= 0:
            digit = num // thisDig
            if digit > 9:
                digit = alphabet[digit-10]
            result += str(digit)
            num = num % thisDig
        else:
            result += '0'
    if result == '':
        result += '0'
    print(result)
