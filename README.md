# 🤖 GigaChat CLI

Консольный инструмент для взаимодействия с моделью **GigaChat** через командную строку. Позволяет отправлять текст, код, логи или коммиты на анализ, объяснение, перевод или суммирование. Поддерживает чтение ввода из stdin и аргументов командной строки, а также использование пользовательских и стандартных флагов.

---

## 🛠 Функционал

- Отправка сообщений в GigaChat.
- Чтение ввода из stdin (например: `echo "текст" | python main.py`) или из аргументов командной строки.
- Поддержка флагов:
  - `--check-code` – проверяет следующий код
  - `--review-commit` – проверяет коммит и делает ревью
  - `--explain` – объясняет следующее
  - `--check-log` – проверяет логи и объясняет ошибки
  - `--summarize` – суммирует текст
  - `--translate` – переводит на русский язык
- Возможность указания пользовательского префикса через флаг `--prompt "..."`

---

## 📦 Установка

1. Установите зависимости:

```bash
pip install gigachat python-dotenv
```

2. Создайте файл `.env` рядом с `main.py` со следующими переменными:

```env
GIGACHAT_CREDENTIALS=ваш_токен
GIGACHAT_MODEL=GigaChat-Pro
VERIFY_SSL_CERTS=false
```

---

## 🚀 Примеры использования

```bash
python main.py "Объясни на русском Что такое ООП?"
```
### С флагом:
```bash
echo "def hello():\n    print('Hello')" | python main.py --check-code
```
```bash
cat index.php | python main.py --check-code
```
```bash
git show HEAD | python main.py --review-commit
```

### С пользовательским префиксом:
```bash
tail laravel.log | python main.py --prompt "Объясни на русском"
```

### Без флага:
```bash
echo "Как работает Python?" | python main.py
```

---

## 🧩 Возможные улучшения (если потребуется)

- Добавление поддержки нескольких флагов.
- Автоматическое форматирование кода.
- Добавление опции `--help` для вывода справки.
- Логирование запросов и ответов.

---

## ✅ Требования

- Python 3.8+
- [`gigachat`](https://pypi.org/project/gigachat/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

## 📄 License

MIT License — см. [LICENSE](LICENSE)