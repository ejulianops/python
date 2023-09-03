def word_generator(characters: str, length: int, amount: int):
    random_word = [characters[i : i + length] for i in range(amount)]
    
    for item in random_word:
        yield item

if __name__ == '__main__':
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
