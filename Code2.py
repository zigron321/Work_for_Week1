# Given a list of integers, return true if any value is repeated twice

list = [2,3,4,5,1,2]
x="False"

def twice():
    for i in list:
        for j in list:
         
            if list[i]==list[j]:
                return True
            else:
                return False
    
          


twice()