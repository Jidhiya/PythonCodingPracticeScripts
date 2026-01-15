word = input("Enter a word: ").lower()
count_a = 0
count_b = 0

for ch in word:
    if ch == 'a':
        count_a += 1
    elif ch == 'b':
        count_b += 1
    else:
        continue

print("'a' count:", count_a)
print("'b' count:", count_b)
