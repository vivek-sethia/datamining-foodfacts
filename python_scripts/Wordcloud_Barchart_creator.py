import csv
import os, re
import random
from os import path

from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
from wordcloud import WordCloud


class touple:
    def __init__(self, x, y):
        self.col_val = x
        self.interval_col_val = y


def get_average_x_by_y(x, y):
    pass


# interval_columns_and_intervals is a list of maps<str, list> like
# [{"energy_100g": [100, 1000]}, {"fats_100g": [80, 100]}] to get all items with energy between 100 & 1000
# and fats between 80 & 100
def get_items_within_interval(csvreader, interval_columns_and_intervals):
    pass


#    header = []
#    rownum = 0
#    column_as_num = 0.5  # float value so it causes an error if it doesn't get changed later
#    interval_column_as_num = 0.5
#    for row in csvreader:
#        # Save header row.
#        if rownum == 0:
#            header = row
#            for i in range(len(header)):  # find number-position of column-param
#                if header[i] == column:
#                    column_as_num = i
#                if header[i] == interval_column:
#                    interval_column_as_num = i
#        else:
#            colnum = 0
#            for col in row:
#                if header[colnum] == interval_column:
#                    interval_counter = 0
#                    for interval in intervals:
#                        try:
#                            if interval[0] <= float(col) <= interval[1]:
#                                toupe = touple(row[column_as_num], row[interval_column_as_num])
#                                wordlists[interval_counter].append(toupe)
#                            interval_counter += 1
#                        except ValueError:  # if the col is empty or not a float
#                            if not col == "":  # empty value
#                                print("value error with column-value: %s" % col)

#                colnum += 1

#        rownum += 1

# intervals is a list of lists, e.g. [[0, 100], [101, 200]] to create separate wordlists for
# all items with value 0-100 and all with 101-200
# interval_column is the column we look at for the intervals, e.g. 'energy_100g' so we
# cluster all items with 0-100 kJ energy and all with 101-200 kJ
# column is the column we take the words from, e.g. 'packaging' so we get the packaging-wordlist
# for all items with 0-100 kJ energy and another list for all with 101-200 kJ
def create_word_or_number_lists_by_cluster(csvreader, intervals, interval_column, column):
    wordlists = [[] for i in range(len(intervals))]

    header = []
    rownum = 0
    column_as_num = 0.5  # float value so it causes an error if it doesn't get changed later
    interval_column_as_num = 0.5
    for row in csvreader:
        # Save header row.
        if rownum == 0:
            header = row
            for i in range(len(header)):  # find number-position of column-param
                if header[i] == column:
                    column_as_num = i
                if header[i] == interval_column:
                    interval_column_as_num = i
        else:
            colnum = 0
            for col in row:
                if header[colnum] == interval_column:
                    interval_counter = 0
                    for interval in intervals:
                        try:
                            # for values like "30 g" or "22 mL"; should clean the database so everything uses the
                            # same unit, but for now this will do
                            # if re.search('[a-zA-Z]', col) and any(i.isdigit() for i in col):
                            #    ints_in_str = [int(s) for s in col.split() if s.isdigit()]
                            #    col = ints_in_str[0]

                            if interval[0] <= float(col) <= interval[1]:
                                toupe = touple(row[column_as_num], row[interval_column_as_num])
                                wordlists[interval_counter].append(toupe)
                            interval_counter += 1
                        except ValueError:  # if the col is empty or not a float
                            if not col == "":  # empty value
                                print("value error with column-value: %s" % col)

                colnum += 1

        rownum += 1

    # for wordlist in wordlists:
    #     print(wordlist)
    #     print("\n\n")
    return wordlists


def split_list(ls, chunk_size):
    return [ls[i:i + chunk_size] for i in range(0, len(ls), chunk_size)]


