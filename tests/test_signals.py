from validators import validate_ema_params

def test_signal_dummy():
    fast, slow = 5, 20
    validate_ema_params(fast, slow)
    assert fast < slow
