scores = []

for i in range(8):
    score = int(input("Enter score: "))
    scores.append(score)

odd_scores = [s for s in scores if s % 2 != 0]

if odd_scores:
    print("Highest Odd Score =", max(odd_scores))
else:
    print("No odd score. Trophy not awarded.")

'''
The program takes scores from 8 matches and checks for odd scores.
It finds the highest odd score using the `max()` function.
If no odd score exists, the trophy is not awarded.
'''
