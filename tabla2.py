import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Nodos import *

root = tk.Tk()
root.title('tabla distancias')
root.geometry('400x200')



tree = ttk.Treeview(root, columns = ciudades, show='tree headings')
tree.heading("#0", text="Ciudades")

for i in ciudades:
    
    tree.heading(i, text=i)
    tree.column(i,width=40)
    

# generate sample data


# add data to the treeview
for contact in distancias:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()