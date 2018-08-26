# I'll be using Python 3, for reference.

def custom_repl():
    pie = "delicious"
    pi = 3.14159
    homonyms = (pie != pi)
    code.interact(
        banner="Beholder ",
        local=locals(),
    )

custom_repl()