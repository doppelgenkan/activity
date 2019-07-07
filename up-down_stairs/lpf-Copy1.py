import numpy as np


def _mean_padding(arr):
    len_of_arr = len(arr)
    len_of_newarr = 2 ** len(format(len_of_arr, 'b'))
    additional_arr = np.ones(len_of_newarr - len_of_arr) * np.mean(arr)
    return np.hstack((arr, additional_arr))


class Signal():    
    def __init__(self, arr, samp_hz=1000, rmdc=True):
        self.__samp_hz = samp_hz
        self.__arr = _mean_padding(arr)
        self.__hz_array = self.__to_hz_array(rmdc=rmdc)
        
    
    def __to_hz_array(self, rmdc=True):
        fl = __mean_padding(self.__arr)
        fl_len = len(fl)
        if 2 * cutoff_hz <= samp_hz:
            kc = int( np.round( cutoff_hz * arr_len / samp_hz ) )
            arr = _lpfilter(arr, kc, rmdc)
        return arr[:(fl_len - startpoint)]
