#Write a function that takes a number n and print 1 to n. But
#write for multiples of 3, print "Fizz"
#write for multiples of 5, print "Buzz"


#x=10

def number(x):
    for i in range(x):
        if i%3 !=0 and i%5 !=0:
            print(i)
        elif i%3==0:
            print("fuzz")
        elif i%5==0:
            print("buzz")




number(10)