from SpellChecker import SpellChecker

if __name__ == "__main__":

    # nltk.download("brown")
    # nltk.download("state_union")
    # nltk.download("words")
    # nltk.download('punkt')
    # nltk.download('wordnet')
    # nltk.download('gutenberg')
    # nltk.download('twitter_samples')

    checker = SpellChecker()

    # able - OK
    wrong = checker.check("I was aple to sleep tonight. ")
    print(wrong)

    # bill - X
    wrong = checker.check("The water aill is thirty dollars. ")
    print(wrong)

    # new - X
    wrong = checker.check("Tomorrow is a brand ewnd day.")
    print(wrong)

    # leads - X
    # nowhere - X
    wrong = checker.check("The road lpeds to nowprae.")
    print(wrong)

    # ball - X
    # wall - X
    wrong = checker.check("John kicks the uall to the brick uall. ")
    print(wrong)
