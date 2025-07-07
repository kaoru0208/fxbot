def validate_ema_params(fast: int, slow: int, slow_max: int = 200) -> None:
    if fast <= 0 or slow <= 0:
        raise ValueError("fast と slow は正の整数にしてください")
    if fast >= slow:
        raise ValueError(f"fast({fast}) は slow({slow}) より小さくしてください")
    if slow > slow_max:
        raise ValueError(f"slow({slow}) は上限 {slow_max} を超えています")
