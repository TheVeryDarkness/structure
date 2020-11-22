from math import pi


def αA(αE, As, b, h):
    return αE * As / b / h


def αA_(αE, As_, b, h):
    return αE * As_ / b / h


def solve_Mcr(b, h, fc, ft, Ec, fy, Es, εcu, c, D, N, D_, N_):
    import structure.concrete.轴心受力 as basic
    import structure.concrete.受弯 as bend
    import structure.concrete.受弯.双筋 as double
    import structure.concrete.受弯.双筋.分析 as analysis
    import structure.concrete.受弯.双筋.简化 as simple
    import structure.concrete.受弯.单筋.简化 as part
    fy_ = fy
    αE = basic.αE(Ec, Es)
    print("αE = ", αE)

    As = N * pi * D ** 2 / 4
    print("As = ", As)
    ρ = basic.ρ(b*h, As)
    print("ρ = ", ρ)
    αA = double.αA(αE, As, b, h)
    print("αA = ", αA)

    As_ = N_ * pi * D_ ** 2 / 4
    print("As` = ", As_)
    ρ_ = basic.ρ(b*h, As_)
    print("ρ` = ", ρ_)
    αA_ = double.αA(αE, As_, b, h)
    print("αA' = ", αA_)

    Mcr = analysis.Mcr(αA, αA_, ft, b, h)
    print("Mcr = ", Mcr)
    xcr = 0.5 * h
    print("xcr = 0.5h = ", xcr)
    ε0 = ft / Ec
    print("ε0 = ", ε0)
    εtu = 2 * ε0
    print("εtu = ", εtu)
    φcr = εtu / (h - xcr)
    print("φcr = ", φcr)


def solve_Mu_normal(b, h, fc, ft, Ec, fy, Es, εcu, c, D, N, D_, N_):
    import structure.concrete.轴心受力 as basic
    import structure.concrete.受弯 as bend
    import structure.concrete.受弯.双筋 as double
    import structure.concrete.受弯.双筋.分析 as analysis
    import structure.concrete.受弯.双筋.简化 as simple
    import structure.concrete.受弯.单筋.简化 as part

    fy_ = fy
    αE = basic.αE(Ec, Es)
    print("αE = ", αE)

    As = N * pi * D ** 2 / 4
    print("As = ", As)
    ρ = basic.ρ(b*h, As)
    print("ρ = ", ρ)
    αA = double.αA(αE, As, b, h)
    print("αA = ", αA)
    ε0 = ft / Ec
    print("ε0 = ", ε0)
    εtu = 2 * ε0
    print("εtu = ", εtu)

    As_ = N_ * pi * D_ ** 2 / 4
    print("As` = ", As_)
    ρ_ = basic.ρ(b*h, As_)
    print("ρ` = ", ρ_)
    αA_ = double.αA(αE, As_, b, h)
    print("αA' = ", αA_)
    h0 = h - c - D / 2
    print("h0 = ", h0)
    as_ = 0.08 * h
    print("as' = 0.08h = ", as_)

    ξnb = bend.ξnb(fy, Es, εcu)
    print("ξnb = ", ξnb)
    ξn = analysis.ξn_yield(fc, fy, fy_, ρ, ρ_)
    print("ξn = ", ξn)
    xn = ξn * h0
    print("xn = ", xn)
    if not analysis.can_yield(xn, as_):
        print("达极限时受压钢筋无法屈服")
        raise Exception()
    Mu = analysis.Mu_yield(fc, b, h0, ξn, fy_, As_, as_)
    print("Mu = ", Mu)
    φu = εcu / (ξn * h0)
    print("φu = ", φu)
    return Mu


def solve_Mu_simplified(b, h, fc, ft, Ec, fy, Es, εcu, c, D, N, D_, N_):
    import structure.concrete.轴心受力 as basic
    import structure.concrete.受弯 as bend
    import structure.concrete.受弯.双筋 as double
    import structure.concrete.受弯.双筋.分析 as analysis
    import structure.concrete.受弯.双筋.简化 as simple
    import structure.concrete.受弯.单筋.简化 as part
    fy_ = fy
    αE = basic.αE(Ec, Es)
    print("αE = ", αE)

    As = N * pi * D ** 2 / 4
    print("As = ", As)
    ρ = basic.ρ(b*h, As)
    print("ρ = ", ρ)
    αA = double.αA(αE, As, b, h)
    print("αA = ", αA)
    ε0 = ft / Ec
    print("ε0 = ", ε0)
    εtu = 2 * ε0
    print("εtu = ", εtu)

    As_ = N_ * pi * D_ ** 2 / 4
    print("As` = ", As_)
    ρ_ = basic.ρ(b*h, As_)
    print("ρ` = ", ρ_)
    αA_ = double.αA(αE, As_, b, h)
    print("αA' = ", αA_)
    h0 = h - c - D / 2
    print("h0 = ", h0)
    as_ = 0.08 * h
    print("as' = 0.08h = ", as_)

    As2 = As_ * fy_ / fy  # 抵消部分
    print("As2 = ", As2)
    As1 = As - As2
    print("As1 = ", As1)
    ρ1 = basic.ρ(b*h, As1)
    print("ρ1 = ", ρ1)
    Mu_ = fy_ * As_ * (h0 - as_)
    print("Mu' = ", Mu_)
    α1 = part.α1_linear(fc)
    print("α1 = ", α1)
    x = part.x(α1, fc, b, fy, As1)
    print("x = ", x)
    β1 = part.β1_linear(fc)
    print("β1 = ", β1)
    ξb = part.ξb(β1, fy, Es, εtu)
    print("ξb = ", ξb)
    ξ = part.ξ(ρ1, fy, α1, fc)
    print("ξ = ", ξ)
    Mu = None
    xb = ξb * h0
    print("xb = ", xb)
    if 2 * as_ <= x <= xb:
        print("等效为适筋梁")
        Mu1 = part.Mu(As1, fy, part.γs(ξ), h0)
        print("Mu1 = ", Mu1)
        Mu = Mu1 + Mu_
        print("Mu = ", Mu)
    elif xb < x:
        print("等效为超筋梁")
        Mu1 = part.Mu_over(fy, ξb, As1, h0, ξ)
        print("Mu1 = ", Mu1)
        Mu = Mu1 + Mu_
        print("Mu = ", Mu)
    elif x < 2 * as_:
        print("承载力达到极限时，受压钢筋未屈服")
        Mu = simple.Mu_not_yield(
            Es, εcu, α1, β1, as_, ξ, h0, As, As_, fc, fy
        )
        print("Mu = ", Mu)
    φu = εcu / (ξ / β1 * h0)
    print("φu = ", φu)
    return Mu
