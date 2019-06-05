import numpy as np


def integral(x, s0, startindex, endindex, tau=0.001):
    '''
    Return 被積分データ配列xの台形則にもとずく積分データ配列.
    
    Parameters
    ----------
    x : array-like
        被積分データ. 1-D numpy配列推奨.
    s0 : int or float
        初期値(積分定数).
    statindex : int
        被積分データ配列xの最初のindex.
    endpoint : int
        被積分データ配列xの最後のindex.
    tau : float, optional (0.001)
        積分区切り幅.
    '''
    s = s0
    s_arr = [s0]
    for i in range(startindex, endindex+1):
        s += (x[i] + x[i+1]) / 2 * tau
        s_arr.append(s)
    return np.array(s_arr)