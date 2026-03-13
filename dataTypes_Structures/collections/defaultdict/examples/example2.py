from collections import defaultdict

# las lambda i: expression
# si bien han perdido importancia por las comprehension su uso o focus
# ha cambiado ya que no las utilizamos para definir acciones complejas si no concretas
# y en defaultdict son funcionales para sistemas finacieros o videojuegos

banco = defaultdict(lambda: 100)  # devuelve siempre 100 (como una constante)

banco["Juan"] -= 20

print(banco["Juan"])
print(banco["Maria"])
