def is_valid_dni(s: str) -> bool:
    TABLE: dict = {
        0: "T",
        1: "R",
        2: "W",
        3: "A",
        4: "G",
        5: "M",
        6: "Y",
        7: "F",
        8: "P",
        9: "D",
        10: "X",
        11: "B",
        12: "N",
        13: "J",
        14: "Z",
        15: "S",
        16: "Q",
        17: "V",
        18: "H",
        19: "L",
        20: "C",
        21: "K",
        22: "E",
    }

    if not s.strip() or len(s) != 9 or not s[:8].isdigit() or not s[8].isalpha():
        return False

    number = int(s[0:8])

    if (number % 23) in TABLE:
        if s[-1] == TABLE.get(number % 23):
            return True

    return False


print(is_valid_dni(s="00000001R"))
