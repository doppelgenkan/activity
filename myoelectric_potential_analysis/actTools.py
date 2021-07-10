import numpy as np

def z_(arr):
    arr = np.array(arr)    # ndarrayに強制的に変換
    return (arr - np.mean(arr)) / np.std(arr)

def n_(arr):
    arr = np.array(arr)
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

def frq_array(hz, n):     #フーリエ周波数：0HzとナイキストHz以上は除外
    return (hz/2**n) * np.array(list(range(1, 2**n//2)))

def power_array(arr, hz=1000, n=10, step=1000):
    lis = []
    f = frq_array(hz, n)
    for i in range(0, len(arr)):
        F = np.fft.fft(arr[i: i+2**n])
        if len(F) < 2**n:                      # ある時刻のFの要素数が2^n未満なら
            break                               #           繰り返しストップ
        P = np.abs(F[1: (2**n//2)])**2
        lis.append(mpf)

def mpf_array(arr, hz=1000, n=10):    # nは2^nのn
    lis = []
    f = frq_array(hz, n)
    for i in range(0, len(arr)):
        F = np.fft.fft(arr[i: i+2**n])   # 各時刻のフーリエ変換F
        if len(F) < 2**n:                 # ある時刻のFの要素数が2^n未満なら
            break                           #           繰り返しストップ
        P = np.abs(F[1: (2**n//2)])**2  # 0Hzより大きくナイキストHz未満のパワー
        sumP = np.sum(P)
        mpf = np.dot(f, P) /sumP
        lis.append(mpf)
    return np.array(lis)
