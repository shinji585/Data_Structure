# you have the next: users who registered  but did not pay, your taks is find those users

users: set = {"Microsoft", "Apple", "Samsung", "Xiaomi"}
paid: set = {"Microsoft", "Samsung"}


def difference_set(general_users: set[str], user_paid: set[str]) -> set:
    return general_users.difference(user_paid)


print(f"Users that didn't pay: {difference_set(general_users=users, user_paid=paid)}")
