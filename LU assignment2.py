#Question 1
#Delete all occurrences of an element in a list
list = [1,2,3,4,5,6,7,8,9,10]
remove= 10
for item in list:
	if(item==remove):
		list.remove(remove)
print(list)

#Question 2
#Check whether a string is a pangram.
import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True
string = 'abcdefghijklmnopqrstuvwxyz'
if(ispangram(string) == True):
   print("Yes")
else:
   print("No")
