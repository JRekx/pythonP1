def print_upper_words(words):

    #  print_upper_words(['I','have','the','best','pets'])
    # I
    # HAVE
    # THE
    # BEST
    # PETS

    for word in words:
        print(word.upper())


def print_upper_wordss(words):

    # print_upper_wordss(['Everst','eager','empty','Franklin'])
    # EVERST
    # EAGER
    # EMPTY

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_wordsss(words,must_start_with):
   
#    print_upper_wordsss(['Jordan','Franklin','Bre','Winston'],
#                        must_start_with=['J','B'])
#     JORDAN
#     BRE
   
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break