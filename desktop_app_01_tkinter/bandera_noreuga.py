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

#-----------------------------
# Frame 1
# -----------------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="red", width=780, height=480)
frame_1.place(x=10, y=10)

# -----------------------------
# Frame 2
# -----------------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg="white", width=780, height=90)
frame_2.place(x=10, y=200)

# -----------------------------
# Frame 3
# -----------------------------

frame_3 = Frame(ventana_principal)
frame_3.config(bg="white", width=90, height=480)
frame_3.place(x=220, y=10)

# -----------------------------
# Frame 4
# -----------------------------

frame_4 = Frame(ventana_principal)
frame_4.config(bg="darkblue", width=50, height=480)
frame_4.place(x=240, y=10)

# -----------------------------
# Frame 5
# -----------------------------

frame_5 = Frame(ventana_principal)
frame_5.config(bg="darkblue", width=780, height=50)
frame_5.place(x=10, y=220)


# Metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()


# metodo principal que despliega la ventana en la pantalla
ventana_principal.mainloop()