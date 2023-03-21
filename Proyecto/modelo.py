import sqlite3
from tkinter import messagebox
from tkinter import StringVar
import re
from decorador import get_logger
from observador import Observer

cccli = StringVar
rzcli = StringVar
dircli = StringVar
telcli = StringVar
mailcli = StringVar


class Crud(Observer):
    def __init__(
        self,
    ):
        pass
    
    def crear_base(self):
        conexion = sqlite3.connect("database clientes.db")
        return conexion

    def crear_tabla(self):
        conexion = self.crear_base()
        micursor = conexion.cursor()
        sqltabla = """CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT,
                cuilcuit VARCHAR NOT NULL,
                razonsocial TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                mail TEXT NOT NULL)"""
        micursor.execute(sqltabla)
        conexion.commit()

    ################### Métodos CRUD ####################
    @get_logger
    def alta(self, cuilcuit, razonsocial, direccion, telefono, mail, tree):
        conexion = self.crear_base()
        micursor = conexion.cursor()
        data = (
            cuilcuit.get(),
            razonsocial.get(),
            direccion.get(),
            telefono.get(),
            mail.get(),
        )
        sqlinsertar = "INSERT INTO clientes(cuilcuit, razonsocial, direccion, telefono, mail) VALUES(?, ?, ?, ?, ?)"
        if (
            cuilcuit == ""
            or razonsocial == ""
            or direccion == ""
            or telefono == ""
            or mail == ""
        ):

            messagebox.showerror("Error", "Por favor ingrese datos correctamente")

        else:

            cadena = cuilcuit.get()
            patron = re.compile("\d[0-9]")
            
            if re.match(patron, cadena):
                micursor.execute(sqlinsertar, data)
                conexion.commit()
                conexion.close()

                print("alta")
            else:
                messagebox.showerror("Error", "Por favor ingrese datos correctamente")
        self.actualizar_treeview(tree)
        self.notificar(cuilcuit.get(), razonsocial.get(), direccion.get(), telefono.get(), mail.get())
    
    @get_logger
    def consultar(self):
        sql = "SELECT * FROM clientes ORDER BY id ASC"
        conexion = self.crear_base()
        micursor = conexion.cursor()
        datos = micursor.execute(sql)
        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
        print(resultado)
    
    @get_logger
    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for elements in records:
            mitreview.delete(elements)
        
        sql = "SELECT * FROM clientes ORDER BY id ASC"
        conexion = self.crear_base()
        micursor = conexion.cursor()
        datos = micursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert(
                "",
                0,
                text=fila[0],
                values=(fila[1], fila[2], fila[3], fila[4], fila[5]),
            )


    @get_logger
    def baja(self, tree):
        valor = tree.selection()
        print(valor)
        item = tree.item(valor)
        print(item)
        print(item["text"])
        id_cli = item["text"]
        
        conexion = self.crear_base()
        micursor = conexion.cursor()
        data = (id_cli,)
        sql = "DELETE FROM clientes WHERE ID=?"
        micursor.execute(sql, data)
        conexion.commit()
        tree.delete(valor)
        self.quitar(valor,)
        
    
    @get_logger     
    def modificar(self, cuilcuit, razonsocial, direccion, telefono, mail, tree):
        valor = tree.selection()
        item = tree.item(valor)
        print(item["text"])
        id_cli = item["text"]

        conexion = self.crear_base()
        micursor = conexion.cursor()

        data = (
            cuilcuit,
            razonsocial,
            direccion,
            telefono,
            mail,
            id_cli,
        )
        sql = "UPDATE clientes SET (cuilcuit, razonsocial, direccion, telefono, mail) = (?,?,?,?,?) WHERE id=?;"

        if (
            cuilcuit == ""
            or razonsocial == ""
            or direccion == ""
            or telefono == ""
            or mail == ""
        ):
        
            messagebox.showerror("Error", "Por favor ingrese datos correctamente")

        else:
            cadena = cuilcuit
            patron = re.compile("\d[0-9]")

            if re.match(patron, cadena):
                micursor.execute(sql, data)
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Modificar Registro", "Los datos fueron modificados correctamente")

                print("alta")
            else:
                messagebox.showerror("Error", "Por favor ingrese datos correctamente")
               
        self.actualizar_treeview(tree)
        


