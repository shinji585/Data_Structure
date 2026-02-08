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
#
#
# A mapping is an interface / behavior, not a concrete data structure.
#
# In this section we're going to study ChainMap that is a mapping who groups multiple mappings and presents them as one logical mapping
#
# an example to how use ChainMap is the next
defaults: dict = {"host": "localhost", "port": 5432}
env: dict = {"port": 5433}
cli_args: dict = {"debug": True}

config = ChainMap(cli_args, env, defaults)

# al llamar cada key estamos obteniendo keys individuales por mapping
print(config["debug"])
print(config["port"])
print(config["host"])

# ChainMap is great for
# confioguration layers
# this is the canonical use:
# command-line arguments
# environment variables
# config file
# defaults
#
# y es mejor que estar haciendo
# final = {}
# final.update(defaults)
# final.update(env)
# final.update(cli)
#
# you do:
# final = ChainMap(clic,env,defaults)
#
# we have some mutability rules
#
# 1. reads: reads search all mapping
# 2. writes go only to the first mapping
# example:
# config["timeout"] = 30
# this adds "timeout" to cli_args, not to env or defaults
# 3. deletes:
# only allowed if "port" exists in the first mapping
# del config["port"]
# otherwise -> KeyError
#
#
