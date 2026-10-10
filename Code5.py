# Input nums = [3,0,1]
# So the range is {0,1,2,3}, 2 is missing from nums. Print just missing number

#list = [3,0,1]

#for i in range(len(list)+1):
#    if i not in list:
#        print(i)


list = [4,0,-5]

for i in range(min(list),max(list)+1):
    if i not in list:
        print(i)