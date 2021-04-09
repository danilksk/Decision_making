# Предопределённые переменные 
massiv = [[-121,62,245,245,245,245],
		[-100,-14,198,380,380,380],
		[-216,33,150,332,315,515],
		[-264,-81,101,284,468,650]] # Исходный массив
a = 0.47 # Альфа для критерия Гурвица

# Временные переменные
temp = 0
temp_method_1 = 0
temp_method_2 = 0
temp_method_3 = 0 

# Пустые списки для содержания значений
massiv_1 = []
massiv_2 = []
massiv_3 = [] # Списки для содержания значений Zi

# Кр. Лапласа
for i in range(len(massiv)):
    for j in range(len(massiv[i])): # Проход по всем значениям исходного массивы
        temp_method_1 = temp_method_1 + (1/len(massiv[i]) * massiv[i][j]) #Формула Критерия для составления списка с Zi
    massiv_1.append(temp_method_1) # Составления массива из Zi
for i in range(len(massiv_1)): 
    if massiv_1[i] == max(massiv_1): # Проход по списку с Zi для нахождения максимума, который и будет значением Критерия
        print("По критерию Лапласа -> D",i+1) #Вывод значения


# Кр. Гурвица
for i in range(len(massiv)): 
     temp_method_3 = a*min(massiv[i]) + (1-a)*max(massiv[i]) #Формула Критерия для составления списка с Zi
     massiv_3.append(temp_method_3)
for i in range(len(massiv_3)):
    if massiv_3[i] == max(massiv_3): # Проход по списку с Zi для нахождения максимума, который и будет значением Критерия
        print("По критерию Гурвица -> D",i+1)

#Кр. Сэвиджа
massiv_loss = list(massiv) #Создание копии оригинальной матрицы для создания матрицы убытков
massiv_loss_max = [] #Пустой список чтобы содержать в нём максимумы столбцов для составления матрицы убытков
for i in range(len(massiv[i])):
    temp_method_2 = massiv_loss[1][i] #Выведение первого элемента столбца для нахождения максиума относительно его
    for j in range(len(massiv)):
        if massiv_loss[j][i] > temp_method_2: # Сравнение элемента массива с текущим максимумом
            temp_method_2 = massiv_loss[j][i]
    massiv_loss_max.append(temp_method_2) #Введение максимального элемента столбца в список максимумов столбцов
for i in range(len(massiv)):
    for j in range(len(massiv[1])):
        massiv_loss[i][j] = massiv_loss_max[i] - massiv_loss[i][j] #Непосредственный подсчёт таблицы убытков
for i in range(len(massiv)):
    massiv_2.append(max(massiv_loss[i])) #Составление списка Zi на основе матрицы убытков
for i in range(len(massiv_2)):
    if massiv_2[i] == min(massiv_2): # Проход по списку с Zi для нахождения максимума, который и будет значением Критерия
        print("По критерию Сэвиджа -> D",i+1)
        break # Если есть одиннаковые значения, оба из которых являются максимум - выводится только первый


