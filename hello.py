# this program says hello and asks for my name

print('sup')
print('and what be your name, ya bish?') #ask for their name
datName = input()
if datName == 'Zach':
    print('YoU aRe ThE mAkEr!1!1')
    print('indentation means this is still the block')
else:
    print('heeeeey good ta know ya ' + datName)
    print('dat name is pretty long it has ' + str(len(datName)) + ' characters, dawg')
print('how many years did you has') #ask for that age yo
datAge = input()
if datAge == '32':
    print('ooooooohhhhhh datsa niceeeee')
elif int(datAge) < 32:
    print('dag you still a li\'l chil\' I\'m lookin\' for someone who at least 32')
else:
    print('ohhhhh snap i dint kno u was ' + datAge + ' already, dawg')
