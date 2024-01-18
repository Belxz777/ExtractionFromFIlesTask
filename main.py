cat_list = []
dog_list = []

# читаем файл ветклиник
with open('vetclinic.txt', 'r',encoding='utf-8') as file:
  # читаем все строки файла и записываем в переменную lines 
    lines = file.readlines()
  #  print(lines)

# далее проходим циклом for по каждой строке 
for line in lines:
# выделяем тип животного , имя и болезнь
# все значения разграничены запятой и мы может выделить именно значения 
    # с помощью метода split
    animal, name, disease = line.strip().split(',')
   # print(animal, name, disease)
    # дальше проверям если тип животного кошка добавляем его в массив cats_list 
    # иначе в dogs_list 
    if animal.lower() == 'кошка':
        cat_list.append((name, disease))
    elif animal.lower() == 'собака':
        dog_list.append((name, disease))

# далее открываем файл cats.txt для записи в него массива кошек 
with open('cats.txt', 'w',encoding='utf-8') as cat_file:
    for name, disease in cat_list:
        cat_file.write(f'{name},{disease}\n')
# то же самое делаем с собаками 
with open('dogs.txt', 'w',encoding='utf-8') as dog_file:
    for name, disease in dog_list:
        dog_file.write(f'{name},{disease}\n')