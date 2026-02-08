# a chainmap groups multiple dicts or other mappings together to create a single, updateable view. if no maps are specified, a single empty dictionary is provided so that a new chan always has at leasst one mapping
from collections import ChainMap

# example
baseline = {"music": "bach", "art": "rembrandt"}
adjustments = {"art": "van gogh", "opera": "carmen"}

print(list(ChainMap(adjustments, baseline)))

# A mapping is any object that:
#
# associates keys -> values
# supports key lookup like obj[key]
# has methods like:
# .keys()
# .values()
# .items()
