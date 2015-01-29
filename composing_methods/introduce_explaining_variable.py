__doc__ = """Introduce Explaining Variable

You have a complicated expression.
Put the result of the expression, or parts of the expression, in a temporary
variable with a name that explains the purpose."""

PROVERBS = (u"A good anvil does not fear the hammer. "
            u"A good beginning is half the battle. "
            u"A good beginning makes a good ending. "
            u"A good deed is never lost. "
            u"A good dog deserves a good bone. "
            u"A good example is the best sermon. "
            u"A good face is a letter of recommendation. "
            u"A good Jack makes a good Jill. "
            u"A good marksman may miss. "
            u"A good name is better than riches. "
            u"A good name is sooner lost than won. "
            u"A good name keeps its lustre in the dark. "
            u"A good wife makes a good husband. ")


# Original code
def get_names(phrases):
    for word in phrases.split():
        if word.capitalize() == word and word.lower() not in (u"the", u"a"):
            yield word.strip('.:,!?')


# Refactored code
def ref_get_names(phrases):
    words = phrases.split()
    is_capital = lambda word: True if word.capitalize() == word else False
    is_article = lambda word: True if word.lower() in (u"the", u"a") else False

    for word in words:
        if is_capital(word) and not is_article(word):
            strip_word = word.strip('.:,!?')
            yield strip_word


# Tests
if __name__ == '__main__':
    original = [name for name in get_names(PROVERBS)]
    refactored = [name for name in ref_get_names(PROVERBS)]
    assert original == refactored
