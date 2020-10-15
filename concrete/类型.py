from enum import Enum
'''
混凝土和钢筋等的类型
'''
class 钢筋种类(Enum):
    带勾光面钢筋 = 1
    带肋钢筋     = 2
    螺旋肋钢丝   = 3
    三股钢绞线   = 4 
    七股钢绞线   = 5