import os

current_dir = os.path.dirname(__file__)    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'tips.txt')           # добавляем к этому пути имя файла 
print(current_dir)
print(file_path)