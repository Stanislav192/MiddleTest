import pytest
import os
from main_tasks import write_to_file

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

def test_write_to_file(setup_files):
    content = ["test line 1\n", "test line 2\n", "test line 3\n"]
    output_file = "test_output.txt"

    write_to_file(output_file, content)

    assert os.path.exists(output_file)

    with open(output_file, 'r') as f:
        written_content = f.readlines()

    assert written_content == content

    # Після виконання тесту видаляємо тимчасові файли
    os.remove(output_file)