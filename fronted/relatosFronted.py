import tkinter as tk
from tkinter import filedialog, Text

# Funciones para manejar los botones
def verificar_datos():
    print("Verificando datos...")

def limpiar_formulario():
    # Limpiar todos los campos del formulario
    nombre_entry.delete(0, tk.END)
    documento_entry.delete(0, tk.END)
    fecha_nacimiento_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    municipio_entry.delete(0, tk.END)
    departamento_entry.delete(0, tk.END)
    relato_text.delete("1.0", tk.END)
    fecha_desaparicion_entry.delete(0, tk.END)
    lugar_entry.delete(0, tk.END)
    origen_relato_entry.delete(0, tk.END)

def cargar_archivo():
    archivo = filedialog.askopenfile(filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx"), ("All Files", "*.*")])
    if archivo:
        print(f"Archivo cargado: {archivo.name}")

def guardar_datos():
    print("Guardando datos...")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Información - Desaparecidos")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

# Crear el frame superior para el encabezado
header_frame = tk.Frame(root, bg="#88bdbc", bd=5)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="Bienvenidos - Relatos después de aquél día", font=("Arial", 16), bg="#88bdbc", fg="white")
header_label.pack(pady=10)

# Crear el frame principal para dividir la ventana en dos partes
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Parte izquierda (Formulario)
form_frame = tk.Frame(main_frame, bg="white", bd=2, relief=tk.GROOVE)
form_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Nombre del desaparecido
tk.Label(form_frame, text="Nombre del Desaparecido:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
nombre_entry = tk.Entry(form_frame)
nombre_entry.pack(fill=tk.X, padx=5)

# Documento del desaparecido
tk.Label(form_frame, text="Documento del Desaparecido:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
documento_entry = tk.Entry(form_frame)
documento_entry.pack(fill=tk.X, padx=5)

# Fecha de nacimiento
tk.Label(form_frame, text="Fecha de Nacimiento:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
fecha_nacimiento_entry = tk.Entry(form_frame)
fecha_nacimiento_entry.pack(fill=tk.X, padx=5)

# Edad
tk.Label(form_frame, text="Edad:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
edad_entry = tk.Entry(form_frame)
edad_entry.pack(fill=tk.X, padx=5)

# Municipio
tk.Label(form_frame, text="Municipio:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
municipio_entry = tk.Entry(form_frame)
municipio_entry.pack(fill=tk.X, padx=5)

# Departamento
tk.Label(form_frame, text="Departamento:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
departamento_entry = tk.Entry(form_frame)
departamento_entry.pack(fill=tk.X, padx=5)

# Relato de desaparición
tk.Label(form_frame, text="Relato de Desaparición:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
relato_text = Text(form_frame, height=5)
relato_text.pack(fill=tk.X, padx=5, pady=5)

# Fecha de desaparición
tk.Label(form_frame, text="Fecha de Desaparición:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
fecha_desaparicion_entry = tk.Entry(form_frame)
fecha_desaparicion_entry.pack(fill=tk.X, padx=5)

# Lugar de desaparición
tk.Label(form_frame, text="Lugar de Desaparición:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
lugar_entry = tk.Entry(form_frame)
lugar_entry.pack(fill=tk.X, padx=5)

# Origen del relato
tk.Label(form_frame, text="Origen del Relato:", bg="white", font=("Arial", 12)).pack(anchor="w", pady=5)
origen_relato_entry = tk.Entry(form_frame)
origen_relato_entry.pack(fill=tk.X, padx=5)

# Botón para cargar archivo
tk.Button(form_frame, text="Cargar Archivo", command=cargar_archivo, bg="#88bdbc", fg="white").pack(pady=10)


button_frame = tk.Frame(main_frame, bg="#f1f1f1", bd=2, relief=tk.GROOVE)
button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

tk.Button(button_frame, text="Verificar", command=verificar_datos, bg="#88bdbc", fg="white", font=("Arial", 12)).pack(pady=10, fill=tk.X)
tk.Button(button_frame, text="Limpiar", command=limpiar_formulario, bg="#88bdbc", fg="white", font=("Arial", 12)).pack(pady=10, fill=tk.X)
tk.Button(button_frame, text="Guardar", command=guardar_datos, bg="#88bdbc", fg="white", font=("Arial", 12)).pack(pady=10, fill=tk.X)

# Footer
footer_frame = tk.Frame(root, bg="#4a6572", bd=5)
footer_frame.pack(fill=tk.X)
footer_label = tk.Label(footer_frame, text="&copy; 2024 Registro de Desaparecidos", bg="#4a6572", fg="white", font=("Arial", 10))
footer_label.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
