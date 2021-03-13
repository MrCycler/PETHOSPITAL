# OPERCUBE BACKEND - DJANGO REST FRAMEWORK BOILERPLATE

## 1. AUTOR:
- Juan Manuel Mendoza Jacinto (https://github.com/fararay)

## 2. LOCAL PROJECT SETUP:
## 2.2. BASIC PLATFORM SETUP
#### NOTA: Yo ejecuto el proyecto local en OS Windows
- #### YO USO ANACONDA PARA EL DESARROLLO DE PROYECTOS EN PYTHON DISPONIBLE EN: (https://www.anaconda.com/products/individual)

<p align="center"> 
<img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png" alt="anaconda"  style="height:100px;">
</p>

- #### APERTURE EL ANANCONDA PROMPT O ENTRE A ANACONDA DESDE CMD CON EL COMANDO:
`C:/Users/User/anaconda3/Scripts/activate`
- #### ES [BUENA PRÁCTICA](https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace) CREAR UN ENTORNO VIRTUAL USANDO EL COMANDO:
`conda create -n venv_project python=3.6`
- #### SIEMPRE PUEDES ACTIVAR EL ENTORNO VIRTUAL USANDO EL COMANDO:
`conda activate venv_project`
## 2.3. DJANGO SETUP
- #### DEBE TENER INSTALADO DJANGO EN SU ENTORNO VIRTUAL, PARA INSTALARLO USE EN UN ENTORNO VIRTUAL EL COMANDO:
`pip install django`

<p align="center"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/1200px-Django_logo.svg.png" alt="django" style="height:80px;">
</p>

- #### PUEDE USAR EL SIGUIENTE COMANDO PARA VERIFICAR LOS PAQUETES INSTALADOS EN SU ENTRONO VIRTUAL:
`pip freeze`
#### NOTA LOS PAQUETES USUALES QUE SE INSTALAN CON DJANGO POR DEFECTO SON:
`asgiref, certifi, django, pytz, sqlparse, wincertstore`
- #### PARA CREAR UN NUEVO PROYECTO CON DJANGO USE EL COMANDO:
`django-admin startproject project_name`
- #### PARA CREAR UN NUEVO PROYECTO CON DJANGO USE EL COMANDO:
`django-admin startproject project_name`
- #### PARA EJECUTAR EL PROYECTO COMO PRUEBA EN LOCAL USAR (IGNORE LOS MENSAJES DE ERROR):
`python manage.py runserver`