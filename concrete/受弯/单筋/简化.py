def α1(β1, ε0, εcu):
    '''
    (5-40)
    '''
    return (1 - ε0 / εcu / 3) / β1


def α1_linear(fcu):
    if fcu <= 50:
        return 1
    if fcu <= 80:
        return 1 - (fcu - 50) / 500
    raise Exception("Out of consideration.")


def β1(ε0, εcu):
    '''
    (5-41)
    '''
    tmp = ε0 / εcu
    return (6 - 4 * tmp + tmp**2) / (6 - 2 * tmp)


def β1_linear(fcu):
    if fcu <= 50:
        return 0.8
    if fcu <= 80:
        return 0.8 - (fcu - 50) / 500
    raise Exception("Out of consideration.")


def ξb(β1, fy, Es, εcu):
    '''
    (5-43)
    ξn = x / h0
    '''
    return β1 / (1 + fy / Es / εcu)


def x(α1, fc, b, fy, As):
    '''
    (5-47)
    适筋梁
    '''
    return fy * As / α1 / fc / b


def Mu_x(fy, As, h0, x):
    '''
    (5-48)
    适筋梁
    '''
    return fy * As * (h0 - x / 2)


def ξ(ρ, fy, α1, fc):
    '''
    (5-49)
    ξn = x / h0
    '''
    return ρ * fy / α1 / fc


def Mu(As, fy, γs, h0):
    '''
    (5-50)
    适筋构件
    '''
    return As * fy * γs * h0


def αs(ξ):
    '''
    (5-51)
    '''
    return ξ * (1 - ξ / 2)


def γs(ξ):
    '''
    (5-52)
    '''
    return 1 - ξ / 2


def ρmax(ξb, α1, fc, fy):
    '''
    (5-53)
    '''
    return ξb * α1 * fc / fy


def ρb(ξb, α1, fc, fy):
    return ρmax(ξb, α1, fc, fy)


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


def σs_linear(fy, ξ, ξb):
    '''
    (5-65)
    '''
    return fy * (ξ - 0.8) / (ξb - 0.8)


def ξ_over(α1, fc, b, h0, ξb, fy, As):
    '''
    联立(5-65)和(5-45)
    超筋构件
    '''
    n = 0.8 * fy * As
    d = fy * As - α1 * fc * b * h0 * (ξb - 0.8)
    return n / d


def Mu_over(fy, ξb, As, h0, ξ):
    '''
    联立(5-65)和(5-45)
    超筋构件
    '''
    return fy * (ξ - 0.8) / (ξb - 0.8) * As * h0 * (1 - ξ / 2)
