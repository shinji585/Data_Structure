import re

# you receive a list of files names as strings
files_name: list = ["data.csv", "image.png", "report.pdf", "data.csv", "image.png"]

# build a set of file extensions (without the dot)


def set_extesions(files_name: list[str]) -> set:
    # para obtener el valor despues del punto tenemos que aplicar el siguiente regex
    # \.(.+)
    return {re.findall(r"\.(.+)", x)[0] for x in files_name}


print(set_extesions(files_name=files_name))
