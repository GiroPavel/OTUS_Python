# OTUS_Python
Homeworks

[Робота с функциями](https://github.com/GiroPavel/OTUS_Python/blob/master/homework_1/task.py "Робота с функциями")

[Классы](https://github.com/GiroPavel/OTUS_Python/tree/master/homework_2 "Классы")

[Базовый фронтенд](https://github.com/GiroPavel/OTUS_Python/tree/master/homework_4 "Базовый фронтенд")
- Нажатие на кнопку "Заказать звонок"
- Панель администрирования - /administration 

[Docker; системы контроля зависимостей](https://github.com/GiroPavel/OTUS_Python/tree/master/homework_5 "Docker; системы контроля зависимостей")
- Заруск проекта:
  1. Установить git на локальной машине
  
     https://git-scm.com/book/ru/v2/Введение-Установка-Git
     
  2. Установить Docker
  
     https://docs.docker.com/engine/install/
     
  3. Склонировать репозиторий в любую директорию
  
     git clone https://github.com/GiroPavel/OTUS_Python.git
     
  4. Зайти в директорию с проектом 
  
     cd homework_5
     
  5. Выполнить команду
  
     docker build . -t web_app
     
  6. Посмотреть образ
  
      docker images
      
  7. Запомнить IMAGE ID 
  
  8. Запустить контейнер из образа командой
  
     docker run -d -p=5000:5000 IMAGE ID(из пункта 7)

[Flask + SQLAlchemy; docker-compose](https://github.com/GiroPavel/OTUS_Python/tree/master/homework_6 "Flask + SQLAlchemy; docker-compose")
- Нажатие на кнопку "Заказать звонок" -> всплывающее окно -> заполняем форму -> отправляем -> данные в базe
- Панель администрирования - /administration - выбрать вкладку "Входящие звонки" - данный подтягиваются из базы
