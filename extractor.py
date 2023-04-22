'''

file: extractor.py

This program separates the odd and even numbers into categorized text files.

1. Look for numbers.txt file
2. Iterate through every number from numbers.txt
    - If even, store it on even.txt
    - If odd, store it on odd.txt
3. Remember to close the txt file! (Use with operator for a foolproof execution!)

'''

def open_file_and_extract():

    # Look for numbers.txt file
    try:
        with open('numbers.txt') as numbers:
            # Iterate through every number from numbers.txt
            for line in numbers:
                print(line.strip())

    except FileNotFoundError:
        return 'File numbers.txt is not found'

print(open_file_and_extract())