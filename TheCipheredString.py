#Building a cipher

import random

#Global variable to store the key later on throughout the function
global_key = None #We initialize it with the None value

def cipher(string_input): #Here we defined the cipher function which takes the 
    #argument string_input
    global global_key
    
    #We will generate a random number between 1-26 and assign it to the "key" variable
    key = random.randint(1, 26) #We display the range as arguments of the random.randit method
    
    #We need to store the key globally so we can access it below
    global_key = key
    
    #Here is how we will encode each letter using the randomly generated key from above
    #all while assigning it to the ciphered_result variable
    ciphered_string = ''.join(chr(key + ord(char)) for char in string_input)
    #we use the for loop to iterate through the string entered and assign keys based on the
    #random integer from the range we listed above in the randint function
    
    return ciphered_string

def decipher(ciphered_string):
    global global_key
    
    #We need to verify if a key is available for deciphering, so that it doesn't equal None
    if global_key is None:
        print("Error! No key is available!")
        return None
    
    #Decipher each letter using the key we stored before:
    deciphered_string = ''.join(chr(ord(char) - global_key) for char in ciphered_string)
    #we're basically just reversing the original cipher function here by iterating through
    #the encoded string using the global "key" from the prior function (why we made it global)
    
    return deciphered_string

def main():
    #Get user input here:
    original_string = input("Enter a string: ")
    
    #Encode the input string and print the result here:
    ciphered_string = cipher(original_string)
    print("Ciphered String=", ciphered_string)
    
    #Decipher the ciphered string and print the result here:
    deciphered_string = decipher(ciphered_string)
    print("Deciphered String=", deciphered_string)
    
    #Verify if the deciphered result matches the original string
    if deciphered_string == original_string:
        print("Great! Deciphered string matches the original string that you wrote.")
    else:
        print("Error! Deciphered string does not match the original string that you wrote.")

#Now call the main function:
main()