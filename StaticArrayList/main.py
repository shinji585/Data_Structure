import customtkinter as ctk
from view.FixedArrayListView import MatteApp


def main() -> None:
    root = ctk.CTk()
    MatteApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

