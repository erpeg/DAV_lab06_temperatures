#!/usr/bin/python

import argparse
import matplotlib.pyplot as plt
import csv
import collections

# possible key_value: year, country_id, Country
def dict_to_plot(list, key_value):
    # creating dictionary of column indexes
    col_dict = {}
    for value, key in enumerate(list[0]):
        col_dict[key] = value
    # using col_dict to index by passed in the function name of column
    temps_dict = collections.OrderedDict()
    for line in list[1:]:
        if line[col_dict[key_value]] in temps_dict:
            temps_dict[line[col_dict[key_value]]].append(line[3])
        else:
            temps_dict[line[col_dict[key_value]]] = [line[3]]
    return temps_dict

def max_min(values_list):
    try:
        max_temp = round(max([max(temp) for temp in values_list]), 0)
        min_temp = round(min([min(temp) for temp in values_list]), 0)
        max_temp_mod = max_temp + 2
        min_temp_mod = min_temp - 2
    except:
        max_temp = round(max(values_list), 0)
        min_temp = round(min(values_list), 0)
        max_temp_mod = max_temp + 10
        min_temp_mod = min_temp - 10
    return min_temp, max_temp, min_temp_mod, max_temp_mod

def open_file(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        file = [row for row in reader]
    return file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', type=str, help='input .csv file')
    parser.add_argument('-m', '--mode', type=str, help='mode: scatter, box')
    parser.add_argument('-c', '--color', type=str, help='chose color of plot indicators')
    args = parser.parse_args()

    file_list = open_file(args.input_file)

    if args.mode == 'scatter':
        fig, ax = plt.subplots()

        # load data
        data = dict_to_plot(file_list, key_value='year')

        # create ordered dict
        ordered_data = collections.OrderedDict()

        # sorting loaded dict
        for key in sorted(data):
            ordered_data[key] = [float(element) for element in data[key]]

        years = [int(year) for year in ordered_data.keys()][::-1]
        temps = [temps for temps in ordered_data.values()][::-1]

        for year, temp in zip(years, temps):
            ax.scatter([year] * len(temp), temp)

        if args.color:
            plt.scatter(color = args.color)

        ax.set_ylim(max_min(temps)[2:4])
        # ax.set_xlim(max_min(years))


        # plt.savefig('test.png')
    print('plotting fig')
    plt.show()
    print('done')


if __name__ == '__main__':
    main()