# Flamelingo

Flamelingo - приложение для изучения языков в игровой форме. Помимо улучшения лексикона, навыков говорения и слуха вы можете углубиться в культуру какой-либо нации. Вы сможете познакомиться не только с разговорной речью, но и с культурой, традициями и атмосферой выбранного вами языка. Имеет удобный интерфейс для внедрения в учебный процесс.

## Предварительные требования

1. Python 3.12
2. PostgreSQL
3. Redis

## Переменные окружения

- DEBUG - режим работы. Во время разработки устанавливать в true

### Обязательные поля

- BASE_URL, FLOWER_URL - URL для редиректов
- DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS - переменные для доступа к базе данных.
- REDIS_HOST, REDIS_PORT - переменные для доступа к Redis
- SESSION_SECRET - переменная для шифрования сессий

### Необязательные поля

- AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_BUCKET_NAME, AWS_S3_ENDPOINT_URL, AWS_S3_USE_SSL, AWS_DEFAULT_ACL, AWS_QUERYSTRING_AUTH, AWS_S3_CUSTOM_DOMAIN - переменные для доступа к S3 хранилищу. Указывать только при DEBUG = false
- GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET - переменные для доступа к google oauth
- LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET - переменные для доступа к linkedin oauth
- MICROSOFT_CLIENT_ID, MICROSOFT_CLIENT_SECRET - переменные для доступа к microsoft oauth
- SMTP_HOST, SMTP_PORT, SMTP_EMAIL, SMTP_PASSWORD - переменные для доступа к SMTP-серверу. Указывать только при DEBUG = false

## Запуск

1. Установите вышеупомянутые переменные окружения
2. Установите uv `pip install uv`
3. Установите зависимости `uv sync`
4. Выполните миграции `make migrate`
5. Если вы работаете в VS Code нажмите F1 и выберите Terminals: Run, иначе в 3 терминалах запустите команды, указанные в .vscode/terminals.json

## Дальнейшая работа

### Вход в учетную запись админа

1. Перейдите на BASE_URL/admin/login
2. Введите логин и пароль (admin@example.com, admin)
