import os

# Enhancements:
# 1. Gives suggestions to improve password strength.
# 2. Displays password strength using stars.
# 3. Shows session statistics when the user quits.

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
         "u", "v", "w", "x", "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
         "U", "V", "W", "X", "Y", "Z"]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
           "-", "_", "=", "+", "[", "]", "{", "}", "|", ";",
           ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\",
           "`", "~"]


def word_in_file(word, filename, case_sensitive=False):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if case_sensitive:
                if word == line:
                    return True
            else:
                if word.lower() == line.lower():
                    return True

    return False


def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    return False


def word_complexity(word):
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_suggestions(password):
    suggestions = []

    if not word_has_character(password, LOWER):
        suggestions.append("Add lowercase letters.")

    if not word_has_character(password, UPPER):
        suggestions.append("Add uppercase letters.")

    if not word_has_character(password, DIGITS):
        suggestions.append("Add numbers.")

    if not word_has_character(password, SPECIAL):
        suggestions.append("Add special characters.")

    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print("- " + suggestion)
    else:
        print("Your password uses all four character types!")


def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    strength = 1 + word_complexity(password)
    return strength


def main():
    total_checked = 0
    strong_passwords = 0

    password = ""

    while password.lower() != "q":
        password = input("Enter a password to test (q to quit): ")

        if password.lower() != "q":
            strength = password_strength(password)

            total_checked += 1

            if strength == 5:
                strong_passwords += 1

            print(f"Password strength: {strength}/5")
            print("Rating: " + "★" * strength + "☆" * (5 - strength))

            if strength < 5:
                password_suggestions(password)

            print()

    print("Session Statistics")
    print(f"Passwords checked: {total_checked}")
    print(f"Strong passwords: {strong_passwords}")


if __name__ == "__main__":
    main()
