
from math import pi


def αA(αE, As, b, h): return αE * As / b / h


def solve_Mu(b, h, fy, fc, ft, Ec, Es, c, εcu, *d):
    import structure.concrete.受弯.单筋 as single
    import structure.concrete.受弯.单筋.简化 as simple
    import structure.concrete.受弯.单筋.分析 as analysis
    import structure.concrete.轴心受力 as axis

    As = pi * sum([D**2 for D in d]) / 4
    print("As = ", As)
    print("As / bh = ", As / b / h)
    ρ = axis.ρ(b * h, As)
    print("ρ = ", ρ)
    αE = axis.αE(Ec, Es)
    print("αE = ", αE)
    αA = single.αA(αE, As, b, h)
    print("αA = ", αA)
    h0 = h - c - max(d) / 2
    print("h0 = ", h0)

    ρmin = simple.ρmin(ft, fy)
    print("ρmin = ", ρmin)
    α1 = simple.α1_linear(fc)
    print("α1 = ", α1)
    ξb = simple.ξb(α1, fy, Es, εcu)
    print("ξb = ", ξb)
    ρb = simple.ρb(ξb, α1, fc, fy)
    print("ρb = ", ρb)

    if ρ < ρmin:
        print("少筋梁。")
        Mu = analysis.Mcr_middle(αA, ft, b, h)
    elif ρ > ρb:
        print("超筋梁。")
        ξ = simple.ξ_over(α1, fc, b, h0, ξb, fy, As)
        print("ξ = ", ξ)
        Mu = simple.Mu_over(fy, ξb, As, h0, ξ)
    else:
        x = simple.x(α1, fc, b, fy, As)
        print("x = ", x)
        Mu = simple.Mu_x(fy, As, h0, x)
    print("Mu = ", Mu)
