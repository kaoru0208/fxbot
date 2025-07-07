import os

import pytest

SKIP_OANDA = pytest.mark.skipif(
    not os.getenv("OANDA_TOKEN"), reason="OANDA_TOKEN が無いためスキップ"
)


def pytest_collection_modifyitems(config, items):
    for item in items:
        # ファイル名やマーカー名で判定（例: test_api.py だけスキップ）
        if "test_api.py" in str(item.fspath):
            item.add_marker(SKIP_OANDA)
