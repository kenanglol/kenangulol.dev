---
title: "TickPilot"
description: "ABD hisselerinin canlı verisiyle çalışan, kararlarını risk kontrolünden geçiren ve işlemleri yalnızca kendi içinde simüle eden algoritmik portföy altyapısı."
status: "sea"
years: "2026 –"
stack: ["Python", "SQLite", "Docker", "GitHub Actions", "Alpaca API"]
weight: 2
---

TickPilot, alım satım stratejilerini gerçek para riske atmadan canlı piyasada denemek için kurduğum bir altyapı. Alpaca'dan ABD borsalarının anlık verisini alıyor, stratejilerin kararlarını bir risk kontrolünden geçiriyor ve emirleri yalnızca kendi içinde simüle ediyor; hiçbir aracı kuruma emir gitmiyor. Eylül 2026'dan beri bir sunucuda kesintisiz çalışıyor. Hedefim önce ABD piyasasında olgunlaştırmak, sonra Borsa İstanbul'a taşımak.

## Nasıl çalışıyor

Sistem üç servisten oluşuyor ve her biri kendi verisinin tek sahibi. market-data, Alpaca'ya bağlanan ve dış ağa çıkabilen tek servis: veriyi doğruluyor, akış bayatladığında ya da koptuğunda bunu bildiriyor ve 30 hissenin olaylarını sıralı bir günlüğe yazıyor. strategy-host bu günlüğü okuyup SMA kesişimi, RSI ve açılış aralığı kırılımı stratejilerini çalıştırıyor. Stratejiler yalnızca al ya da sat diyebiliyor, nakde ve pozisyona dokunamıyor. core ise risk kontrolünü, simüle emirleri ve muhasebe defterini yönetiyor. Her stratejinin 3.000 dolarlık ayrı bir sanal bütçesi var ve kâr-zararı ayrı izleniyor.

Bunların yanında kayıtlı bir seansı canlı sisteme dokunmadan hızlandırılmış olarak yeniden oynatan bir replay aracı, gece yedeklerinden günlük rapor üreten bir panel ve bir sorun sürdüğünde Telegram'dan haber veren bir izleme servisi var.

## Yaptıklarım

Servis sınırlarını ve bir kararın emre dönüşene kadar izlediği tek yolu tasarladım, önemli kararları dokuz mimari karar kaydında (ADR) yazılı tuttum. Canlı veri akışını, strateji eklenti yapısını, katmanlı risk motorunu ve yayın düzenini kurdum. Servisler salt okunur dosya sistemiyle ve dışarıya port açmadan çalışıyor; her sürüm commit SHA'sıyla yayınlanıyor ve sağlık kontrolünden geçemezse kendiliğinden bir önceki sürüme dönüyor.

En çok şey öğrendiğim kısım, canlı verinin tasarımı değiştirdiği yerler oldu. İlk altı seansta sinyallerin yaklaşık yarısı, stratejinin elinde olmayan hisseyi satmaya çalışıyordu. Bunun üzerine ne kadar alınacağı kararını stratejiden alıp risk bütçesine bıraktım. Altı seansın verisi sunucuda 18 GiB'ı geçince de veriyi sıcak ve arşiv katmanlarına ayıran bir yapı tasarladım.

Projede 150'yi aşkın commit, 48 pull request ve 570 test var. Claude Code ile geliştiriyorum; kaynak kodu şimdilik kapalı.
