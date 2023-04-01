# DjangoTestInterviewTask
## CRUD операции (M3-Core, ObjectPack)


### **Установка и запуск проекта**
### Чтобы запустить проект, выполните следующие шаги:

1. Клонируйте репозиторий на свой компьютер:
https://github.com/hahawait/DjangoTestInterviewTask

2. Установите зависимости из файла requirements.txt:
**pip install -r requirements.txt**

3. Создайте и настройте базу данных:
**python manage.py migrate**

4. Запустите сервер:
**python manage.py runserver**

### UPD 
Возможны конфликты с версией Python (я использовал 3.10.7). В таком случае стоит обратить внимание на содержимое ошибок и подредачить исходники библиотек. 
В моем случае была ошибка с Collections. Решение - collections.abc