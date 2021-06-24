#Import the random library
import random

#Create lists of the different types of characters to check whether or not our password meets certain requirements
lowerCase = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z')

upperCase = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

specialCase = ('!', '@', '#', '$', '%', '^', '&', '*')

#List of all the other lists that we will use our random.choice() function on to create our password
total = ('!', '@', '#', '$', '%', '^', '&', '*', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5',
         '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*')

#Main program function
def main():

    #while loop to keep the program running until a password that meets our requirements is made
    while True:

        #list that we append new characters of the password to during each iteration of our for loop
        passwordList = []

        #string that we will end up using to convert our passwordList to for ease of copy/paste
        password = ""

        #for loop that adds a new character to our password during each iteration of the given range
        #to make the password larger or smaller, we can change the number in the range() value
        for x in range(10):

            #use the random.choice() function to choose a random character from our 'total' list
            x = random.choice(total)

            #append the character
            passwordList.append(x)

        #check and see if the password we created matched all of the requirements
        lower = any(item in passwordList for item in lowerCase)
        upper = any(item in passwordList for item in upperCase)
        number = any(item in passwordList for item in numbers)
        special = any(item in passwordList for item in specialCase)

        #if all of the requirements are met, we can continue, else we go to the beggining of our while loop
        if lower and upper and number and special:

            #for loop that converts our password from a list into a string
            for i in passwordList:
                password += i

            #print the password!!!
            print(password)

            #when we return the True boolean, our while loop ends
            return True

#RUN OUR PROGRAM
if __name__ == "__main__":
    main()