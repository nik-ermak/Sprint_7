# Sprint_7
Проект по автоматизации API-тестов для сервиса Яндекс Самокат
Спринт 7 - Тестирование API
Ссылка на сервис - https://qa-scooter.praktikum-services.ru

В корневой директории проекта содержатся вспомогательные инструменты для тестирования и набор тестов:
1. urls_for_test - в файле содержится url и необходимые ручки для тестирования;
2. helper - в файле содержатся вспомогательные методы для генерации данных;
3. tests - в директории содержатся тесты;
4. conftest - в файле содержится фикстура используемая в тестах
5. allure-results - файл содержит JSON-файлы в которых результаты выполнения тестов;
6. requirements - в файле перечислены все внешние зависимости тестов;
7. api_methods - в файле содержатся методы используемые в тестах
8. README - в файле содержится общая информация по проекту.

В рамках проекта было необходимо проверить лишь определённую функциональность:
1. Создание курьера, а также проверка на повторное использование логина, создание курьера с невалидными данными и отсутствием некоторых из них;
2. Авторизация курьера, а также проверка на авторизацию с невалидными данными и отсутствием некоторых обязательных;
3. Создание заказа с указанием 1-го, 2-х и без указания цвета самоката
4. Получение списка заказов

Для запуска всех тестов необходимо в терминал ввести команду: pytest -v
Для запуска всех тестов и получения Allure-отчёта нужно воспользоваться командой: pytest --alluredir=allure_results
Для генерации Allure-отчёта в виде веб-страницы нужно воспользоваться командой: allure serve allure_results
