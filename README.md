# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

## İş Problemi

Bir oyun şirketi, müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona) oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

Örneğin: Türkiye'den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.

## Veri Seti Hikayesi

"Persona.csv" veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

- **Price:** Müşterinin harcama tutarı
- **Source:** Müşterinin bağlandığı cihaz türü
- **Sex:** Müşterinin cinsiyeti
- **Country:** Müşterinin ülkesi
- **Age:** Müşterinin yaşı

################# Uygulama Öncesi #####################

  |  PRICE  |  SOURCE  |   SEX   | COUNTRY |  AGE  |
| ------- | -------- | ------- | ------- | ---- |
|   39    | android  |  male   |   bra   |  17  |
|   39    | android  |  male   |   bra   |  17  |
|   49    | android  |  male   |   bra   |  17  |
|   29    | android  |  male   |   tur   |  17  |
|   49    | android  |  male   |   tur   |  17  |


################# Uygulama Sonrası #####################

  | customers_level_based       |    PRICE   | SEGMENT |
| -------------------------- | ---------- | ------- |
| BRA_ANDROID_FEMALE_0_18    | 1139.80000 |    A    |
| BRA_ANDROID_FEMALE_19_23   | 1070.60000 |    A    |
| BRA_ANDROID_FEMALE_24_30   |  508.14286 |    A    |
| BRA_ANDROID_FEMALE_31_40   |  233.16667 |    C    |
| BRA_ANDROID_FEMALE_41_66   |  236.66667 |    C    |

