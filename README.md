# CoreMLProject

Пример проекта для ДС-ов чтоб разрабатываеть в структуре удобной к деплою в будущем.

## Папки: 
+ [ml_lib](./ml_lib/README.md) - базовая папка для моделей
+ [ml_lib_doc](./ml_lib_doc/README.md) - документация к ml_lib
+ requirements - необходимые библиотеки для разработки
  + base.txt - то что исключительно при работе необходимо
  + lint.txt - содержит линтеры для проверки кода
  + test.txt - содержит библиотеки для тестов (если вы их пишите)
  + dev.txt - для разработки (все остальные блоки инсталит)
+ [research](./research/README.md) - папка с кодом экспериментов
+ [resources](./resources/README.md) - папка в которую складываются все файлы для ресерча и модели
+ [tests](./tests/README.md) - тесты на код
+ [data_handler](./data_handler/README.md) - работа с данными
+ [rest_flask](./rest_flask/README.md) - подключение rest_api

## Старт разработки

> создать [виртуальное окружение](https://virtualenv.pypa.io/en/latest/) <br>
> `virtualenv venv`

> "войти" в него <br>
> Linux|Mac: <br>
> `sources venv/bin/activate`<br>
> Windows: <br>
> `venv\Scripts\activate`

> установить библиотеки для разработки<br>
> `pip install -r requirements\dev.txt`

> проинициализировать [pre-commit](https://pre-commit.com/): <br>
> `pre-commit install`

> проинициализировать [git-flow](https://danielkummer.github.io/git-flow-cheatsheet/index.html#): <br>
> `git flow init`

## переменные окружения 

> `APP_CONFIG` - путь к конфигу flask <br>
> <u>example</u>: APP_CONFIG=rest_flask.config.DevConfig