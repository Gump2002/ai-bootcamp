import pytest 
from ai_bootcamp.metrics import rms
def test_rms_basic():
	assert rms([3,4]) ==pytest.approx(3.5355, abs=1e-3)

def test_rms_single():
	assert rms([5]) == 5.0

def test_rms_empty_raises():
	with pytest.raises(ValueError):
		rms([])