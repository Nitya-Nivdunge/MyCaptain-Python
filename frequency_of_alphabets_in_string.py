# Taking input from user
inp_string = str(input("Enter your string / word : "))

# initial declarations
main_dict = {}
sorted_dict = {}

# Function to create initial dictionary and sort it later 
def most_frequent():
    # for loop to iterate through the string 
    for letter in inp_string:
        if letter in main_dict:
            main_dict[letter] = main_dict[letter] + 1
        else :
            main_dict[letter] = 1
        
    # To sort the Dictionary values ( Ascending )
    sorted_keys = sorted(main_dict , key = main_dict.get , reverse = True )
    for letter in sorted_keys:
        sorted_dict[letter] = main_dict[letter]
    
    return(sorted_dict)

# Printing final sorted Dictionary
print("\nOutput : " , most_frequent()) 
