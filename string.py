mystr="saquib bin halim" #string Initialization

print(mystr)

print(len(mystr)) #length function
print(mystr[0:4]) #slicing

print(mystr[-4:-2]) #negative slicing
print(mystr[0:4:2])

print(mystr.isalnum()) #check if string is alphanumeric
print(mystr.isalpha()) #check if string is alphabetic
print(mystr.isdigit()) #check if string is digit
print(mystr.count("o")) #count the number of occurrences of a substring
print(mystr.capitalize()) #capitalize the first letter of the string
print(mystr.upper()) #convert the string to uppercase
print(mystr.lower()) #convert the string to lowercase