a = 10
b = 25
c = 15

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("First Number:", a)
print("Second Number:", b)
print("Third Number:", c)
print("Largest Number:", largest)