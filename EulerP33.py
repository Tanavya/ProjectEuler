

product = 1
for denum in range(10,100):
    for num in range(10, denum):
        d = ""
        n = ""
        str_denum = str(denum)
        str_num = str(num)

        for digit in str_denum:
            if digit not in str_num and "0" not in str_num and "0" not in str_denum:
                d += digit


        for digit in str_num:

            if digit not in str_denum and "0" not in str_num and "0" not in str_denum :
                n += digit


        try:
            if float(n)/float(d) == num/float(denum) and (n,d) != (str_num,str_denum):
                print str(num) + "/" + str(denum), "->", str(n) + "/" + str(d), " "
                product *= float(n)/float(d)
        except:
            pass

print "Product ->", product

num = round(product, 3)
denum = 1

while True:


    if int(num) == num:
        break

    num *= 10
    denum *= 10

num = int(num)
denum = int(denum)

for i in range(2, num):
    while True:
        if num % i == 0 and denum % i == 0:
            num /= i
            denum /= i

        else:
            break

print "Fraction ->", str(num) + "/" + str(denum)
