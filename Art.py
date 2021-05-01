from tkinter import *
window = Tk()
#Зададим размер окна
window.minsize(width=700, height=700)

#Заголовок окна
window.title=("Chebu-pizza")
#Создадим холст для геометрических фигур
canv=Canvas(window, width=700, height=700, bg='lightblue', cursor='pencil')
#Вывод холста в GUI
canv.pack()


#создадим многоугольник
canv.create_polygon([200,250],[200,500],[416.5,375], fill="lemon chiffon", outline="magenta2")






window.mainloop()