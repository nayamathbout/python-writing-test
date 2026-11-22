"""
Main file with main manu functions
"""


import typing_utils

def main_menu():
    """menu choices that the user choses"""
    stop = False 
    while not stop: 
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print("""Test your typing prestation: 
1) Easy
2) Medium
3) Hard
4) Score
q) quit
""")
        choice = input("Enter your level: ")

        if choice == "q": 
            print("See you next time :)")
            stop = True

        elif choice in ('Easy', 'easy', '1'):
            try: 
                score, user_name = typing_utils.typing_test("easy.txt")
                typing_utils.save_score(score, user_name)
            except FileNotFoundError: 
                print("Sorry, the game is not ready yet, come back later")

        elif choice in ('Medium', 'medium', '2'): 
            try: 
                score, user_name = typing_utils.typing_test("medium.txt")
                typing_utils.save_score(score, user_name)
            except FileNotFoundError: 
                print("Sorry, the game is not ready yet, come back later")

        elif choice in ('hard', 'Hard', '3'): 
            try: 
                score, user_name = typing_utils.typing_test("hard.txt")
                typing_utils.save_score(score, user_name)
            except FileNotFoundError: 
                print("Sorry, the game is not ready yet, come back later")

        elif choice in ('Score', 'score', '4'):
            print(typing_utils.print_scores())

        else: 
            print("Enter a valid choice")

        if not stop: 
            input("\nPress enter to continue...")

if __name__ == "__main__": 
    main_menu()
