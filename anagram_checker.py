def anagram_check(s1,s2):
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")

    if sorted(s1) == sorted(s2):
        print("\nThey are anagrams")
    else:
        print("\nThey are not anagrams")


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

anagram_check(str1,str2)
