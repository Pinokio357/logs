import argparse

"""
пример запуска в терминале:
python ./hw_15_3.py 42 5
"""


parser =argparse.ArgumentParser("homework parser")
parser.add_argument("nums", type=int, nargs="*", metavar="N",
                    help="введите загадываемое число и количество попыток(оба числа должны быть целыми положительными)")
args = parser.parse_args()

def guess_number(num, count):
    def game():
        for i in range(1, count + 1):
            data = input("введите число: ")
            try:
                number = int(data)
            except:
                print("нужно ввести целое положительное число")
            else:
                if number < num:
                    print(f"число {number} меньше загаданного")
                elif number > num:
                    print(f"число {number} больше загаданного")
                else:

                    return print(f"вы угадали число {num} с {i} попыток")

        return print(f"вы не угадали число {num} с {count} попыток")

    return game


num = args.nums[0]
count = args.nums[1]
guess_number(num, count)()
