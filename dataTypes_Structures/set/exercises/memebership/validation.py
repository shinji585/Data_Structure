# you have:
# a set of allwed commands
# a list of incoming commands
# filter out invalid commands


def validation[T](allwed_commands: set[T], incoming_commands: list[T]) -> set[T]:
    return {x for x in incoming_commands if x in allwed_commands}
