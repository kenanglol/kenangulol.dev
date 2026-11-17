---
title: "Borsa tahmini için hibrit bir derin öğrenme modeli"
description: "Ege Üniversitesi bitirme tezim: ARIMA, yapay sinir ağı ve teknik göstergeleri birleştirerek hisse senedi ve endeks fiyatı tahmini. TÜBİTAK 2209-A desteğiyle."
status: "harbour"
years: "2021"
role: "Lisans tezi, Ege Üniversitesi"
stack: ["Python", "ARIMA", "Yapay sinir ağı (MLP)", "scikit-learn"]
weight: 4
---

Ege Üniversitesi Bilgisayar Mühendisliği'ndeki lisans tezim, Temmuz 2021'de Dr. Öğr. Üyesi Özgür Gümüş danışmanlığında tamamlandı. Verilerin ve hesaplama araçlarının bütçesi TÜBİTAK'ın 2209-A Üniversite Öğrencileri Araştırma Projeleri programından karşılandı.

## Problem

Borsa verisi bir zaman serisi, bu yüzden fiyat tahmininde hem ARIMA gibi istatistiksel modeller hem de yapay sinir ağları sık kullanılıyor. Literatürde ikisini birleştiren hibrit modeller var: seriyi doğrusal ve doğrusal olmayan iki parçaya ayırıp her parçayı ona uygun modele veriyorlar. Ben bu yapının üstüne, teknik analizde kullanılan göstergeleri de ekleyince tahmin başarısının nasıl değiştiğini inceledim.

## Model

1. Fiyat serisi Dickey-Fuller testinden geçene kadar fark alma ya da logaritma ile durağanlaştırılıyor.
2. Hareketli ortalama ile seri ikiye ayrılıyor: hareketli ortalamanın kendisi doğrusal kısım, ham veriyle arasındaki fark doğrusal olmayan kısım.
3. Doğrusal kısım ARIMA ile tahmin ediliyor.
4. Yapay sinir ağına şunlar birlikte veriliyor: ARIMA tahmini, doğrusal olmayan kısım, önceki günlerin ham değerleri ve seçilen teknik göstergeler. Ağın çıktısı nihai fiyat tahmini.

Günlük açılış, kapanış, en yüksek, en düşük ve hacim değerlerinden 42 teknik gösterge türettim. Hepsini birden vermek sonucu kötüleştirdi, hatta tek başına ARIMA'nın gerisinde kaldı. Bu yüzden scikit-learn'ün SelectKBest algoritmasıyla kapanış fiyatıyla en ilişkili göstergeleri seçtim. Beş veri setinin dördünde aynı göstergeler öne çıktı: VWAP, SMA12, EMA12, EMA26 ve Ichimoku. Sinir ağının parametreleri ızgara taramasıyla (grid search) belirlendi.

## Veri

Üç hisse senedi ve iki endeks, günlük verilerle:

- **FROTO** (Ford Otosan), 2016 – 2021
- **S&P 500**, 1997 – 2019
- **TUPRS** (Tüpraş), 2008 – 2021
- **XBANK** (BIST Banka endeksi), 2008 – 2021
- **YKBNK** (Yapı Kredi), 2006 – 2019

FROTO, TUPRS ve S&P 500 uzun vadede sürekli yükselen seriler; XBANK ve YKBNK ise yıllar içinde inip çıkan bir grafik çiziyor. Bu fark, modelin farklı karakterdeki serilerde de çalışıp çalışmadığını görmek için önemliydi.

## Sonuçlar

Önerilen modeli tek başına ARIMA, tek başına yapay sinir ağı, Zhang'in hibrit yöntemi ve Büyükşahin'in hibrit yöntemiyle karşılaştırdım. Diğer modelleri kendi makalelerindeki verilerle de çalıştırıp yayımlanan sonuçlarla örtüştüğünü kontrol ettim. Aşağıdaki tablo MAPE değerlerini gösteriyor; düşük olan daha iyi.

| Veri seti | ARIMA | ANN | Zhang | Büyükşahin | Önerilen |
|---|---:|---:|---:|---:|---:|
| FROTO | 2,22 | 2,41 | 1,72 | 0,71 | **0,55** |
| S&P 500 | 0,59 | 0,76 | 0,59 | 0,58 | **0,34** |
| TUPRS | 1,45 | 1,66 | 1,38 | 1,65 | **0,27** |
| XBANK | 1,69 | 1,90 | 1,67 | 1,82 | **0,48** |
| YKBNK | 1,38 | 1,62 | 1,56 | 1,62 | **0,20** |

Önerilen model beş veri setinin hepsinde, MAE, MSE ve MAPE ölçütlerinin üçünde de en düşük hatayı verdi. Fark en çok TUPRS ve YKBNK'te açıldı. Diğer modeller arasında sıralama Zhang'in yöntemi, ARIMA, Büyükşahin'in yöntemi ve tek başına yapay sinir ağı şeklinde oldu.

## Sınırları

- Başarının ana kaynağı teknik göstergeler. Bu da modeli hisse senedi ve endeks verisine bağlıyor; başka zaman serilerinde aynı avantajı sağlamaz.
- Göstergeleri hesaplamak için sadece kapanış fiyatı yetmiyor, açılış, en yüksek, en düşük ve hacim de gerekiyor. Bu yüzden model kısa vadeli tahmin için uygun, uzun vadeli tahmin yapamıyor.

Bir sonraki adım olarak, hibrit yapıdaki çok katmanlı algılayıcının yerine özyinelemeli sinir ağları (RNN, LSTM) kullanmanın başarıyı artıracağını düşünüyordum.
