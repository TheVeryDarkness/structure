from math import sqrt


def σci(M, y0, I0):
    '''
    (5-7)
    '''
    return M * y0 / I0


def σs(αE, M, h0, xn, I0):
    '''
    (5-8)
    '''
    return αE * M * (h0 - xn) / I0


def xcr(αE, As, b, h):
    '''
    (5-12)
    '''
    return (b * h + 2 * αE * As)/(b * h + αE * As) * h / 2


def φcr(εs, h0, xcr):
    '''
    (5-9)
    开裂时
    '''
    return εs / (h0 - xcr)


def φcr_normal(εtu, h):
    '''
    (5-13)
    一般钢筋混凝土梁
    '''
    return 2 * εtu / h


def Mcr(ft, b, h, xcr, αE, As, h0):
    '''
    (5-14)
    '''
    return ft * b * (h - xcr) * (h / 2 + xcr / 6) + 2 * αE * ft * As * (h0 - xcr / 3)


def Mcr_middle(αA, ft, b, h):
    '''
    (5-15)
    h0 = 0.92 * h
    xcr = 0.5 * h
    '''
    return 0.292 * (1 + 2.5 * αA) * ft * b * h**2


def ξn(fc, Es, ρ, εc_t=0.0033, ε0=0.002):
    '''

    '''
    a = fc * (1 / ε0 - εc_t / 3 / ε0**2)
    b = Es * ρ
    c = - Es * ρ
    return (-b + sqrt(b**2 - 4 * a * c)) / a / 2


def Mu_weak(σs, As, h0, ξn):
    '''
    (5-35)
    强度等级不大于C50
    '''
    return σs * As * h0 * (1 - 0.412 * ξn)


def ξn_weak_fit(ρ, fy, fc):
    '''
    (5-36)
    强度等级不大于C50的适筋梁
    '''
    return 1.253 * ρ * fy / fc


def Mu_weak_fit(fy, As, h0, ξn):
    '''
    (5-37)
    强度等级不大于C50的适筋梁
    '''
    return fy * As * h0 * (1 - 0.412 * ξn)


def αA(αE, As, b, h):
    '''
    (pre 5-15)
    '''
    return 2 * αE * As / b / h


def M_e(σs, As, h0, ξn, ε0, εct):
    '''
    (5-22)
    弹性阶段
    '''
    return σs * As * h0 * (1 - ξn / 3)


def yc_ep_0(ξn, h0, εc_t, ε0=0.002):
    '''
    (5-24)
    '''
    return ξn * h0 * (4 - (ε0 / εc_t)**2) / (12 - 4 * (ε0 / εc_t))


def M_ep_0(σs, As, h0, ξn, ε0, εct):
    '''
    (5-28)
    弹塑性阶段，εct小于ε0
    '''
    tmp = εct / ε0
    return σs * As * h0 * (1 - ξn * (4 - tmp) / (3 - tmp) / 4)


def yc_ep_1(ξn, h0, εc_t, ε0=0.002):
    '''
    (5-30)
    '''
    return ξn * h0 * (1 - (6 - (ε0 / εc_t)**2) / (12 - 4 * (ε0 / εc_t)))


def ycu(ξn, h0, εcu=0.0033, ε0=0.002):
    return yc_ep_1(ξn=ξn, h0=h0, εc_t=εcu, ε0=ε0)


def M_ep_1(σs, As, h0, ξn, ε0, εct):
    '''
    (5-33)
    弹塑性阶段，ε0不大于εct不大于εcu
    '''
    tmp = εct / ε0
    return σs * As * h0 * (1 - ξn * (1 - (6 - tmp**2) / (3 - tmp) / 4))
