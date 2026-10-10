# Collect anagrams in list of lists i.e. combine all strings with similar alphabets in one list
# then put all those lists in one universal list
from collections import Counter

str = ["eat", "ate", "tan", "tea", "nat","bat"]
list =[]


def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
    

print(anagrams("eat", "ate"))
