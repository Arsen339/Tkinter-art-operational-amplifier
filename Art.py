from tkinter import *
window = Tk()
#Зададим размер окна
window.minsize(width=700, height=700)

#Заголовок окна
window.title=("Chebu-pizza")
#Создадим холст для геометрических фигур
canv=Canvas(window, width=700, height=700, bg='lightgrey', cursor='pencil')
#Вывод холста в GUI
canv.pack()


#создадим многоугольник(треугольник-тело)
canv.create_polygon([350,200],[200,500],[500,500], fill="lemon chiffon", outline="magenta2")

#Создаем линии(ножки)
#Левая нога
canv.create_line(210,500,210,630, width=5, fill="yellow")
#Правая нога
canv.create_line(490,500,490,630, width=5, fill="yellow")
#Создаем левую лапку
canv.create_line(210,630,190,660, width=5, fill="yellow")
canv.create_line(210,630,200,670, width=5, fill="yellow")
canv.create_line(210,630,220,665, width=5, fill="yellow")
canv.create_line(210,630,232,655, width=5, fill="yellow")
#Создаем правую лапку

canv.create_line(490,630,475,660, width=5, fill="yellow")
canv.create_line(490,630,485,675, width=5, fill="yellow")
canv.create_line(490,630,500,665, width=5, fill="yellow")
canv.create_line(490,630,520,655, width=5, fill="yellow")



canv.create_line(280,340,175,305, width=5, fill="yellow")
canv.create_line(400,300,500,300, width=5, fill="yellow")


#Создаем круги(инверсный вход.Точки-координаты противоположных углов треугольника)
canv.create_oval([200,510],[220,490], fill="lightyellow", outline="black")



#Вставим текст(+,-,ко-ко-ко, Uвых,k=-Roc/R1)
canv.create_text(320, 330, 
              text="+",
              justify=CENTER, font="Verdana 14")
canv.create_text(380, 330, 
              text="-",
              justify=CENTER, font="Verdana 14")
canv.create_text(330, 460, 
              text="k=-Roc/R1",
              justify=CENTER, font="Verdana 14")






window.mainloop()