import re, sys
import csv


# intervals is a list of lists, e.g. [[0, 100], [101, 200]] to create separate wordlists for
# all items with value 0-100 and all with 101-200
# interval_column is the column we look at for the intervals, e.g. 'energy_100g' so we
# cluster all items with 0-100 kJ energy and all with 101-200 kJ
# column is the column we take the words from, e.g. 'packaging' so we get the packaging-wordlist
# for all items with 0-100 kJ energy and another list for all with 101-200 kJ
def create_wordlists_by_cluster(csvreader, intervals, interval_column, column):
    wordlists = [[] for i in range(len(intervals))]

    header = []
    rownum = 0
    column_as_num = 0.5  # float value so it causes an error if it doesn't get changed later
    for row in csvreader:
        # Save header row.
        if rownum == 0:
            header = row
            for i in range(len(header)):  # find number-position of column-param
                if header[i] == column:
                    column_as_num = i
                    break
        else:
            colnum = 0
            for col in row:
                if header[colnum] == interval_column:
                    interval_counter = 0
                    for interval in intervals:
                        try:
                            if interval[0] <= float(col) <= interval[1]:
                                wordlists[interval_counter].append(row[column_as_num])
                            interval_counter += 1
                        except ValueError:  # if the col is empty or not a float
                            pass

                colnum += 1

        rownum += 1

    for wordlist in wordlists:
        print(wordlist)
        print("\n\n")
    return wordlists


def run():
    csv.field_size_limit(9999999)

    with open('en.openfoodfacts.org.products.csv', newline='', encoding='utf-8') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)

        create_wordlists_by_cluster(reader, [[0, 100], [101, 1000], [1001, 3000]], 'energy_100g', 'packaging')
        sys.exit()

        packaging = []
        header = []
        rownum = 0
        for row in reader:
            # Save header row.
            if rownum == 0:
                header = row
            else:
                colnum = 0
                for col in row:
                    # print('%-8s: %s' % (header[colnum], col))
                    if header[colnum] == "packaging":
                        packaging.append(col)

                    colnum += 1

            rownum += 1

        packaging = list(filter(None, packaging))
        print(packaging)
        with open('python_parser_output.txt', 'w', encoding='utf-8') as f:
            f.write(", ".join(packaging))


if __name__ == "__main__":
    run()
