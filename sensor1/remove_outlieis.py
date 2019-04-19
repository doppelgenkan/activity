def remove_outliers(dfrm, item, mul=4):
    '''
    データフレームdfrmの項目itemのデータから，外れ値を取り除いたpandas.DataFrame.Seriesを返す.
    
    Parameters
    ----------
    dfrm : データフレーム変数.
    
    item : データフレーム項目名.
        正の整数のとき，データフレーム項目リストのindex.
    mul : option (mul=4)
        平均値 ± mul * 標準偏差
    '''
    if type(item) == int:                  #itemが整数のとき
        item = dfrm.columns.values[item]   #itemを項目名に変更
    series = dfrm[item]
    m = series.describe()['mean']  #平均値
    s = series.describe()['std']   #標準偏差
    lower_lim = m - mul * s        #平均値 + mul * 標準偏差 
    upper_lim = m + mul * s        #平均値 - mul * 標準偏差
    return dfrm.query(f'{lower_lim} <= {item} <= {upper_lim}').loc[:,item]  #dfrmのitemデータから外れ値を取り除いたシリーズ