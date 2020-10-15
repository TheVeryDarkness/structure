import structure.concrete.基本性质 as basic
'''
轴心受力构件
'''
def A(A0, As):
    '''
    构件截面积
    '''
    return A0 if As / A0 <= 0.03 else A0 - As
def αE(Ec, Es):
    '''
    钢筋和混凝土弹性模量的比值
    '''
    return Es / Ec
def ρ(A0, As):
    '''
    纵向受力钢筋的配筋率
    '''
    return As / A(A0, As)
def Nt(Ec, Es, A0, As, fy, εt0, εy, εsh, ε):
    '''
    轴向拉力
    '''
    _A = A(A0, As)
    if ε <= εt0:
        return (Ec * _A + Es * As) * ε
    if ε <= εy:
        return Es * As * ε
    if ε <= εsh:
        return fy * As
    return 0
def Ntcr(Ec, Es, A0, As, εt0):
    '''
    
    '''
    _A = A(A0, As)
    return (Ec * _A + Es * As) * εt0
def Ntu(As, fy):
    '''
    极限拉应力
    '''
    return fy * As
def ρmin(ft, fy):
    '''
    最小配筋率
    '''
    return ft / fy
def Nc(fc, fy, Es, A0, As, ε, εy):
    return basic.σc_Rüsch(fc, ε) * A(A0, As) + basic.σs(Es, ε, εy, fy) * As
