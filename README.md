# colegio-elasticsearch

## Paguinas para buscar en la coleccion de documentos

### /document/

Peticion GET

Devuelve todos los documentos guardados 

### /document/?search=engine&fields=dispositionTitle,date,volume,legislationTranscriptCopy&disposition=1,2,3

"search":"<palabra_a_buscar>"

"fields":"dispositionTitle,date,volume" 

Si no se envia fields en la peticion GET se hace una busqueda en todos los campos, se tiene que separar con coma ( , ) cada campo especifico en donde deseas buscar 

"disposition":"1,2,4" 

Campo para hacer una busqueda mas precisa con el numero de disposicion separado por comas 

Devuelve una clave http 200 OK

devuelve un json con cada documento y con la misma forma con la que se suben los documentos

        {
            "id": "",
            "dispositionTitle": "",
            "date": "",
            "volume": "",
            "pageNumbers": "",
            "legislationTranscriptOriginal": "documentoPDF",
            "legislationTranscriptCopy": "",
            "place": "",
            "dispositionNumber": "",
            "dispositionTypeId": "",
            "affairId": "",
            "affairId",
        }

## Paguinas para subir documentos

### /document/

Peticion POST

Se sube con un formulario html con los siguientes campos

        {
            "id": "",
            "dispositionTitle": "",
            "date": "",
            "volume": "",
            "pageNumbers": "",
            "legislationTranscriptOriginal": "documentoPDF",
            "legislationTranscriptCopy": "",
            "place": "",
            "dispositionNumber": "",
            "dispositionTypeId": "",
            "affairId": "",
            "affairId",
        }

Devuelve el mismo documento que se creo con una respuesta http 200 OK

## Configuracion de sistema de autenticacion Oauth2

Para autenticacion se necesita registrar la aplicacion en el sistema de autenticacion Oauth2, se debe de entrar al siguiente link con una cuenta de administrador Django:

### /o/applications/

En la paguina se da click en new application y meter las siguientes opciones en el formulario:

- Client type: Confidential
- Authorization grant type: Resource owner password-based

El nombre puede ser cualquiera que consideres

Despues de registrarse se obtiene un client_id y client_secret que se deben poner en las variables de entorno CLIENT_ID y CLIENT_SECRET respectivamente

## Sistema de autenticacion 

### /authentication/register/ 

Peticion POST 

Para registrar un nuevo usuario y obtener un token para accesar 

        {
            "username":"",
            "password":""
        }

Regresa el siguiente json con token para autenticarse

        {
            "access_token": "dRX9ekV8D2SucxERFWhH4QnlDREcYT",
            "expires_in": 36000,
            "token_type": "Bearer",
            "scope": "read write",
            "refresh_token": "8JcCfcbGfpTL9TjlvE0J7nGphfyqYK",
            "user": {
                "username": ""
            }
        }

### /authentication/token/

Peticion POST 

Para pedir iniciar sesion con un usario ya registrado

        {
            "username":"",
            "password":""
        }

Regresa el siguiente json con las misma forma que en el registro

        {
            "access_token": "HjE2x8eGi0oHy9TT8GgpdZ6keyat2V",
            "expires_in": 36000,
            "token_type": "Bearer",
            "scope": "read write",
            "refresh_token": "5MKrfsCcj0zAVeYR1JNFEhrPRgJPji",
            "user": {
                "username": ""
            }
        }

### /authentication/token/refresh/

Peticion POST 

Se envia el refresh token de la sesion para refrescarlo y obtener uno nuevo

        {"refresh_token": "<token>"}

Regresa un json con un nuevo token

        {
            "access_token": "BvCEMEzH8FZ96SKylbtboILK9FLF7k",
            "expires_in": 36000,
            "token_type": "Bearer",
            "scope": "read write",
            "refresh_token": "N0omRJWoszPyv5pnEQyCHqkpCaSLvx"
        }

### /authentication/token/revoke/

Peticion POST 

Se envia el token de la sesion para cerrar la sesion e invalidar el token

        {"token": "<token>"}

Regresa un json con el siguiente mensaje

        {
            "message": "token revoked"
        }

## Variables de entorno .env

### Settings django elastic/settings.py 

        SECRET_KEY=
        DEBUG=
        DATABASE_NAME=
        DATABASE_USER=
        DATABASE_PASSWORD=
        DATABASE_HOST=
        DATABASE_PORT=

### Configuracion servidor elastic search en formato (localhost:9200)

        ELASTICSEARCH_SERVER=

### Settings Oauth2 users/views.py 

        CLIENT_ID=
        CLIENT_SECRET=

### Se pone el server en formato http://localhost:8000 sin un slash (/) al final

        SERVER=