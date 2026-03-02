import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from typing import Optional, Callable, Type

from model.FixedArrayList import FixedArrayList


BG = "#1a1a2e"
SURFACE = "#16213e"
CELL_FILL = "#0f3460"
CELL_EMPTY = "#16213e"
CELL_HL = "#e94560"
CELL_DONE = "#4ecca3"
CELL_BORDER = "#2a2a5e"
TEXT_MAIN = "#eeeeee"
TEXT_DIM = "#a8a8b3"
ACCENT = "#4ecca3"
CLR_SUCCESS: str = "#4ecca3"
CLR_DANGER: str = "#e94560"
FONT_MONO = ("Courier New", 10)


def _chain(a: Callable[[], None], b: Callable[[], None]) -> Callable[[], None]:
    def _run() -> None:
        a()
        b()

    return _run


class MatteApp:
    def __init__(self, root: tb.Window) -> None:
        self.root = root
        self.root.title("Fixed Array Engine")
        self.root.geometry("860x580")
        self.root.minsize(520, 420)
        self.root.resizable(True, True)

        self.array: Optional[FixedArrayList] = None
        self.cast_type: Type = str
        self._pending_anim: Optional[str] = None

        self._build_layout()
        self._show_create_controls()
        self.root.bind("<Configure>", self._on_resize)

    # ── Layout ──────────────────────────────────────────────────────────────

    def _build_layout(self) -> None:
        header = tk.Frame(self.root, bg=SURFACE, height=50)
        header.pack(fill=X, side=TOP)
        header.pack_propagate(False)

        tk.Label(
            header,
            text="[ FIXED ARRAY ENGINE ]",
            font=("Courier New", 13, "bold"),
            bg=SURFACE,
            fg=ACCENT,
        ).place(relx=0.5, rely=0.5, anchor="center")

        self.info_lbl = tk.Label(
            header,
            text="create an array to begin",
            font=FONT_MONO,
            bg=SURFACE,
            fg=TEXT_DIM,
        )
        self.info_lbl.place(relx=0.98, rely=0.5, anchor="e")

        self.canvas = tk.Canvas(self.root, bg=BG, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)

        footer = tk.Frame(self.root, bg=SURFACE, height=70)
        footer.pack(fill=X, side=BOTTOM)
        footer.pack_propagate(False)

        self.ctrl = tk.Frame(footer, bg=SURFACE)
        self.ctrl.place(relx=0.5, rely=0.5, anchor="center")

    # ── Info bar ─────────────────────────────────────────────────────────────

    def _set_info(self, msg: str, color: str = TEXT_DIM) -> None:
        self.info_lbl.config(text=msg, fg=color)

    def _refresh_info(self) -> None:
        if self.array:
            n, c = self.array.__size__, self.array.__capacity__
            self.info_lbl.config(text=f"size={n}  cap={c}", fg=ACCENT)
        else:
            self.info_lbl.config(text="create an array to begin", fg=TEXT_DIM)

    # ── Drawing ──────────────────────────────────────────────────────────────

    def _canvas_size(self) -> tuple[int, int]:
        self.root.update_idletasks()
        W = self.canvas.winfo_width()
        H = self.canvas.winfo_height()
        if W < 50:
            W = self.root.winfo_width()
        if H < 50:
            H = max(200, self.root.winfo_height() - 120)
        return W, H

    def _cell_dims(self) -> tuple[int, int, int, int]:
        assert self.array is not None
        W, H = self._canvas_size()
        cap = self.array.__capacity__
        gap = 6
        cell_w = max(20, min(90, (W - 60) // max(cap, 1) - gap))
        cell_h = min(cell_w + 8, max(28, int(H * 0.38)))
        total = cap * (cell_w + gap) - gap
        x0 = (W - total) // 2
        y0 = (H - cell_h) // 2
        return cell_w, cell_h, x0, y0

    def _rounded_rect(
        self, x1: int, y1: int, x2: int, y2: int, r: int, fill: str, outline: str
    ) -> None:
        pts: list[int] = [
            x1 + r,
            y1,
            x2 - r,
            y1,
            x2,
            y1,
            x2,
            y1 + r,
            x2,
            y2 - r,
            x2,
            y2,
            x2 - r,
            y2,
            x1 + r,
            y2,
            x1,
            y2,
            x1,
            y2 - r,
            x1,
            y1 + r,
            x1,
            y1,
        ]
        self.canvas.create_polygon(
            pts, fill=fill, smooth=True, outline=outline, width=2
        )

    def _draw_cell(
        self,
        i: int,
        cell_w: int,
        cell_h: int,
        x0: int,
        y0: int,
        highlight: int,
        done: int,
    ) -> None:
        assert self.array is not None
        gap = 6
        x1 = x0 + i * (cell_w + gap)
        x2 = x1 + cell_w
        y1 = y0
        y2 = y0 + cell_h
        filled = i < self.array.__size__

        if i == highlight:
            fill, outline = CELL_HL, CELL_HL
        elif i == done:
            fill, outline = CELL_DONE, CELL_DONE
        elif filled:
            fill, outline = CELL_FILL, ACCENT
        else:
            fill, outline = CELL_EMPTY, CELL_BORDER

        self._rounded_rect(x1, y1, x2, y2, 7, fill, outline)

        self.canvas.create_text(
            (x1 + x2) // 2, y1 - 10, text=f"{i}", font=("Courier New", 8), fill=TEXT_DIM
        )

        if filled:
            raw = str(self.array.__A__[i])
            txt = raw if len(raw) <= 6 else raw[:5] + "…"
            fsize = max(8, min(16, cell_w // 4))
            self.canvas.create_text(
                (x1 + x2) // 2,
                (y1 + y2) // 2,
                text=txt,
                font=("Courier New", fsize, "bold"),
                fill=TEXT_MAIN,
            )
        else:
            self.canvas.create_text(
                (x1 + x2) // 2,
                (y1 + y2) // 2,
                text="·",
                font=("Courier New", 14),
                fill=TEXT_DIM,
            )

    def _draw_all(self, highlight: int = -1, done: int = -1) -> None:
        self.canvas.delete("all")
        if not self.array:
            return
        cell_w, cell_h, x0, y0 = self._cell_dims()
        for i in range(self.array.__capacity__):
            self._draw_cell(i, cell_w, cell_h, x0, y0, highlight, done)

    # ── Animation ────────────────────────────────────────────────────────────

    def _animate(
        self,
        highlight: int = -1,
        done: int = -1,
        callback: Optional[Callable[[], None]] = None,
    ) -> None:
        if not self.array:
            return
        cap = self.array.__capacity__
        delay = max(15, min(140, 1400 // max(cap, 1)))
        self._anim_step(0, cap, highlight, done, callback, delay)

    def _anim_step(
        self,
        step: int,
        total: int,
        highlight: int,
        done: int,
        callback: Optional[Callable[[], None]],
        delay: int,
    ) -> None:
        if not self.array:
            return
        self.canvas.delete("all")
        cell_w, cell_h, x0, y0 = self._cell_dims()
        for i in range(step + 1):
            self._draw_cell(i, cell_w, cell_h, x0, y0, highlight, done)
        if step < total - 1:
            self.root.after(
                delay,
                lambda: self._anim_step(
                    step + 1, total, highlight, done, callback, delay
                ),
            )
        elif callback is not None:
            self.root.after(80, callback)

    def _on_resize(self, event: Optional[tk.Event] = None) -> None:
        if self.array:
            self._draw_all()

    # ── Panel helpers ────────────────────────────────────────────────────────

    def _clear(self) -> None:
        for w in self.ctrl.winfo_children():
            w.destroy()

    def _btn(
        self,
        text: str,
        cmd: Callable[[], None],
        style: str = "primary",
        width: int = 11,
    ) -> tb.Button:
        b = tb.Button(self.ctrl, text=text, bootstyle=style, width=width, command=cmd)
        b.configure(cursor="hand2")
        return b

    def _lbl(self, text: str) -> tk.Label:
        return tk.Label(self.ctrl, text=text, font=FONT_MONO, bg=SURFACE, fg=TEXT_DIM)

    def _entry(self, var: tb.StringVar, width: int = 10) -> tk.Entry:
        return tk.Entry(
            self.ctrl,
            textvariable=var,
            width=width,
            font=FONT_MONO,
            bg="#0f3460",
            fg=TEXT_MAIN,
            insertbackground=ACCENT,
            relief="flat",
            highlightthickness=1,
            highlightcolor=ACCENT,
            highlightbackground="#2a2a5e",
        )

    # ── CREATE ───────────────────────────────────────────────────────────────

    def _show_create_controls(self) -> None:
        self._clear()
        type_var = tb.StringVar(value="Integer")
        cap_var = tb.StringVar()

        self._lbl("type:").grid(row=0, column=0, padx=(0, 4))
        tb.Combobox(
            self.ctrl,
            values=["Integer", "String", "Float"],
            textvariable=type_var,
            width=9,
            state="readonly",
            font=FONT_MONO,
        ).grid(row=0, column=1, padx=4)
        self._lbl("capacity:").grid(row=0, column=2, padx=(14, 4))
        e = self._entry(cap_var, 8)
        e.grid(row=0, column=3, padx=4)
        e.focus_set()
        self._btn(
            "▶  Create",
            style="success",
            width=12,
            cmd=lambda: self._do_create(type_var.get(), cap_var.get()),
        ).grid(row=0, column=4, padx=(18, 0))

    def _do_create(self, dtype: str, cap: str) -> None:
        typemap: dict[str, Type] = {"integer": int, "string": str, "float": float}
        try:
            self.cast_type = typemap[dtype.lower()]
            self.array = FixedArrayList(int(cap))
            self._set_info("array created!", CLR_SUCCESS)
            # Dibuja directo sin animación para evitar el problema de canvas no listo
            self._draw_all()
            # Luego muestra el menú
            self._show_category_menu()
            self._refresh_info()
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)

    # ── CATEGORY MENU ────────────────────────────────────────────────────────

    def _show_category_menu(self) -> None:
        self._clear()
        items: list[tuple[str, str, Callable[[], None]]] = [
            ("Insert", "primary-outline", self._show_insert_options),
            ("Remove", "danger-outline", self._show_remove_options),
            ("Search", "info-outline", self._show_search_options),
            ("Get", "secondary-outline", self._show_get_options),
            ("Sort", "warning-outline", self._do_sort),
            ("Reset", "light", self._show_create_controls),
        ]
        for j, (name, style, fn) in enumerate(items):
            self._btn(name, fn, style, width=9).grid(row=0, column=j, padx=6)

    # ── INSERT ───────────────────────────────────────────────────────────────

    def _show_insert_options(self) -> None:
        self._clear()
        self._btn("At Start", lambda: self._show_insert_panel("start"), width=10).grid(
            row=0, column=0, padx=6
        )
        self._btn("At End", lambda: self._show_insert_panel("end"), width=10).grid(
            row=0, column=1, padx=6
        )
        self._btn("At Position", lambda: self._show_insert_panel("pos"), width=13).grid(
            row=0, column=2, padx=6
        )
        self._btn("← Back", self._show_category_menu, "secondary", 8).grid(
            row=0, column=3, padx=6
        )

    def _show_insert_panel(self, mode: str) -> None:
        self._clear()
        val_var = tb.StringVar()
        pos_var = tb.StringVar()
        self._lbl("value:").grid(row=0, column=0, padx=(0, 4))
        self._entry(val_var, 12).grid(row=0, column=1, padx=4)
        col = 2
        if mode == "pos":
            self._lbl("pos:").grid(row=0, column=col, padx=(10, 4))
            self._entry(pos_var, 6).grid(row=0, column=col + 1, padx=4)
            col += 2
        cmds: dict[str, Callable[[], None]] = {
            "end": lambda: self._insert_end(val_var.get()),
            "start": lambda: self._insert_start(val_var.get()),
            "pos": lambda: self._insert_at(pos_var.get(), val_var.get()),
        }
        self._btn("▶ Insert", cmds[mode], "success", 10).grid(
            row=0, column=col, padx=(12, 4)
        )
        self._btn("← Back", self._show_insert_options, "secondary", 8).grid(
            row=0, column=col + 1, padx=4
        )

    def _insert_end(self, val: str) -> None:
        try:
            assert self.array is not None
            self.array.append(self.cast_type(val))
            idx = self.array.__size__ - 1
            self._set_info(f"appended → index {idx}", CLR_SUCCESS)
            self._animate(
                done=idx, callback=_chain(self._refresh_info, self._show_category_menu)
            )
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _insert_start(self, val: str) -> None:
        try:
            assert self.array is not None
            self.array.insert_at_start(self.cast_type(val))
            self._set_info("inserted at start", CLR_SUCCESS)
            self._animate(
                done=0, callback=_chain(self._refresh_info, self._show_category_menu)
            )
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _insert_at(self, pos: str, val: str) -> None:
        try:
            assert self.array is not None
            p = int(pos)
            self.array.insert(p, self.cast_type(val))
            self._set_info(f"inserted at index {p}", CLR_SUCCESS)
            self._animate(
                done=p, callback=_chain(self._refresh_info, self._show_category_menu)
            )
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    # ── REMOVE ───────────────────────────────────────────────────────────────

    def _show_remove_options(self) -> None:
        self._clear()
        self._btn("At Start", self._do_remove_start, "danger-outline", 10).grid(
            row=0, column=0, padx=5
        )
        self._btn("At End", self._do_remove_end, "danger-outline", 10).grid(
            row=0, column=1, padx=5
        )
        self._btn("By Index", self._show_remove_index, "danger-outline", 10).grid(
            row=0, column=2, padx=5
        )
        self._btn("By Value", self._show_remove_value, "danger-outline", 10).grid(
            row=0, column=3, padx=5
        )
        self._btn("← Back", self._show_category_menu, "secondary", 8).grid(
            row=0, column=4, padx=5
        )

    def _do_remove_start(self) -> None:
        try:
            assert self.array is not None
            self._draw_all(highlight=0)
            self.array.remove_at_start()
            self._set_info("removed from start", CLR_SUCCESS)
            cb = _chain(self._refresh_info, self._show_category_menu)
            self.root.after(300, lambda: self._animate(callback=cb))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _do_remove_end(self) -> None:
        try:
            assert self.array is not None
            idx = self.array.__size__ - 1
            self._draw_all(highlight=idx)
            self.array.remove_at_end()
            self._set_info("removed from end", CLR_SUCCESS)
            cb = _chain(self._refresh_info, self._show_category_menu)
            self.root.after(300, lambda: self._animate(callback=cb))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _show_remove_index(self) -> None:
        self._clear()
        idx_var = tb.StringVar()
        self._lbl("index:").grid(row=0, column=0, padx=(0, 4))
        self._entry(idx_var, 7).grid(row=0, column=1, padx=4)
        self._btn(
            "▶ Remove", lambda: self._do_remove_at_index(idx_var.get()), "danger", 10
        ).grid(row=0, column=2, padx=12)
        self._btn("← Back", self._show_remove_options, "secondary", 8).grid(
            row=0, column=3, padx=4
        )

    def _do_remove_at_index(self, idx: str) -> None:
        try:
            assert self.array is not None
            p = int(idx)
            self._draw_all(highlight=p)
            self.array.pop(p)
            self._set_info(f"removed index {p}", CLR_SUCCESS)
            cb = _chain(self._refresh_info, self._show_category_menu)
            self.root.after(300, lambda: self._animate(callback=cb))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _show_remove_value(self) -> None:
        self._clear()
        val_var = tb.StringVar()
        self._lbl("value:").grid(row=0, column=0, padx=(0, 4))
        self._entry(val_var, 10).grid(row=0, column=1, padx=4)
        self._btn(
            "▶ Remove", lambda: self._do_remove_value(val_var.get()), "danger", 10
        ).grid(row=0, column=2, padx=12)
        self._btn("← Back", self._show_remove_options, "secondary", 8).grid(
            row=0, column=3, padx=4
        )

    def _do_remove_value(self, val: str) -> None:
        try:
            assert self.array is not None
            self.array.remove_value(self.cast_type(val))
            self._set_info(f"removed '{val}'", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    # ── SEARCH ───────────────────────────────────────────────────────────────

    def _show_search_options(self) -> None:
        self._clear()
        val_var = tb.StringVar()
        self._lbl("value:").grid(row=0, column=0, padx=(0, 4))
        self._entry(val_var, 12).grid(row=0, column=1, padx=4)
        self._btn(
            "Sequential", lambda: self._do_search_seq(val_var.get()), "info-outline", 12
        ).grid(row=0, column=2, padx=8)
        self._btn(
            "Binary", lambda: self._do_search_bin(val_var.get()), "info-outline", 10
        ).grid(row=0, column=3, padx=8)
        self._btn("← Back", self._show_category_menu, "secondary", 8).grid(
            row=0, column=4, padx=4
        )

    def _do_search_seq(self, val: str) -> None:
        try:
            assert self.array is not None
            idx = self.array.index_of(self.cast_type(val))
            self._draw_all(highlight=idx)
            self._set_info(f"sequential → found at [{idx}]", ACCENT)
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
        self._show_category_menu()

    def _do_search_bin(self, val: str) -> None:
        try:
            assert self.array is not None
            idx = self.array.binary_search(self.cast_type(val))
            self._draw_all(highlight=idx)
            self._set_info(f"binary → found at [{idx}]", ACCENT)
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
        self._show_category_menu()

    # ── GET ──────────────────────────────────────────────────────────────────

    def _show_get_options(self) -> None:
        self._clear()
        idx_var = tb.StringVar()
        self._lbl("index:").grid(row=0, column=0, padx=(0, 4))
        self._entry(idx_var, 10).grid(row=0, column=1, padx=4)
        self._btn("▶ Get", lambda: self._do_get(idx_var.get()), "secondary", 10).grid(
            row=0, column=2, padx=10
        )
        self._btn("← Back", self._show_category_menu, "secondary", 8).grid(
            row=0, column=3, padx=4
        )

    def _do_get(self, idx: str) -> None:
        try:
            assert self.array is not None
            val = self.array.get(int(idx))
            self._draw_all(highlight=int(idx))
            self._set_info(f"get([{idx}]) → {val}", ACCENT)
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
        self._show_category_menu()

    # ── SORT ─────────────────────────────────────────────────────────────────

    def _do_sort(self) -> None:
        try:
            assert self.array is not None
            self.array.sort()
            self._set_info("sorted ✓", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