def create_dir_if_doesnt_exist(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def write_wordlist_to_file(wordlist, file_name):
    with open(file_name + ".txt", 'w', encoding='utf-8') as f:
        f.write(", ".join(wordlist))


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


def write_wordcloud_from_wordlist(wordlist, output_file_name):
    mask = np.array(Image.open("WordcloudMask.png"))

    plt.axis("off")
    if wordlist == []:
        print("Wordlist empty!!!")

    # generate with lower max_font_size
    wordcloud = WordCloud(max_font_size=80, max_words=100, mask=mask).generate(wordlist)
    plt.figure()
    plt.imshow(wordcloud.recolor(color_func=grey_color_func))
    plt.axis("off")
    plt.savefig(output_file_name + '_wordcloud.png', bbox_inches='tight')

    plt.close()


def write_barchart_from_intlist(touple_list, output_file_name, xlabel, ylabel):
    touple_list.sort(key=lambda t: t.interval_col_val)

    chunk_count = 20
    x_axis_blocks = split_list(touple_list, int(len(touple_list) / chunk_count))

    y_axis_blocks_average_col_values = []
    x_axis_blocks_average_interval_col_values = []
    for x_block in x_axis_blocks:
        column_sum = 0
        interval_column_sum = 0
        for touple in x_block:
            try:
                column_sum += float(touple.col_val)
                interval_column_sum += float(touple.interval_col_val)
            except ValueError:
                pass
        y_axis_blocks_average_col_values.append(column_sum / len(x_block))
        x_axis_blocks_average_interval_col_values.append(interval_column_sum / len(x_block))

    # intlist = []
    # for i in range(len(touple_list)):
    #     try:
    #         intlist.append(float(touple_list[i].col_val))
    #     except ValueError:
    #         print("Value error in barchart: %s" % touple_list[i])

    ind = np.arange(chunk_count)
    width = 1
    try:
        width = max(x_axis_blocks_average_interval_col_values) / 30
    except:
        pass

    fig, ax = plt.subplots()

    if x_axis_blocks != []:
        bars = ax.bar(x_axis_blocks_average_interval_col_values, y_axis_blocks_average_col_values, width, color='b')
    else:  # if x axis contains strings instead of numbers
        bars = ax.bar(ind, y_axis_blocks_average_col_values, width, color='b')

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # ax.set_title('title')
    # ax.set_xticks(ind + width)
    # ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

    # ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')
    plt.savefig(output_file_name + '_barchart.png', bbox_inches='tight')


def create_data_folder(csvfile, folder_name, csvreader, intervals, interval_column, column):
    csvfile.seek(0)
    try:
        create_dir_if_doesnt_exist(folder_name)
        wordlists = create_word_or_number_lists_by_cluster(csvreader, intervals, interval_column, column)
        col_only_lists = []
        for wordlist in wordlists:
            wordlist = [wl for wl in wordlist if wl.col_val != "" and wl.interval_col_val != ""]
            ls = [wl.col_val for wl in wordlist]
            col_only_lists.append(ls)

        for i in range(len(intervals)):
            write_wordlist_to_file(col_only_lists[i], folder_name + "/" + str(intervals[i]))
            write_wordcloud_from_wordlist(str(col_only_lists[i]), folder_name + "/" + str(intervals[i]))

            try:
                # print(col_only_lists[0][0], "\n\n")
                # print(col_only_lists[0])
                float(col_only_lists[0][0])
                write_barchart_from_intlist(wordlists[i], folder_name + "/" + str(intervals[i]), interval_column,
                                            column)
            except ValueError:
                pass
    except Exception as e:
        print(e)
        print("Exception with: %s, %s, %s, %s" % (folder_name, str(intervals), str(interval_column), str(column)))


def run():
    csv.field_size_limit(9999999)

    with open('en.openfoodfacts.org.products.csv', newline='', encoding='utf-8') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)

        # create_data_folder(csvfile, "packaging_by_energy", reader, [[0, 100], [101, 1000], [1001, 3000]], 'energy_100g',
        #                   'packaging')
        #
        create_data_folder(csvfile, "fat_by_energy", reader, [[0, 1000], [0, 999999]], 'energy_100g', 'fat_100g')
        #
        # create_data_folder(csvfile, "saturated_fat_by_energy", reader,
        #                   [[0, 1000], [1001, 2000], [2001, 3000], [3001, 5000]],
        #                   'energy_100g', 'saturated-fat_100g')
        #
        # create_data_folder(csvfile, "sugar_by_energy", reader, [[0, 1000], [1001, 2000], [2001, 3000], [3001, 5000]],
        #                   'energy_100g', 'sugars_100g')
        #
        # create_data_folder(csvfile, "energy_by_serving_size", reader, [[0, 9999999]],
        #                   'serving_size', 'energy_100g')
        #
        # create_data_folder(csvfile, "sugars_by_serving_size", reader, [[0, 9999999]],
        #                   'serving_size', 'sugars_100g')
        #
        # create_data_folder(csvfile, "fats_by_serving_size", reader, [[0, 9999999]],
        #                   'serving_size', 'fat_100g')

        create_data_folder(csvfile, "energy_by_fats", reader, [[0, 9999999]],
                           'fat_100g', 'energy_100g')
        create_data_folder(csvfile, "energy_by_carbohydrates", reader, [[0, 9999999]],
                           'carbohydrates_100g', 'energy_100g')
        create_data_folder(csvfile, "energy_by_sugars", reader, [[0, 9999999]],
                           'sugars_100g', 'energy_100g')

        # create_data_folder(csvfile, "additives_by_fats", reader, [[0, 9999999]],
        #                   'fat_100g', 'additives_n')
        # create_data_folder(csvfile, "additives_by_carbohydrates", reader, [[0, 9999999]],
        #                   'carbohydrates_100g', 'additives_n')
        # create_data_folder(csvfile, "additives_by_sugars", reader, [[0, 9999999]],
        #                   'sugars_100g', 'additives_n')
        # create_data_folder(csvfile, "additives_by_energy", reader, [[0, 9999999]],
        #                   'energy_100g', 'additives_n')
        #
        # create_data_folder(csvfile, "cholesterol_by_fats", reader, [[0, 9999999]],
        #                   'fat_100g', 'cholesterol_100g')
        # create_data_folder(csvfile, "cholesterol_by_energy", reader, [[0, 9999999]],
        #                   'energy_100g', 'cholesterol_100g')
        # create_data_folder(csvfile, "cholesterol_by_sodium", reader, [[0, 9999999]],
        #                   'sodium_100g', 'cholesterol_100g')
        #
        # create_data_folder(csvfile, "sodium_by_fats", reader, [[0, 9999999]],
        #                   'fat_100g', 'sodium_100g')
        # create_data_folder(csvfile, "sodium_by_energy", reader, [[0, 9999999]],
        #                   'energy_100g', 'sodium_100g')


if __name__ == "__main__":
    run()
