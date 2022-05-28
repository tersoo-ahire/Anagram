# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    str1 = input("string1:")
    str2 = input("string2:")
    sorted_str1 = sorted(str1)
    sorted_str2 =sorted(str2)

    if len(str1)==len(str2):
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False
    else:
        return False
find_anagram()
