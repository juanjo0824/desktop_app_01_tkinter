# se importa la libreria tkinter con todas sus funciones

from tkinter import *

#----------------------------------------------------
# funciones de la app
#----------------------------------------------------



#-----------------------------------------
# ventana principal
#-----------------------------------------

# se declara una variable llamada ventana_principal que adquiere las caracteristicas de un objeto TK()

ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Juan Jose Delgado Benitez")

# tamaño de la ventana
ventana_principal.geometry("800x500")

# deshabilitar botor maximizar de la ventana
ventana_principal.resizable(0,0)

## Color de fondo de la pantalla
ventana_principal.config(bg="green")

# -----------------------------
# Frame 1
# -----------------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="blue", width=260, height=480)
frame_1.place(x=10, y=10)

# -----------------------------
# Frame 2
# -----------------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg="white", width=260, height=480)
frame_2.place(x=270, y=10)

# -----------------------------
# Frame 3
# -----------------------------

frame_3 = Frame(ventana_principal)
frame_3.config(bg="red", width=260, height=480)
frame_3.place(x=530, y=10)

# Metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()


# metodo principal que despliega la ventana en la pantalla
ventana_principal.mainloop()