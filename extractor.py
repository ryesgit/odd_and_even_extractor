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
        with open('numbers.txt', 'r') as numbers:
            # Iterate through every number from numbers.txt
            numbers = numbers.readlines()

            for index, number in enumerate(numbers):
                # If number is even
                if(int(number.strip()) % 2 == 0):
                    store_to_file(str(number), index, 'even')
                # If number is odd
                else:
                    store_to_file(str(number), index, 'odd')
    except FileNotFoundError:
        return 'File numbers.txt is not found'

def store_to_file(number, index, mode):

    # Determine divisor according to mode
    divisor = 1 if mode == 'odd' else 0
    
    # If number is first on list, create a new file or overwrite existing
    if index == 0:
        with open(f'{mode}.txt', 'w') as even:
            even.write(str(number))
    else:
        with open(f'{mode}.txt', 'a') as even:
            even.write(str(number))


print(open_file_and_extract())