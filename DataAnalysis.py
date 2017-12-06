import matplotlib.pyplot as plt
import pandas as pd
from AnalysisType import *


# Define count_entries()
def count_entries(csv_file, c_size, delimit, colname, colname2,switch):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, delimit, chunksize=c_size):
        # Iterate over the column in DataFrame
        for lab, row in chunk.iterrows():
            if switch == 1:
                counts_dict = TypeLabelandTotal(row, colname, colname2, counts_dict)
            elif switch == 2:
                counts_dict = TypeCount(row, colname, counts_dict)

     # Return counts_dict
    return counts_dict


if __name__ == '__main__':
    result_counts = \
        count_entries('c:\\temp\\LasVegasTripAdvisorReviews-Dataset.csv', 10, ';', 'User country', 'Nr. reviews',2)
    # Print result_counts
    print(result_counts)

    plt.bar(range(len(result_counts)), result_counts.values(), align='center')
    plt.xticks(range(len(result_counts)), list(result_counts.keys()))
    plt.xticks(rotation='vertical')

    plt.show()
