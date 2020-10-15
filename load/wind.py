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
	return (4 * k * v10 ** 2 / n * sqrx / (1 +sqrx) ** (4 / 3))
from enum import Enum
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
	raise
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
	raise
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
	raise
def St(fs, D, v):
	'''
	Strouhal number
	'''
	return fs * D / v
def μs(v, v0):
	return 1 - v ** 2 / v0 ** 2
from math import sqrt
def μs(n):
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
	raise
def μz(z, HTs, HTa, zs, za, αs, αa):
	'''
	未截断
	'''
	return (
		(HTs / zs) ** αs
			*
		(z / zs) ** αs
			/
		(HTa / za) ** αa
	) ** 2
def μz(z, HTs, HTa, zs, za, αs, αa):
	'''
	未截断
	'''
	return (
		(HTs / zs) ** αs
			*
		(z / zs) ** αs
			/
		(HTa / za) ** αa
	) ** 2
def μz(z, s: Landform, a: Landform, zs, za):
	__z = max(z0a(a), z)
	return μz(__z, HT(s), HT(a), zs, za, α(s), α(a))