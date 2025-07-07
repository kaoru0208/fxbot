import pytest
from validators import validate_ema_params

def test_valid():               # 通るケース
    validate_ema_params(5, 20)

@pytest.mark.parametrize("fast,slow", [(5,5), (10,9)])
def test_invalid(fast, slow):   # ダメなケース
    with pytest.raises(ValueError):
        validate_ema_params(fast, slow)
