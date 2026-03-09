import customtkinter as ctk
import tkinter as tk
from typing import Optional, Callable, Type

from model.FixedArrayList import FixedArrayList

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ── Paleta ────────────────────────────────────────────────────────────────────
BG_TOP       = "#181510"
BG_MAIN      = "#1c1e18"
BG_PANEL     = "#211e14"
BORDER       = "#4a3f2a"
TEXT_TITLE   = "#9a7d5a"
TEXT_SUB     = "#6a7a5a"
TEXT_LABEL   = "#8a9070"
INPUT_BG     = "#2a2416"
INPUT_FG     = "#c8b890"
BTN_BG       = "#7aab80"
BTN_HOVER    = "#8fbe95"
BTN_TEXT     = "#1a2a1a"
BTN_RED      = "#8a4a40"
BTN_RED_HV   = "#aa5a50"
BTN_RED_TXT  = "#f0d0c0"
BTN_BLUE     = "#4a6a8a"
BTN_BLUE_HV  = "#5a7a9a"
BTN_BLUE_TXT = "#d0e8f0"
BTN_AMB      = "#8a7a3a"
BTN_AMB_HV   = "#aa9a4a"
BTN_AMB_TXT  = "#f0e8c0"
HATCH        = "#2e2818"
ACCENT       = "#4a4030"
CELL_OUTER   = "#2a2010"
CELL_BORDER  = "#5a4a30"
CELL_INNER   = "#1e1810"
CELL_NOTCH   = "#c8a878"
CELL_HL      = "#8a6a30"
TAB_ACT_BG   = "#232a1e"
TAB_ACT_BRD  = "#7aab80"
TAB_INACT_BG = "#1c1a10"
TAB_INACT_FG = "#5a6050"
TAB_ACT_FG   = "#a0c890"
CLR_SUCCESS  = "#7aab80"
CLR_DANGER   = "#c06050"
FONT_MONO    = ("Courier New", 10)


def _chain(a: Callable[[], None], b: Callable[[], None]) -> Callable[[], None]:
    def _run() -> None:
        a()
        b()
    return _run


# ── Helpers de widgets ────────────────────────────────────────────────────────
def _mk_entry(parent, width=220, height=44) -> ctk.CTkEntry:
    return ctk.CTkEntry(parent, width=width, height=height,
                        fg_color=INPUT_BG, border_color=BORDER, border_width=1,
                        text_color=INPUT_FG, font=("Courier New", 14), corner_radius=4)

def _mk_label(parent, text) -> ctk.CTkLabel:
    return ctk.CTkLabel(parent, text=text, font=("Courier New", 14, "bold"),
                        text_color=TEXT_LABEL)

def _mk_btn(parent, text, cmd,
            fg=BTN_BG, hv=BTN_HOVER, tc=BTN_TEXT, w=160) -> ctk.CTkButton:
    return ctk.CTkButton(parent, text=text, command=cmd,
                         width=w, height=44, fg_color=fg, hover_color=hv,
                         text_color=tc, font=("Courier New", 13, "bold"),
                         corner_radius=4, cursor="hand2")


# ── Decoraciones canvas ───────────────────────────────────────────────────────
def _draw_top_deco(canvas: tk.Canvas) -> None:
    canvas.update_idletasks()
    canvas.create_line(200, 14, 390, 14, fill=ACCENT, width=1)
    canvas.create_line(390, 14, 420, 4,  fill=ACCENT, width=1)
    canvas.create_line(420, 4, 1060, 4,  fill=ACCENT, width=1)
    canvas.create_rectangle(1060, 0, 1180, 28, fill=BORDER, outline="")
    for i in range(20):
        x0 = 1192 + i * 8
        canvas.create_line(x0, 28, x0 + 14, 0, fill=HATCH, width=1)


def _draw_glow(canvas: tk.Canvas) -> None:
    canvas.update_idletasks()
    W, H = canvas.winfo_width(), canvas.winfo_height()
    if W < 2:
        return
    for color, rx, ry in [("#1f2a1f", .70, .80), ("#1c261c", .60, .70), ("#192219", .50, .58)]:
        x0 = int(W * (0.5 - rx / 2)); x1 = int(W * (0.5 + rx / 2))
        y0 = int(H * (0.5 - ry / 2)); y1 = int(H * (0.5 + ry / 2))
        canvas.create_oval(x0, y0, x1, y1, fill=color, outline="")


