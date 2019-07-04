import numpy as np


def _mean_padding(arr):
    len_of_arr = len(arr)
    len_of_newarr = 2 ** len(format(len_of_arr, 'b'))
    additional_arr = np.ones(len_of_newarr - len_of_arr) * np.mean(arr)
    return np.hstack((arr, additional_arr))


class Signal():    
    def __init__(self, arr, samp_hz=1000):
        self.samp_hz = samp_hz
        self.arr = _mean_padding(arr)
        
    
    def dft(self, rmdc=True):
    ''' 
    Return ローパスフィルターを施した1D-numpy配列(デフォルト).
        istime=True を指定すると2D-numpy配列(Parameters の istime を参照).
        
    Parameters
    ----------
    fl : array like
        サンプリングデータ配列. 1D-numpy配列.
    cutoff_hz : int
        ローパスフィルターのカットオフ周波数.
    samp_hz : int, optional (1000)
        サンプル周波数. デフォルトで1000[Hz].
    init : int or float, optional
        初期時刻[sec]. デフォルトでは0[sec]. 
    rmdc : bool, optional (True)
        直流成分(バイアス)を取り除くか否か. デフォルトではTrue(取り除く).
    istime : bool, optional (False)
        istime=True で時刻と対になった2D-numpy配列を返す. shapeは(2^n, 2).
    '''
    fl = _mean_padding(self.arr)
    fl_len = len(fl)
    startpoint = int( init * samp_hz )
    arr = _mean_padding(fl, startpoint=startpoint)
    arr_len = len(arr)
    if 2 * cutoff_hz <= samp_hz:
        kc = int( np.round( cutoff_hz * arr_len / samp_hz ) )
        arr = _lpfilter(arr, kc, rmdc)
    if istime == True:
        t_arr = np.arange(arr_len)/samp_hz + init
        arr = np.array([t_arr, arr]).T
    return arr[:(fl_len - startpoint)]
