import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.") 
    array = np.array(list).reshape(3, 3)
    mean1, var1, std1, maximum1, minimum1, summ1 = [], [], [], [], [], []
    mean2, var2, std2, maximum2, minimum2, summ2 = [], [], [], [], [], []
    for i in range(3):
        mean_ax1, var_ax1, std_ax1, max_ax1, min_ax1, sum_ax1 = array[:,i].mean(), array[:,i].var(), array[:,i].std(), array[:,i].max(), array[:,i].min(), array[:,i].sum() 
        mean_ax2, var_ax2, std_ax2, max_ax2, min_ax2, sum_ax2 = array[i].mean(), array[i].var(), array[i].std(), array[i].max(), array[i].min(), array[i].sum() 
        mean1.append(mean_ax1)
        var1.append(var_ax1)
        std1.append(std_ax1)
        maximum1.append(max_ax1)
        minimum1.append(min_ax1)
        summ1.append(sum_ax1)
        mean2.append(mean_ax2)
        var2.append(var_ax2)
        std2.append(std_ax2)
        maximum2.append(max_ax2)
        minimum2.append(min_ax2)
        summ2.append(sum_ax2)
    mean_flat, var_flat, std_flat, max_flat, min_flat, sum_flat = array.mean(), array.var(), array.std(), array.max(), array.min(), array.sum()
    calculations = {
        'mean': [mean1, mean2, mean_flat],
        'variance': [var1, var2, var_flat],
        'standard deviation': [std1, std2, std_flat],
        'max' : [maximum1, maximum2, max_flat],
        'min': [minimum1, minimum2, min_flat],
        'sum': [summ1, summ2, sum_flat]
    }

    return calculations