import re
import csv


def run():
    csv.field_size_limit(9999999)

    with open('en.openfoodfacts.org.products.csv', newline='', encoding='utf-8') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)

        #reader = csv.reader(csvfile, delimiter='\t', quotechar='|')

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
                    #print('%-8s: %s' % (header[colnum], col))
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
