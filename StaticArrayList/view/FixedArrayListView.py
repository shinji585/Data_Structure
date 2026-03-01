import ttkbootstrap as tb
from ttkbootstrap.constants import *
from typing import Optional, Any, Callable
import time

from model.FixedArrayList import FixedArrayList

class MatteApp:
    def __init__(self, root: tb.Window) -> None:
        self.root = root
        self.root.title("ADVANCED FIXED ARRAY ENGINE")
        self.root.geometry("1100x650")
        self.root.configure(background="#0F0F10")
        
        self.array_list: Optional[FixedArrayList] = None
        self.visual_cells: list[tb.Label] = []
        self.cast_type: Callable = str
        
        self.style_config()
        self.create_layout()

    def style_config(self) -> None:
        style = tb.Style()
        style.configure("TFrame", background="#0F0F10")
        style.configure("Action.TFrame", background="#121214", borderwidth=1, relief="solid")
        style.configure("Cell.TLabel", font=("Inter", 12), anchor=CENTER)
        
        style.configure("Action.TButton", 
                        background="#1A1A1C", 
                        foreground="#E6E6E6", 
                        font=("Inter", 9, "bold"))
        style.map("Action.TButton", background=[("active", "#252528")])

    def create_layout(self) -> None:
        header = tb.Frame(self.root, padding=25)
        header.pack(fill=X)
        tb.Label(header, text="FIXED ARRAY LIST", font=("Inter", 14, "bold"), foreground="#E6E6E6").pack(side=LEFT)
        self.size_label = tb.Label(header, text="NO ARRAY", font=("Inter", 10), foreground="#6F6F74")
        self.size_label.pack(side=RIGHT)

        self.main_stage = tb.Frame(self.root, padding=40)
        self.main_stage.pack(fill=BOTH, expand=True)
        
        self.array_container = tb.Frame(self.main_stage)
        self.array_container.pack(pady=30)
        
        self.status_label = tb.Label(self.main_stage, text="AWAITING INITIALIZATION...", font=("Inter", 10), foreground="#4A4A4E")
        self.status_label.pack(pady=10)

        self.action_panel = tb.Frame(self.root, style="Action.TFrame", padding=20)
        self.action_panel.pack(fill=X, side=BOTTOM)

        self.button_row = tb.Frame(self.action_panel)
        self.button_row.pack(fill=X)

        actions = [
            ("CREATE", self.prep_create), 
            ("ADD OPTIONS", self.prep_add), 
            ("REMOVE OPTIONS", self.prep_remove), 
            ("UPDATE", self.prep_update),
            ("SEARCH MODE", self.prep_search), 
            ("SORT ENGINE", self.run_sort)
        ]

        for text, cmd in actions:
            btn = tb.Button(self.button_row, text=text, command=cmd, style="Action.TButton", width=15)
            btn.pack(side=LEFT, padx=4)

        self.context_frame = tb.Frame(self.action_panel)
        self.context_frame.pack(fill=X, pady=(15, 0))

    def render_array(self, animate: bool = False) -> None:
        for cell in self.visual_cells:
            cell.destroy()
        self.visual_cells = []
        if self.array_list is None: return

        for i in range(self.array_list.__capacity__):
            val = self.array_list.__A__[i]
            display_text = str(val) if i < self.array_list.__size__ else "—"
            is_active = i < self.array_list.__size__
            
            cell = tb.Label(
                self.array_container, 
                text=display_text,
                foreground="#E6E6E6" if is_active else "#333336",
                background="#1B1B1D" if is_active else "#121214",
                width=7, padding=18, relief="solid", font=("Inter", 11, "bold")
            )
            cell.grid(row=0, column=i, padx=5)
            self.visual_cells.append(cell)
            
            if animate:
                self.root.update()
                time.sleep(0.05)
            
        self.size_label.config(text=f"SIZE: {self.array_list.__size__} / {self.array_list.__capacity__}")

    def prep_create(self) -> None:
        self.clear_context()
        self.add_context_label("TYPE:")
        type_combo = tb.Combobox(self.context_frame, values=["Integer", "String", "Float"], width=10, state="readonly")
        type_combo.current(0); type_combo.pack(side=LEFT, padx=5)
        
        self.add_context_label("CAPACITY:")
        ent = tb.Entry(self.context_frame, width=8); ent.pack(side=LEFT, padx=5)
        
        tb.Button(self.context_frame, text="BUILD ARRAY", bootstyle=LIGHT, 
                  command=lambda: self.run_create(ent.get(), type_combo.get())).pack(side=LEFT, padx=10)

    def prep_add(self) -> None:
        if not self.array_list: return
        self.clear_context()
        mode = tb.Combobox(self.context_frame, values=["Append", "At Start", "After Value", "Before Value"], width=12, state="readonly")
        mode.current(0); mode.pack(side=LEFT, padx=5)
        
        v_ent = tb.Entry(self.context_frame, placeholder_text="Value", width=10); v_ent.pack(side=LEFT, padx=5)
        ref_ent = tb.Entry(self.context_frame, placeholder_text="Ref (if After/Before)", width=15); ref_ent.pack(side=LEFT, padx=5)
        
        tb.Button(self.context_frame, text="EXECUTE", bootstyle=SUCCESS, 
                  command=lambda: self.run_add_complex(mode.get(), v_ent.get(), ref_ent.get())).pack(side=LEFT, padx=10)

    def prep_remove(self) -> None:
        if not self.array_list: return
        self.clear_context()
        mode = tb.Combobox(self.context_frame, values=["At Start", "At End", "By Index", "By Value"], width=12, state="readonly")
        mode.current(1); mode.pack(side=LEFT, padx=5)
        
        val_ent = tb.Entry(self.context_frame, placeholder_text="Index or Value", width=15); val_ent.pack(side=LEFT, padx=5)
        
        tb.Button(self.context_frame, text="REMOVE", bootstyle=DANGER, 
                  command=lambda: self.run_remove_complex(mode.get(), val_ent.get())).pack(side=LEFT, padx=10)

    def prep_update(self) -> None:
        if not self.array_list: return
        self.clear_context()
        self.add_context_label("INDEX:")
        i_ent = tb.Entry(self.context_frame, width=5); i_ent.pack(side=LEFT, padx=5)
        self.add_context_label("VALUE:")
        v_ent = tb.Entry(self.context_frame, width=10); v_ent.pack(side=LEFT, padx=5)
        tb.Button(self.context_frame, text="UPDATE", bootstyle=LIGHT, 
                  command=lambda: self.run_update(i_ent.get(), v_ent.get())).pack(side=LEFT, padx=10)

    def prep_search(self) -> None:
        if not self.array_list: return
        self.clear_context()
        mode = tb.Combobox(self.context_frame, values=["Sequential (index_of)", "Binary Search"], width=18, state="readonly")
        mode.current(0); mode.pack(side=LEFT, padx=5)
        
        v_ent = tb.Entry(self.context_frame, placeholder_text="Search Value", width=15); v_ent.pack(side=LEFT, padx=5)
        
        tb.Button(self.context_frame, text="FIND", bootstyle=INFO, 
                  command=lambda: self.run_search_complex(mode.get(), v_ent.get())).pack(side=LEFT, padx=10)

    def run_create(self, cap: str, t: str) -> None:
        try:
            self.cast_type = {"Integer": int, "String": str, "Float": float}[t]
            self.array_list = FixedArrayList(int(cap))
            self.render_array(animate=True)
            self.status_label.config(text=f"SYSTEM INITIALIZED WITH {t.upper()} ARRAY", foreground="#E6E6E6")
        except Exception as e: self.show_error(str(e))

    def run_add_complex(self, mode: str, val: str, ref: str) -> None:
        if not self.array_list: return
        try:
            v = self.cast_type(val)
            if mode == "Append": self.array_list.append(v)
            elif mode == "At Start": self.array_list.insert_at_start(v)
            elif mode == "After Value": self.array_list.insert_after(v, self.cast_type(ref))
            elif mode == "Before Value": self.array_list.insert_before(v, self.cast_type(ref))
            self.render_array()
        except Exception as e: self.show_error(str(e))

    def run_remove_complex(self, mode: str, target: str) -> None:
        if not self.array_list: return
        try:
            if mode == "At Start": self.array_list.remove_at_start()
            elif mode == "At End": self.array_list.remove_at_end()
            elif mode == "By Index": self.array_list.pop(int(target))
            elif mode == "By Value": self.array_list.remove_value(self.cast_type(target))
            self.render_array()
        except Exception as e: self.show_error(str(e))

    def run_update(self, idx: str, val: str) -> None:
        if not self.array_list: return
        try:
            self.array_list.__setitem__(int(idx), self.cast_type(val))
            self.render_array()
        except Exception as e: self.show_error(str(e))

    def run_search_complex(self, mode: str, val: str) -> None:
        if not self.array_list: return
        try:
            v = self.cast_type(val)
            idx = self.array_list.index_of(v) if "Sequential" in mode else self.array_list.binary_search(v)
            self.render_array()
            self.visual_cells[idx].config(background="#3D5AFE", foreground="white") # type: ignore
            self.status_label.config(text=f"VALUE {val} FOUND AT INDEX {idx}", foreground="#3D5AFE")
        except Exception as e: self.show_error(str(e))

    def run_sort(self) -> None:
        if not self.array_list: return
        try:
            self.array_list.sort()
            self.render_array(animate=True)
            self.status_label.config(text="ARRAY SORTED (INSERTION ALGORITHM)", foreground="#00E676")
        except Exception as e: self.show_error(str(e))

    def clear_context(self) -> None:
        for w in self.context_frame.winfo_children(): w.destroy()
        self.status_label.config(text="", foreground="#6F6F74")

    def add_context_label(self, txt: str) -> None:
        tb.Label(self.context_frame, text=txt, foreground="#9A9A9E", font=("Inter", 9)).pack(side=LEFT, padx=5)

    def show_error(self, msg: str) -> None:
        self.status_label.config(text=f"ERROR: {msg.upper()}", foreground="#FF5252")