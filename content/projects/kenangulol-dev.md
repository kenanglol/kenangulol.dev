---
title: "kenangulol.dev"
description: "Bu site: Ege haritası üstünde bir seyir defteri. Haritası ve çizimleri koddan üretiliyor."
status: "sea"
years: "2026"
stack: ["Hugo", "Python", "SVG", "Cloudflare Workers"]
repo: "https://github.com/kenanglol/kenangulol.dev"
weight: 2
---

Okuduğunuz site. Yazılarımı ve rotamı tuttuğum bir seyir defteri olarak tasarlandı.

- Ana sayfadaki deniz haritası her derlemede aynı çıkan, Python ile üretilmiş bir SVG. Kıyı şeridi, adalar ve derinlik eğrileri bir yükseklik alanından çıkarılıyor.
- Sayfalardaki çizimler (pusula gülü, kızaktaki tekne, liman planı, deniz feneri) de koddan çiziliyor ve açık ile koyu temaya göre renk değiştiriyor.
- Hugo ile derleniyor, Cloudflare Workers üzerinde yayınlanıyor. Yorumlar GitHub Discussions'ta tutuluyor, sitede analitik yok.
