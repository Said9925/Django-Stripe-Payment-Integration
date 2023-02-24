# Django Stripe Payment Integration

### Это простое веб-приложение Django, демонстрирующее, как интегрировать платежную систему Stripe в веб-приложение с помощью Django, Stripe API и библиотеки Stripe Python.

---
## Функции
- Модель предмета Django с полями (название, описание, цена)
- GET /buy/{id} - API для получения идентификатора сеанса Stripe для оплаты выбранного предмета
- GET /item/{id} - API для получения простейшей HTML-страницы с информацией о выбранном Товаре и с кнопкой «Купить» при нажатии который переходит на страницу оплаты Stripe через библиотеку Stripe JS.
---
## Технологии
### Этот проект был создан с использованием следующих технологий:
- Python 3.8+
- Django 3.1+
- Stripe API
- Stripe Python library
--- 
## Установка
### Чтобы установить и запустить этот проект, выполните следующие действия:
1. Clone the repository: `git clone https://github.com/yourusername/your-repo.git`
2. Перейдите в каталог проекта:
3. Установите зависимости проекта: `pip install -r requirements.txt
`
4. Настройте переменные среды:
    - STRIPE_SECRET_KEY: секретный ключ Stripe API
    - STRIPE_PUBLIC_KEY: открытый ключ Stripe API.
5. Запустите миграцию базы данных: `python manage.py migrate`
6. Запустите сервер Django: `python manage.py runserver`
7. Перейдите на http://localhost:8000/item/{id} в веб-браузере, чтобы просмотреть веб-приложение.

