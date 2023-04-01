"""
Для сборки пакета нужно выполнить следующую команду:
python setup.py sdist --formats=gztar --dist-dir=./

После этого в корневой папке проекта появится файл m3_project-1.0.tar.gz.

Чтобы установить пакет, нужно создать виртуальное окружение, активировать его и выполнить команду:
pip install m3_project-1.0.tar.gz --extra-index-url http://pypi.bars-open.ru/simple/ --trusted-host pypi.bars-open.ru

После установки пакета можно запустить приложение при помощи команды:
python <path_to_venv>/lib/python3.6/site-packages/m3_project/manage.py runserver 0.0.0.0:8000
Здесь <path_to_venv> - путь к корневой папке виртуального окружения, созданного при установке зависимостей.
"""

from setuptools import setup, find_packages

setup(
    name='m3_project',
    version='1.0',
    author='hahawait',
    packages=find_packages(),
    install_requires=[
        'django==2.2.2',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.47'
    ],
    extras_require={
        'bars-open': [
            'm3-objectpack==2.2.47'
        ]
    },
    dependency_links=[
        'http://pypi.bars-open.ru/simple/'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
