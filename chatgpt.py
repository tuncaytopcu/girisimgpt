import os
import sys
import time
import openai

openai.api_type = "azure"
openai.api_key = "API_KEY" # Özel api key buraya eklenir
openai.api_version = "2023-03-15-preview"
openai.api_base = "https://girisimgpt.openai.azure.com/"

tanitimdosyasi = """HARCY
Girişim Adı: Harcy

Ekip:
Melih Gazi Küşüm - İşletme Mühendisi - Kurucu Ortak
Ahmet Haris Lala - Yüksek Mimar - Kurucu Ortak
Sektör: Cleantech, construction

Bulunulan Programlar:
İTÜ Çekirdek BIGG (TÜBİTAK 1512)
İTÜ Çekirdek Ön Kuluçka
İTÜ Çekirdek Enerjim Sensin Hızlandırma Programı
Lonca Kuluçka Merkezi
Zemin İstanbul

Şirket Özeti: Tekstil atıklarından binalarda kullanılmak üzere ısı yalıtım malzemeleri üretimi 

Problem: 
Tekstil atıklarının bertarafı problemi
Isı yalıtım malzemelerinin insan sağlığına ve doğaya zararlı malzemeler içermesi
Mevcut ısı yalıtım malzemelerinin maliyet problemi 

Çözüm: Tekstil atıklarından geri kazanım yolu ile daha uygun fiyatlı, sağlık ve çevre dostu bina ısı yalıtım malzemesi üretimi

Ürün:
Geri kazanılmış polyester yünü:
Uygun fiyat 
Sağlık ve çevre dostu 
Uygulama kolaylığı

Pazarlama Stratejisi:
Taş yününün daha uygun fiyatlı, sağlıklı ve çevre dostu alternatifi olmak 
XPS’in pazar payını hedeflemek

Kanallar: 
Birebir 
Satış Distribütör ve yapı marketler 
BIM Obje Pazar Yeri 
Yapı Fuarları

Rakip: 
Konvansiyonel Isı Yalıtım Malzemeleri: 
Taş yünü, Cam yünü ve XPS

Rekabet Avantajı:
Düşük maliyet 
Yüksek yalıtım değeri 
Uygulama Kolaylığı

Ulaşılan Sayılar:
14 firmadan niyet mektubu 
3 İşbirliği teklifi 
1 Ar&Ge Süreci 
1 Ön satış sözleşmesi

Hedef Pazar: Dünya Bina Yalıtımı Pazarı - 29,24 milyar USD

Müşteri Segmenti:
XPS kullanan müteahhit firmalar 
Doğa dostu projeler gerçekleştiren müteahhit firmalar
"""

systemPrompt = {"role":"system","content":f"""Sen HARCY girişimini tanıtan bir asistansın. Kullanıcı merhaba dediğinde kısaca girişimi anlat.
                Daha sonra kullanıcının sorularını yaratıcı bir şekilde cevapla.
                TANITIM DOSYASI:
                {tanitimdosyasi}"""}

def get_response(incoming_msg):
    data = []
    data.append({"role": "user", "content": incoming_msg})

    if len(data)<2:
        messages = [ systemPrompt ]
    else:
        messages = []

    response = openai.ChatCompletion.create(engine="girisimgpt", messages=messages, temperature=0.5)
    content = response["choices"][0]["message"]

    messages.extend(data)
    messages.append(content)
    return content["content"]