# ══════════════════════════════════════════════════════════════════════════════
#  Canvas de celdas del array  (visual estilo imagen)
# ══════════════════════════════════════════════════════════════════════════════
class _ArrayCanvas(tk.Canvas):
    CELL_W   = 118
    CELL_H   = 130
    CELL_PAD = 5
    NOTCH_W  = 46
    NOTCH_H  = 13

    def __init__(self, master, **kw):
        super().__init__(master, bg=BG_MAIN, highlightthickness=0, **kw)
        self.array: Optional[FixedArrayList] = None
        self._highlight = -1
        self._done      = -1

    def set_array(self, arr: FixedArrayList) -> None:
        self.array = arr
        self._highlight = -1
        self._done      = -1
        self.after(80, self.draw_all)

    def draw_all(self, highlight: int = -1, done: int = -1) -> None:
        self._highlight = highlight
        self._done      = done
        self._render()

    def _render(self) -> None:
        self.delete("all")
        if self.array is None:
            return
        cap = self.array.__capacity__
        cw, ch, cp = self.CELL_W, self.CELL_H, self.CELL_PAD
        total_w = cap * cw + (cap - 1) * cp
        self.update_idletasks()
        # Usar el ancho del widget propio; si aún no está listo, del master
        W = self.winfo_width()
        if W < 10:
            W = self.master.winfo_width()
        if W < 10:
            W = 1200

        rpx, rpy = 28, 18
        rx0 = (W - total_w) // 2 - rpx
        rx1 = rx0 + total_w + rpx * 2
        ry0 = 16
        ry1 = ry0 + ch + rpy * 2

        # Rail exterior
        self._rrect(rx0, ry0, rx1, ry1, 14,
                    fill=CELL_OUTER, outline=CELL_BORDER, width=2)

        # Indicadores laterales dorados
        for sx in [rx0 + 7, rx1 - 17]:
            my = (ry0 + ry1) // 2
            self.create_rectangle(sx, my - 20, sx + 10, my + 20,
                                  fill=CELL_NOTCH, outline="")

        ox = (W - total_w) // 2
        oy = ry0 + rpy
        for i in range(cap):
            x0 = ox + i * (cw + cp)
            self._draw_cell(x0, oy, x0 + cw, oy + ch, i)

        self.configure(height=ry1 + 22)

    def _draw_cell(self, x0, y0, x1, y1, idx):
        nh = self.NOTCH_H
        nw = self.NOTCH_W // 2
        nx = (x0 + x1) // 2

        filled = self.array is not None and idx < self.array.__size__

        if idx == self._highlight:
            outer = CELL_HL
        elif idx == self._done:
            outer = "#4a7a50"
        else:
            outer = "#2e2214"

        self._rrect(x0, y0, x1, y1, 9, fill=outer, outline=CELL_BORDER, width=1)

        # Muesca superior
        self.create_rectangle(nx - nw, y0 - 1, nx + nw, y0 + nh,
                              fill="#272010", outline=CELL_BORDER, width=1)
        self.create_rectangle(nx - nw + 7, y0 + 3, nx + nw - 7, y0 + nh - 3,
                              fill=CELL_NOTCH, outline="")

        # Interior oscuro
        pad = 9
        self._rrect(x0 + pad, y0 + nh + 5, x1 - pad, y1 - pad, 7,
                    fill=CELL_INNER, outline=CELL_BORDER, width=1)

        # Índice
        self.create_text(x0 + pad + 7, y0 + nh + 11,
                         text=str(idx), fill="#5a4a30",
                         font=("Courier New", 8), anchor="nw")

        # Valor
        if filled and self.array.__A__[idx] is not None:
            raw = str(self.array.__A__[idx])
            txt = raw if len(raw) <= 7 else raw[:6] + "…"
            self.create_text((x0 + x1) // 2, (y0 + nh + 5 + y1 - pad) // 2,
                             text=txt, fill=INPUT_FG,
                             font=("Courier New", 12, "bold"))
        else:
            self.create_text((x0 + x1) // 2, (y0 + nh + 5 + y1 - pad) // 2,
                             text="·", fill="#4a4030", font=("Courier New", 14))

    def _rrect(self, x0, y0, x1, y1, r, **kw):
        self.create_polygon(
            x0+r, y0,  x1-r, y0,  x1, y0,    x1, y0+r,
            x1, y1-r,  x1, y1,    x1-r, y1,  x0+r, y1,
            x0, y1,    x0, y1-r,  x0, y0+r,  x0, y0,
            smooth=True, **kw)


