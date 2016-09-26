import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

mode = int(input('mode:')) #Считываем номер преобразования. 
image = Image.open("planet.png") #Открываем изображение.
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
pix = image.load() #Выгружаем значения пикселей.
if (mode == 2):
    for i in range(width):
        for j in range(height):
            if(i%24==0 and j%24==0):
             a = pix[i, j][0]
             b = pix[i, j][1]
             c = pix[i, j][2]
             y=i//25
             x=j//25
             draw.point((y, x), (a, b,c))
image.save("ans.jpg", "JPEG")
del draw