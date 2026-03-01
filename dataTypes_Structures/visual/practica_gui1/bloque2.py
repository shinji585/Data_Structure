import ttkbootstrap as tb

root = tb.Window(themename="flatly")
root.title("Bloque 2: Dominando el Grid")
root.geometry("600x400")

# creamos el contenedor (frame) para que el array este separado de los botones
array_frame = tb.Frame(root, padding=20)
array_frame.grid(row=0, column=0, padx=0, pady=0)


# dibuamos 5 celdas usando un bucle (como si fuera tu capacidad)


for i in range(5):
    # creamos un label que parece una casilla de memoria
    celda = tb.Label(
        array_frame,
        text="None",
        font=("Helvetica", 12),
        width=8,  # define el ancho
        relief="solid",  # añade un borde solido
        anchor="center",  # centra el texto
        bootstyle="secondary",  # color gris de bootstrap
    )

    # cada celda va en la misma fila (0) paero distinta columna
    celda.grid(row=0, column=i, padx=5, pady=5)


# añadimos un boton en una fila distinta (debajo del array)
btn_insertar = tb.Button(root, text="Boton de Prueba", bootstyle="success")
btn_insertar.grid(row=1, column=0, padx=20)

root.mainloop()
