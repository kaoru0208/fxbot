<!-- プロジェクト名と CI バッジ -->
# fxbot  
![CI](https://github.com/kaoru0208/fxbot/actions/workflows/ci.yml/badge.svg)

## ✨ 何ができる？
- EMA クロスや Walk‑Forward 最適化など、FX/株価のアルゴリズム検証を **ワンコマンド** で実行  
- Optuna を使ったパラメータ自動探索  
- OANDA API（デモ／ライブ）に接続してリアルタイム検証  
- GitHub Actions で自動テスト・Lint・Docker ビルドまで完備

---

## 🖥️ クイックスタート

```bash
git clone https://github.com/kaoru0208/fxbot.git
cd fxbot
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt        # 依存をインストール
python -m pip install -e .                       # 開発モードでパッケージ登録
pytest -q                                        # すべてのテストを実行

