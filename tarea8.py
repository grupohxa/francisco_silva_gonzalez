import tkinter as tk
from tkinter import messagebox
import mysql.connector

# creamos la conexion a la BD
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='semana8'
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error de conexión: {err}")
        return None

# Funciones CRUD
def add_fauna_flora():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO FaunaFlora (ID, NombreCientifico, Habitat, EstadoConservacion, RegionGeografica) VALUES (%s, %s, %s, %s, %s)",
                           (id_entry.get(), nombre_entry.get(), habitat_entry.get(), estado_entry.get(), region_entry.get()))
            conn.commit()
            messagebox.showinfo("Éxito", "Objeto de Fauna/Flora agregado exitosamente")
            show_fauna_flora()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo agregar: {err}")
        finally:
            cursor.close()
            conn.close()

def show_fauna_flora():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM FaunaFlora")
        records = cursor.fetchall()
        listbox.delete(0, tk.END)  # Limpiar la lista
        for record in records:
            listbox.insert(tk.END, record)
        cursor.close()
        conn.close()

def delete_fauna_flora():
    selected = listbox.curselection()
    if selected:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            item = listbox.get(selected[0])
            try:
                cursor.execute("DELETE FROM FaunaFlora WHERE ID = %s", (item[0],))
                conn.commit()
                messagebox.showinfo("Éxito", "Objeto de Fauna/Flora eliminado exitosamente")
                show_fauna_flora()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo eliminar: {err}")
            finally:
                cursor.close()
                conn.close()

def update_fauna_flora():
    selected = listbox.curselection()
    if selected:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            item = listbox.get(selected[0])
            try:
                cursor.execute("UPDATE FaunaFlora SET NombreCientifico=%s, Habitat=%s, EstadoConservacion=%s, RegionGeografica=%s WHERE ID=%s",
                               (nombre_entry.get(), habitat_entry.get(), estado_entry.get(), region_entry.get(), item[0]))
                conn.commit()
                messagebox.showinfo("Éxito", "Información actualizada correctamente")
                show_fauna_flora()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo actualizar: {err}")
            finally:
                cursor.close()
                conn.close()

# se crea la interfaz gráfica o GUI
root = tk.Tk()
root.title("Gestión de Fauna/Flora")

# Labels (etiquetas) y Entry fields (caja de texto)
tk.Label(root, text="ID").grid(row=0, column=0)
tk.Label(root, text="Nombre Científico -->").grid(row=1, column=0)
tk.Label(root, text="Hábitat -->").grid(row=2, column=0)
tk.Label(root, text="Estado de Conservación -->").grid(row=3, column=0)
tk.Label(root, text="Región Geográfica -->").grid(row=4, column=0)

id_entry = tk.Entry(root)
nombre_entry = tk.Entry(root)
habitat_entry = tk.Entry(root)
estado_entry = tk.Entry(root)
region_entry = tk.Entry(root)

id_entry.grid(row=0, column=1)
nombre_entry.grid(row=1, column=1)
habitat_entry.grid(row=2, column=1)
estado_entry.grid(row=3, column=1)
region_entry.grid(row=4, column=1)

# Botones para las operaciones CRUD
tk.Button(root, text="Agregar", command=add_fauna_flora).grid(row=5, column=0)
tk.Button(root, text="Mostrar", command=show_fauna_flora).grid(row=5, column=1)
tk.Button(root, text="Eliminar", command=delete_fauna_flora).grid(row=6, column=0)
tk.Button(root, text="Actualizar", command=update_fauna_flora).grid(row=6, column=1)

# Listbox para mostrar datos
listbox = tk.Listbox(root, width=100)
listbox.grid(row=7, column=0, columnspan=2)

# Ejecutamos la aplicación GUI
show_fauna_flora()
root.mainloop()

