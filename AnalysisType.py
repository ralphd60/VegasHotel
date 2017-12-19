

# receives a label and a value and totals to provide a sum of that value
def type_label_and_total(row, col, col2, counts_dict2):
    '''this function will take 2 columns, one will be the x axis (label- like country or hotel)
       and a colmn with numbers and adds the total'''
    if row[col] in counts_dict2.keys():
        counts_dict2[row[col]] += row[col2]
    else:
        counts_dict2[row[col]] = row[col2]

    return counts_dict2
# receives a label and then counts that label
def type_count (row, col, counts_dict2):
    if row[col] in counts_dict2.keys():
        counts_dict2[row[col]] += 1
    else:
        counts_dict2[row[col]] = 1

    return counts_dict2
