# en esta seccion vamos a estudiar que son los punteros y como implementarlos utilizando lo que viene siendo el concepto de nodo
#
# pointer structures do not store elements next to each other.
#
# instead, each element points to another element


# so we could have different position and they could be separate in memory
# for example one could be here
#
#
#
#
#
#
#
# and the other could be here
# but they are related because the first has the point of the other


# the pointers structure could grow dinamically if you want to add another element to an array, sometimes you must:
# allocate new memory
# copy the array
#
#
# pointer structure avoid this
