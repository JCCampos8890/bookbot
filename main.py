import sys # Import the sys module to access command line arguments
from stats import get_num_words
from stats import counting_chars
from stats import sorted_list




def get_book_text(path): # Function to read the book text from a file
    with open(path) as f: # Open the file at the given path
        return f.read() # Read the contents of the file and return it

def main():
    # Check if there are enough arguments (script name + book path = 2)
    if len(sys.argv) != 2: # If the number of arguments is not 2
        print("Usage: python3 main.py <path_to_book>") # Print the usage message
        sys.exit(1) # Exit with error code 1

    path = sys.argv[1]  # Get the path from the command line arguments  
    book_text = get_book_text(path) # Read the book text from the file
        
    word_count = get_num_words(book_text) # Get the number of words in the book

    char_count = counting_chars(book_text) # Get the count of each character in the book
    sorted_char_count = sorted_list(char_count) # Sort the character count
    
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters with their counts
    for char, count in sorted_char_count:
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()