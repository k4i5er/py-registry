from tkinter.ttk import Frame, Button, Entry, Label, Style
from tkinter import Tk, LEFT, RIGHT, TOP, BOTTOM, X, StringVar, W, END, Toplevel

# CRUD = Create, Read, Update, Delete

registry = []
i = 0

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


def delete_entry_text():
    entry_name.delete(0, END)
    entry_lastname.delete(0, END)
    entry_home_email.delete(0, END)
    entry_work_email.delete(0, END)
    entry_home_address.delete(0, END)
    entry_work_address.delete(0, END)


def delete_entry_browse_text():
    entry_name_browse.delete(0, END)
    entry_lastname_browse.delete(0, END)
    entry_home_email_browse.delete(0, END)
    entry_work_email_browse.delete(0, END)
    entry_home_address_browse.delete(0, END)
    entry_work_address_browse.delete(0, END)


def disable_entry_browse():
    entry_name_browse.state(['readonly'])
    entry_lastname_browse.state(['readonly'])
    entry_home_email_browse.state(['readonly'])
    entry_work_email_browse.state(['readonly'])
    entry_home_address_browse.state(['readonly'])
    entry_work_address_browse.state(['readonly'])


def save_record():
    # Obtener la información de los widgets de entrada y colocarla en la estructura de datos
    registry.append(
        {
            'name': txt_name.get(),
            'lastname': txt_lastname.get(),
            'emails': {
                'personal': txt_home_email.get(),
                'work': txt_work_email.get()
            },
            'addresses': {
                'home': txt_home_address.get(),
                'work': txt_work_address.get()
            }
        }
    )
    delete_entry_text()


def save_record_at():
    registry[i] = {
        'name': entry_name_browse.get(),
        'lastname': entry_lastname_browse.get(),
        'emails': {
            'personal': entry_home_email_browse.get(),
            'work': entry_work_email_browse.get()
        },
        'addresses': {
            'home': entry_home_address_browse.get(),
            'work': entry_work_address_browse.get()
        }
    }
    disable_entry_browse()
    btn_modify_record.configure(
        text='Modificar registro', command=modify_record)
    # print(registry)


def show_records():
    entry_name_browse.state(['!readonly'])
    entry_lastname_browse.state(['!readonly'])
    entry_home_email_browse.state(['!readonly'])
    entry_work_email_browse.state(['!readonly'])
    entry_home_address_browse.state(['!readonly'])
    entry_work_address_browse.state(['!readonly'])

    delete_entry_browse_text()

    entry_name_browse.insert(0, registry[i]['name'])
    entry_lastname_browse.insert(0, registry[i]['lastname'])
    entry_home_email_browse.insert(0, registry[i]['emails']['personal'])
    entry_work_email_browse.insert(0, registry[i]['emails']['work'])
    entry_home_address_browse.insert(0, registry[i]['addresses']['home'])
    entry_work_address_browse.insert(0, registry[i]['addresses']['work'])

    disable_entry_browse()


def modify_record():
    entry_name_browse.state(['!readonly'])
    entry_lastname_browse.state(['!readonly'])
    entry_home_email_browse.state(['!readonly'])
    entry_work_email_browse.state(['!readonly'])
    entry_home_address_browse.state(['!readonly'])
    entry_work_address_browse.state(['!readonly'])

    btn_modify_record.configure(
        text='Guardar registro', command=save_record_at)


def show_prev():
    global i
    print('pa\'tras')
    i -= 1  # i = i-1
    if i == 0:
        btn_prev.pack_forget()
    else:
        btn_prev.pack(side=LEFT, expand=1)

    btn_next.pack(side=LEFT, expand=1)
    show_records()


def show_next():
    global i
    print('pa\'delante')
    # len(registry)<len(registry)+1 # cuando no hemos rebasado el último registro de la lista
    i += 1  # i = i+1
    btn_prev.pack(side=LEFT, expand=1, before=btn_next)
    if i == len(registry) - 1:  # Cuando estamos en el último registro de la lista
        btn_next.pack_forget()
    show_records()


