# Cooks-Companion
Запускати на версії `Python>=3.10`<br>

# Встановлення
Викнонуйте наступні команди в терміналі:
```bash
git clone https://github.com/zakharfsk/Cooks-Companion.git
cd Cooks-Companion

python -m pip install virtualenv
python -m virtualenv venv

# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate.bat

python -m pip install -r requirements.txt

# Migration
python manage.py makemigrations
python manage.py migrate

# Run
python manage.py runserver
```

# PS
В проекті використовуться запроси до Штучного інтелекта і вони обмежені(+- 6 запросів на весь сайт)
