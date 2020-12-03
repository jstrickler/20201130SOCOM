

def main():
    word_list = get_word_list()
    count = 0
    for word in word_list:
        if is_palindrome(word):
            print(word)
            count += 1
    print(f"Found {count} palindromes")

def get_word_list():
    with open('DATA/words.txt') as words_in:
        return words_in.read().splitlines()

def is_palindrome(word):
    return list(word) == list(reversed(word))

if __name__ == '__main__':
    main()

