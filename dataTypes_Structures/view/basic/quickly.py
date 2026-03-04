import tkinter as tk

# iniciamos la ventana
root = tk.Tk()
root.title("My first GUI")  # agregamos un nombre a la ventana


def on_click():
    lbl.config(text="Button Clicked!")


lbl = tk.Label(root, text="Label 1 ")
lbl.grid(row=0, column=0)


print(lbl.config().keys())

btn = tk.Button(
    root, text="Button 1", command=on_click
)  # pasamoe le root por que es la ventada padre
btn.grid(row=0, column=1)  # agregaos el boton a nuestra venta


# corremos la ventana
root.mainloop()
