# errors
payment errors beautification

# sample request

curl -X GET \
  https://pm18g7bj98.execute-api.eu-central-1.amazonaws.com/api/error/10005 \
  -H 'Postman-Token: 70201f7c-da30-4993-ad85-ac729cd8fd2c' \
  -H 'cache-control: no-cache' \
  -H 'x-api-key: itRY0IcFJJ4J0Va71uSMG2Op3nBx5j8i7t3DTDEP'

# sample successful response

{
    "errorcode": "10005",
    "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olacak 1000 den fazla senaryo söz konusu olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
}

# sample failure response

{
    "Code": "NotFoundError",
    "Message": "NotFoundError: 10006"
}
