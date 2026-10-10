# Given a list of size n, return the element repeated most

list = [1,3,5,3,4,2,2,5,2]

def most():
   
    x = max(set(list), key=list.count)

    print(x)  # Output: 3



most()
    