# you have:
# a large list of banned words
# a sentence (list of words)
# check whether the sentence contains any banned word
#
# constraint:
# design this so it scales well


def performance_mindset(banned_words: list[str], sentence: str) -> bool:
    # we get the values
    banned_words_sentence: set = {word for word in sentence if word in banned_words}
    if not banned_words_sentence:
        return True
    else:
        return False
