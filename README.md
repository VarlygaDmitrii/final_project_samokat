# Тест на проверку получения информации по заказу по треку.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest -v create-order.py

- Задание 1 БД - проверено, из за бага о задвоении принятых курьером заказов отображаются также и дубли

SELECT c.login,
COUNT(o."inDelivery")
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON o."courierId" = c.id
WHERE o."inDelivery" = True
GROUP BY c.login;

Задание 2 БД - проверено, отмененные заказы (cancelled) по факту работы бэка причисляются к статусу - 0, ошибка работы бэкенда.

SELECT track,
CASE
WHEN cancelled = TRUE THEN '-1'
WHEN finished = TRUE THEN '2'
WHEN "inDelivery" = TRUE THEN '1'
ELSE '0'
END
FROM "Orders";
