import math

field_names = ('id', 'product_group', 'product_name',
               'purchase_price', 'purchase_date', 'purchase_quantity',
               'sale_price', 'sale_date', 'sale_quantity',
               'expiration_date', 'stock_quantity', 'unit',)


purchase_index = [1, 2, 3, 4, 5, 11]
stock_index = [0, 1, 2, 3, 6, 9, 10, 11]
sale_index = [0, 1, 2, 6, 7, 8, 11]
transactions_index = [2, 4, 5, 7, 8, 9, 10, 11]
products_index = [0]


def select_fieldnames(index):
    """Select the fieldnames for the table that needs to be built."""
    selected_field_names = []
    for number in index:
        for name in field_names:
            if name == field_names[number]:
                selected_field_names.append(name)
    return selected_field_names


def set_column_widths(cols, index):
    """Return a list with the maximum widths of the table columns."""
    column_widths = []
    for fieldname in select_fieldnames(index):
        max_width = 0
        width = [row[fieldname] for row in cols]
        for item in width:
            if len(item) > max_width:
                max_width = len(item)
        column_widths.append(max_width + 2)
    return column_widths


def make_line(cols, index, dash):
    """Return a single or double dash line."""
    line = ""
    for column_width in set_column_widths(cols, index):
        line_part = f"+{dash * column_width }"
        line += line_part
    return f"{line}+"


def left_aligned(row):
    return (row['product_group'], row['product_name'], row['unit'])


def right_aligned(row):
    return (row['purchase_quantity'], row['stock_quantity'], row['sale_quantity'])


def right_aligned_price(row):
    return (row['purchase_price'], row['sale_price'])


def format_valutas(row):
    if (row['purchase_price'] == '0'):
        row['purchase_price'] = '0.00'
    if (row['purchase_price'][-2] == '.'):
        row['purchase_price'] += '0'
    if (row['sale_price'] == '0'):
        row['sale_price'] = '0.00'
    if (row['sale_price'][-2] == '.'):
        row['sale_price'] += '0'


def make_table(rows, index):
    """Print a neatly formatted table with automatic ajustable column-widths."""
    no_blank_lines = []
    for row in rows:
        if row['stock_quantity'] != '0':
            no_blank_lines.append(row)
    line_count = 0
    index_list = range(len(index))
    for row in no_blank_lines:
        row_list = []
        format_valutas(row)
        if line_count <= 1:
            print(make_line(no_blank_lines, index, '='))
        else:
            print(make_line(no_blank_lines, index, '-'))

        for i in index_list:
            # define lay-out table-header
            if line_count == 0:
                title = row[select_fieldnames(index)[i]]
                column = title.replace('_', ' ').title()
            else:
                column = row[select_fieldnames(index)[i]]
            # define padding
            padding = set_column_widths(no_blank_lines, index)[i]
            if row[select_fieldnames(index)[i]] in left_aligned(row):
                padding_left = ' '
                padding_right = (padding - len(column) - 1) * ' '
            elif row[select_fieldnames(index)[i]] in right_aligned(row):
                padding_left = (padding - len(column) - 1) * ' '
                padding_right = ' '
            elif row[select_fieldnames(index)[i]] in right_aligned_price(row) and line_count > 0:
                padding_left = ' €' + (padding - len(column) - 3) * ' '
                padding_right = ' '
            else:
                padding_left = int(math.floor(
                    padding - len(column))/2) * ' '
                padding_right = int(math.floor(
                    padding + 1 - len(column))/2) * ' '
            # assemble cell and row content
            cell = f"|{padding_left}{column}{padding_right}"
            row_list.append(cell)
            table_row = ''.join(row_list)
        print(f"{table_row}|")
        line_count += 1
    print(make_line(no_blank_lines, index, '='))
