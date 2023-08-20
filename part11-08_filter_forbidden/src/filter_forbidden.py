def filter_forbidden(string: str, forbidden: str):
    characters_left = [character for character in string if character not in forbidden]
    return ''.join(characters_left)

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)