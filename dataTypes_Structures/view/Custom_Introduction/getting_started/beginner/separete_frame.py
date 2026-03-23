# podemos serparar la logica cuando creamos un frame y esto es una buena practica ya que nos ayuda a 
# organizar correctamente la logica visual del programa para no tener que enredarnos dividiendo 
# una clase para el frame y otra para la app principal 

import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame): 
    def __init__(self, master):
        super().__init__(master)
        
        # master viene siendo el estado de la app o de la clase que consume a el frame 
        self.checkbox_1 = customtkinter.CTkCheckBox(self,text="checkbox 1")
        self.checkbox_1.grid(row=0,column=0,padx=10,pady=(10,0),sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self,text="checkbox 2")
        self.checkbox_2.grid(row=1,column=0,padx=10,pady=(10,0),sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(self,text="checkbox 3")
        self.checkbox_3.grid(row=2,column=0,padx=10,pady=(10,0),sticky="w")
        
    # para obtener el tipo de checkbox seleccionado realizamos de la siguiente forma 
    def get(self) -> list: 
        checked_checkboxes: list = []
        if self.checkbox_1.get() == 1: 
            checked_checkboxes.append(self.checkbox_1.cget("text"))
        elif self.checkbox_2.get() == 1: 
            checked_checkboxes.append(self.checkbox_2.cget("text"))
        else: 
            checked_checkboxes.append(self.checkbox_3.cget("text"))
            
        return checked_checkboxes
        
        
        
    
# creamos la clase app 
class App(customtkinter.CTk): 
    
    def __init__(self) -> None:
        super().__init__()
        
        
        self.title("My app")
        self.geometry("400x180")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        
        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0,column=0,padx=10,pady=(10,0),sticky="nsw")
        
        self.button = customtkinter.CTkButton(self,text="my button",command=self.button_callback)
        self.button.grid(row=3,column=0,padx=10,pady=10,sticky="ew")
        
    def button_callback(self) -> None: 
        print(f"Checked checkboxes: {self.checkbox_frame.get()}")
        
        
# creamos una instancia 
app = App()
app.mainloop()


# una mejor forma de hacer lo anterior se dara en el archivo dynamic frame class