'''
钢筋与混凝土的粘结作用
'''
def τ(V, γs, h, μs):
	'''
	裂缝出现前作用在钢筋表面的粘结应力
	'''
	return V / γs / h / μs
def τu(Tu, μs, lc):
	'''
	拔出试验测试粘结强度
	'''
	return Tu / μs / lc
def la(α, fy, ft, d):
	'''
	钢筋锚固长度
	'''
	return α * fy / ft * d