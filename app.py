from chalice import Chalice, NotFoundError

app = Chalice(app_name='app')

ERRORS = {

    "05":
        {
            "errorcode": "05",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olacak 1000 den fazla senaryo söz konusu olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },
    "0005":
        {
            "errorcode": "0005",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olacak 1000 den fazla senaryo söz konusu olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },
    "10005":
        {
            "errorcode": "10005",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olacak 1000 den fazla senaryo söz konusu olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },
    "GWERROR_05":
        {
            "errorcode": "GWERROR_05",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olacak 1000 den fazla senaryo söz konusu olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },

    "ERR20005":
        {
            "errorcode": "ERR20005",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olacak 1000 den fazla senaryo söz konusu olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },

    "12":
        {
            "errorcode": "12",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olabilecek nedenlerin başında cvv cvc değerlerinin yanlış girilmesi olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },
    "0012":
        {
            "errorcode": "0012",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olabilecek nedenlerin başında cvv cvc değerlerinin yanlış girilmesi olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },
    "10012":
        {
            "errorcode": "10012",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olabilecek nedenlerin başında cvv cvc değerlerinin yanlış girilmesi olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },

    "ERR20012":
        {
            "errorcode": "ERR20012",
            "errormessage": "Kartınız işleme onay vermedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır. Bu hata mesajına sebep olabilecek nedenlerin başında cvv cvc değerlerinin yanlış girilmesi olabilir. Hata sebebini öğrenmek için kartınızı aldığınız kuruluşun çağrı merkezi aracılığı ile kart operasyonları birimine talep oluşturunuz."
        },
    "51":
        {
            "errorcode": "51",
            "errormessage": "Kartınızın limitini aştınız. Mobil veya internet bankacılığınız ile kullanılabilir kart limitinizi artırabilirsiniz."
        },
    "0051":
        {
            "errorcode": "0051",
            "errormessage": "Kartınızın limitini aştınız. Mobil veya internet bankacılığınız ile kullanılabilir kart limitinizi artırabilirsiniz."
        },
    "10051":
        {
            "errorcode": "10051",
            "errormessage": "Kartınızın limitini aştınız. Mobil veya internet bankacılığınız ile kullanılabilir kart limitinizi artırabilirsiniz."
        },
    "GWERROR_51":
        {
            "errorcode": "GWERROR_51",
            "errormessage": "Kartınızın limitini aştınız. Mobil veya internet bankacılığınız ile kullanılabilir kart limitinizi artırabilirsiniz."
        },

    "ERR20051":
        {
            "errorcode": "ERR20051",
            "errormessage": "Kartınızın limitini aştınız. Mobil veya internet bankacılığınız ile kullanılabilir kart limitinizi artırabilirsiniz."
        },
    "54":
        {
            "errorcode": "54",
            "errormessage": "Kartınızın üzerinde yer alan tarih bilgisi ile ilgili bir sorun oluştu. Kartınızı aldığınız kuruluş bu işlemi son kullanma tarihi geçmiş, hatalı, süresi dolmuş kart işlemi olarak bildirdi."
        },
    "0054":
        {
            "errorcode": "0054",
            "errormessage": "Kartınızın üzerinde yer alan tarih bilgisi ile ilgili bir sorun oluştu. Kartınızı aldığınız kuruluş bu işlemi son kullanma tarihi geçmiş, hatalı, süresi dolmuş kart işlemi olarak bildirdi."
        },
    "10054":
        {
            "errorcode": "10054",
            "errormessage": "Kartınızın üzerinde yer alan tarih bilgisi ile ilgili bir sorun oluştu. Kartınızı aldığınız kuruluş bu işlemi son kullanma tarihi geçmiş, hatalı, süresi dolmuş kart işlemi olarak bildirdi."
        },
    "GWERROR_54":
        {
            "errorcode": "GWERROR_54",
            "errormessage": "Kartınızın üzerinde yer alan tarih bilgisi ile ilgili bir sorun oluştu. Kartınızı aldığınız kuruluş bu işlemi son kullanma tarihi geçmiş, hatalı, süresi dolmuş kart işlemi olarak bildirdi."
        },

    "ERR20054":
        {
            "errorcode": "ERR20054",
            "errormessage": "Kartınızın üzerinde yer alan tarih bilgisi ile ilgili bir sorun oluştu. Kartınızı aldığınız kuruluş bu işlemi son kullanma tarihi geçmiş, hatalı, süresi dolmuş kart işlemi olarak bildirdi."
        },
    "57":
        {
            "errorcode": "57",
            "errormessage": "Kartınızı çıkaran kuruluş tarafından bu işlem tipine onay verilmedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır.  Bu hata mesajına sebep olacak  bir çok senaryo olabilir. En sık karşılaşılan, kartınızın online işlem yetkilerini mobil veya internet veya telefon bankacılığı ile kontrol ettirmenizdir."
        },
    "0057":
        {
            "errorcode": "0057",
            "errormessage": "Kartınızı çıkaran kuruluş tarafından bu işlem tipine onay verilmedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır.  Bu hata mesajına sebep olacak  bir çok senaryo olabilir. En sık karşılaşılan, kartınızın online işlem yetkilerini mobil veya internet veya telefon bankacılığı ile kontrol ettirmenizdir."
        },
    "10057":
        {
            "errorcode": "10057",
            "errormessage": "Kartınızı çıkaran kuruluş tarafından bu işlem tipine onay verilmedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır.  Bu hata mesajına sebep olacak  bir çok senaryo olabilir. En sık karşılaşılan, kartınızın online işlem yetkilerini mobil veya internet veya telefon bankacılığı ile kontrol ettirmenizdir."
        },
    "GWERROR_57":
        {
            "errorcode": "GWERROR_57",
            "errormessage": "Kartınızı çıkaran kuruluş tarafından bu işlem tipine onay verilmedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır.  Bu hata mesajına sebep olacak  bir çok senaryo olabilir. En sık karşılaşılan, kartınızın online işlem yetkilerini mobil veya internet veya telefon bankacılığı ile kontrol ettirmenizdir."
        },

    "ERR20057":
        {
            "errorcode": "ERR20057",
            "errormessage": "Kartınızı çıkaran kuruluş tarafından bu işlem tipine onay verilmedi. Kartınızı üreten kuruluş güvenlik sebebi ile bu hata hakkında detaylı bilgi paylaşmamaktadır.  Bu hata mesajına sebep olacak  bir çok senaryo olabilir. En sık karşılaşılan, kartınızın online işlem yetkilerini mobil veya internet veya telefon bankacılığı ile kontrol ettirmenizdir."
        },
    "93":
        {
            "errorcode": "93",
            "errormessage": "Kartınız eticaret işlemlerine kapalıdır. Kartınızı internet alışverişlerine açtırmak için mobil uygulama veya internet veya telefon bankacılığını kullanarak kartınızı aldığınız kuruluş ile iletişime geçebilirsiniz."
        },
    "0093":
        {
            "errorcode": "0093",
            "errormessage": "Kartınız eticaret işlemlerine kapalıdır. Kartınızı internet alışverişlerine açtırmak için mobil uygulama veya internet veya telefon bankacılığını kullanarak kartınızı aldığınız kuruluş ile iletişime geçebilirsiniz."
        },
    "10093":
        {
            "errorcode": "10093",
            "errormessage": "Kartınız eticaret işlemlerine kapalıdır. Kartınızı internet alışverişlerine açtırmak için mobil uygulama veya internet veya telefon bankacılığını kullanarak kartınızı aldığınız kuruluş ile iletişime geçebilirsiniz."
        },
    "GWERROR_93":
        {
            "errorcode": "GWERROR_93",
            "errormessage": "Kartınız eticaret işlemlerine kapalıdır. Kartınızı internet alışverişlerine açtırmak için mobil uygulama veya internet veya telefon bankacılığını kullanarak kartınızı aldığınız kuruluş ile iletişime geçebilirsiniz."
        },

    "ERR20093":
        {
            "errorcode": "ERR20093",
            "errormessage": "Kartınız eticaret işlemlerine kapalıdır. Kartınızı internet alışverişlerine açtırmak için mobil uygulama veya internet veya telefon bankacılığını kullanarak kartınızı aldığınız kuruluş ile iletişime geçebilirsiniz."
        }
}

@app.route('/error/{error}', api_key_required=True, methods=['GET'], content_types=['application/json'])
def error(error):
    if error in ERRORS:
        return ERRORS[error]
    raise NotFoundError(error)
