odds = 0
top = 0
while top == 0:
    print('you wanna know some odds?  up to what numbar plz?')
    top = input()
while odds < int(top):
    odds = odds +1
    if odds % 2 == 0:
        continue
    print(odds)
print('those are the odds')
