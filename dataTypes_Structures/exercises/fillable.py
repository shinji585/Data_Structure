def fillable(stock: dict[str, int], merch: str, n: int) -> bool:
    if merch in stock:
        # tomamos el valor de la stock para verificar si tenemos suficiente
        stock_n: int = stock[merch]
        if stock_n >= n and n >= 1:
            return True
        else:
            return False
    else:
        return False


# una forma mas sencilla de resolver este ejercicio es utilizando get
# y validando si es true entonces este nos devuelve verdadero y si es false devuelve falso


def fillable2(stock: dict[str, int], merch: str, n: int) -> bool:
    return stock.get(merch, 0) >= n


# y se resulve el problema mas rapido
