import customtkinter

# para crear grids los cuales puedan ser configurables en formato de matrix y poder asignar los widget
# en las posiciones que nosotros queramos hacemos los siguiente

app = customtkinter.CTk()
app.title("Custom Grid")
app.geometry("300x300")


# creamos una grid de 3x3
for i in range(3):
    app.grid_rowconfigure(i, weight=1)
    app.grid_columnconfigure(i, weight=1)


# luego de crear el grid de 3x3 podemos nosotros configurar un widget
def show_position(widget: customtkinter.CTkButton) -> None:
    info = widget.grid_info()
    i = info["row"]
    j = info["column"]
    print(f"Button is at row {i}, column {j}")


# sticky es un valor que le pasamos a button y este nos dice donde
# el widget se queda pegad dentro de su propia celda
#
# sticky accepts directions
# these directions are:
# "n" -> north (top)
# "s" -> south (bottom)
# "e" -> east (right)
# "w" -> west (left)
button = customtkinter.CTkButton(
    app, text="Click Me", command=lambda: show_position(button)
)

button.grid(row=1, column=1, padx=20, pady=20, sticky="n")


# nosotros podemos agregar checkboxes
checkbox_1 = customtkinter.CTkCheckBox(app, text="Checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(app, text="Checkbox 2")
checkbox_2.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="w")

app.mainloop()
