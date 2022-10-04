# Instrucciones para levantar el proyecto

- Crear un entorno virutal con el comando `python -m venv mientorno`
- Una vez creado activar el entorno con el comando `source mientorno/bin/activate`
- Una vez activado procedemos a instalar los paquetes necesarios con el comando `pip install -r requirements.txt`
- Levantamos el proyecto con `python manage.py runserver`
- Finalmente podemos acceder a la siguiente liga http://127.0.0.1:8000/admin


# Accesos para el admin de Django
- User: alonso
- Pass: alonso
- Cabe mencionar que ya tenemos datos en la base de datos de sqlite para las pruebas

# Rutas para probar las peticiones a la API
### - Metodo POST para crear un maestro
- URL: http://127.0.0.1:8000/api/v1/maestros
[![](https://i.postimg.cc/3rZRzMVr/Captura-de-Pantalla-2022-10-04-a-la-s-0-25-15.png)](https://i.postimg.cc/3rZRzMVr/Captura-de-Pantalla-2022-10-04-a-la-s-0-25-15.png)
### - Metodo GET para obtener todos los maestros
- En el body no lleva ningun dato, hay que mandarlo vacio
[![](https://i.postimg.cc/Xq2ybt2P/Captura-de-Pantalla-2022-10-04-a-la-s-0-37-16.png)](https://i.postimg.cc/Xq2ybt2P/Captura-de-Pantalla-2022-10-04-a-la-s-0-37-16.png)
### - Metodo GET obtener el sueldo total
- URL: http://127.0.0.1:8000/api/v1/sum-sueldo
[![](https://i.postimg.cc/Hxd2sD2W/Captura-de-Pantalla-2022-10-04-a-la-s-0-40-20.png)](https://i.postimg.cc/Hxd2sD2W/Captura-de-Pantalla-2022-10-04-a-la-s-0-40-20.png)
### - Metodo GET para obtener los salones con el codigo COD
- URL: http://127.0.0.1:8000/api/v1/salones-cod
[![](https://i.postimg.cc/RFWc0StB/Captura-de-Pantalla-2022-10-04-a-la-s-0-43-34.png)](https://i.postimg.cc/RFWc0StB/Captura-de-Pantalla-2022-10-04-a-la-s-0-43-34.png)
### - Metodo GET para obtener todos los maestros y el total de salones por maestro.
[![](https://i.postimg.cc/DZ1w6RkG/Captura-de-Pantalla-2022-10-04-a-la-s-0-44-53.png)](https://i.postimg.cc/DZ1w6RkG/Captura-de-Pantalla-2022-10-04-a-la-s-0-44-53.png)
