# Diploma_Rostelekom

Созданы автоматизированные тесты PyCharm, для запуска тестов необходима библиотека pytest, selenium, time.
При создании автоматизированных тестов использовались методы тест дизайна: Разбиение на классы эквивалентноти, Анализ граничных значений, Исследовательское тестирование, Предугадывание ошибок. 
Для запуска автотестов необходимо выполнить следующие команды:

1. В терминале ввести git clone (https://github.com/AnnaZaitsava1408/Diploma_Rostelekom/tree/master)
2. В PyCharm установить библиотеки pytest == 6.2.5, selenium == 4.9.0, pytest-selenium == 4.0.0, time
3. Запустить тесты.

Произвелась автоматизация тестов для регистрации  сайта "Ростелеком" ссылка https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=dec4ba85-fd87-4792-bcb0-860384b5c0be.
В файлах test_reg_positive и test_reg_negative представлены негативные и позитивные тесты для регистрации на сайте через почту, номер тел.
В файлах test_auth_positive и test_auth_negative представлены негативные и позитивные тесты для авторизации на сайте через почту, номер тел, логин.
В файле test_auth_social_networks представлены тесты, для проверки возможности быстрого входа через соцсети, такие как VK,OK, T-ID, Mail.

Кол-во авто.тестов в файле:
1. test_reg_positive - 11
2. test_reg_negative - 18
3. test_auth_positive - 6
4. test_auth_negative - 9
5. test_auth_social_networks - 4
