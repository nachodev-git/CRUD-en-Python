from tkinter import Tk
import vista
import observador


class Controller:
    def __init__(self, root_w):
        self.root = root_w
        self.objeto_vista = vista.Vista_principal(self.root)
        self.el_observador = observador.ConcreteObserverA(self.objeto_vista.objeto)


if __name__ == "__main__":
    root_tk = Tk()
    mi_app = Controller(root_tk)
    root_tk.mainloop()

