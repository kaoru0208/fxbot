cat > validators.py <<'PY'
def validate_ema_params(fast: int, slow: int, slow_max: int = 200) -> None:
    if fast <= 0 or slow <= 0:
        raise ValueError("fast, slow must be positive")
    if fast >= slow:
        raise ValueError(f"fast ({fast}) must be < slow ({slow})")
    if slow > slow_max:
        raise ValueError(f"slow ({slow}) exceeds limit {slow_max}")
PY

