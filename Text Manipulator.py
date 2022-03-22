#Hunter Bossetto 10-26-2021

def main():
    choice = 0
    word_count = 0
    count = 0
    vowels = 'aeiou'
    user_string = ''
    user_list = []

    displayMenu()
    choice = int(input('Enter your choice:'))
    while (choice != 5):
        if (choice == 1):
            user_string = input('Enter a string:')
            user_string = user_string.upper()
            print(user_string)
        elif (choice == 2):
            user_string = input('Enter a string:')
            user_string = user_string.lower()
            print(user_string)
        elif (choice == 3):
            user_string = input('Enter a string:')
            user_list = user_string.split()
            print (len(user_list))
        elif (choice == 4):
            user_string = input('Enter a string:')
            for ch in user_string.lower():
                if vowels.find(ch) >= 0:
                    count = count + 1
            print(count)
            count = 0
        else:
            print('Incorrect entry, please try again.')
        displayMenu()
        choice = int(input('Enter your choice:'))
        

def displayMenu():
    print('Enter 1 to convert a string to uppercase:')
    print('Enter 2 to convert a string to lowercase:')
    print('Enter 3 to count the number of words in a string:')
    print('Enter 4 to count the number of vowels in a string:')
    print('Enter 5 to exit:')

main()
    
