# a list of users who logged in yesterday
# a list of users who logged in today
# your taks is build a structure that contains all unique users who logged in at least once

yesterday_logged: list[str] = [
    "samuel",
    "santiago",
    "angela",
    "mariana",
    "daniela",
    "katrina",
    "james",
    "cristiano",
    "ronaldo",
    "messi",
]
today_logged: list[str] = ["samuel", "messi", "cristiano", "catalina"]


def set_union(yesterday: list[str], today: list[str]) -> set[str]:
    return set(today).union(yesterday)


print(
    f"Users logged yesterday and today: {set_union(yesterday=yesterday_logged, today=today_logged)}"
)
