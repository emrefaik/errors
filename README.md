# errors
payment errors beautification

for api key requests please send us a mail kartliodemeler@gmail.com

# sample request

```curl
curl -X GET \
  https://pm18g7bj98.execute-api.eu-central-1.amazonaws.com/api/error/10005 \
  -H 'x-api-key: itRY0IcFJJ4J0Va71uSMG2Op3nBx5j8i7t3DTDEP'
```

# sample successful response


```js
{
    "errorcode": "10005",
    "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olacak 1000 den fazla senaryo söz konusu olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
}
```
# sample failure response


```js
{
    "Code": "NotFoundError",
    "Message": "NotFoundError: 10006"
}
```
# swagger


```js
{
  "swagger": "2.0",
  "info": {
    "version": "1.0",
    "title": "app"
  },
  "host": "pm18g7bj98.execute-api.eu-central-1.amazonaws.com",
  "basePath": "/api",
  "schemes": [
    "https"
  ],
  "paths": {
    "/error/{error}": {
      "get": {
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "error",
            "in": "path",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "200 response",
            "schema": {
              "$ref": "#/definitions/Empty"
            }
          }
        },
        "security": [
          {
            "api_key": []
          }
        ]
      }
    }
  },
  "securityDefinitions": {
    "api_key": {
      "type": "apiKey",
      "name": "x-api-key",
      "in": "header"
    }
  },
  "definitions": {
    "Empty": {
      "type": "object",
      "title": "Empty Schema"
    }
  }
}
```
