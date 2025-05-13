#7. Reverse the letters of a string
word = input("Enter a word: ")
# Function to reverse the letters of a string
def reverse_string(word):
    return word[::-1]  
# Call the function and print the result
reversed_word = reverse_string(word)
print("The reversed word is: ", reversed_word)