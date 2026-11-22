"""
fixed functions
"""

from operator import itemgetter


def read_file(filename):
    """Reads the text file"""
    with open(filename, "r") as file_handler:
        return file_handler.readlines()

def typing_test(level_file):
    """the typing test with all the function"""
    total_words = 0
    total_chars = 0
    word_prestation = 100
    letter_prestation = 100
    wrong_letters = {}
    lines = read_file(level_file)
    print_score = (f"""Word prestation: {round(word_prestation, 2)}% 
Letter prestation: {round(letter_prestation, 2)}%
Wrong letters: {wrong_letters}""")
    for line in lines: 
        line = line.rstrip("\n")
        total_words += len(line.split())
        for _ in (line.replace(" ", "")):
            total_chars += 1
    for line in lines:
        print(print_score)
        print("\nType the following line:")
        print(line.strip())
        user_input = input("") 
        line = line.split()
        if user_input == "": 
            for _ in range(1, len(line) + 1):
                user_input += " "
        user_input = user_input.split()
        words_score = words_score_oper(total_words, user_input, line)
        word_prestation -= words_score
        chars_score, wrong_letter_list = char_score_oper(total_chars, user_input, line)
        letter_prestation -= chars_score
        wrong_letters = wrong_letter(wrong_letter_list, wrong_letters)
        print_score = (f"""Word prestation: {round(word_prestation, 2)}% 
Letter prestation: {round(letter_prestation, 2)}%
Wrong letters: {wrong_letters}""")
    print("Your game results: ")
    print(print_score)
    name = input("Type your name to save your score: ")
    return print_score, name


def words_score_oper(total, user_input, words):
    """calculates the missed word score"""
    user_total_words = 0
    for i, word in enumerate (words):
        try: 
            if word != user_input[i]:
                user_total_words += 1 
        except IndexError:
            user_total_words += 1
    word_score = round(user_total_words / total * 100, 2) 
    return word_score

def char_score_oper(total, user_input, words):
    """calculates the missed character score and the wrong characters"""
    user_total_chars = 0
    wrong_letters_list = []
    for i, word in enumerate(words):
        try:
            if word != user_input[i]:
                for index, char in enumerate(word):
                    if char != user_input[i][index]:
                        user_total_chars += 1
                        wrong_letters_list.append(char)
        except IndexError:
            for index, char in enumerate(word):
                try: 
                    if char != user_input[i][index]:
                        user_total_chars += 1
                        wrong_letters_list.append(char)
                except IndexError:
                    user_total_chars += 1
                    wrong_letters_list.append(char)
    char_score = round(user_total_chars / total * 100, 2)
    return char_score, wrong_letters_list


def wrong_letter(wrong_letters_list, wrong_letters_dict):
    """calculates the number of wrong characters"""
    for char in wrong_letters_list: 
        if char in wrong_letters_dict:
            wrong_letters_dict[char] += 1 
        else: 
            wrong_letters_dict[char] = 1 
    sorted_dict = sorted(wrong_letters_dict.items(), key=itemgetter(1, 0), reverse=True)
    return dict(sorted_dict)

def save_score(user_score, name): 
    """saves the score and name in score.txt"""
    with open("score.txt", "a") as file_reader: 
        file_reader.write(f"""\n{name}: 
{user_score}\n""")

def print_scores(): 
    """prints the score file"""
    try: 
        with open("score.txt", "r") as file_reader: 
            content = file_reader.read()
        if not content.strip():
            return "No scores recorded yet."
        return content
    except FileNotFoundError:
        return "No scores recorded yet."
