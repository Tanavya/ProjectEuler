
import string
with open("wordsEulerP44", "r") as f:
    wordsList = f.read()


wordsList = wordsList.replace("\"", "")
triangularNumbers = []
x = 0
n = 1
while x < 240:
    x = 0.5 * float(n**2 + n)
    triangularNumbers.append(x)
    n += 1

print triangularNumbers

print wordsList
print wordsList.split(",")

count = 0
for word in wordsList.split(","):
    score = []
    for letter in word:
        score.append(string.ascii_uppercase.index(letter) + 1)
    if sum(score) in triangularNumbers:
        print word, score, sum(score)
        count += 1

print count
