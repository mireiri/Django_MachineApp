import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn
import numpy as np


def graphpy(file_path):
    df = pd.read_excel(file_path)
    x = df['PAX']
    y = df['WGT']

    corr_score = np.corrcoef(x, y)[0][1]
    corr_score = '{:.2}'.format(corr_score)

    plt.figure()
    plt.title('CorrCoef : ' + corr_score)
    plt.grid()
    seaborn.regplot(x=x, y=y, data=df)
    plt.savefig('download/' + file_path[6:-5] + '_graph.png')
    plt.close('all')


if __name__ == '__main__':
    graphpy('sample1.xlsx')
