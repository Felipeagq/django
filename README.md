# DJANGO    
## Ambiente virutal y Settings
```powershell
# creamos entorno virtual
python -m virtualenv venv

# activamos el entorno virtual
.\venv\Scripts\activate

# instalamos django en el entorno
pip install django

# creamos el project
django-admin startproject [projecto] .
```

## Primeros pasos
```powershell
# realizamos las migraciones predeterminadas sqlite
python manage.py migrate

# Corremos el servidor
python manage.py runserver
```

## Views
Para crear Views en Django:
- debemos crear un archivo llamado views dentro de nuestro [projecto] y ahí empezar hacer las funciones de las vistas.
- Agregarlo en el archivo de urls, tener en cuenta que django agrega automaticamente el primer "/".

### Vista estatica:
- ![Agregar vista al archivo de views](./imagenes/vista1.jpg)
- ![Agregar la vista al archivo de urls](./imagenes/agregar_vista_url.jpg)

### Vista con parametros Url:
- dentro del mismo archivo views.py
- ![](./imagenes/vista2.jpg)
- ![](./imagenes/agregar_vista2.jpg)

### Plantillas:
- Necesitaremos:
    - Template.
    - Contexto.
    - Render.
- Dentro del proyeto creamos una carpeta llamada templates.
- ![](./imagenes/vista_plantilla.jpg)