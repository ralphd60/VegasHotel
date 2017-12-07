import matplotlib.pyplot as plt

def GraphOutput(result_counts):

    plt.bar(range(len(result_counts)), result_counts.values(), align='center',color = 'red')
    plt.xticks(range(len(result_counts)), list(result_counts.keys()))
    plt.xticks(rotation='vertical', fontsize = 5)
    plt.title('Vegas Hotel Survey', fontsize=10, color = 'blue')

    plt.show()