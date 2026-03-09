# FixedArrayListView — Documentación del Frontend

> **Archivo:** `view/FixedArrayListView.py`  
> **Librería UI:** `customtkinter` (ctk) + `tkinter` nativo (tk)  
> **Modelo:** `model.FixedArrayList.FixedArrayList`

---

## 1. ¿Qué es customtkinter?

`customtkinter` es una librería construida **encima de tkinter** que moderniza sus widgets. La importas así:

```python
import customtkinter as ctk
import tkinter as tk  # tkinter nativo también se usa para Canvas
```

Antes de crear cualquier ventana, se configuran dos cosas globales:

```python
ctk.set_appearance_mode("dark")       # "dark" | "light" | "system"
ctk.set_default_color_theme("dark-blue")  # tema base de colores
```

Estas dos líneas **deben ir al inicio del módulo**, antes de instanciar nada.

---

## 2. Estructura general de la app

```
MatteApp
├── ctk.CTkFrame  → _header         (título, subtítulo, info_lbl)
├── tk.Canvas     → deco            (líneas decorativas superiores)
├── ctk.CTkFrame  → _center
│   ├── _ArrayCanvas  → canvas      (celdas del array — tk.Canvas)
│   └── tk.Canvas     → _glow_cv   (fondo con resplandor verde)
└── ctk.CTkFrame  → _footer
    └── ctk.CTkFrame  → ctrl        (controles dinámicos — cambia según operación)
```

La ventana raíz es un `ctk.CTk()` que se pasa desde el `main.py`.

---

## 3. La ventana raíz — `ctk.CTk`

```python
# main.py
import customtkinter as ctk
from view.FixedArrayListView import MatteApp

def main():
    root = ctk.CTk()
    MatteApp(root)
    root.mainloop()
```

| Método / Propiedad | Qué hace |
|---|---|
| `ctk.CTk()` | Crea la ventana principal (equivale a `tk.Tk()`) |
| `root.title("texto")` | Título de la barra de la ventana |
| `root.geometry("1380x760")` | Tamaño inicial `"anchoXalto"` |
| `root.resizable(True, True)` | Permite redimensionar (ancho, alto) |
| `root.configure(fg_color=COLOR)` | Color de fondo de la ventana |
| `root.mainloop()` | Inicia el loop de eventos — bloquea hasta cerrar |
| `root.after(ms, callback)` | Ejecuta `callback` después de `ms` milisegundos |
| `root.bind("<Configure>", fn)` | Llama `fn` cada vez que la ventana cambia de tamaño |

---

## 4. Widgets de customtkinter usados

### 4.1 `ctk.CTkFrame` — contenedor

El equivalente moderno de `tk.Frame`. Se usa para agrupar widgets y darles fondo.

```python
frame = ctk.CTkFrame(
    parent,
    fg_color="#211e14",   # color de fondo
    corner_radius=0,      # 0 = sin bordes redondeados
    height=130            # altura fija en píxeles
)
frame.pack(fill="x")          # ocupa todo el ancho
frame.pack_propagate(False)   # impide que los hijos cambien el tamaño del frame
```

> **`pack_propagate(False)`** es clave cuando le pones `height` fijo a un frame — sin esto, el frame se encoge al tamaño de sus hijos.

---

### 4.2 `ctk.CTkLabel` — texto

```python
label = ctk.CTkLabel(
    parent,
    text="[ FIXED ARRAY ENGINE ]",
    font=("Courier New", 44, "bold"),  # (familia, tamaño, estilo)
    text_color="#9a7d5a"
)
label.pack(pady=(26, 2))   # padding vertical: (arriba, abajo)

# Para actualizar el texto después:
label.configure(text="nuevo texto", text_color="#color")
```

---

### 4.3 `ctk.CTkButton` — botón

```python
btn = ctk.CTkButton(
    parent,
    text="▶  Create",
    command=mi_funcion,       # callback al hacer click
    width=200,
    height=44,
    fg_color="#7aab80",       # color de fondo normal
    hover_color="#8fbe95",    # color al pasar el mouse
    text_color="#1a2a1a",
    font=("Courier New", 13, "bold"),
    corner_radius=4,
    cursor="hand2"            # cursor de mano al hover
)
btn.grid(row=0, column=4)
```

