import pytest
import os
from main_tasks import read_file, compare_files

@pytest.fixture
def setup_files():
    #Створюємо тимчасові файли для тестування
    file1_content = [
        "line1\n",
        "line2\n",
        "line3\n"
    ]
    file2_content = [
        "line2\n",
        "line3\n",
        "line4\n"
    ]

    file1 = "test1_file1.txt"
    file2 = "test1_file2.txt"

    #Записуємо вміст файлів
    with open(file1, 'w') as f1:
        f1.writelines(file1_content)

    with open(file2, 'w') as f2:
        f2.writelines(file2_content)

    yield file1, file2

    #Після виконання тесту видаляємо тимчасові файли
    os.remove(file1)
    os.remove(file2)

def test_compare_files(setup_files):
    file1, file2 = setup_files

    file1_content = read_file(file1)
    file2_content = read_file(file2)

    common_lines, different_lines = compare_files(file1_content, file2_content)

    assert common_lines == ["line2\n", "line3\n"]
    assert different_lines == ["line1\n", "line4\n"]



