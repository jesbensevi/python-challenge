# CODE CHALLENGE

---

## Challenge

Se crearon 2 microservicios para la solución del problema, el primero(**ms-signin**) se encarga del login del usuario, mientras que el segundo(**ms-signout**) se encarga de cerrar la sesión del usuario, también se creo una base de datos PostgreSQL para almacenar los datos de los usuarios.

### Deployment

Para el despliegue solo es necesario tener instalado Docker:
[Docker](https://docs.docker.com/engine/install/) - guia de instalacion.

Para el despliegue de los microservicios y la BD se debe ejecutar el siguiente comando en la raiz del proyecto:

```bash
docker compose up
```

esto hace que se creen 3 imagenes de docker, una para cada microservicio y la base de datos.

### Seed de la base de datos

para poder tener usuarios usamos un script sql que se encuentra en la carpeta **seed-db**, este consta de la creación de la tabla y el insert de 10 usuarios para poder usarlo en los ms esto se ejecuta con el docker compose, por lo que no es necesario hacer un insert manual.

### ms-signin

Este microservicio se encarga de hacer el login del usuario, para esto valida la existencia del username en la base de datos y retorna un JWT para el uso de sesiones en Frontend, a parte de retornar en el body tambien hace un set de una cookie con el JWT para que el usuario pueda usarla en el ms-signout.

Este ms se encuentra en el puerto 80 desde local podemos verlo de la siguiente manera:

```bash
localhost:80/signin
```

ejemplo de request:

```bash
curl --location 'localhost:80/signin' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "email2@mail.com",
    "password": "password2"
}'
```

### ms-signout

Este microservicio se encarga de hacer el logout del usuario, para esto valida la existencia de la cookie en el request y la elimina, si la cookie no existe retorna un error.

Este ms se encuentra en el puerto 81 desde local podemos verlo de la siguiente manera:

```bash
localhost:81/signout
```

ejemplo de request:

```bash
curl --location 'localhost:81/signout' \
--header 'Cookie: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVtYWlsMkBtYWlsLmNvbSIsImV4cCI6MTY3Nzc4ODQzMn0.dJXKqnJsFrJyfAjhHMeDKlFi7GUy03pM2hrndnoOJYQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "email2@mail.com"
}'
```
