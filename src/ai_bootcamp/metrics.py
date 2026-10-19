"""信号特征量：RMS 有效值"""
import math
def rms(xs):
	if not xs:
		raise ValueError("rms()需要非空序列")
	return math.sqrt(sum(x*x for x in xs)/ len(xs))