class Kettle(object):

    power_source = "electricity" #class attribute

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75

hamilton = Kettle("Hamilton", 14.55)

print("models: {0.make} = ${0.price}, {1.make} = ${1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power) #doesn't exist, power is only instance variable on kenwood
print("switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("switch kenwood to gas")
kenwood.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