La función `_mk_btn` del view es un helper que crea botones con los valores por defecto del tema:

```python
def _mk_btn(parent, text, cmd, fg=BTN_BG, hv=BTN_HOVER, tc=BTN_TEXT, w=160):
    return ctk.CTkButton(parent, text=text, command=cmd,
                         width=w, height=44, fg_color=fg, hover_color=hv,
                         text_color=tc, font=("Courier New", 13, "bold"),
                         corner_radius=4, cursor="hand2")
```

---

### 4.4 `ctk.CTkEntry` — campo de texto

```python
entry = ctk.CTkEntry(
    parent,
    width=260,
    height=44,
    fg_color="#2a2416",       # fondo del input
    border_color="#4a3f2a",   # color del borde
    border_width=1,
    text_color="#c8b890",
    font=("Courier New", 14),
    corner_radius=4
)
entry.grid(row=0, column=3, padx=(0, 24))

# Leer el valor:
valor = entry.get()

# Vincular a una variable:
var = ctk.StringVar()
entry.configure(textvariable=var)
valor = var.get()

# Escuchar Enter:
entry.bind("<Return>", lambda event: mi_funcion())

# Poner el foco al abrir el panel:
entry.focus_set()
```

---

### 4.5 `ctk.CTkOptionMenu` — menú desplegable

```python
variable = ctk.StringVar(value="Integer")

menu = ctk.CTkOptionMenu(
    parent,
    values=["Integer", "String", "Float"],
    variable=variable,
    width=180,
    height=44,
    fg_color="#2a2416",
    button_color="#4a3f2a",
    button_hover_color="#2e2818",
    text_color="#c8b890",
    dropdown_fg_color="#2a2416",
    dropdown_text_color="#c8b890",
    dropdown_hover_color="#2e2818",
    font=("Courier New", 14),
    dropdown_font=("Courier New", 13),
    corner_radius=4
)
menu.grid(row=0, column=1)

# Leer el valor seleccionado:
seleccion = variable.get()   # "Integer", "String" o "Float"
```

---

### 4.6 `ctk.StringVar` — variable reactiva

`ctk.StringVar` (y `tk.StringVar`) son variables observables que se pueden vincular a widgets.

```python
var = ctk.StringVar(value="valor_inicial")

# Leer
print(var.get())

# Escribir
var.set("nuevo valor")

# Vincular a un entry
entry.configure(textvariable=var)
```

---

## 5. Gestores de layout

customtkinter usa los mismos tres gestores de tkinter: `pack`, `grid` y `place`. **No mezcles `pack` y `grid` en el mismo contenedor padre.**

### `pack` — apilado automático

```python
widget.pack(fill="x")              # ocupa todo el ancho
widget.pack(fill="both", expand=True)  # ocupa todo el espacio restante
widget.pack(side="bottom")         # se pega al fondo
widget.pack(pady=(30, 0))          # padding vertical (arriba, abajo)
widget.pack(padx=10)               # padding horizontal
```

### `grid` — cuadrícula

Se usa en el panel de controles (`self.ctrl`) porque necesitamos alinear etiquetas, inputs y botones en columnas:

```python
widget.grid(row=0, column=0)               # fila 0, columna 0
widget.grid(row=0, column=1, padx=(0, 24)) # padding horizontal
widget.grid(row=0, column=2, sticky="e")   # alineado a la derecha
```

### `place` — posición absoluta o relativa

```python
widget.place(relx=0.5, rely=0.55, anchor="center")  # centrado exacto
widget.place(relx=0.98, rely=0.5, anchor="e")        # pegado a la derecha
widget.place(x=0, y=0, relwidth=1.0)                 # esquina superior, ancho completo
```

> En el view, `self.ctrl` usa `place(relx=0.5, rely=0.55, anchor="center")` para que los controles queden centrados en el footer sin importar el tamaño de la ventana.

