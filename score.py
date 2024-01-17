import requests

def valid_word(word):
    api_key = "YOUR_WORDNIK_API_KEY"  # Replace with your Wordnik API key
    url = f"https://api.wordnik.com/v4/word.json/{word}/definitions?api_key={api_key}"
    response = requests.get(url)
    return len(response.json()) > 0


def word_score(word, letter_multipliers, word_multiplier):
    scrabble_scores = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    score = 0
    for i, letter in enumerate(word.lower()):
        score += scrabble_scores.get(letter, 0) * letter_multipliers[i]
    score *= word_multiplier
    return score

def menu(select):
    word = input("Enter a word: ")

    match select:
        case '1':
            letter_multipliers = list(map(int, input("Enter the letter multipliers (as space-separated integers): ").split()))
            word_multiplier = int(input("Enter the word multiplier: "))
            score = word_score(word, letter_multipliers, word_multiplier)
            print(f"The Scrabble score for '{word}' is {score}.")

        case '2':
            
            if valid_word(word):
                print(f"'{word}' is a valid Scrabble word.")
            else:
                print(f"'{word}' is not a valid Scrabble word.")

while(1):
    menu(input("Select: \n1) word score\n2) word check\n... "))
