import itertools
import random
import argparse
import logging

# Для ТЕСТА команда для запуска:   python chess.py --attempts 5

logging.basicConfig(filename='queens_solver.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def queens(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            row1, col1 = queens_positions[i]
            row2, col2 = queens_positions[j]

            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                return False
    return True

def generation_successful(attempts):
    successful_args = []

    permutations = list(itertools.permutations(range(1, 9)))
    random.shuffle(permutations)

    for permutation in permutations:
        queens_positions = [(i + 1, permutation[i]) for i in range(8)]
        if queens(queens_positions):
            successful_args.append(queens_positions)
            if len(successful_args) == attempts:
                break

    return successful_args

def main():
    parser = argparse.ArgumentParser(description='Solve the N-Queens problem.')
    parser.add_argument('--attempts', type=int, default=4, help='Number of successful arrangements to find.')
    args = parser.parse_args()

    successful_arrangements = generation_successful(args.attempts)
    print(f"{args.attempts} успешных расстановки:")
    logging.info(f"Finding {args.attempts} successful arrangements.")

    for i, arrangement in enumerate(successful_arrangements, 1):
        print(f'Расстановка {i}: {arrangement}')
        logging.info(f'Successful arrangement {i}: {arrangement}')

if __name__ == "__main__":
    main()