def delete_record():
    global i
    print(f'You\'ve been choosen for deletion! Record {i+1}')
    print(registry)
    # len(regsitry) -> 2
    # i -> 1 cuando estoy en el último registro
    # registry.pop(i) elimina la posición 2 de mi lista
    # show_records() tratará de mostrar los datos de la posición 2 de la lista (índice 1)
    # registry[0]
    # registry[1] <-- Lo quiero borrar
    # registry[2]
    # registry[3]
    # i -> 1 es el índice del registro visualizado
    registry.pop(i)
    # registry[0]
    # registry[1] (antes 2)
    # registry[2] (antes 3)

    # registry[0]
    # registry[1] <-- quiero elimiarlo
    # i -> 1 es el índice del registro visualizado
    # registry.pop(i)
    # registry[0] <-- me debe mostrar este registro
    # ¿qué debe suceder con i?
    # Solución: ajustar a i
    # i -> len(registry)-1

    if i > len(registry) - 1:
        i = len(registry)-1

    print(registry)
    if len(registry) > 0:
        show_records()
    elif len(registry) == 0:
        browse_window.destroy()

    if i == len(registry) - 1:
        btn_next.pack_forget()
    if len(registry) == 1:
        btn_prev.pack_forget()


def browse_records_window():
    global entry_name_browse
    global entry_lastname_browse
    global entry_home_address_browse
    global entry_home_email_browse
    global entry_work_address_browse
    global entry_work_email_browse
    global btn_modify_record
    global btn_prev
    global btn_next
    global browse_window
    global i

    browse_window = Toplevel(root)
    browse_window.title('Consulta de registros - Registro de participantes')
    browse_window.geometry('350x400')

    frm_name = Frame(browse_window)

    Label(frm_name, text="Nombre").pack(side=LEFT)
    entry_name_browse = Entry(frm_name)
    entry_name_browse.pack(side=LEFT, padx=10, fill=X, expand=1)
    frm_name.pack(fill=X, padx=10, pady=10)

    frm_lastname = Frame(browse_window)
    Label(frm_lastname, text="Apellidos").pack(side=LEFT)
    entry_lastname_browse = Entry(frm_lastname)
    entry_lastname_browse.pack(side=LEFT, padx=10, fill=X, expand=1)
    frm_lastname.pack(fill=X, padx=10, pady=10)

    frm_emails = Frame(browse_window)
    Label(frm_emails, text="Correos electrónicos").pack(anchor=W)

    frm_home_email = Frame(frm_emails)
    Label(frm_home_email, text="Personal").pack(side=LEFT)
    entry_home_email_browse = Entry(frm_home_email)
    entry_home_email_browse.pack(side=LEFT, padx=10, fill=X, expand=1)
    frm_home_email.pack(fill=X, padx=10, pady=10)

    frm_work_email = Frame(frm_emails)
    Label(frm_work_email, text="Laboral").pack(side=LEFT)
    entry_work_email_browse = Entry(frm_work_email)
    entry_work_email_browse.pack(side=LEFT, padx=10, fill=X, expand=1)
    frm_work_email.pack(fill=X, padx=10, pady=10)

    frm_emails.pack(fill=X, padx=10, pady=10)

    frm_adresses = Frame(browse_window)
    Label(frm_adresses, text="Direcciones").pack(anchor=W)

    frm_home_address = Frame(frm_adresses)
    Label(frm_home_address, text="Casa").pack(side=LEFT)
    entry_home_address_browse = Entry(frm_home_address)
    entry_home_address_browse.pack(side=LEFT, padx=10, fill=X, expand=1)
    frm_home_address.pack(fill=X, padx=10, pady=10)

    frm_work_address = Frame(frm_adresses)
    Label(frm_work_address, text="Trabajo").pack(side=LEFT)
    entry_work_address_browse = Entry(frm_work_address)
    entry_work_address_browse.pack(side=LEFT, padx=10, fill=X, expand=1)
    frm_work_address.pack(fill=X, padx=10, pady=10)

    frm_adresses.pack(fill=X, padx=10, pady=10)

    frm_buttons = Frame(browse_window)

    frm_browsing_buttons = Frame(frm_buttons)
    btn_prev = Button(frm_browsing_buttons, text='Previo', command=show_prev)
    # if i == 0:
    #     btn_prev.pack_forget()
    # else:
    #     btn_prev.pack(side=LEFT, expand=1)

    btn_next = Button(frm_browsing_buttons,
                      text='Siguiente', command=show_next)
    if len(registry) == 1:
        btn_next.pack_forget()
    else:
        btn_next.pack(side=LEFT, expand=1)

    frm_browsing_buttons.pack(fill=X)

    frm_modify = Frame(frm_buttons)
    btn_modify_record = Button(
        frm_modify, text='Modificar registro', command=modify_record)
    btn_modify_record.pack(side=LEFT, expand=1)
    btn_delete_record = Button(
        frm_modify, text='Eliminar registro', command=delete_record)
    btn_delete_record.pack(side=LEFT, expand=1)
    Button(frm_modify, text='Regresar', command=browse_window.destroy).pack(
        side=LEFT, expand=1)
    frm_modify.pack(fill=X)

    frm_buttons.pack(fill=X)
    print(f'i >>>>>>> {i}')
    i = 0
    show_records()


