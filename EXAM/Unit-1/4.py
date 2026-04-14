name = input("Enter player name: ")

vowels = "aeiouAEIOU"
count = 0

for ch in name:
    if ch in vowels:
        count += 1

if count > 4:
    print("Name not allowed")
else:
    print("Name accepted")
