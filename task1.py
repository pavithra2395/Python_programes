import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt

def load_data(path, header):
    marks_df = pd.read_csv(path, header=header)
    return marks_df

if __name__ == "__main__":
    
    data = load_data("marks.csv",None)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    admitted = data.loc[y == 1]
    not_admitted = data.loc[y == 0]
    
    plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Eligible')
    plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10, label='Not eligible')
    plt.legend()
    plt.show()