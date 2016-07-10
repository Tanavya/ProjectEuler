"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["hundred"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


def ToWord(x):



    one = x % 10
    ten = (x / 10) % 10
    hundred = (x / 100) % 10
    thousand = (x / 1000) % 10


    STR = ""

    if x % 100 > 0:

        if thousand > 0:
            STR += ones[thousand - 1] + " thousand "

        if hundred > 0:
            STR += ones[hundred - 1] + " hundred and "

        if ten > 1:
            STR += tens[ten - 1] + " "
            if one > 0:
                STR += ones[one - 1]

        if ten == 1:
            STR += teens[one]

        if ten == 0 and one > 0:
            STR += ones[one - 1]

    else:

        if thousand > 0:
            STR += ones[thousand - 1] + " thousand "

        if hundred > 0:
            STR += ones[hundred - 1] + " hundred"


    return x, STR, len(STR.replace(" ", ""))


count = 0


for i in range(1, 1001):
    print ToWord(i)
    count += ToWord(i)[2]

print count
