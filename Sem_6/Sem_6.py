import os
import logging
from collections import namedtuple

# Для ТЕСТА команда для запуска: python Sem_6.py C:\путь\путь\путь\PyCharm_HW_Final\Sem_6

logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_file_info(path):

    if not os.path.exists(path) or not os.path.isdir(path):
        logging.error(f'Директория не найдена: {path}')
        return

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        is_directory = os.path.isdir(item_path)

        name = os.path.splitext(item)[0] if not is_directory else item

        extension = os.path.splitext(item)[1] if not is_directory else ""

        parent_directory = os.path.basename(path)

        file_info = FileInfo(name, extension, is_directory, parent_directory)
        logging.info(file_info)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Собрать информацию о файлах и каталогах в указанной директории.')
    parser.add_argument('directory_path', type=str, help='Путь к директории для анализа')

    args = parser.parse_args()
    directory_path = args.directory_path

    get_file_info(directory_path)
