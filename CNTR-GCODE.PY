import re

def parse_gcode(file_path):
    # Чтение G-кода и извлечение координат X и Y
    x_coords = []
    y_coords = []
    with open(file_path, 'r') as file:
        for line in file:
            # Ищем строки с командами G1 для перемещения с координатами X и Y
            match = re.search(r'G1\s+X(-?\d+\.\d*)\s+Y(-?\d+\.\d*)', line)
            if match:
                x = float(match.group(1))
                y = float(match.group(2))
                x_coords.append(x)
                y_coords.append(y)
    return x_coords, y_coords

def calculate_bounding_box(x_coords, y_coords):
    # Определяем габариты контура
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    # Центр прямоугольника с округлением до 4 знаков после запятой
    center_x = round((min_x + max_x) / 2, 4)
    center_y = round((min_y + max_y) / 2, 4)
    
    return (min_x, min_y, max_x, max_y), (center_x, center_y)

# Пример использования
file_path = 'plt-7.txt'  # Укажите путь к вашему файлу G-кода
x_coords, y_coords = parse_gcode(file_path)
bounding_box, center = calculate_bounding_box(x_coords, y_coords)

print("Bounding box:", bounding_box)
print("Center coordinates:", center)
