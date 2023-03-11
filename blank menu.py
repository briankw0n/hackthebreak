
def main(display_menu=False):
    string_menu = '''
        =============================
         - Test menu - v1
        -----------------------------
        [1] 
        [2] 
        [3] 
        [4] 
        [0] Exit
        ============================
        '''
    while display_menu is True:
        print(string_menu)
        # Get user input and check if valid
        while True:
            try:
                choice = int(input("Please choose between [1-4], or [0] to exit: "))

                if choice in range(5):
                    break
                continue
            except ValueError:
                continue

        # Run based on user input
        if choice == 1:
            print("------------------------")
            print("Running [1]", '\n')

        elif choice == 2:
            print("------------------------")
            print("Running [2]", '\n')

        elif choice == 3:
            print("------------------------")
            print("Running [3]", '\n')

        elif choice == 4:
            print("------------------------")
            print("Running [4]", '\n')

        elif choice == 0:
            print("Good bye!")
            break

        print('\n')
        print('Type any key to continue...', end=" ")
        if input():
            continue

    if display_menu is False:
        pass


if __name__ == '__main__':
    main(display_menu=True)