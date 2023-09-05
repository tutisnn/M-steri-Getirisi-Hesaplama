import pandas as pd
import numpy as np




#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################
# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df=pd.read_csv("persona.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())

#Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
print(df["SOURCE"].nunique() )
print(   df["SOURCE"].value_counts() )

#Soru 3: Kaç unique PRICE vardır?
print(df["PRICE"].nunique() )

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
print(   df["PRICE"].value_counts() )


# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

print(   df["COUNTRY"].value_counts() )

print(df.groupby("COUNTRY")["PRICE"].count())



# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
print(df.groupby("COUNTRY").agg({"PRICE" : "sum"}) )

# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?
df["SOURCE"].value_counts()

#Soru 8: Ülkelere göre PRICE ortalamaları nedir
print( df.groupby("COUNTRY").agg({"PRICE" : "mean"})  )

#§ Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
print( df.groupby("SOURCE")["PRICE"].mean()  )

#Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
print(df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE" : "mean"})) 


#Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir
print(df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE" : "mean"})) 

#Görev 3:• Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df=df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE" : "mean"}).sort_values("PRICE",ascending=False)
print(agg_df.head())

#Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
print(agg_df.reset_index(inplace=True))

#Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz

bins=[0,19,24,31,41, agg_df["AGE"].max()]
mlabels= ['0_18', '19_23', '24_30', '31_40', '41_'+ str(agg_df["AGE"].max())]
agg_df["AGE_CAT"]=pd.cut(agg_df["AGE"],bins,labels=mlabels )
print(agg_df.head())

#Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız
# Yeni eklenecek değişkenin adı: customers_level_based
#Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.

agg_df["customers_level_based"]=agg_df[["COUNTRY","SOURCE","SEX","AGE_CAT"]].agg(lambda x: '_'.join(x).upper(),axis=1)
print(agg_df.head(20))

#Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız)


agg_df["SEGMENT"]=pd.qcut(agg_df["PRICE"],4,labels=["D","C","B","A"])
print(agg_df.head())
print(agg_df.groupby("SEGMENT").agg({"PRICE":["sum","max","mean"]}))

#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user="TUR_ANDROID_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"]==new_user])

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]






