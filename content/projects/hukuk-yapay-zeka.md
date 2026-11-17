---
title: "turkhukuku.org"
description: "Türk hukukuna özel bir yapay zeka asistanı: avukatların dava, duruşma ve evrak takibini Türk hukukuna özel bir yapay zekayla aynı masaüstü uygulamasında birleştiren bir girişim."
status: "slip"
years: "2026 –"
role: "Kurucu ortak ve yazılım mimarı"
stack: ["Tauri", "React", "TypeScript", "PostgreSQL", "pgvector", "Python", "MCP"]
weight: 1
---

turkhukuku.org, avukatlarla yazılımcıların birlikte kurduğu, henüz yayınlanmamış bir legal-tech girişimi. Bugün avukatlar dosya takibini bir yerde, içtihat ve mevzuat araştırmasını başka yerlerde yapıyor. Biz bunları tek bir masaüstü uygulamasında topluyoruz: her dava evrakları, duruşmaları ve notlarıyla kendi çalışma alanı oluyor, yapay zeka da o davanın bağlamında, kanun maddesi ve emsal kararla desteklenmiş cevaplar veriyor. Bilmediği bir şeyi tahmin etmiyor, soruyor.

Projede kurucu ortak ve yazılım mimarıyım; mimari kararlar, veri hatları, yapay zeka altyapısı ve yayın süreci bende. Kamuya açık hukuk verisi için iki hat kurduk. İlki on milyonu aşkın yargı kararını atıf analiziyle en etkili olanlara indiriyor, kişisel verileri temizliyor ve yüz binlerce parçayı hibrit aramaya açıyor; sorgu planındaki tek bir düzeltmeyle arama süresi dakikalardan milisaniyelere indi. İkincisi Türk mevzuatının tamamını madde, fıkra ve bent düzeyinde, sürümleriyle birlikte bir veritabanına dönüştürüyor. Avukatların "önce madde, sonra karar" isteği bu veri modelini doğrudan belirledi.

Masaüstü uygulaması Tauri ve React ile yazıldı ve kendini otomatik güncelliyor. Gizlilik ilk günden mimarinin parçası: müvekkil ve dava verisi model eğitiminde kullanılmayacak, bu veriyle çalışan yapay zeka Türkiye'de çalışacak.

Geliştirmede Claude'u yakından kullanıyorum. Planlama ve doğrulamayı güçlü model yapıyor, mekanik toplu işleri daha ucuz bir model; ucuz modelin çıkardığı sayıları her seferinde kodla yeniden sayıyoruz.
