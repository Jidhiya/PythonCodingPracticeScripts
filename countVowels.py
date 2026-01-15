word = str(input("enter the word:"))
count = 0
for ch in word:
    if ch in 'aeiouAEIOU':
        count += 1
print("Number of vowels:", count)

    
    
