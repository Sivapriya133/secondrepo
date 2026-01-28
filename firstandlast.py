
'''sum of first and last digits'''

s = int(input("enter a number: "))
sm = 0

while s != 0:
    r = s % 10
    sm = sm + r
    s = s // 10

print("sum of digits:", sm)
print(last digits:",sm)
