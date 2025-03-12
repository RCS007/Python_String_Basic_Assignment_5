# Question 5

# Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting
# number and an ending number and then display just that section of the text. (remember Python starts
# counting from 0 and not 1).

# Ask the user to enter the first line of a nursery rhyme
rhyme = input("Enter the first line of a nursery rhyme: ")

# Display the length of the string
print(f"The length of the string is: {len(rhyme)}")

# Ask for a starting and ending number
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))

# Display the selected section of the text
print(f"The selected section of the text is: {rhyme[start:end]}")
