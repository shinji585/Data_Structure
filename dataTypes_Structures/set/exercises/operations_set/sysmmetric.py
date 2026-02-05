# you have two systems that track feature flags

goats_history: set = {
    "Pele",
    "Diego Maradona",
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Johan Cruyff",
    "Zinedine Zidane",
    "Ronaldinho",
    "Ronaldo Nazario",
    "Franz Beckenbauer",
}
goats_still_playing: set = {
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Kylian Mbappe",
    "Erling Haaland",
    "Kevin De Bruyne",
    "Mohamed Salah",
}


def sysmetric_set(A: set, B: set) -> set:
    return A.symmetric_difference(B)


print(
    f"The sysmetric difference is: {sysmetric_set(A=goats_history, B=goats_still_playing)}"
)
