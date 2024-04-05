def read_file(filename):
    #Зчитуємо вміст файлу.
    with open(filename, 'r') as file:
        content = file.readlines()
    return content

#Порівнюємо вміст двох файлів.
def compare_files(file1_content, file2_content):
    common_lines = []
    diff_lines = []

    for line in file1_content:
        if line in file2_content:
            common_lines.append(line)
        else:
            diff_lines.append(line)

    for line in file2_content:
        if line not in file1_content:
            diff_lines.append(line)

    return common_lines, diff_lines

#Записуємо рядки у файл.
def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def main():
    file1 = "file1.txt"
    file2 = "file2.txt"
    same_file = "same.txt"
    diff_file = "diff.txt"

    #Зчитуємо вміст файлів
    file1_content = read_file(file1)
    file2_content = read_file(file2)

    #Порівнюємо файли
    common_lines, different_lines = compare_files(file1_content, file2_content)

    #Записуємо результати у відповідні файли
    write_to_file(same_file, common_lines)
    write_to_file(diff_file, different_lines)

    print("The operation is complete.")

if __name__ == "__main__":
    main()