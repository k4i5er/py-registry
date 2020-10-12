from tkinter.ttk import Frame, Button, Entry, Label, Style
from tkinter import Tk, LEFT, RIGHT, TOP, BOTTOM, X, StringVar, W

registry = []

# registry = [
#     {
#         'name': 'Juan',
#         'lastname': 'Pérez',
#         'emails': {
#             'personal': 'juanitop@gmail.com',
#             'work': 'jperez@work.com'
#         },
#         'addresses': {
#             'home': 'Av. del olvido, #7, col. Niño perdido, C.P. 39000, Acapulco, Gro',
#             'work': 'Av. Cuauhtémoc #45, col. Centro, C.P. 39300, Acapulco, Gro.'
#         }
#     }
# ]


def save_record():
    # Obtener la información de los widgets de entrada y colocarla en la estructura de datos
    print(txt_name.get())


root = Tk()

root.geometry('350x400')
root.title('Registro de participantes')

frm_name = Frame(root)
Label(frm_name, text="Nombre").pack(side=LEFT)
txt_name = StringVar()
Entry(frm_name, textvariable=txt_name).pack(
    side=LEFT, padx=10, fill=X, expand=1)
frm_name.pack(fill=X, padx=10, pady=10)

frm_lastname = Frame(root)
Label(frm_lastname, text="Apellidos").pack(side=LEFT)
txt_lastname = StringVar()
Entry(frm_lastname, textvariable=txt_lastname).pack(
    side=LEFT, padx=10, fill=X, expand=1)
frm_lastname.pack(fill=X, padx=10, pady=10)

frm_emails = Frame(root)
Label(frm_emails, text="Correos electrónicos").pack(anchor=W)

frm_home_email = Frame(frm_emails)
Label(frm_home_email, text="Personal").pack(side=LEFT)
txt_home_email = StringVar()
Entry(frm_home_email, textvariable=txt_home_email).pack(
    side=LEFT, padx=10, fill=X, expand=1)
frm_home_email.pack(fill=X, padx=10, pady=10)

frm_work_email = Frame(frm_emails)
Label(frm_work_email, text="Laboral").pack(side=LEFT)
txt_work_email = StringVar()
Entry(frm_work_email, textvariable=txt_work_email).pack(
    side=LEFT, padx=10, fill=X, expand=1)
frm_work_email.pack(fill=X, padx=10, pady=10)

frm_emails.pack(fill=X, padx=10, pady=10)

frm_adresses = Frame(root)
Label(frm_adresses, text="Direcciones").pack(anchor=W)

frm_home_address = Frame(frm_adresses)
Label(frm_home_address, text="Casa").pack(side=LEFT)
txt_home_address = StringVar()
Entry(frm_home_address, textvariable=txt_home_address).pack(
    side=LEFT, padx=10, fill=X, expand=1)
frm_home_address.pack(fill=X, padx=10, pady=10)

frm_work_address = Frame(frm_adresses)
Label(frm_work_address, text="Trabajo").pack(side=LEFT)
txt_work_address = StringVar()
Entry(frm_work_address, textvariable=txt_work_address).pack(
    side=LEFT, padx=10, fill=X, expand=1)
frm_work_address.pack(fill=X, padx=10, pady=10)

frm_adresses.pack(fill=X, padx=10, pady=10)

frm_buttons = Frame(root)

Button(frm_buttons, text='Enviar registro',
       command=save_record).pack(side=LEFT, expand=1)
Button(frm_buttons, text='Salir', command=root.destroy).pack(
    side=LEFT, expand=1)

frm_buttons.pack(fill=X)

root.mainloop()
