def α1(β1, ε0, εtu):
    return (1 - ε0 / εtu / 3) / β1


def β1(ε0, εcu):
    tmp = ε0 / εcu
    return (6 - 4 * tmp + tmp**2) / (6 - 2 * tmp)


def ξb(β1, fy, Es, εcu):
    return β1 / (1 + fy / Es / εcu)


def ρmax(ξb, α1, fc, fy):
    '''
    (5-53)
    '''
    return ξb * α1 * fc / fy


def αsmax(ξb):
    '''
    (5-55)
    '''
    return ξb * (1 - ξb / 2)


def Mumax(ξb, α1, fc, b, h0):
    '''
    (5-54)
    '''
    return αsmax(ξb) * α1 * fc * b * (h0**2)


def ρmin(ft, fy):
    '''
    (5-59)
    《混凝土结构设计规范》（GB50010）
    '''
    return 0.45 * ft / fy
