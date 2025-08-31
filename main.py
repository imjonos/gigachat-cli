from gigachat import GigaChat
import sys
from dotenv import load_dotenv
import os

load_dotenv()

credentials = os.getenv("GIGACHAT_CREDENTIALS")
model = os.getenv("GIGACHAT_MODEL")
verify_ssl_certs = os.getenv("VERIFY_SSL_CERTS").lower() == "true"

flags = {
    "--check-code": "Проверь следующий код:\n",
    "--review-commit": "Проверь следующий коммит и сделай его ревью:\n",
    "--explain": "Объясни мне следующее:\n",
    "--check-log": "Проверь логи и объясни найденные ошибки:\n",
    "--summarize": "Суммируй следующий текст:\n",
    "--translate": "Переведи на русский язык:\n"
}

prompt = ""
args = sys.argv[1:]
flag_prefix = ""

if "--help" in args:
    print('--help')
    print('--prompt text')
    for flag in list(flags.keys()):
        print(flag)
    exit(0)

if "--prompt" in args:
    prefix_index = args.index("--prompt")
    if prefix_index + 1 < len(args):
        prompt = args[prefix_index + 1] + "\n"
        del args[prefix_index:prefix_index + 2]

for flag in list(flags.keys()):
    if flag in args:
        flag_index = args.index(flag)
        del args[flag_index]
        flag_prefix = flags[flag]
        break  # пока только один флаг

if args:
    message = ' '.join(args)
else:
    message = sys.stdin.read().strip()

if not message:
    print("Error: Please provide a message either as an argument or via stdin.")
    exit(1)

full_message = prompt + " " + flag_prefix + message

giga = GigaChat(
    credentials=credentials,
    model=model,
    verify_ssl_certs=verify_ssl_certs,
)

response = giga.chat(full_message)

print(response.choices[0].message.content)