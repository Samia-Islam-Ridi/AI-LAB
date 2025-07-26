# Problem - 2
# Methode-1: Using nested if concept
'''
a = int(input())
b = int(input())
c = int(input())

if a>=b:
    if a>=c:
        print(a,"is the largest ")
    else:
        print(c,"is the largest")
else:
    if b>=c:
        print(b, "is the largest")
    else:
        print(c,"is the largest")
'''

# Methode-2: Using logical operators
a = int(input())
b = int(input())
c = int(input())

if a>=b and a>=c:
    print(a, "is the largest")
elif b>=a and b>=c:
    print(b, "is the largest")
else:
    print(c, "is the largest")