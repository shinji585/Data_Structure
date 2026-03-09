import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame): 
    def __init__(self, master,values,title):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        # podemos agregar titulos a los frames para diferenciar las acciones 
        self.title = title
        self.values = values 
        self.checkboxes = []
        
        
        self.title = customtkinter.CTkLabel(self,text=self.title,fg_color="gray30",corner_radius=6)
        self.title.grid(row=0,column=0,padx=10,pady=(10,0),sticky="ew")
        
        for i, value in enumerate(self.values): 
            checkbox = customtkinter.CTkCheckBox(self,text=value)
            checkbox.grid(row=1+i,column=0,padx=10,pady=(10,0),sticky="w")
            self.checkboxes.append(checkbox) 
            
            
            
    def get(self): 
        checked_checboxes = []
        for checkbox in self.checkboxes: 
            if checkbox.get() == 1: 
                checked_checboxes.append(checkbox.cget("text"))
                
        return checked_checboxes
    
    
class App(customtkinter.CTk): 
    
    def __init__(self):
        super().__init__()
        self.title("My app")
        self.geometry("400x180")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        
        self.checkbox_frame = MyCheckboxFrame(self,values=["value 1", "value 2", "value 3"]) 
        self.checkbox_frame.grid(row=0,column=0,padx=10,pady=(10,0),sticky="nsw") 
        
        
        self.button = customtkinter.CTkButton(self,text="my button", command=self.button_callback)
        self.button.grid(row=3,column=0,padx=10,pady=10,sticky="ew")      
 
 
    def button_callback(self): 
        print(f"Checkboxex: {self.checkbox_frame}")   
        
app = App()

app.mainloop()     