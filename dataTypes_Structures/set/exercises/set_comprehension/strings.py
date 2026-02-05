# given a list of words:
# build a set containing the lenght of each word
# include only words longer that 4 characters
# ask yourself: why do duplicates disappear naturally here?

words: list[str] = [
    "panaderia",
    "autopista",
    "tienda",
    "comcercio",
    "abasto",
    "centro comercial",
]


def take_lenght(words: list[str]) -> set:
    return {len(x) for x in words if len(x) > 4}


print(f"Set words caontaining the lenght of each word: \n{take_lenght(words=words)}")


# set eliminate the repetitive values and that's the reason for why the set looks smaller than the spected
