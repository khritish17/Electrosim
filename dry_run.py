import electromulation as ele

# v,c = ele.resistors(resistance= 20, input_ = 0.5)
# print(v)
# print(c)

voltage = []
current = []
for vol in range(0, 20):
    v, c = ele.resistors(resistance=1000,input_=vol)
    voltage.append(v)
    current.append(c)
print(voltage)
print(current)
