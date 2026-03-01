import ttkbootstrap as tb 
from view.FixedArrayListView import MatteApp

def main(): 
    # creamos la ventana principal 
    root = tb.Window(
        title="Data Structures Lab",
        themename="darkly",
        resizable=(False,False)
    )
    
    # instanciamos la clase visual 
    app = MatteApp(root=root)
    
    # iniciamos el bucle de la aplicacion 
    root.mainloop()
    
if __name__ == "__main__": 
    main()