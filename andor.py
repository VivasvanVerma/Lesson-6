a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter one last number: "))
if a and b and c:
    print("All values are True")
elif a or b or c:
    print("Atleast one value is True")
else:
    print("No value is true")

if a>0 or b>0 or c>0:
    print("Atlease one value if greater than zero")
else:
    print("No value is greater than zero.")