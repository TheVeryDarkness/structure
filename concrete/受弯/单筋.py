def σci(M, y0, I0):
    return M * y0 / I0


def σs(αE, M, h0, xn, I0):
    return αE * M * (h0 - xn) / I0


def xcr(αE, As, b, h):
    return (b * h + 2 * αE * As)/(b * h + αE * As) * h / 2


def φcr(εs, h0, xcr):
    '''
    开裂时
    '''
    return εs / (h0 - xcr)


def φcr_normal(εtu, h):
    '''
    一般钢筋混凝土梁
    '''
    return 2 * εtu / h


def Mcr(ft, b, h, xcr, αE, As, h0):
    return ft * b * (h - xcr) * (h / 2 + xcr / 6) + 2 * αE * ft * As * (h0 - xcr / 3)


def Mu_weak(σs, As, h0, ξn):
    '''
    强度等级不大于C50
    '''
    return σs * As * h0 * (1 - 0.412 * ξn)


def ξn_weak_fit(ρ, fy, fc):
    '''
    强度等级不大于C50的适筋梁
    '''
    return 1.253 * ρ * fy / fc


def Mu_weak_fit(σs, As, h0, ξn):
    '''
    强度等级不大于C50的适筋梁
    '''
    return σs * As * h0 * (1 - 0.412 * ξn)


def αA(αE, As, b, h):
    return 2 * αE * As / b / h


def α1(β1, ε0, εtu):
    return (1 - ε0 / εtu / 3) / β1


def β1(ε0, εcu):
    tmp = ε0 / εcu
    return (6 - 4 * tmp + tmp**2) / (6 - 2 * tmp)


def ξb(β1, fy, Es, εcu):
    return β1 / (1 + fy / Es / εcu)


def ρmax(ξb, α1, fc, fy):
    return ξb * α1 * fc / fy


def αsmax(ξb):
    return ξb * (1 - ξb / 2)


def Mumax(ξb, α1, fc, b, h0):
    return αsmax(ξb) * α1 * fc * b * (h0**2)


def M_e(σs, As, h0, ξn, ε0, εct):
    '''
    弹性阶段
    '''
    return σs * As * h0 * (1 - ξn / 3)


def M_ep_0(σs, As, h0, ξn, ε0, εct):
    '''
    弹塑性阶段，εct小于ε0
    '''
    tmp = εct / ε0
    return σs * As * h0 * (1 - ξn * (4 - tmp) / (3 - tmp) / 4)


def M_ep_1(σs, As, h0, ξn, ε0, εct):
    '''
    弹塑性阶段，ε0不大于εct不大于εcu
    '''
    tmp = εct / ε0
    return σs * As * h0 * (1 - ξn * (1 - (6 - tmp**2) / (3 - tmp) / 4))