---

## 6. `tk.Canvas` — dibujo vectorial

`customtkinter` no tiene un canvas propio, así que se usa el `tk.Canvas` nativo para todo lo que requiere dibujo custom: las celdas del array, el glow y las líneas decorativas.

```python
canvas = tk.Canvas(
    parent,
    bg="#1c1e18",
    highlightthickness=0,  # quita el borde azul por defecto de tkinter
    height=220
)
canvas.pack(fill="x")
```

### Primitivas de dibujo

```python
# Línea
canvas.create_line(x0, y0, x1, y1, fill="#color", width=1)

# Rectángulo
canvas.create_rectangle(x0, y0, x1, y1, fill="#color", outline="#color")

# Óvalo / Elipse
canvas.create_oval(x0, y0, x1, y1, fill="#color", outline="")

# Polígono (usado para esquinas redondeadas)
canvas.create_polygon([x0,y0, x1,y1, ...], fill="#color", smooth=True, outline="#color", width=2)

# Texto
canvas.create_text(cx, cy, text="hola", font=("Courier New", 12, "bold"),
                   fill="#color", anchor="nw")  # anchor: "nw","center","e", etc.

# Limpiar todo
canvas.delete("all")

# Cambiar tamaño dinámicamente
canvas.configure(height=nuevo_alto)
```

### Obtener el tamaño real del canvas

```python
canvas.update_idletasks()  # fuerza el cálculo del layout
W = canvas.winfo_width()
H = canvas.winfo_height()
```

> **`update_idletasks()`** es necesario porque tkinter calcula los tamaños de forma lazy. Sin esta llamada, `winfo_width()` puede devolver 1 si el widget aún no se ha renderizado.

---

## 7. `_ArrayCanvas` — la clase de celdas

Es una subclase de `tk.Canvas` que encapsula todo el dibujo del array.

```python
class _ArrayCanvas(tk.Canvas):
    CELL_W   = 118   # ancho de cada celda en píxeles
    CELL_H   = 130   # alto de cada celda
    CELL_PAD = 5     # espacio entre celdas
    NOTCH_W  = 46    # ancho de la muesca superior
    NOTCH_H  = 13    # alto de la muesca superior
```

| Método | Qué hace |
|---|---|
| `set_array(arr)` | Vincula un `FixedArrayList`, resetea highlights y programa un render |
| `draw_all(highlight, done)` | Redibuja todo marcando un índice (highlight=naranja, done=verde) |
| `_render()` | Lógica principal de dibujo: rail exterior + celdas |
| `_draw_cell(x0,y0,x1,y1,idx)` | Dibuja una celda individual con muesca, interior e índice |
| `_rrect(x0,y0,x1,y1,r,**kw)` | Helper: rectángulo con esquinas redondeadas via `create_polygon` |

### Cómo funciona el centrado

```python
W = self.winfo_width()
if W < 10:
    W = self.master.winfo_width()  # fallback al padre
if W < 10:
    W = 1200                        # fallback absoluto

total_w = cap * CELL_W + (cap - 1) * CELL_PAD
ox = (W - total_w) // 2            # origen X centrado
```

### Cómo se dibuja una esquina redondeada

tkinter no tiene `border-radius` nativo. Se simula con un polígono de 12 puntos:

```python
def _rrect(self, x0, y0, x1, y1, r, **kw):
    self.create_polygon(
        x0+r, y0,   x1-r, y0,   x1, y0,     x1, y0+r,
        x1, y1-r,   x1, y1,     x1-r, y1,   x0+r, y1,
        x0, y1,     x0, y1-r,   x0, y0+r,   x0, y0,
        smooth=True, **kw)
```

`smooth=True` hace que tkinter interpole las esquinas como curvas Bezier.

---

## 8. El sistema de paneles dinámicos

El footer tiene un frame `self.ctrl` que se vacía y rellena según la operación activa. El patrón es siempre el mismo:

