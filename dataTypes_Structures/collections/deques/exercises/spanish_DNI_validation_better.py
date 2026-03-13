# the next code is a better solucion than my made in spanish_DNI_validation


def is_valid_dni(s: str) -> bool:
    if len(s) != 9:
        return False
    text, num_slice = "TRWAGMYFPDXBNJZSQVHLCKE", s[:-1]
    return num_slice.isdigit() and text[int(num_slice) % 23] == s[-1]

    # here text take all "TRWAGMYFPDXBNJZSQVHLCKE" and num_slice take the numbers of the dni
    # then before return we see is those values are digin and we take the position where the number could stay
    # on the text and check if it is equivalent to the last value is this is ok we return true and if is false then return false
    # this form is better and use less code
