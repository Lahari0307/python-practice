string = (input("enter the string: "))
vowels = "aeiouAEIOU"
vowel_count = 0 
for char in string:
    if char in vowels:
        vowel_count +=1
print("the vowel count is ",vowel_count)