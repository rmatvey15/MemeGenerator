from PIL import Image, ImageDraw, ImageFont
image_file = ""
print("Генератор мемов запущен!")
print("Список картинок: ")
print("1 Ниндзя.jpg")
print("2 Грустный человек.jpg")
print("3 Весёлая девочка.jpg")
print("4 Весёлый гриб.jpg")
print("5 Огонёк.jpg")
image_number = int(input("Введите номер картинки: "))
if image_number == 1:
    image_file = "Ниндзя.jpg"
elif image_number == 2:
    image_file = "Грустный человек.jpg"
elif image_number == 3:
    image_file = "Весёлая девочка.jpg"
elif image_number == 4:
    image_file = "Весёлый гриб.jpg"
elif image_number == 5:
    image_file = "Огонёк.jpg"
top_text = input("Введите верхнюю строку: ")
bottom_text = input("Введите нижнюю строку: ")
print(top_text, bottom_text)
image = Image.open(image_file)
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=70)
text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]
draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="black")
text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]
draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="black")
image.save("new_meme.jpg")
