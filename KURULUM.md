# Kurulum notları

Siteyi yayına almak ve yönetmek için gereken adımlar. Sırayla gitmek en kolayı.

## 1. Cloudflare'e bağlama

1. Cloudflare panelinde **Workers & Pages → Create → Import a repository** yolunu izle.
2. GitHub bağlantısı istendiğinde **Cloudflare Workers and Pages** uygulamasını kur. Erişim için **Only select repositories** seçip sadece `kenangulol.dev` reposunu ver.
3. Repoyu seç ve kurulum ekranını şöyle doldur:
   - **Build command:** `hugo --gc --minify`
   - **Deploy command:** `npx wrangler deploy` (varsayılan, dokunma)
   - **Preview command:** `npx wrangler preview` (varsayılan, dokunma)

   Yayınlanan klasör (`public/`) `wrangler.jsonc` dosyasından okunur. Aynı dosya, build command boş kalsa bile her yayından önce siteyi derler.
4. Aynı ekranda **Advanced settings → Build variables** altına şu değişkeni ekle (sonradan projenin **Settings → Build** bölümünden de eklenebilir):
   - `HUGO_VERSION` = `0.170.0`

   Cloudflare'in derleme ortamında Hugo kurulu geliyor ama eski bir sürüm. Bu değişken sitenin geliştirildiği sürümü kullanmasını sağlar.
5. İlk derleme bitince site `kenangulol-dev.<hesap-adın>.workers.dev` adresinde açılır.

Bundan sonra `main` dalına yapılan her `git push` siteyi otomatik olarak yeniden yayınlar.

## 2. Alan adı

1. `kenangulol.dev` alan adını **Cloudflare Registrar** üzerinden al.
2. Worker'ın ayarlarında **Domains & Routes → Add → Custom domain** ile `kenangulol.dev` ekle. HTTPS sertifikası otomatik gelir.
3. İstersen `www.kenangulol.dev` adresini de ekleyip ana alana yönlendirebilirsin.

## 3. Yorumlar (Giscus)

1. Bu reponun **Settings → General → Features** bölümünden **Discussions** özelliğini aç.
2. [github.com/apps/giscus](https://github.com/apps/giscus) adresinden Giscus uygulamasını kur, yine sadece bu repoya erişim ver.
3. [giscus.app](https://giscus.app) sayfasında:
   - Repository: `kenanglol/kenangulol.dev`
   - Page ↔ Discussions mapping: **pathname**
   - Discussion category: **Announcements** (yeni tartışmayı sadece sen açabilirsin, ziyaretçiler yorum yazar)
4. Sayfanın ürettiği koddaki `data-repo-id` ve `data-category-id` değerlerini `hugo.toml` içindeki `[params.giscus]` bölümüne yaz:

   ```toml
   repoId = "R_..."
   categoryId = "DIC_..."
   ```

Bu iki değer boş kaldığı sürece yorum kutusu sayfaya hiç eklenmez, site yine çalışır.

## 4. Kişisel bilgiler

Sitede iletişim için yalnızca e-posta, LinkedIn ve GitHub var. Telefon numarası, adres ve yaşanan şehir bilerek yazılmıyor; CV de PDF olarak paylaşılmıyor. Herkese açık bir sayfada bu bilgiler spam ve arama robotlarına açık olur. CV'yi isteyen kişiye doğrudan gönder.

## 5. Yazı yazma

Her yazı `content/posts/` altında bir Markdown dosyasıdır. Türkçe sürüm `ad.md`, İngilizce sürüm `ad.en.md` olur. İki dosyanın adı aynı olduğunda site bunları birbirinin çevirisi sayar ve dil düğmesi doğru sayfaya gider.

```markdown
---
title: "Yazının başlığı"
date: 2026-12-01
description: "Listede başlığın altında görünen tek cümlelik özet."
tags: ["java", "ödeme sistemleri"]
draft: true
---

Yazı burada başlar.
```

- `draft: true` olan yazı yayınlanmaz. Hazır olunca bu satırı sil.
- İngilizce sürümde adresin İngilizce olması için `slug: "post-title"` ekleyebilirsin.
- Bir yazıyı tek dilde yazmak sorun değil. Sadece o dilin listesinde görünür.
- Yazmadan önce yerelde görmek için: `hugo server -D` ve tarayıcıda `http://localhost:1313`.

Yeni bir yazı eklemek için `content/posts/` altına bir Markdown dosyası aç; mevcut yazıları örnek olarak kullanabilirsin.

## 6. Projeler ve rota

- Her proje `content/projects/` altında bir dosyadır (`ad.md` ve `ad.en.md`). Türkçe adres `/projeler/ad/` olur.
- Projenin durumu `status` alanıyla belirlenir: `slip` (kızakta, yapımı sürüyor), `sea` (denizde, yayında), `harbour` (limanda, tamamlandı). Sıralama `weight` ile yapılır.
- `stack` kullanılan teknolojilerin listesidir, `repo` doldurulursa sayfada **Kaynak kodu** düğmesi çıkar.
- Kariyer ve eğitim `content/rota.md` ve `rota.en.md` dosyalarındaki `ports` listesindedir. Her liman bir iş yeri ya da okuldur; dosyada eskiden yeniye yazılır, sayfada en yenisi en üstte gösterilir. `current: true` olan şu anki konum olarak işaretlenir. Eski `/cv/` adresi Rota sayfasına yönlendirir.

## 7. E-posta (isteğe bağlı)

Cloudflare **Email Routing** ile `iletisim@kenangulol.dev` gibi bir adresi Proton adresine yönlendirebilirsin. Sonra `hugo.toml` içindeki `email` değerini yeni adresle değiştir.

## 8. Çizimler

Ana sayfadaki haritayı `tools/make_chart.py`, sayfalardaki çizimleri (pusula gülü, kızaktaki tekne, liman planı, deniz feneri) `tools/make_vignettes.py` üretir. `python tools/make_vignettes.py` çizimleri `assets/img/vignettes/` klasörüne yeniden yazar.

Harita için: Farklı bir kıyı şeridi istersen:

```sh
pip install numpy scikit-image
python tools/make_chart.py --seed 7
```

Komut `assets/img/chart.svg` dosyasını yeniden yazar. İsim yazısının durduğu alt bölge her zaman açık deniz olarak bırakılır.
