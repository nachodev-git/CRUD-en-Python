from tkinter import StringVar
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import ttk
import modelo
from tkinter import ttk

cccli = StringVar
rzcli = StringVar
dircli = StringVar
telcli = StringVar
mailcli = StringVar

class Vista_principal:
    def __init__(self, ventana):
        self.root = ventana

        self.root.title("CRUD DE CLIENTES ----- By Aires Pampeanos")
        self.root.geometry("935x500")
        self.objeto = modelo.Crud()
               
        self.tree = ttk.Treeview()

        self.cccli = StringVar()
        self.rzcli = StringVar()
        self.dircli = StringVar()
        self.telcli = StringVar()
        self.mailcli = StringVar()

        self.l2 = Label(self.root, text="Cuil-Cuit")
        self.l2.place(x=50, y=10)
        self.e2 = Entry(self.root, textvariable=self.cccli, width=50)
        self.e2.place(x=150, y=10)

        self.l3 = Label(self.root, text="Razón Social")
        self.l3.place(x=50, y=30)
        self.e3 = Entry(self.root, textvariable=self.rzcli, width=50)
        self.e3.place(x=150, y=30)

        self.l4 = Label(self.root, text="Dirección")
        self.l4.place(x=50, y=50)
        self.e4 = Entry(self.root, textvariable=self.dircli, width=50)
        self.e4.place(x=150, y=50)

        self.l5 = Label(self.root, text="Teléfono")
        self.l5.place(x=50, y=70)
        self.e5 = Entry(self.root, textvariable=self.telcli, width=50)
        self.e5.place(x=150, y=70)

        self.l6 = Label(self.root, text="e-mail")
        self.l6.place(x=50, y=90)
        self.e6 = Entry(self.root, textvariable=self.mailcli, width=50)
        self.e6.place(x=150, y=90)

        ############## Tree View ##############

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.tree.column("#0", width=50, minwidth=50, anchor="w")
        self.tree.column("col1", width=80, minwidth=80, anchor="w")
        self.tree.column("col1", width=80, minwidth=80, anchor="w")
        self.tree.column("col1", width=80, minwidth=80, anchor="w")
        self.tree.column("col1", width=80, minwidth=80, anchor="w")
        self.tree.column("col1", width=80, minwidth=80, anchor="w")

        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Cuil_Cuit")
        self.tree.heading("col2", text="Razon Social")
        self.tree.heading("col3", text="Dirección")
        self.tree.heading("col4", text="Teléfono")
        self.tree.heading("col5", text="e-mail")

        self.tree.place(x=0, y=180)

        ############## Botones ##############
        self.boton_alta = Button(
            self.root,
            text="Crear Registro",
            command=lambda: self.objeto.alta(
                self.cccli,
                self.rzcli,
                self.dircli,
                self.telcli,
                self.mailcli,
                self.tree,
            ),
        )
        self.boton_alta.place(x=50, y=130)
        self.limpiar_campos()

        self.btn_modificar = Button(
            self.root,
            text="Modificar Registro",
            command=lambda: self.objeto.modificar(
                self.cccli.get(),
                self.rzcli.get(),
                self.dircli.get(),
                self.telcli.get(),
                self.mailcli.get(),
                self.tree,
            ),
        )
        self.btn_modificar.place(x=150, y=130)

        self.btn_mostrar = Button(
            self.root,
            text="Mostrar Lista",
            command=lambda: self.objeto.actualizar_treeview(self.tree),
        )
        self.btn_mostrar.place(x=275, y=130)

        self.btn_borrar = Button(
            self.root,
            text="Eliminar Registro",
            command=lambda: self.objeto.baja(self.tree),
            bg="#F70301",
            fg="#FFFFFF",
        )
        
        self.btn_borrar.place(x=370, y=130)

        self.btn_salir = Button(self.root, text="Salir",command=exit)
        self.btn_salir.place(x=500, y=130)

    def limpiar_campos(self):

        self.cccli.set = ""
        self.rzcli.set = ""
        self.dircli.set = ""
        self.telcli.set = ""
        self.mailcli.set = ""
