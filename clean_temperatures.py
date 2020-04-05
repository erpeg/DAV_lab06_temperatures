#!/usr/bin/python

import argparse
import pandas

def file_to_nested_list(file_name):
    with open(file_name) as file:
        file = file.read().split('\n')
        file = [line.replace('\"', '').split(',') for line in file]
    return file


def main():
    # creating a parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', type=str, help='Pass name of file to clean')
    args = parser.parse_args()

    list_of_temps = file_to_nested_list(args.file_name)

    nr_categories = len(list_of_temps[0])

    # removing incomplete lines
    list_of_temps = [line for line in list_of_temps if len(line) == nr_categories]

    new_list = []

    # removing lines with lacking temperatures
    # 4 - Avg temp
    # 5 - Avg Unc Temp
    # 6 - City
    # 8 - Country
    for line in list_of_temps:
        if line[4] == 'NA':
            break
        elif line[5] == 'NA':
            break
        elif line[6] == 'NA':
            break
        elif line[8] == 'NA':
            break
        else:
            new_list.append(line)


    # list_of_temps = [line for line in list_of_temps if line[4] != 'NA' and line[5] != 'NA'] # poprawić conditions
    # list_of_temps = [line for line in list_of_temps if line[6] != 'NA' and line[8] != 'NA'] # poprawić conditions





    for line in new_list[0:50]:
        print(line)
    print(len(list_of_temps[-1]))


if __name__ == '__main__':
    main()
