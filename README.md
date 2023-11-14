# fastAPI
Servicio API REST que permite realizar las 4 operaciones matemáticas básicas entre dos numeros que ingresan como parametros de la aplicacion a través de peticiones HTTP.

## Ejecución local

1. Clonar el repositorio:

git clone https://github.com/cdsantosg/fastAPI.git

2. Ingresar al directorio del proyecto
   cd fastAPI
   
4. construir la imagen de Docker
   sudo docker build -t fastapi .
   
6. Ejecutar el contenedor Docker
   sudo docker run -d --name fastapi -p 80:80 fastapi

El entorno estará disponible en:

http://127.0.0.1/docs
   