```python
def _clear(self) -> None:
    for w in self.ctrl.winfo_children():
        w.destroy()   # destruye todos los widgets hijos

def _show_insert_options(self) -> None:
    self._clear()                          # 1. limpiar
    _mk_btn(self.ctrl, "At End", ...).grid(...)  # 2. construir nuevos widgets
    _mk_btn(self.ctrl, "← Back", self._show_category_menu, ...).grid(...)
```

> El botón **← Back** simplemente llama al método que construye el panel anterior. No hay un stack de navegación — cada panel se reconstruye desde cero.

---

## 9. Animación con `root.after`

La animación de celdas revelándose de izquierda a derecha se hace con recursión temporizada:

```python
def _animate(self, highlight=-1, done=-1, callback=None):
    cap = self.array.__capacity__
    delay = max(15, min(140, 1400 // max(cap, 1)))  # más celdas = más rápido
    self._anim_step(0, cap, highlight, done, callback, delay)

def _anim_step(self, step, total, highlight, done, callback, delay):
    # dibuja celdas 0..step
    ...
    if step < total - 1:
        self.root.after(delay, lambda: self._anim_step(step+1, ...))
    elif callback:
        self.root.after(80, callback)  # al terminar, ejecuta el callback
```

`root.after(ms, fn)` no bloquea — programa `fn` para ejecutarse en `ms` milisegundos dentro del loop de eventos. Esto permite animar sin congelar la UI.

### `_chain` — encadenar dos callbacks

```python
def _chain(a, b):
    def _run():
        a()
        b()
    return _run

# Uso:
callback = _chain(self._refresh_info, self._show_category_menu)
# Primero actualiza el info_lbl, luego muestra el menú principal
```

---

## 10. La barra de información (`info_lbl`)

Es un `CTkLabel` posicionado con `place` en el header, alineado a la derecha:

```python
self.info_lbl = ctk.CTkLabel(self._header, text="", ...)
self.info_lbl.place(relx=0.98, rely=0.5, anchor="e")
```

Se actualiza con:

```python
def _set_info(self, msg: str, color: str = TEXT_SUB) -> None:
    self.info_lbl.configure(text=msg, text_color=color)

def _refresh_info(self) -> None:
    n, c = self.array.__size__, self.array.__capacity__
    self._set_info(f"size={n}  cap={c}", CLR_SUCCESS)
```

---

## 11. Paleta de colores

Todas las constantes de color están definidas al inicio del módulo como strings hex. Esto centraliza el tema y facilita cambios:

| Constante | Color | Uso |
|---|---|---|
| `BG_TOP` | `#181510` | Fondo del header |
| `BG_MAIN` | `#1c1e18` | Fondo principal |
| `BG_PANEL` | `#211e14` | Fondo del footer |
| `TEXT_TITLE` | `#9a7d5a` | Título principal (marrón dorado) |
| `TEXT_SUB` | `#6a7a5a` | Subtítulo (verde grisáceo) |
| `INPUT_BG` | `#2a2416` | Fondo de inputs y dropdowns |
| `INPUT_FG` | `#c8b890` | Texto dentro de inputs |
| `BTN_BG` | `#7aab80` | Botones primarios (verde salvia) |
| `BTN_RED` | `#8a4a40` | Botones de remove (rojo oscuro) |
| `BTN_BLUE` | `#4a6a8a` | Botones de search (azul pizarra) |
| `BTN_AMB` | `#8a7a3a` | Botones de sort bubble/binary (ámbar) |
| `CELL_NOTCH` | `#c8a878` | Muescas doradas de las celdas |
| `CELL_HL` | `#8a6a30` | Celda resaltada (búsqueda / remove) |
| `CLR_SUCCESS` | `#7aab80` | Mensajes de éxito |
| `CLR_DANGER` | `#c06050` | Mensajes de error |

---

## 12. Flujo completo de una operación

Ejemplo: el usuario inserta un valor al final.

