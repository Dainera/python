# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import argparse


def count_salary(hours, rate_per_hour, award=0):
    try:
        if hours <= 0:
            print('Hours must be more than 0')
        elif rate_per_hour <= 0:
            print('Rate must be more than 0')
        elif award < 0:
            print('Award must be more than 0 or equal')
        else:
            return round((hours * rate_per_hour) + award, 4)
    except ValueError:
        print('Bad values')


args_parser = argparse.ArgumentParser(add_help=True, description='Employee salary calculating')

args_parser.add_argument('hours', help='Working hours', type=int)
args_parser.add_argument('rate', help='Rate per hour', type=float)
args_parser.add_argument('award', help='Award', type=float)

args = args_parser.parse_args()

print(f'Salary: {count_salary(args.hours, args.rate, args.award)}')
