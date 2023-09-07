import sys
import logging

# Для ТЕСТА команда для запуска: python dictionary.py 8 топор:1.5 пиво:3 горелка:2 удочка:2 фонарик:0.5 котелок:1 ож:1 спички:0.5

logging.basicConfig(filename='backpack.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

def find_possible_combinations(items, max_weight):
    combinations = []

    def find_combinations(item_index, current_combination, current_weight):
        if current_weight == max_weight:
            combinations.append(current_combination[:])
            return

        if current_weight > max_weight or item_index == len(items):
            return

        item, weight = items[item_index]
        if current_weight + weight <= max_weight:
            current_combination.append(item)
            find_combinations(item_index + 1, current_combination, current_weight + weight)
            current_combination.pop()
        find_combinations(item_index + 1, current_combination, current_weight)

    find_combinations(0, [], 0)
    return combinations

def main():
    if len(sys.argv) < 3:
        print("Использование: python dictionary.py <вместимость рюкзака> <предмет1:вес1> <предмет2:вес2> ...")
        return

    backpack_capacity = float(sys.argv[1])
    items_list = [(item_weight.split(':')[0].lower(), float(item_weight.split(':')[1])) for item_weight in sys.argv[2:]]

    combinations = find_possible_combinations(items_list, backpack_capacity)

    if len(combinations):
        for i, combination in enumerate(combinations, start=1):
            print(f'Вариант {i}')
            print(f'Вещи: {", ".join(combination)}')
            print(f'Общая масса: {sum(items[1] for items in items_list if items[0] in combination)}')
            print('---')
            logging.info(f'Вариант {i}')
            logging.info(f'Вещи: {", ".join(combination)}')
            logging.info(f'Общая масса: {sum(items[1] for items in items_list if items[0] in combination)}')
    else:
        print("Нет подходящих комбинаций")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Произошла ошибка: {str(e)}", exc_info=True)
