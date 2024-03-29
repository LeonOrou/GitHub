import random


def convert(unconverted_input):
    string_user_word = ""
    for letter in unconverted_input:
        string_user_word += letter
    return string_user_word


def letter_duplicates(word, letter):
    start_at = -1
    duplicate_list = []
    while True:
        try:
            duplicate_item = word.index(letter, start_at+1)
        except ValueError:
            break
        else:
            duplicate_list.append(duplicate_item)
            start_at = duplicate_item
    return duplicate_list


guess_word = random.choice(['alarm', 'apple', 'human', 'chair', 'smile', 'birth', 'brain', 'super', 'breed', 'dream',
                            'delay', 'enjoy', 'start', 'force', 'funny', 'great', 'heavy', 'image', 'lough', 'level',
                            'media', 'major', 'offer', 'ocean', 'piece', 'proud', 'score', 'smart', 'think', 'times',
                            'train', 'video', 'virus', 'write', 'world', 'value'])
print('Guess the word!')
attempts_left = 11
converted_user_word = ""
guess0 = "_ "
guess1 = "_ "
guess2 = "_ "
guess3 = "_ "
guess4 = "_ "
guess5 = "_ "
while converted_user_word != guess_word:
    unconverted_user_word = [guess0, guess1, guess2, guess3, guess4]
    print(f"{guess0} {guess1} {guess2} {guess3} {guess4}")
    guess = input("Guess a character: ").lower()
    if guess in guess_word:
        index_list = letter_duplicates(guess_word, guess)
        guess_index = index_list
        if 0 in guess_index:
            guess0 = guess
        if 1 in guess_index:
            guess1 = guess
        if 2 in guess_index:
            guess2 = guess
        if 3 in guess_index:
            guess3 = guess
        if 4 in guess_index:
            guess4 = guess
        unconverted_user_word = [guess0, guess1, guess2, guess3, guess4]
        converted_user_word = convert(unconverted_input=unconverted_user_word)
    else:
        attempts_left -= 1
        print(f"Ops! '{guess}' was not a character of the word! Attempts left : {attempts_left}")
        if attempts_left < 1:
            print("""
            You lost all lives, try again?""")
            break
    if converted_user_word == guess_word:
        print(f"{guess0} {guess1} {guess2} {guess3} {guess4}")
        print(f"""
Congratulations! You guessed '{guess_word}' right!
You were {attempts_left} attempts close to death!""""")
