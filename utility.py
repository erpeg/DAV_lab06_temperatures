#!/usr/bin/python3

import argparse
import matplotlib.pyplot as plt
import csv
import collections

# possible key_value: year, country_id, Country
def dict_to_plot(list, x_axis, y_axis):
    # creating dictionary of column indexes
    col_dict = {}
    col_names = list[0]
    for value, key in enumerate(list[0]):
        col_dict[key] = value
    # using col_dict to index by passed in the function name of column
    temps_dict = collections.OrderedDict()
    try:
        for line in list[1:]:
            if line[col_dict[x_axis]] in temps_dict:
                temps_dict[line[col_dict[x_axis]]].append(line[col_names.index(y_axis)])
            else:
                temps_dict[line[col_dict[x_axis]]] = [line[col_names.index(y_axis)]]
    except:
        print('Improper names of axises')
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

def data_for_scatter(file_path, xax, yax):
    file_list = open_file(file_path)
    col_names = file_list[0]
    data = dict_to_plot(file_list, x_axis=xax, y_axis=yax)

    # create ordered dict
    ordered_data = collections.OrderedDict()

    # sorting loaded dict
    for key in sorted(data):
        ordered_data[key] = [float(element) for element in data[key]]

    years = [int(year) for year in ordered_data.keys()][::-1]
    temps = [temps for temps in ordered_data.values()][::-1]

    return years, temps, col_names



