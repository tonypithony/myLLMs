# conda create --name TesseracT
# conda activate TesseracT

# https://codeby.net/threads/raspoznaem-tekst-na-izobrazhenii-dvumja-bibliotekami-s-pomoschju-python.80139/

# pip install pytesseract
# pip install easyocr


import os.path
from PIL import Image

import easyocr
import pytesseract

# Если вы используете ОС Windows # путь к исполняемому файлу tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# распозавание с помощью pytesseract, открытие картинки PIL.Image
def teseract_recognition(path_img):
    return pytesseract.image_to_string(Image.open(path_img), lang='rus+eng', config=r'--oem 3 --psm 6')


mag_ratio=2

# распознавание с помощью easyocr, параметры: отключена детализация вывода,
# включены параграфы и установлена точность текста
def easyocr_recognition(path_img):
    return easyocr.Reader(['ru','en'], gpu=False).readtext(path_img,
        detail=1,
# detail= если значение равно 1 (по умолчанию), то вывод будет подробным с координатами ограничивающего прямоугольника.
# В противном случае, если значение равно 0, выходные данные состоят только из распознанных текстов.
        paragraph=True, # объединить результат в параграф
        contrast_ths=0.1, 
# Текстовое поле с контрастом ниже этого значения будет передано в модель 2 раза.
# Первый - с исходным изображением, второй - с контрастом, отрегулированным по значению 'adjust_contrast'.
# В результате будет возвращено изображение с более уверенным уровнем.
        adjust_contrast= 0.5, # целевой уровень контрастности для низкоконтрастного текстового поля
        text_threshold=0.8, # порог достоверности текста
        low_text=0.4, # оценка низкой границы текста
        mag_ratio=mag_ratio, # коэффициент увеличения изображения
        slope_ths=0.1)
# Максимальный наклон (delta y/delta x) для рассматриваемого слияния.
# Малое значение означает, что плиточные боксы не будут объединяться.


# сохранение текста в текстовый файл
def save_text(text, name):
    with open(f'{name}.txt', 'w', encoding='utf-8') as file:
        file.write(str(text))
    print(f'[+] Распознанный текст сохранен в файл: "{name}.txt"')
    main()
    return


# ввод данных и выбор библиотеки для распознавания
def main():
    path_img = input('\n[+] Введите путь к картинке\n - Для выхода введите x\n   >>> ')
    if path_img == "x":
        exit(0)
    if not os.path.exists(path_img):
        print('[+] Картинки не существует')

    user_change = input('\n[+] Выберите библиотеку для распознавания текста:\n   [1] Tesseract OCR\n   '
                        '[2] EasyOCR\n   [3] Выход\n   >>> ')
    if user_change == "1":
        save_text(teseract_recognition(path_img), os.path.split(path_img)[1].split(".")[0] + "TesseractOCR")
    elif user_change == '2':
        save_text(easyocr_recognition(path_img), os.path.split(path_img)[1].split(".")[0] + "mr=" + str(mag_ratio))
    elif user_change == "3":
        exit(0)
    else:
        print('[+] Неопознанный ввод. Повторите все сначала')
        main()


if __name__ == "__main__":
    main()


# import pytesseract
# from PIL import Image

# # img = Image.open('phone_number.png')
# # img = Image.open('eng_text.png')
# img = Image.open('test1.jpg')

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
# # C:\Program Files\Tesseract-OCR

# file_name = img.filename
# file_name = file_name.split(".")[0]

# # custom_config = r'--oem 3 --psm 13'
# custom_config = r'--oem 3 --psm 6'

# text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
# print(text)

# with open(f'{file_name}.txt', 'w') as text_file:
#     text_file.write(text)