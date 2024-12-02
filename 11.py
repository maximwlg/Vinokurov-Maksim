from tkinter import *
from pprint import pprint
import json

def clicked():
    username = 'maximwlg'
    url = f'https://api.github.com/users/{username}'
    user_data = requests.get(url).json()

    selected_keys = {'company', 'created_at', 'email', 'id', 'url'}
    filtered_data = {key: user_data[key] for key in selected_keys if key in user_data}

    with open('data_file.json', 'w') as write_file:
        json.dump(filtered_data, write_file, indent=2)

    close()

def close():
    newindow = Tk()
    newindow.geometry('400x150')
    newindow.title('Файлы загружены')

    lbl2 = Label(newindow, text='Файлы успешно загружены!', font=('Arial', 20))
    lbl2.pack(pady=50)

    window.destroy()

window = Tk()
window.geometry('600x100')
window.title('11')

lbl = Label(window, text='  Номер зачётки 14', font = ('Arial', 50))
lbl.grid (column=0, row=0)

btn = Button(window, text='кнопка', command=clicked)
btn.grid (column=0, row=10)

window.mainloop()