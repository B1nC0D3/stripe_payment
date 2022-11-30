# Имитация интернет-магазина

Это небольшой сайт-имитация интернет-магазина, в котором можно делать тестовые оплаты товара с помощью платежной системы Stripe.

---
## Запуск приложения
Сайт доступен по ip: 51.250.83.193

Данные от админки:
```
username=admin
password=1111
```
В случае запуска локально:
C установленным Docker выполните следующее:
```
    docker-compose up 
```
Сайт будет доступен по адресу: localhost
    
 

---

## Заполнение .env файла
```
DJANGO_SECRET_KEY='Ur_djago_sercet_key'
STRIPE_PUBLIC_KEY='Ur_stripe_public_key'
STRIPE_SECRET_KEY='Ur_stripe_secret_key'
DB_ENGINE=django.db.engine
DB_NAME=database_name 
POSTGRES_USER=database_user
POSTGRES_PASSWORD=database_password
DB_HOST=database_host
DB_PORT=database_port
```
 ---

## Технологии

- Python 3.9
- Django 2.2
- Stripe