# ══════════════════════════════════════════════════════════════════════════════
#  MatteApp  — reescrita en customtkinter, misma lógica que el view original
# ══════════════════════════════════════════════════════════════════════════════
class MatteApp:
    def __init__(self, root: ctk.CTk) -> None:
        self.root = root
        self.root.title("Fixed Array Engine")
        self.root.geometry("1380x760")
        self.root.resizable(True, True)
        self.root.configure(fg_color=BG_MAIN)

        self.array: Optional[FixedArrayList] = None
        self.cast_type: Type = str

        self._build_layout()
        self._show_create_controls()
        self.root.bind("<Configure>", self._on_resize)

    # ── Layout ────────────────────────────────────────────────────────────────

    def _build_layout(self) -> None:
        # Header
        self._header = ctk.CTkFrame(self.root, fg_color=BG_TOP,
                                     corner_radius=0, height=130)
        self._header.pack(fill="x", side="top")
        self._header.pack_propagate(False)

        self._title_lbl = ctk.CTkLabel(
            self._header, text="[ FIXED ARRAY ENGINE ]",
            font=("Courier New", 44, "bold"), text_color=TEXT_TITLE)
        self._title_lbl.pack(pady=(26, 2))

        self._sub_lbl = ctk.CTkLabel(
            self._header, text="create an array to begin",
            font=("Courier New", 16), text_color=TEXT_SUB)
        self._sub_lbl.pack()

        self.info_lbl = ctk.CTkLabel(
            self._header, text="",
            font=("Courier New", 13), text_color=TEXT_SUB)
        self.info_lbl.place(relx=0.98, rely=0.5, anchor="e")

        # Línea decorativa
        deco = tk.Canvas(self.root, height=28, bg=BG_MAIN, highlightthickness=0)
        deco.pack(fill="x")
        self.root.after(60, lambda: _draw_top_deco(deco))

        # Centro: glow debajo, array canvas encima — ambos con pack
        self._center = ctk.CTkFrame(self.root, fg_color=BG_MAIN, corner_radius=0)
        self._center.pack(fill="both", expand=True)

        self.canvas = _ArrayCanvas(self._center, height=220)
        self.canvas.pack(fill="x", pady=(30, 0))

        self._glow_cv = tk.Canvas(self._center, bg=BG_MAIN, highlightthickness=0)
        self._glow_cv.pack(fill="both", expand=True)

        # Panel inferior (footer)
        self._footer = ctk.CTkFrame(self.root, fg_color=BG_PANEL,
                                     corner_radius=0, height=110)
        self._footer.pack(fill="x", side="bottom")
        self._footer.pack_propagate(False)
        tk.Canvas(self._footer, height=2, bg=ACCENT,
                  highlightthickness=0).pack(fill="x")

        self.ctrl = ctk.CTkFrame(self._footer, fg_color="transparent")
        self.ctrl.place(relx=0.5, rely=0.55, anchor="center")

    def _place_canvas(self) -> None:
        self._glow_cv.delete("all")
        _draw_glow(self._glow_cv)
        self.canvas._render()

    # ── Info bar ──────────────────────────────────────────────────────────────

    def _set_info(self, msg: str, color: str = TEXT_SUB) -> None:
        self.info_lbl.configure(text=msg, text_color=color)

    def _refresh_info(self) -> None:
        if self.array:
            n, c = self.array.__size__, self.array.__capacity__
            self._set_info(f"size={n}  cap={c}", CLR_SUCCESS)
        else:
            self._set_info("create an array to begin", TEXT_SUB)

    # ── Draw / Animate ────────────────────────────────────────────────────────

    def _draw_all(self, highlight: int = -1, done: int = -1) -> None:
        self.canvas.draw_all(highlight, done)

    def _animate(self, highlight: int = -1, done: int = -1,
                 callback: Optional[Callable[[], None]] = None) -> None:
        if not self.array:
            return
        cap = self.array.__capacity__
        delay = max(15, min(140, 1400 // max(cap, 1)))
        self._anim_step(0, cap, highlight, done, callback, delay)

    def _anim_step(self, step: int, total: int, highlight: int, done: int,
                   callback: Optional[Callable[[], None]], delay: int) -> None:
        if not self.array:
            return
        self.canvas.delete("all")
        cw, ch, cp = self.canvas.CELL_W, self.canvas.CELL_H, self.canvas.CELL_PAD
        total_w = self.array.__capacity__ * cw + (self.array.__capacity__ - 1) * cp
        W = self.canvas.winfo_width() or 1200
        rpx, rpy = 28, 18
        rx0 = (W - total_w) // 2 - rpx
        rx1 = rx0 + total_w + rpx * 2
        ry0 = 16; ry1 = ry0 + ch + rpy * 2
        self.canvas._rrect(rx0, ry0, rx1, ry1, 14, fill=CELL_OUTER, outline=CELL_BORDER, width=2)
        for sx in [rx0 + 7, rx1 - 17]:
            my = (ry0 + ry1) // 2
            self.canvas.create_rectangle(sx, my - 20, sx + 10, my + 20, fill=CELL_NOTCH, outline="")
        ox = (W - total_w) // 2; oy = ry0 + rpy
        for i in range(step + 1):
            x0 = ox + i * (cw + cp)
            self.canvas._highlight = highlight
            self.canvas._done = done
            self.canvas._draw_cell(x0, oy, x0 + cw, oy + ch, i)

        if step < total - 1:
            self.root.after(delay,
                lambda: self._anim_step(step+1, total, highlight, done, callback, delay))
        elif callback is not None:
            self.root.after(80, callback)

    def _on_resize(self, event=None) -> None:
        if self.array:
            self.canvas._render()

    # ── Panel helpers ─────────────────────────────────────────────────────────

    def _clear(self) -> None:
        for w in self.ctrl.winfo_children():
            w.destroy()

    # ── Pantalla CREATE ───────────────────────────────────────────────────────

    def _show_create_controls(self) -> None:
        # Restaurar header al estado inicial
        self._title_lbl.configure(text="[ FIXED ARRAY ENGINE ]")
        self._sub_lbl.configure(text="create an array to begin")
        self._set_info("")

        self._clear()
        type_var = ctk.StringVar(value="Integer")
        cap_var  = ctk.StringVar()

        _mk_label(self.ctrl, "type:").grid(row=0, column=0, padx=(0, 8))
        ctk.CTkOptionMenu(
            self.ctrl, values=["Integer", "String", "Float"],
            variable=type_var, width=180, height=44,
            fg_color=INPUT_BG, button_color=BORDER, button_hover_color=HATCH,
            text_color=INPUT_FG, dropdown_fg_color=INPUT_BG,
            dropdown_text_color=INPUT_FG, dropdown_hover_color=HATCH,
            font=("Courier New", 14), dropdown_font=("Courier New", 13),
            corner_radius=4
        ).grid(row=0, column=1, padx=(0, 24))

        _mk_label(self.ctrl, "capacity:").grid(row=0, column=2, padx=(0, 8))
        e = _mk_entry(self.ctrl, width=260)
        e.configure(textvariable=cap_var)
        e.grid(row=0, column=3, padx=(0, 24))
        e.focus_set()
        e.bind("<Return>", lambda ev: self._do_create(type_var.get(), cap_var.get()))

        _mk_btn(self.ctrl, "▶  Create",
                lambda: self._do_create(type_var.get(), cap_var.get()),
                w=200).grid(row=0, column=4)

    def _do_create(self, dtype: str, cap: str) -> None:
        typemap: dict[str, Type] = {"integer": int, "string": str, "float": float}
        try:
            self.cast_type = typemap[dtype.lower()]
            self.array = FixedArrayList(int(cap))
            self._set_info("array created!", CLR_SUCCESS)
            self.canvas.set_array(self.array)
            self.root.after(150, self.canvas._render)
            self._show_category_menu()
            self._refresh_info()
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)

    # ── Menú de categorías ────────────────────────────────────────────────────

    def _show_category_menu(self) -> None:
        self._title_lbl.configure(text="[ ARRAY ENGINE OPERATIONS DASHBOARD ]",
                                   font=("Courier New", 33, "bold"))
        self._sub_lbl.configure(text="interact with your array")
        self._clear()

        items = [
            ("INSERT",  BTN_BG,   BTN_HOVER,   BTN_TEXT,    self._show_insert_options),
            ("REMOVE",  BTN_RED,  BTN_RED_HV,  BTN_RED_TXT, self._show_remove_options),
            ("SORT",    BTN_AMB,  BTN_AMB_HV,  BTN_AMB_TXT, self._show_sort_options),
            ("SEARCH",  BTN_BLUE, BTN_BLUE_HV, BTN_BLUE_TXT,self._show_search_options),
            ("GET",     BTN_BG,   BTN_HOVER,   BTN_TEXT,    self._show_get_options),
            ("RESET",   BORDER,   ACCENT,      INPUT_FG,    self._show_create_controls),
        ]
        for j, (name, fg, hv, tc, fn) in enumerate(items):
            _mk_btn(self.ctrl, name, fn, fg=fg, hv=hv, tc=tc, w=150).grid(
                row=0, column=j, padx=8)

    # ── INSERT ────────────────────────────────────────────────────────────────

    def _show_insert_options(self) -> None:
        self._clear()
        ops = [
            ("At Start",     lambda: self._show_insert_panel("start")),
            ("At End",       lambda: self._show_insert_panel("end")),
            ("At Position",  lambda: self._show_insert_panel("pos")),
            ("After Value",  lambda: self._show_insert_panel("after")),
            ("Before Value", lambda: self._show_insert_panel("before")),
        ]
        for j, (name, fn) in enumerate(ops):
            _mk_btn(self.ctrl, name, fn, w=140).grid(row=0, column=j, padx=6)
        _mk_btn(self.ctrl, "← Back", self._show_category_menu,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(
            row=0, column=len(ops), padx=6)

    def _show_insert_panel(self, mode: str) -> None:
        self._clear()
        val_var = ctk.StringVar()
        ref_var = ctk.StringVar()

        _mk_label(self.ctrl, "value:").grid(row=0, column=0, padx=(0, 6))
        val_e = _mk_entry(self.ctrl, width=220)
        val_e.configure(textvariable=val_var)
        val_e.grid(row=0, column=1, padx=(0, 18))
        val_e.focus_set()

        col = 2
        if mode in ("pos", "after", "before"):
            lbl = {"pos": "index:", "after": "after:", "before": "before:"}[mode]
            _mk_label(self.ctrl, lbl).grid(row=0, column=col, padx=(0, 6))
            ref_e = _mk_entry(self.ctrl, width=160)
            ref_e.configure(textvariable=ref_var)
            ref_e.grid(row=0, column=col + 1, padx=(0, 18))
            col += 2

        cmds = {
            "end":    lambda: self._insert_end(val_var.get()),
            "start":  lambda: self._insert_start(val_var.get()),
            "pos":    lambda: self._insert_at(ref_var.get(), val_var.get()),
            "after":  lambda: self._insert_after(val_var.get(), ref_var.get()),
            "before": lambda: self._insert_before(val_var.get(), ref_var.get()),
        }
        _mk_btn(self.ctrl, "▶ Insert", cmds[mode], w=150).grid(
            row=0, column=col, padx=(0, 8))
        _mk_btn(self.ctrl, "← Back", self._show_insert_options,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(
            row=0, column=col + 1, padx=0)

    def _insert_end(self, val: str) -> None:
        try:
            assert self.array is not None
            self.array.append(self.cast_type(val))
            idx = self.array.__size__ - 1
            self._set_info(f"appended → index {idx}", CLR_SUCCESS)
            self._animate(done=idx,
                          callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _insert_start(self, val: str) -> None:
        try:
            assert self.array is not None
            self.array.insert_at_start(self.cast_type(val))
            self._set_info("inserted at start", CLR_SUCCESS)
            self._animate(done=0,
                          callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _insert_at(self, pos: str, val: str) -> None:
        try:
            assert self.array is not None
            p = int(pos)
            self.array.insert(p, self.cast_type(val))
            self._set_info(f"inserted at index {p}", CLR_SUCCESS)
            self._animate(done=p,
                          callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _insert_after(self, val: str, reference: str) -> None:
        try:
            assert self.array is not None
            self.array.insert_after(self.cast_type(val), self.cast_type(reference))
            self._set_info(f"inserted after '{reference}'", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    def _insert_before(self, val: str, reference: str) -> None:
        try:
            assert self.array is not None
            self.array.insert_before(self.cast_type(val), self.cast_type(reference))
            self._set_info(f"inserted before '{reference}'", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    # ── REMOVE ────────────────────────────────────────────────────────────────

    def _show_remove_options(self) -> None:
        self._clear()
        ops = [
            ("At Start", self._do_remove_start),
            ("At End",   self._do_remove_end),
            ("By Index", self._show_remove_index),
            ("By Value", self._show_remove_value),
        ]
        for j, (name, fn) in enumerate(ops):
            _mk_btn(self.ctrl, name, fn,
                    fg=BTN_RED, hv=BTN_RED_HV, tc=BTN_RED_TXT, w=140).grid(
                row=0, column=j, padx=6)
        _mk_btn(self.ctrl, "← Back", self._show_category_menu,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(
            row=0, column=len(ops), padx=6)

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
        idx_var = ctk.StringVar()
        _mk_label(self.ctrl, "index:").grid(row=0, column=0, padx=(0, 6))
        e = _mk_entry(self.ctrl, width=200)
        e.configure(textvariable=idx_var)
        e.grid(row=0, column=1, padx=(0, 18))
        e.focus_set()
        e.bind("<Return>", lambda ev: self._do_remove_at_index(idx_var.get()))
        _mk_btn(self.ctrl, "▶ Remove",
                lambda: self._do_remove_at_index(idx_var.get()),
                fg=BTN_RED, hv=BTN_RED_HV, tc=BTN_RED_TXT, w=150).grid(
            row=0, column=2, padx=(0, 8))
        _mk_btn(self.ctrl, "← Back", self._show_remove_options,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(row=0, column=3)

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
        val_var = ctk.StringVar()
        _mk_label(self.ctrl, "value:").grid(row=0, column=0, padx=(0, 6))
        e = _mk_entry(self.ctrl, width=220)
        e.configure(textvariable=val_var)
        e.grid(row=0, column=1, padx=(0, 18))
        e.focus_set()
        e.bind("<Return>", lambda ev: self._do_remove_value(val_var.get()))
        _mk_btn(self.ctrl, "▶ Remove",
                lambda: self._do_remove_value(val_var.get()),
                fg=BTN_RED, hv=BTN_RED_HV, tc=BTN_RED_TXT, w=150).grid(
            row=0, column=2, padx=(0, 8))
        _mk_btn(self.ctrl, "← Back", self._show_remove_options,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(row=0, column=3)

    def _do_remove_value(self, val: str) -> None:
        try:
            assert self.array is not None
            self.array.remove_value(self.cast_type(val))
            self._set_info(f"removed '{val}'", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
            self._show_category_menu()

    # ── SORT ──────────────────────────────────────────────────────────────────
    # Todos los algoritmos de FixedArrayList expuestos como botones

    def _show_sort_options(self) -> None:
        self._clear()
        algos = [
            ("Insertion Sort", self._do_sort_insertion, BTN_BG,   BTN_HOVER,   BTN_TEXT),
            ("Selection Sort", self._do_sort_selection, BTN_BG,   BTN_HOVER,   BTN_TEXT),
            ("Bubble Sort",    self._do_sort_bubble,    BTN_AMB,  BTN_AMB_HV,  BTN_AMB_TXT),
            ("Quick Sort",     self._do_sort_quick,     BTN_BLUE, BTN_BLUE_HV, BTN_BLUE_TXT),
        ]
        for j, (name, fn, fg, hv, tc) in enumerate(algos):
            _mk_btn(self.ctrl, name, fn, fg=fg, hv=hv, tc=tc, w=150).grid(
                row=0, column=j, padx=6)
        _mk_btn(self.ctrl, "← Back", self._show_category_menu,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(
            row=0, column=len(algos), padx=6)

    def _do_sort_insertion(self) -> None:
        try:
            assert self.array is not None
            self.array.sort()
            self._set_info("insertion sort ✓", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER); self._show_category_menu()

    def _do_sort_selection(self) -> None:
        try:
            assert self.array is not None
            self.array.selection_sort()
            self._set_info("selection sort ✓", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER); self._show_category_menu()

    def _do_sort_bubble(self) -> None:
        try:
            assert self.array is not None
            self.array.bubble_sort()
            self._set_info("bubble sort ✓", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER); self._show_category_menu()

    def _do_sort_quick(self) -> None:
        try:
            assert self.array is not None
            self.array.quick_sort()
            self._set_info("quick sort ✓", CLR_SUCCESS)
            self._animate(callback=_chain(self._refresh_info, self._show_category_menu))
        except Exception as e:
            self._set_info(str(e), CLR_DANGER); self._show_category_menu()

    # ── SEARCH ────────────────────────────────────────────────────────────────

    def _show_search_options(self) -> None:
        self._clear()
        val_var = ctk.StringVar()
        _mk_label(self.ctrl, "value:").grid(row=0, column=0, padx=(0, 6))
        e = _mk_entry(self.ctrl, width=240)
        e.configure(textvariable=val_var)
        e.grid(row=0, column=1, padx=(0, 18))
        e.focus_set()
        _mk_btn(self.ctrl, "Sequential",
                lambda: self._do_search_seq(val_var.get()),
                fg=BTN_BLUE, hv=BTN_BLUE_HV, tc=BTN_BLUE_TXT, w=150).grid(
            row=0, column=2, padx=(0, 8))
        _mk_btn(self.ctrl, "Binary ★",
                lambda: self._do_search_bin(val_var.get()),
                fg=BTN_AMB, hv=BTN_AMB_HV, tc=BTN_AMB_TXT, w=140).grid(
            row=0, column=3, padx=(0, 18))
        _mk_btn(self.ctrl, "← Back", self._show_category_menu,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(row=0, column=4)

    def _do_search_seq(self, val: str) -> None:
        try:
            assert self.array is not None
            idx = self.array.index_of(self.cast_type(val))
            self._draw_all(highlight=idx)
            self._set_info(f"sequential → found at [{idx}]", CLR_SUCCESS)
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
        self._show_category_menu()

    def _do_search_bin(self, val: str) -> None:
        try:
            assert self.array is not None
            idx = self.array.binary_search(self.cast_type(val))
            self._draw_all(highlight=idx)
            self._set_info(f"binary → found at [{idx}]", CLR_SUCCESS)
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
        self._show_category_menu()

    # ── GET ───────────────────────────────────────────────────────────────────

    def _show_get_options(self) -> None:
        self._clear()
        idx_var = ctk.StringVar()
        _mk_label(self.ctrl, "index:").grid(row=0, column=0, padx=(0, 6))
        e = _mk_entry(self.ctrl, width=200)
        e.configure(textvariable=idx_var)
        e.grid(row=0, column=1, padx=(0, 18))
        e.focus_set()
        e.bind("<Return>", lambda ev: self._do_get(idx_var.get()))
        _mk_btn(self.ctrl, "▶ Get",
                lambda: self._do_get(idx_var.get()), w=140).grid(
            row=0, column=2, padx=(0, 18))
        _mk_btn(self.ctrl, "← Back", self._show_category_menu,
                fg=BORDER, hv=ACCENT, tc=INPUT_FG, w=110).grid(row=0, column=3)

    def _do_get(self, idx: str) -> None:
        try:
            assert self.array is not None
            val = self.array.get(int(idx))
            self._draw_all(highlight=int(idx))
            self._set_info(f"get([{idx}]) → {val}", CLR_SUCCESS)
        except Exception as e:
            self._set_info(str(e), CLR_DANGER)
        self._show_category_menu()