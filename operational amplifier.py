from tkinter import *

#Функция для кнопки
def clicked():
    lbl.configure(text="Вкусно!")



window = Tk()
#Зададим размер окна
window.geometry('1000x1000')

#Заголовок окна
window.title=("Chebu-pizza")

#Создание текста
lbl = Label(window, text="Съедобный операционный усилитель", font=("Arial Bold", 30))

#(Поместим текст в определенную колонку)
lbl.grid(column=0, row=0)

#Создадим кнопку
btn = Button(window, text="Съесть", bg="black", fg="red", command=clicked)
btn.grid(column=1, row=0)

#Создадим холст для геометрических фигур
canv=Canvas(window,width=1000, height=1000, bg='lightgray', cursor='pencil')
#Вывод холста в GUI
canv.pack()







#Бесконечный цикл для окна(Пишется в конце)
window.mainloop()