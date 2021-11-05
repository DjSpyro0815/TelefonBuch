import tkinter as tk


contact_names = list()
contact_numbers = list()

def read_contacts_from_file():
    with open('Kontakte','r') as f:
        contact_strings = f.readlines()
        print(contact_strings)

        for contact in contact_strings:
            contact = contact.rstrip('\n')
            contact = contact.split(', ')

            contact_names.append(contact[0])
            contact_numbers.append(contact[1])

def display_contact_for_number():
    i = contact_listbox.curselection()[0]
    number = contact_numbers[i]
    numbers_label['text'] = number

read_contacts_from_file()

window = tk.Tk()
window.title("LilaBlassBlaueSeiten")
window.geometry('300x300')
window.config(bg='purple')

numbers_label = tk.Label(text='Moin Moin was geht')
numbers_label.config(font=('Arial', 20, 'bold'), bg='purple')


contact_names_var = tk.StringVar(value=contact_names)
contact_listbox = tk.Listbox(window, height=10, width=30, listvariable=contact_names_var)
contact_listbox.bind('<<ListboxSelect>>', lambda e: display_contact_for_number())

numbers_label.pack(pady=10)
contact_listbox.pack()




window.mainloop()