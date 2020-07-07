import sys

try:
    x = int(input(""))
    y = int(input(""))
except ValueError:
    print("ValueError")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("ZeroDivisionError")
    sys.exit(1)
    
print(result)