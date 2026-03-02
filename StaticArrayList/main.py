import ttkbootstrap as tb
from view.FixedArrayListView import MatteApp


def main() -> None:
    root = tb.Window(themename="darkly")
    MatteApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