```
1. _show_category_menu()
   └── crea botón INSERT → llama _show_insert_options()

2. _show_insert_options()
   └── crea botón "At End" → llama _show_insert_panel("end")

3. _show_insert_panel("end")
   └── crea entry de valor + botón "▶ Insert" → llama _insert_end(val)

4. _insert_end(val)
   ├── self.array.append(cast_type(val))   ← llama al modelo
   ├── self._set_info("appended → index N", CLR_SUCCESS)
   └── self._animate(done=N, callback=_chain(_refresh_info, _show_category_menu))

5. _animate() / _anim_step()
   └── redibuja celdas progresivamente con after()

6. Al terminar la animación:
   ├── _refresh_info()  → actualiza "size=N  cap=M"
   └── _show_category_menu()  → vuelve al menú principal
```

---

## 13. Manejo de errores

Todas las operaciones siguen el mismo patrón `try / except`:

```python
def _insert_end(self, val: str) -> None:
    try:
        assert self.array is not None
        self.array.append(self.cast_type(val))
        self._set_info(f"appended → index {self.array.__size__ - 1}", CLR_SUCCESS)
        self._animate(...)
    except Exception as e:
        self._set_info(str(e), CLR_DANGER)   # muestra el mensaje de la excepción
        self._show_category_menu()            # vuelve al menú sin crashear
```

Las excepciones del modelo (`FullArrayError`, `EmptyArrayError`, etc.) se propagan naturalmente hasta aquí y se muestran en el `info_lbl` en rojo.

---

## 14. Referencia rápida de métodos de `MatteApp`

| Método | Categoría | Descripción |
|---|---|---|
| `__init__` | Setup | Configura ventana y construye layout |
| `_build_layout` | Setup | Crea header, canvas, footer |
| `_place_canvas` | Render | Redibuja glow y celdas |
| `_set_info` | UI | Actualiza el label de estado |
| `_refresh_info` | UI | Muestra size/cap actuales |
| `_draw_all` | Render | Redibuja el array con highlight opcional |
| `_animate` | Animación | Inicia animación de revelado |
| `_anim_step` | Animación | Un paso de la animación recursiva |
| `_on_resize` | Evento | Responde al redimensionado de ventana |
| `_clear` | UI | Vacía el panel de controles |
| `_show_create_controls` | Panel | Pantalla inicial (tipo + capacidad) |
| `_do_create` | Lógica | Instancia `FixedArrayList` |
| `_show_category_menu` | Panel | Menú principal con las 6 categorías |
| `_show_insert_options` | Panel | Sub-menú de inserción |
| `_show_insert_panel` | Panel | Panel de input para insertar |
| `_insert_end` | Lógica | Llama a `array.append()` |
| `_insert_start` | Lógica | Llama a `array.insert_at_start()` |
| `_insert_at` | Lógica | Llama a `array.insert(idx, val)` |
| `_insert_after` | Lógica | Llama a `array.insert_after()` |
| `_insert_before` | Lógica | Llama a `array.insert_before()` |
| `_show_remove_options` | Panel | Sub-menú de eliminación |
| `_do_remove_start` | Lógica | Llama a `array.remove_at_start()` |
| `_do_remove_end` | Lógica | Llama a `array.remove_at_end()` |
| `_do_remove_at_index` | Lógica | Llama a `array.pop(idx)` |
| `_do_remove_value` | Lógica | Llama a `array.remove_value()` |
| `_show_sort_options` | Panel | Sub-menú con los 4 algoritmos |
| `_do_sort_insertion` | Lógica | Llama a `array.sort()` |
| `_do_sort_selection` | Lógica | Llama a `array.selection_sort()` |
| `_do_sort_bubble` | Lógica | Llama a `array.bubble_sort()` |
| `_do_sort_quick` | Lógica | Llama a `array.quick_sort()` |
| `_show_search_options` | Panel | Panel con Sequential y Binary |
| `_do_search_seq` | Lógica | Llama a `array.index_of()` |
| `_do_search_bin` | Lógica | Llama a `array.binary_search()` |
| `_show_get_options` | Panel | Panel para obtener por índice |
| `_do_get` | Lógica | Llama a `array.get(idx)` |