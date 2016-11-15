import re
import traceback


def split_by_comma_and_space(string):
    delims = "   ", ","
    regex_pattern = '|'.join(map(re.escape, delims))

    return re.split(regex_pattern, string)


def split_by_tabs(string):
    return re.split(r'\t+', string)


# takes string lists of categories and entries
# returns dict<str, str>{category_i : entry_i}
def create_item(categories, entries):
    try:
        item_dict = dict()
        for i in range(len(categories)):  # (min(len(entries), len(categories))):
            category = categories[i]
            try:
                entry = entries[i]
            except IndexError:
                entry = "n/a"

            item_dict[category] = entry

        return item_dict

    except:
        print("\n\nError: couldn't load an item")

        if len(categories) != len(entries):
            print("\nThere's " + str(len(categories) - len(entries)) + " more categories than entries")

        print("\nCategories: " + str(categories))
        print("\nEntries: " + str(entries))


def run():
    with open('en.openfoodfacts.org.products.csv', newline='', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        line_count = len(lines)

        # first line contains categories like code, url, creator etc.
        categories = lines[0].split()
        print(categories)

        items = []
        for i in range(1, line_count):
            # general fields are separated by tabs
            # entries with missing information violate the rule; <field>-to-be-completed isn't separated by tab
            # fieldstr = re.split(r'\t+', lines[i])
            # while len(fieldstr) < 5:
            #     fieldstr.append("")

            # fields = {"general_information": fieldstr[0], "tags": fieldstr[1], "ingredients": fieldstr[2],
            #           "misc_data": fieldstr[3], "nutrition_facts": fieldstr[4]}

            # for key, value in fields.items():
            #     print(key, value)

            entries = split_by_tabs(lines[i])
            items.append(create_item(categories, entries))
            print(len(items))

        """   for item in items:
                if item["energy_100g"] != "n/a":
                    for category, entry in item.items():
                        print(category, entry)
                    break"""

        while True:
            try:
                inp = input("Select item by number in list")
                if not inp:
                    break

                inp2 = input("Select category ('all' for all)")

                selected_item = items[int(inp)]
                if inp2 == 'all':
                    for category, entry in selected_item.items():
                        print(category, entry)
                else:
                    print(selected_item[inp2])
            except Exception as e:
                print("enter a number between 0 and " + str(line_count - 1) +
                      " pls - or maybe your selected category doesn't exist")
                print(e)
                traceback.print_exc()


if __name__ == "__main__":
    run()
