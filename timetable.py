timestable = input("What times table would you want to see up till 10: ")
numbers = range(0, int(timestable) * 11, int(timestable))
for numbers in numbers:
    print(numbers)