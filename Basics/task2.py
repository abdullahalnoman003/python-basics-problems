numbers = []

for i in range(10):
    num = int(input(f"Enter {i+1} integer : "))
    numbers.append(num)

total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
count = 0
for i in numbers:
    if i % 2 == 0:
        count +=1

print("\nNumbers:", numbers)
print("Sum =", total)
print("Maximum =", maximum)
print("Minimum =", minimum)
print("Even numbers count =",count)