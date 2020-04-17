#!/usr/bin/python3
import argparse
import matplotlib.pyplot as plt
import utility as ut


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', type=str, help='input .csv file')
    parser.add_argument('-s', '--show_save', type=str, help='presenting plot; mode: 0(showing plot), 1(saving plot to given path)')
    args = parser.parse_args()
    # assigning columns' to the proper axes
    x_axis = 'year'
    y_axis = 'AverageTemperatureCelsius'

    data = ut.data_for_scatter(args.input_file, xax=x_axis, yax=y_axis)

    fig, ax = plt.subplots(figsize=(6.5, 4))
    years = data[0]
    temps = data[1]
    col_names = data[2]

    for year, temp in zip(years, temps):
        ax.scatter([year] * len(temp), temp, edgecolors='black', facecolors='none')

    ax.set_ylim(ut.max_min(temps)[2:4])
    # set title of axes
    ax.set_ylabel(y_axis, fontsize=14)
    ax.set_xlabel(x_axis, fontsize=14)

    ax.tick_params(labelsize=13)
    ax.tick_params(axis='y', labelrotation=90)

    print('Plotting fig')
    if args.show_save == '0':
        plt.show()
    else:
        plt.savefig('plots/task2a.png')
        print('Saving plot in plots dir.')
    print('Done')

if __name__ == '__main__':
    main()