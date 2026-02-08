# we have some operations that we could use after create chainmaps
from collections import ChainMap

users: dict = {"samuel": 20, "santiago": 15}
trabajo_sueldo: dict = {"ingeniero": 1000, "desempleado": 0}

personas_status = ChainMap(users, trabajo_sueldo)

# algunas de las operaciones que podemos aplicar son
#
# 1. list of underlying mapping
print(personas_status.maps)  # nos devuelve una lista de los datos que contiene


# 2. chainmaps without the first mapping
print(personas_status.parents)  # nos devuelve el chainmaps sin tener el primer mapping

# 3. create a new layer on top
print(
    personas_status.new_child({"mariana": 25, "camila": 32})
)  # cada hijo se agrega por izquierda al comienzo de la lista
