def print_upper_words(words, must_start_with): 
    """ if starts with one of given, print each word on seperate line, uppercase """

    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word.upper())
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})