'''
关于混凝土和钢的基本力学性质
'''
def σc_E_Hognestad(fc, εc, Ec):
    '''
    美国的E.Hognestad建议的模型
    '''
    ε0 = fc / Ec
    εcu = 0.38
    if εc <= ε0:
        return fc * (2 * εc / ε0 - (εc / ε0) ** 2)
    if εc <= εcu:
        return fc * (1 - 0.15 * (εc - ε0) / (εcu - ε0))
    return 0
def σc_Rüsch(fc, εc):
    '''
    德国的Rüsch建议的模型
    '''
    ε0 = 0.002
    εcu = 0.0035
    if εc <= ε0:
        return fc * (2 * εc / ε0 - (εc / ε0) ** 2)
    if εc <= εcu:
        return fc
    return 0
def σc_GB50010(fc, fcu, εc):
    '''
    中国的GB 50010建议的模型
    '''
    n = 2 - (fcu - 50) / 60
    n = n if n > 2 else 2
    ε0 = 0.002 + 0.5 * (fcu - 50) * 1e-5
    εcu = 0.0033 - (fcu - 50) * 1e-5
    if εc <= ε0:
        return fc * (2 * εc / ε0 - (εc / ε0) ** n)
    if εc <= εcu:
        return fc
    return 0
def σc(fc, fcu, εc, Ec, module = "Rüsch"):
    '''
    有多个模型可采用，但默认使用Rüsch建议的模型
    '''
    switch = {  
        "Rüsch"    : σc_Rüsch,
        "Hognestad": σc_E_Hognestad,
        "GB50010"  : σc_GB50010
    }
    return switch[module](fc = fc, fcu = fcu, εc = εc, Ec = Ec)
def σs(Es, ε, εy, fy):
    '''
    钢的应变
    '''
    return Es * ε if ε <= εy else fy