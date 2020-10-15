import structure.concrete.类型 as type
'''
部分系数
'''
def 外形系数(t: type.钢筋种类) -> float:
    s = type.钢筋种类
    switch = {  
        s.带勾光面钢筋 : 0.16,
        s.带肋钢筋     : 0.14,
        s.螺旋肋钢丝   : 0.13,
        s.三股钢绞线   : 0.16,
        s.七股钢绞线   : 0.17
    }
    return switch[t]