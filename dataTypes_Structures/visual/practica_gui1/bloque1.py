import ttkbootstrap as tb


# creamos la ventana principal
# themename: puede ser "darkly", "flatly", "cosmo", "superhero", etc.


root = tb.Window(themename="darkly")


# configuramos la ventana
root.title("Practica de estructuras de datos")
root.geometry("500x300")

# añadimos un componenete simple (label)
label = tb.Label(text="My FixedArraylist GUI", font=("Helvetica", 18))
label.pack(pady=20)


# el "corazon": el main loop mantiene la ventana en un ciclo
root.mainloop()
