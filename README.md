### **リポジトリのクローン**

git clone https://github.com/Lae-402/rackproject.git



### **仮想環境作成・有効化**

python -m venv env

source env/bin/activate  # macOS/Linux

env\Scripts\activate.bat  # Windows



### **使用パッケージ・依存関係インストール**

pip install -r requirements.txt



### **DBマイグレーション**

python manage.py migrate



### **サーバー起動**

python manage.py runserver
