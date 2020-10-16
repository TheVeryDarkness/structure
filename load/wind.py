from functools import partial
from math import e, tan, pi, sin, sqrt
from enum import Enum

'''
    HT 梯度风高度
    m(z) 单位长度（沿z向）上的质量
    B(z) 结构迎风面宽度
    R 脉动风荷载的共振分量因子
    Bz 脉动风荷载的背景分量因子
'''


def w(γ, g, v):
    return γ * v * v / g / 2


def Svf(n, k, v10):
    '''
    水平脉动风速的功率谱密度经验公式
    By Davenport from Cananada
    '''
    L = 1200
    x = n * L / v10
    sqrx = x ** 2
    return (4 * k * v10 ** 2 / n * sqrx / (1 + sqrx) ** (4 / 3))


class Vortex(Enum):
    Subcritical = 0
    Suppercritical = 1
    Transcritical = 2


def getVortex(Re) -> Vortex:
    if Re >= 3500000:
        return Vortex.Transcritical
    if Re >= 300000:
        return Vortex.Suppercritical
    if Re >= 300:
        return Vortex.Subcritical
    raise Exception()


class Landform(Enum):
    A = 0
    B = 1
    C = 2
    D = 3


def α(lf: Landform):
    '''
    风速变化指数
    '''
    if lf == Landform.A:
        return 0.12
    if lf == Landform.B:
        return 0.15
    if lf == Landform.C:
        return 0.22
    if lf == Landform.D:
        return 0.30
    raise Exception()


def HT(lf: Landform):
    '''
    梯度风高度
    '''
    if lf == Landform.A:
        return 300
    if lf == Landform.B:
        return 350
    if lf == Landform.C:
        return 450
    if lf == Landform.D:
        return 550
    raise Exception()


def St(fs, D, v):
    '''
    Strouhal number
    '''
    return fs * D / v


def μs_v(v, v0):
    return 1 - v ** 2 / v0 ** 2


def μs_n(n):
    '''
    风载体型系数
    '''
    return 0.7 + 1.2 / sqrt(n)


def z0a(lf: Landform):
    if lf == Landform.A:
        return 5
    if lf == Landform.B:
        return 10
    if lf == Landform.C:
        return 15
    if lf == Landform.D:
        return 30
    raise Exception()


def μz_z_HT_α(HTs, HTa, zs, za, αs, αa, z0 = 0):
    return (
        (HTs / zs) ** αs
        /
        (HTa / za) ** αa
    ) ** 2


def μz_z_s_a(za, a: Landform, zs = 10, s: Landform = Landform.B):
    return μz_z_HT_α(HT(s), HT(a), zs, max(z0a(a), za), α(s), α(a))


def I10(lf: Landform):
    if lf == Landform.A:
        return 0.12
    if lf == Landform.B:
        return 0.14
    if lf == Landform.C:
        return 0.23
    if lf == Landform.D:
        return 0.39
    raise Exception()


class build(Enum):
    '''
    弯剪型
    弯曲型
    剪切型
    '''
    高层建筑 = 1
    高耸结构 = 2
    低层建筑 = 3


def k(lf: Landform, bt: build):
    l = Landform
    b = build
    switch = {
        l.A: {b.高层建筑: 0.944, b.高耸结构: 1.276},
        l.B: {b.高层建筑: 0.670, b.高耸结构: 0.910},
        l.C: {b.高层建筑: 0.295, b.高耸结构: 0.404},
        l.D: {b.高层建筑: 0.112, b.高耸结构: 0.155}
    }
    return switch[lf][bt]


def α1(lf: Landform, bt: build):
    l = Landform
    b = build
    switch = {
        l.A: {b.高层建筑: 0.155, b.高耸结构: 0.186},
        l.B: {b.高层建筑: 0.187, b.高耸结构: 0.218},
        l.C: {b.高层建筑: 0.261, b.高耸结构: 0.292},
        l.D: {b.高层建筑: 0.346, b.高耸结构: 0.376}
    }
    return switch[lf][bt]


def φ1(z, H, bt: build):
    b = build
    if bt == b.高耸结构:
        return 2 * (z / H) ** 2 - 4 / 3 * (z / H) ** 3 + (z / H) ** 4 / 3
    if bt == b.高层建筑:
        return tan(pi * (z / H) ** 0.7 / 4)
    if bt == b.低层建筑:
        return sin(pi * z / 2 / H)
    raise Exception()


def kw(lf: Landform):
    l = Landform
    switch = {
        l.A: 1.28,
        l.B: 1.0,
        l.C: 0.54,
        l.D: 0.26
    }
    return switch[lf]


class struct(Enum):
    钢结构 = 1
    有填充墙的钢结构 = 2
    钢筋混凝土结构 = 3
    砌体结构 = 3


def x1(f1, kw, w0):
    return min(30 * f1 / sqrt(kw * w0), 5)


def ξ1(sm: struct):
    m = struct
    switch = {
        m.钢结构: 0.01,
        m.有填充墙的钢结构: 0.02,
        m.钢筋混凝土结构: 0.05
    }
    return switch[sm]


def R(f1, kw, w0, sm: struct):
    __x1 = x1(f1, kw, w0)
    return sqrt(pi * __x1 ** 2 / 6 / ξ1(sm) / (1 + __x1 ** 2) ** (4/3))


def ρx(z, B):
    __B = B(z)
    return 10 * sqrt(__B + 50 * e ** (- __B / 50) - 50) / __B


def ρz(H):
    return 10 * sqrt(H + 60 * e ** (- H / 60) - 60) / H


def Bz(z, k, H, α1, ρx, ρz, φ1, μz, lf: Landform):
    '''
    脉动风荷载的背景分量因子
    '''
    switch = {
        Landform.A: 300,
        Landform.B: 350,
        Landform.C: 450,
        Landform.D: 550,
    }
    _H = min(switch[lf], H)
    return k * H ** α1 * ρx(z) * ρz * φ1(z) / μz(z)


def σq(z, w0, I10, B, μs, ω1, m, Bz, μz, φ1, R):
    return (
        2 * w0 * I10 * B(z) * μs / ω1 ** 2 / m
        *
        Bz * μz(z) / φ1(z)
        *
        sqrt(1 + R ** 2)
    )


def Pd(z, ω1, m, φ1, σq, g = 2.5):
    return g * ω1 ** 2 * m(z) * φ1(z) * σq(z)


def β_z_I10_Bz_R(z, I10, Bz, R, g = 2.5):
    return 1 + 2 * g * I10 * Bz(z) * sqrt(1 + R ** 2)


def w_z(z, w0, μz, μs, β):
    return β(z) * μs * μz(z) * w0
