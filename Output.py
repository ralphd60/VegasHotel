import matplotlib.pyplot as plt
import numpy as np

def graph_output(result_counts):
    N = len(result_counts)
    width = .75
    ind = np.arange(N)

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, result_counts.values(), width, align='edge', color='g')
    ax.set_xticks(ind + width / 2)
    ax.set_ylabel('Results')
    ax.set_title('Vegas Hotel Survey', fontsize=10, color='b')
    ax.set_xticklabels(list(result_counts.keys()), rotation=90, fontsize=7)

    # ax.legend((rects1[0], ('Reviews')

    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center', va='bottom',
                    fontsize=5)

    autolabel(rects1)

    plt.show()