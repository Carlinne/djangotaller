git clone https://github.com/xtornasol512/flaskapp.git

-------------------------------------------------------------------------------------------------------------
Crear un entorno virtual en python
py -3 -m pip install virtualenv
py -3 -m virtualenv djangoproj
Ir a la siguiente direccion: C:\Users\Carlinne Pacheco\djangoproj\Scripts
 dentro de esa carpeta hay un activate.bat
C:\Users\Carlinne Pacheco\djangoproj\Scripts>activate.bat
se ejecuta en lote...
Nos aparece el entorno virtual
(DJANGO~1) C:\Users\Carlinne Pacheco\djangoproj\Scripts>pip install flask
*****Version del pip
pip --version
python (entramos al prompt de python version 3.5)

Buscamos la carpeta que descargamos ...
(DJANGO~1) C:\Users\Carlinne Pacheco\djangoproj\Scripts>cd /

(DJANGO~1) C:\>cd proyectos

(DJANGO~1) C:\proyectos>cd flaskapp

(DJANGO~1) C:\proyectos\flaskapp>python app.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 157-510-513

produccion
Archivos necesarios...
desarrollo
Desarrollo de la aplicación...

Asi se crea un entorno virtual ***************************
C:\Users\Carlinne Pacheco>cd /

C:\>cd proyectos

C:\proyectos>cd djangotaller

--Dentro de la carpeta venv se crea django
C:\proyectos\djangotaller>py -3 -m virtualenv venv/django
Using base prefix 'C:\\Users\\Carlinne Pacheco\\AppData\\Local\\Programs\\Python\\Python35-32'
New python executable in C:\proyectos\djangotaller\venv\django\Scripts\python.exe
Installing setuptools, pip, wheel...done.

C:\proyectos\djangotaller>cd venv

C:\proyectos\djangotaller\venv>cd django

C:\proyectos\djangotaller\venv\django>cd Scripts

C:\proyectos\djangotaller\venv\django\Scripts>activate.bat

(django) C:\proyectos\djangotaller\venv\django\Scripts>

Iniciar un repositorio
(django) C:\proyectos\djangotaller\venv\django\Scripts>git init
Initialized empty Git repository in C:/proyectos/djangotaller/venv/django/Scripts/.git/