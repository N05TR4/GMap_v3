import tkinter
from tkinter import *
from tkinter import ttk


class Product:

    def __init__(self, window):
        # Ventana

        self.wind = window
        self.wind.title('Escuela Secundaria tecnica # 91')
        self.wind.configure(background='gray')

        # Pestañas
        self._tab_control = ttk.Notebook(self.wind)
        self.tab1 = tkinter.Frame(self._tab_control, bg='gray')
        self._tab_control.add(self.tab1, text='Alumnos')
        lbl1 = Label(self.tab1, text='Jorge Alberto Rodriguez Gomez')
        self._tab_control.grid(row=1, column=0)
        lbl1.grid(row=1, column=0)

        ######Pestaña 2
        self.tab2 = tkinter.Frame(self._tab_control, bg='gray')
        self._tab_control.add(self.tab2, text='Profesores')
        lbl2 = Label(self.tab2, text='Roberto Macías')
        self._tab_control.grid(row=1, column=0)
        lbl2.grid(column=0, row=0)


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()