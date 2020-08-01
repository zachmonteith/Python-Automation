times = '0'
while int(times) == 0: 
    print('how many times you wanna do this?')
    times = input()
for i in range(int(times)):
    print('ok, here\'s time #' + str(i + 1))
print('hope you enjoyed those times')
