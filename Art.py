from tkinter import *
from PIL import ImageTk, Image

#Имя файла с головой курицы
#Параметризовано имя файла
path=("head.gif")

window = Tk()
#Зададим размер окна
window.minsize(width=700, height=700)

#Заголовок окна
window.title=("Chebu-pizza")
#Создадим холст для геометрических фигур
canv=Canvas(window, width=700, height=700, bg='white', cursor='pencil')
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


#Рисуем  левое крылышко
canv.create_polygon([280,340],[310,280],[230,200],[175,305], fill="yellow", outline="yellow")
canv.create_polygon([175,305],[160,280],[193,272],fill="yellow", outline="yellow")
canv.create_polygon([193,272.3],[155,230],[211,238.1], fill="yellow", outline="yellow")
canv.create_polygon([211,238.1],[187,198],[230,200], fill="yellow", outline="yellow")

#Рисуем  правое крылышко
canv.create_polygon([390,280],[420,340],[510,290],[470,220], fill="yellow", outline="yellow")
canv.create_polygon([510,290],[540,260],[497,267.25],fill="yellow", outline="yellow")
canv.create_polygon([497,267.25],[545,220],[483,242.75], fill="yellow", outline="yellow")
canv.create_polygon([483,242.75],[520,198],[470,220], fill="yellow", outline="yellow")


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

canv.create_text(350, 60, 
            text="Uвых",
            justify=CENTER, font="Verdana 14")
canv.create_text(230, 160, 
            text="ко-ко-ко!",
            justify=CENTER, font="Verdana 14")
canv.create_text(245, 270, 
            text="Uпитания",
            justify=CENTER, font="Verdana 14")
canv.create_text(460, 280, 
            text="Uпитания",
            justify=CENTER, font="Verdana 14")
canv.create_text(460, 280, 
            text="Uпитания",
            justify=CENTER, font="Verdana 14")
canv.create_text(195, 555, 
            text="R1",
            justify=CENTER, font="Verdana 14")
canv.create_text(70, 310, 
            text="Rос",
            justify=CENTER, font="Verdana 14")




#Импортируем библиотеку для работы с изображениями и вставляем фото
pilImage = Image.open(path)
image = ImageTk.PhotoImage(pilImage)
imagesprite = canv.create_image(350,160,image=image)


#Нарисуем сопротивления
#Нарисуем R1
canv.create_line(180,600,225,600, width=2, fill="magenta2")
canv.create_line(225,600,225,540, width=2, fill="magenta2")
canv.create_line(225,540,180,540, width=2, fill="magenta2")
canv.create_line(180,540,180,600, width=2, fill="magenta2")
#Нарисуем Rос
canv.create_line(95,340,120,340, width=2, fill="magenta2")
canv.create_line(120,340,120,300, width=2, fill="magenta2")
canv.create_line(120,300,95,300, width=2, fill="magenta2")
canv.create_line(95,300,95,340, width=2, fill="magenta2")

#Нарисуем провода
canv.create_line(210,520,110,520, width=2, fill="black")
canv.create_line(110,520,110,120, width=2, fill="black")
canv.create_line(110,120,310,120, width=2, fill="black")

#Нарисуем заземление
canv.create_line(490,520,550,520, width=2, fill="black")
canv.create_line(550,550,550,490, width=4, fill="black")






window.mainloop()



    
