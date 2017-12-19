import pandas as pd
from AnalysisType import *
from Output import *


# Define count_entries()
def count_entries(csv_file, c_size, delimit, *args):
    """Return a dictionary with counts of or totals of a second column
    occurrences as value for each key."""
    # counts how many arguments in order to determine how many columns are used
    switch = len(args)

    # initialize and empty list to hold the arguments
    colname = []

    # populate the list with arguments (may want to use key word argument dictionary
    for argv in args:
        colname.append(argv)
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, delimit, chunksize=c_size):
        # Iterate over the column in DataFrame
        for lab, row in chunk.iterrows():
            if switch == 2:
                counts_dict = type_label_and_total(row, colname[0], colname[1], counts_dict)
            elif switch == 1:
                counts_dict = type_count(row, colname[0], counts_dict)
    # Return counts_dict
    return counts_dict


if __name__ == '__main__':
    result_counts = \
        count_entries('c:\\temp\\LasVegasTripAdvisorReviews-Dataset.csv', 100, ';', 'User country', 'Nr. hotel reviews')
        # count_entries('c:\\temp\\NYPD_Motor_Vehicle_Collisions.csv', 10000, ',', 'CONTRIBUTING FACTOR VEHICLE 1',\
        # 'NUMBER OF PERSONS KILLED')

    # Print result_counts
    print(result_counts)

    graph_output(result_counts)

