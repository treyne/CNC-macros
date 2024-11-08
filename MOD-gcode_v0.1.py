def process_gcode(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    contour_lines = []
    is_in_contour = False
    e_value = "E1"

    for i, line in enumerate(lines):
    # Заменяем E101 на E1
        if "E101" in line:
            line = line.replace("E101", "")
            
        if "M20" in line:
            line = line.replace("M20", "")    
            
        if "G0" in line:
            line = line.replace("G0", "G92")        
        
        
        if "M21" in line:
            line = line.replace("M21", "M2")
            next_line = lines[i + 1]
        # Проверяем, содержит ли текущая строка "(Insert wire)"
        if "(Insert wire)" in line:
            e_value = "E1"  # Устанавливаем E1 для нового контура
            if i + 3 < len(lines):
                 # Добавляем текущую строку и E1
                processed_lines.append(line)
                processed_lines.append(e_value + "\n")
                # next_line = lines[i + 1]
                # processed_lines.append(next_line)  # Добавляем следующую строку в результат    
            is_in_contour = True
            contour_lines = []
            continue
        elif "(Break wire)" in line:
            # Добавляем исходный контур с E1
            processed_lines.extend(contour_lines)

            # Создаем копию контура и заменяем E1 на E2, H1 на H2
            processed_lines.append("E2" + "\n")
            for contour_line in contour_lines:
                processed_lines.append(contour_line.replace("E1", "E2").replace("H1", "H2"))

            # Закрываем контур и добавляем (Break wire)
            processed_lines.append(line)
            is_in_contour = False
            continue

        # Если в контуре, сохраняем строки для дальнейшей обработки
        if is_in_contour:
            contour_lines.append(line)
        else:
            processed_lines.append(line)

    # Записываем результат в файл
    with open(output_file, 'w') as file:
        file.writelines(processed_lines)


# Пример использования
input_file = 'plt-7.txt'  # Имя исходного файла
output_file = 'output.gcode'  # Имя выходного файла
process_gcode(input_file, output_file)