root = Tk()

root.geometry('350x400')
root.title('Registro de participantes')

frm_name = Frame(root)
Label(frm_name, text="Nombre").pack(side=LEFT)
txt_name = StringVar()
entry_name = Entry(frm_name, textvariable=txt_name)
entry_name.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_name.pack(fill=X, padx=10, pady=10)

frm_lastname = Frame(root)
Label(frm_lastname, text="Apellidos").pack(side=LEFT)
txt_lastname = StringVar()
entry_lastname = Entry(frm_lastname, textvariable=txt_lastname)
entry_lastname.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_lastname.pack(fill=X, padx=10, pady=10)

frm_emails = Frame(root)
Label(frm_emails, text="Correos electrónicos").pack(anchor=W)

frm_home_email = Frame(frm_emails)
Label(frm_home_email, text="Personal").pack(side=LEFT)
txt_home_email = StringVar()
entry_home_email = Entry(frm_home_email, textvariable=txt_home_email)
entry_home_email.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_home_email.pack(fill=X, padx=10, pady=10)

frm_work_email = Frame(frm_emails)
Label(frm_work_email, text="Laboral").pack(side=LEFT)
txt_work_email = StringVar()
entry_work_email = Entry(frm_work_email, textvariable=txt_work_email)
entry_work_email.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_work_email.pack(fill=X, padx=10, pady=10)

frm_emails.pack(fill=X, padx=10, pady=10)

frm_adresses = Frame(root)
Label(frm_adresses, text="Direcciones").pack(anchor=W)

frm_home_address = Frame(frm_adresses)
Label(frm_home_address, text="Casa").pack(side=LEFT)
txt_home_address = StringVar()
entry_home_address = Entry(frm_home_address, textvariable=txt_home_address)
entry_home_address.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_home_address.pack(fill=X, padx=10, pady=10)

frm_work_address = Frame(frm_adresses)
Label(frm_work_address, text="Trabajo").pack(side=LEFT)
txt_work_address = StringVar()
entry_work_address = Entry(frm_work_address, textvariable=txt_work_address)
entry_work_address.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_work_address.pack(fill=X, padx=10, pady=10)

frm_adresses.pack(fill=X, padx=10, pady=10)

frm_buttons = Frame(root)

Button(frm_buttons, text='Enviar registro',
       command=save_record).pack(side=LEFT, expand=1)
Button(frm_buttons, text='Consultar registros',
       command=browse_records_window).pack(side=LEFT, expand=1)
Button(frm_buttons, text='Salir', command=root.destroy).pack(
    side=LEFT, expand=1)

frm_buttons.pack(fill=X)

root.mainloop()
