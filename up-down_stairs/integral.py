import numpy as np
from scipy import integrate


def trapez(x, s0, startindex, endindex, tau=0.001):
    '''
    Return 被積分データ配列xの台形則にもとずく積分データ配列.
    
    Parameters
    ----------
    x : array like
        被積分データ. 1D-numpy配列推奨.
    s0 : int or float
        初期値(積分定数).
    statindex : int
        被積分データ配列xの任意の最初のindex.
    endindex : int
        被積分データ配列xの任意の最後のindex.
    tau : float, optional (0.001)
        積分区切り幅.
    '''
    s = s0
    s_arr = [s0]
    for i in range(startindex, endindex):
        s += (x[i] + x[i+1]) / 2 * tau
        s_arr.append(s)
    return np.array(s_arr)


def simps(x, s0, startindex, endindex, tau=0.001):
    '''
    Return 被積分データ配列xのSimpson則にもとずく積分データ配列.
    
    Parameters
    ----------
    x : array like
        被積分データ. 1D-numpy配列推奨.
    s0 : int or float
        初期値(積分定数).
    statindex : int
        被積分データ配列xの任意の最初のindex.
    endindex : int
        被積分データ配列xの任意の最後のindex.
    tau : float, optional (0.001)
        積分区切り幅.
    '''
    s = s0
    s_arr =[s0]
    for i in range(startindex, endindex):
        s = s0 + integrate.simps(x[:i+1], dx=tau)
        s_arr.append(s)
    return np.array(s_arr)