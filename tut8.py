mystr= "ashu is a good boy"
print(len(mystr)) #string length
#print(mystr[0:19]) #string slicing
#print(mystr[0:19:2]) #Advanced/Extended slicing
#print(mystr[::-1])#Negative indices(helps in reversing the string)
print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.endswith("boy"))
print(mystr.count("o"))#count no. of specified letters
print(mystr.capitalize())#Only capitalize the first letter
print(mystr.upper())#Capitalize all
print(mystr.lower())#all in small letter
print(mystr.find("is"))
print(mystr.replace("ashu","jinesh"))#replace any word