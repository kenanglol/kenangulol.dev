---
title: "kenangulol.dev"
description: "Bu site: Ege haritası üstünde bir seyir defteri. Haritası ve çizimleri koddan üretiliyor, analitik ve izleme yok."
status: "sea"
years: "2026"
role: "Tasarım ve geliştirme"
stack: ["Hugo", "Python (NumPy, scikit-image)", "SVG", "CSS", "Cloudflare Workers", "Giscus"]
repo: "https://github.com/kenanglol/kenangulol.dev"
weight: 2
---

Okuduğunuz site. Yazılarımı, projelerimi ve kariyer rotamı tuttuğum bir seyir defteri olarak tasarlandı. Siteyi Claude ile birlikte tasarlayıp kurdum.

## Fikir

Site çoğunlukla uzun yazılardan oluşacağı için düz bir blog şablonu istemedim. Tema, uzun vadede yelken öğrenme ve Ege'de tekneyle yaşama hayalimden geliyor: her sayfa bir deniz haritasının parçası gibi.

- **Ana sayfa** bir Ege haritasıyla açılıyor: kıyı şeridi, adalar, derinlik eğrileri ve iskandil rakamları. Adım haritadaki deniz adları gibi seyrek aralıklı italik harflerle yazılı.
- **Yazılar** bir seyir defterindeki kayıtlar gibi listeleniyor: solda tarih, sağda başlık.
- **Projeler** durumlarına göre işaretli: kızakta (yapımı sürüyor), denizde (yayında), limanda (tamamlandı).
- **Rota** kariyerimi ve eğitimimi haritaya işlenmiş bir rota olarak gösteriyor: her iş yeri bir liman, bugünkü konum ışıklı.

## Tasarım

- **Renkler:** soğuk tonlu harita kâğıdı, derin su için CV'mdeki teal, zeytin yeşili ve gerçek deniz haritalarında fenerler ile şamandıralar için kullanılan macenta.
- **Yazı tipleri:** metin için uzun okumaya göre tasarlanmış Literata, menü ve etiketler için Barlow Semi Condensed. İkisi de sitenin kendi sunucusundan geliyor.
- **Çizimler:** her bölüm, eski haritaların kenarlarındaki kıyı görünüşleri gibi küçük bir çizimle açılıyor. Yazılarda pusula gülü ve seyir hattı var, projelerde kızaktaki bir yelkenli, rotada bir liman planı, bulunamayan sayfada bir deniz feneri. Fener, haritalardaki gibi "Fl(2) 10s" ritminde, yani on saniyede iki kez çakıyor.
- **Açık ve koyu tema:** site cihaz ayarını izliyor, sağ üstteki düğmeyle değiştirilebiliyor. Açık temanın zemini uzun okumada gözü yormasın diye hafif koyulaştırıldı.

## Teknik

- **Harita ve çizimler koddan üretiliyor.** Harita için Python ile bir yükseklik alanı oluşturuyorum, kıyıları ve derinlik eğrilerini scikit-image ile bu alandan çıkarıyorum. Sabit bir tohum değeri kullandığım için her derlemede aynı harita çıkıyor. Çizimler de Python ile SVG olarak yazılıyor. Renkleri CSS'ten aldıkları için temaya göre değişiyorlar.
- **Hugo** ile derleniyor. Türkçe varsayılan dil, İngilizce `/en/` altında. Çeviriler dosya adlarıyla eşleşiyor, dil düğmesi doğrudan sayfanın çevirisine gidiyor.
- **Cloudflare Workers** üzerinde yayında. `main` dalına yapılan her gönderim siteyi yeniden yayınlıyor, diğer dallar ayrı önizleme adreslerine çıkıyor.
- **Yorumlar** Giscus ile bu reponun GitHub Discussions bölümünde tutuluyor. Ayrıca bir sunucuya ya da veritabanına gerek yok.
- **Gizlilik:** analitik, çerez ya da izleme yok. Yazı tipleri dahil her şey sitenin kendi sunucusundan geliyor. Dışarıya giden tek istek, yazı sayfalarındaki yorum kutusu.
