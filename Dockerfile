FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /inventory_management

# 依存関係のインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# ポート8000を開放
EXPOSE 8000

# アプリケーションの実行コマンド
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
