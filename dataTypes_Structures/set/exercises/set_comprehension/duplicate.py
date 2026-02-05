# you are given a list of email addresses
# normalize them to lowercase
# build a set of unique emails


def build_set_emalis(emails: list[str]) -> set[str]:
    return {str(x).lower() for x in emails}
