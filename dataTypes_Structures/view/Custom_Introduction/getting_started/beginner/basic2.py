import customtkinter


# definimos un metodo
def button_callbakc() -> None:
    print("Button pressed")


# creamos la ventana
app = customtkinter.CTk()
app.title("My app")  # nos permite definir un titulo
app.geometry("400x150")  # definimos los pixeles que tendra la ventana


# para definir widget tenemos que tener en cuenta siempre pasar la ventana a dicho widget para que este sepa
# cual es el parametro master y donde se debe dibujar (esto depende del tipo de lienzo que estemos manejando)

button = customtkinter.CTkButton(
    app, text="My button", command=button_callbakc
)  # recorar siempre pasar los metodos que se aplicaran sobre el widget sin parentesis
# app.grid_rowconfigure(0, weight=1)
# app.grid_columnconfigure(0, weight=1)
button.grid(
    row=0, column=0, padx=20, pady=20
)  # grid nos permite ubicar los elementos en formato de matrix donde row es i donde lo ubicamos y column es j donde lo ubicamos
# algo tambien a tener en cuenta es padx y pady en donde estos nos dicen el tamaño en pixel que tendra dicho componente

# para ubicar un boton en el centro utilizanmos una funcion llamada
# grid_rowconfigure() la cual toma un peso en la columna y este peso debe ser diferente a zero para que no collapse el size del boton nunca mas
# para centrar exactamente el elemento tenemos que configurar tambien la columna pasando le los mismos valores y que esta pueda crecer ya que si no crece entonces no puede ubicarse en el centro


app.mainloop()
