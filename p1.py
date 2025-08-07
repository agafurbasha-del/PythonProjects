import time
a=10
print('value is ',a)
print()
print('address is ',id(a))
print()
time.sleep(2)
print('end of program')
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b