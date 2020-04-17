#!/usr/bin/python3
import argparse
import matplotlib.pyplot as plt
import utility as ut
import numpy as np
import matplotlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', type=str, help='input .csv file')
    parser.add_argument('-s', '--show_save', type=str, help='presenting plot; mode: 0(showing plot), 1(saving plot to given path)')
    args = parser.parse_args()

    # assigning columns' to the proper axes
    x_axis = 'year'
    y_axis = 'AverageTemperatureCelsius'

    data = ut.data_for_scatter(args.input_file, xax=x_axis, yax=y_axis)

    fig, ax = plt.subplots(figsize=(7, 5))
    years = data[0]
    temps = data[1]
    col_names = data[2]

    for year, temp in zip(years, temps):
        ax.scatter([year] * len(temp), temp, color='black', s=20)

    ax.set_ylim(ut.max_min(temps)[2:4])

    # setting values of ticks for future grid
    major_xticks = np.arange(1800, 2100, 100)
    major_yticks = np.arange(-10, 40, 10)
    minor_xticks = np.arange(1750, 2000, 50)
    minor_yticks = np.arange(-10, 40, 5)

    ax.set_xticks(major_xticks)
    ax.set_yticks(major_yticks)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_yticks(minor_yticks, minor=True)

    # background and grid
    ax.set_axisbelow(True)  # grid behind scatter
    ax.set_facecolor('0.8') # background colour
    ax.grid(which='major', b=True, linestyle='-', linewidth=1.5, color='0.95')
    ax.grid(which='minor', b=True, linestyle='-', linewidth=.5, color='0.95')

    # set title of axes
    ax.set_ylabel(y_axis, fontsize=15)
    ax.set_xlabel(x_axis, fontsize=15)

    # set properties of ticks
    plt.xticks(color='gray', alpha=0.7)
    plt.yticks(color='gray', alpha=0.7)
    ax.tick_params(which='major', labelsize=15, length=5, width=1, color='0.7') # showing major spines
    ax.tick_params(which='minor', color='1') # hiding minor spines

    # hiding frames
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    print('Plotting fig')
    if args.show_save == '0':
        plt.show()
    else:
        plt.savefig('plots/task2b.png', bbox_inches='tight')
        print('Saving plot in plots dir.')
    print('Done')

if __name__ == '__main__':
    main()