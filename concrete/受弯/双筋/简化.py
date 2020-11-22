def Mu_not_yield(Es, εcu, α1, β1, as_, ξ, h0, As, As_, fc, fy):
    '''
    (5-78)
    '''
    x = ξ * h0
    σs_ = Es * εcu * (β1 * as_ / ξ / h0 - 1)
    return (
        (σs_ * As_ + fy * As) * (h0 - x / 2)
        -
        σs_ * As_ * (h0 - as_)
    )


def Mu_not_yield_simplified(fy, As, h0, as_):
    '''
    (5-79)
    取x = 2as'
    '''
    return fy * As * h0 * (1 - as_ / h0)
