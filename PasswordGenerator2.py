import string
import random
import os
import pyperclip
import string_utils

print("Bryan's Random Password Generator\n")
print("You can choose the strength of the password you want to generate.\n")
print("--Weak - generates an 8 character password using a 6 letter word and 2 random digits.")
print("--Moderate - generates an 8 character password made up of random letters and numbers")
print("--Strong - generates a 16 character password made up of random letters and numbers\n")


#Define possible characters
#characters = string.ascii_letters + string.digits

letters = string.ascii_letters
numbers = string.digits

#Turn characters string into list
#def split(characters):
#    return [char for char in characters]

def split(letters):
    return [char for char in letters]

def split(numbers):
    return [char for char in numbers]

site = input("Please enter the site you're generating a password for: ")
userName = input("Please enter the username for the site: ")


#Receive input on strength of password
print ("What strength of password do you want?")
strengthPw = int(input("1 - Weak \n2 - Moderate \n3 - Strong \nEnter selection: "))


#Define number of characters per strength
if strengthPw == 1:
    randChar = 8
elif strengthPw == 2:
    randChar = 8
elif strengthPw == 3:
    randChar = 16
else:
    print("Error! You did not enter a valid selection.")

#Generate Random Password
if strengthPw == 1:
    lines = open("wordlist").read()
    words = lines.split()
    digits = str(random.randint(10, 99)) #Generate random 2 digit number
    word = random.choice(words) #Randomly chooses word from list of over 5000 6 letter words
    password = (word + digits) #Concatenates word and numbers
else:
    halfChar = int(randChar / 2)
    word = "".join((random.choices(letters, k = halfChar))) #Chooses random letters in the amount of half the password length
    num = "".join((random.choices(numbers, k = halfChar)))  #Chooses random numbers in the amount of half the password length
    str(num) 
    passJoin = word + num  #Concatenates letters and numbers to one string
    password = string_utils.shuffle(passJoin) #Shuffles new string to create password


#Output credentials to passwords.txt file
f = open("passwords.txt","a+")
f.write("Site: ")
f.write(site + "\n")
f.write("Username: ")
f.write(userName +"\n")
f.write("Password: ")
f.write(password + "\n")
f.write("\n\n")
f.close()

#Copy password to clipboard
pyperclip.copy(password)


#Display credentials in command window
print("Site:",site)
print("Username:",userName)
print ("Password:",password)
print ("Password has been copied to the clipboard")
os.system("pause")