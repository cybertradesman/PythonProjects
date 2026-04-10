tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],  # column 0
    ['Alice', 'Bob', 'Carol', 'David'],           # column 1
    ['dogs', 'cats', 'moose', 'goose']           # column 2
]

def printTable(table_data):
    # colWidths[i] will hold the maximum width (number of characters)
    # of any string in column i.
    colWidths = [0] * len(table_data)  # Here: [0, 0, 0]

    # First pass: figure out how wide each column needs to be.
    # We loop over columns by index (0, 1, 2 for this table).
    for i in range(len(table_data)):
        # table[i] is the i-th column list, e.g. ['apples', 'oranges', ...]
        for item in table_data[i]:
            # item is a single string in this column (e.g. 'apples')
            # If this string is longer than the current recorded width,
            # update colWidths[i].
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)
                # For column 0 this will walk through 'apples', 'oranges',
                # 'cherries', 'banana' and end up with the length of the longest word in that column (8), and so on for the next 2 lists/columns

    # Second pass: print the table row by row.
    # zip(*table_data) transposes the column-based structure into row tuples.
    # It produces:
    # ('apples',  'Alice', 'dogs')
    # ('oranges', 'Bob',   'cats')
    # ('cherries','Carol', 'moose')
    # ('banana',  'David', 'goose')
    for row in zip(*table_data):
        # Here, row is a tuple containing one item from each column.
        # enumerate(row) gives us (column_index, item) pairs.
        line = ' '.join(
            item.center(colWidths[j])      # right-justify this cell
             # So for the row ('apples', 'Alice', 'dogs'):
             # j=0, item='apples' -> rjust(colWidths[0]) colWidths[0] = 8 characters wide (for word 'cherries' in original table data),len('oranges') = 7,
             # j=1, item='Alice'  -> rjust(colWidths[1]) colWidths[1] = 5 characters wide column, len('Bob') = 3, 
             # j=2, item='dogs'   -> rjust(colWidths[2]) = 5 characters wide column, len('cats') = 4,
            for j, item in enumerate(row) # j = column index, item = cell string
        ) # A comprehension inside join, a GENERATOR EXPRESSION
        """
       cells = []
       for j, item in enumerate(row):
            cells.append(item.rjust(colWidths[j])) # .append('apples').rjust(8), .append('Alice').rjust(5), and so on

       line = ' '.join(cells) # Join all formatted cells into one string
       """
        # The join then combines the padded strings into one printable line.
        print(line)

printTable(tableData)