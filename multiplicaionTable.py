num = int(input("Enter a number: "))
times = 1
for i in range(1, 11):
    times = num * i
    print(f"{num} x {i} = {times}")