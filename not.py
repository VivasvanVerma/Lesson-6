a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter one more number: "))
print(a != b)
print(b != c)
print(a != c)

x = input("Enter a string: ")
y = input("Enter another string: ")
if x != y:
    print(x, "and", y, "are different")
else:
    print(x, "and", y, "are the same")

num = int(input("Enter a number: "))
if num%2 != 0:
    print(num, "is odd")
else:
    print(num, "is even")
