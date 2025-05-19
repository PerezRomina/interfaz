import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def saludo():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Aqui va un mensaje de bienvenida", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("Bienvenido","Hola, bienvenido")).pack()

def alumno():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Registro de los datos del alumno", font=("Arial", 12)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Elige una opcion:").pack()
    genero_seleccionado = tk.StringVar(value="Masculino")
    tk.Radiobutton(area_dinamica, text="Masculino", variable=genero_seleccionado, value="Masculino").pack()
    tk.Radiobutton(area_dinamica, text="Femenino", variable=genero_seleccionado, value="Femenino").pack()

    tk.Label(area_dinamica, text="Semestre:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Primero", "Segundo", "Tercero", "Cuarto", "Quinto", "Sexto" ])
    combo.pack()
    combo.current(0)

    def guardar_opciones():
        valor = campo_texto_uno.get()
        messagebox.showinfo("Revisión", f"Alumno: {valor}\nGenero: {genero_seleccionado.get()}\nSemestre: {combo.get()}")

    tk.Button(area_dinamica, text="da click para mostrar los datos que se ingresaron", command=guardar_opciones).pack(pady=10)

def color():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def Cuestionario():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Cuestionario para el alummo",font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Categorias")
ventana_principal.geometry("700x600")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=saludo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos a ingresar", command=alumno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Colores predeterminados", command=color, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Visualizar cuestionario", command=Cuestionario, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salida", command=ventana_principal.destroy, width=15).pack(pady=30)

saludo()
ventana_principal.mainloop()
