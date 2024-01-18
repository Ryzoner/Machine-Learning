import csv

# Путь к файлу с данными о ноутбуках
input_file = 'laptops_data.txt'

# Список для хранения данных о ноутбуках
laptops_data = []

# Чтение данных из файла
with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(',')
        model = parts[0]
        configuration = parts[1]
        price = float(parts[2])
        laptop = {"Model": model, "Configuration": configuration, "Price": price}
        laptops_data.append(laptop)

# Путь к выходному файлу CSV
output_file = 'laptops.csv'

# Запись данных в CSV файл
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Model', 'Configuration', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for laptop in laptops_data:
        writer.writerow(laptop)
