# el siguiente ejemplo de customtkinter explica y muestra como costumizar el background de la ventana que creamos de la app
# el resto de cosas ya han sido estudiadas previamente las que no seran estudiandas
import customtkinter

customtkinter.set_appearance_mode(
    "black"
)  # el modo de visualizacion de la ventana (negra, blanca, roja, etc.)
customtkinter.set_default_color_theme(
    "green"
)  # el tema que toma los componentes de estas por defecto

app = customtkinter.CTk()
app.geometry("400x240")


def button_function() -> None:
    print("button pressed")


button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()

# en el codigo anterior los metodos nuevos son
# set_appearance_mode: this controls the global appearance of the application.
# customtkinter actually supports these modes:
# "light", "dark", "system"
# "system" takes the operating system theme


# set_default_color_theme: this change the accent color of widgets and affects things like: button color, checkbox color, slider color, porgress bars

# grid is not the only method to place elements there is another that is place and this function
# positions widgets using coordinates.
#
# places works follow this form: instead of rows and columns, it uses positions inside the window.
# absolute position button.place(x=100,y=50) the meaning of this is -> 100 pixeles from the left and 50 pixeles from the top

# anchor=customtkinter.CENTER defines which part of the widget is aligned to the coordninates
