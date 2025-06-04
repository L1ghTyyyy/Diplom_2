# Тесты API: Пользователи и Заказы

Автоматические тесты для проверки API:

* создания и авторизации пользователей,
* изменения их данных,
* создания и получения заказов.

Все тесты сопровождаются Allure-отчётом.

---

## Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## Запуск тестов с Allure-отчётом

1. Запуск тестов и сохранение результатов:

   ```bash
   pytest tests --alluredir=allure_results
   ```

2. Генерация и открытие отчёта:

   ```bash
   allure serve allure_results
   ```

---

## Покрытие тестами

### Создание пользователя

* `test_create_unique_user` — уникальный пользователь
* `test_create_user_already_exist` — пользователь уже существует
* `test_create_user_with_no_fill_data` — не заполнено обязательное поле

### Логин

* `test_user_login` — успешный логин
* `test_login_nonexistent_user` — неверный логин/пароль

### Изменение данных пользователя

* `test_change_user_data` — с авторизацией (можно изменить любое поле)
* `test_change_unauthorized_user_data` — без авторизации (проверка ошибки)

### Создание заказа

* `test_create_order_with_authorized_user` — с авторизацией
* `test_create_order_by_unauthorized_user` — без авторизации
* `test_create_order_with_ingredients` — с ингредиентами
* `test_create_order_without_ingredients` — без ингредиентов
* `test_create_order_with_invalid_hash` — с неверным хешем ингредиентов

### Получение заказов

* `test_get_orders_by_authorized_user` — авторизованный пользователь
* `test_get_orders_by_unauthorized_user` — неавторизованный пользователь

---

## Структура

```
├── tests/               # Тесты
├── allure_results/      # Сырые данные для Allure
├── requirements.txt     # Зависимости
└── README.md            # Этот файл
```
