def Mcr(αA, αA_, ft, b, h):
    '''
    (5-69)
    '''
    return 0.292 * (1 + 2.5 * αA + 0.25 * αA_) * ft * b * h**2


def ξn(fc, Es, εcu, h0, ρ, ρ_, as_):
    '''
    (5-70)
    '''
    a = 0.798 * fc
    b = Es * εcu * ρ + Es * εcu * ρ_
    c = -Es * εcu * ρ - Es * as_ / h0 * εcu * ρ_
    from structure.basic import quadratic_solve
    return quadratic_solve(a, b, c)


def Mu(σs, σs_, As, As_, h0, ξn, as_):
    '''
    (5-71)
    '''
    return σs * As * h0 * (1 - 0.412 * ξn) + σs_ * As_ * h0 * (0.412*ξn, as_/h0)


def can_yield(xn, as_):
    '''
    HPB300, HRB335, HRBF335, HRB400, HRBF400, RRB400
    '''
    return xn >= 2.5 * as_


def ξn_yield(fc, fy, fy_, ρ, ρ_):
    '''
    (5-73)
    '''
    return 1.253 * (ρ * fy / fc - ρ_ * fy_ / fc)


def Mu_yield(fc, b, h0, ξn, fy_, As_, as_):
    '''
    (5-74)
    '''
    return fc * b * h0**2 * ξn*(0.798 - 0.329 * ξn) + fy_ * As_ * h0 * (1 - as_ / h0)
