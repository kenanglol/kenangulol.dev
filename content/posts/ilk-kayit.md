---
title: "Seyir defterine ilk kayıt"
date: 2026-11-17
description: "Bu site neden var ve burada neler yazacağım."
tags: ["site"]
---

Bir teknenin seyir defterine her gün aynı şeyler yazılır: tarih, konum, rüzgâr, ne yapıldığı. Tek bir kayıt sıradan görünür, ama defter dolunca bir yolculuk ortaya çıkar. Bu siteyi de öyle düşünüyorum.

Burada çoğunlukla şunlar hakkında yazacağım:

- Bankacılıkta eski sistemleri yeni mimarilere taşırken öğrendiklerim
- Ödeme sistemleri, provizyon akışları ve bunların arkasındaki tasarım kararları
- Yapay zekanın gerçek bir ürüne dönüşmesi: MCP sunucuları, LLM'ler ve hukuk

Kayıtlar kod da içerecek. Örneğin bu defterin bir kaydı Java'da şöyle görünürdü:

```java
record Kayit(LocalDate tarih, String baslik, Set<String> konular) {

    Kayit {
        Objects.requireNonNull(tarih, "Her kaydın bir tarihi olur");
        konular = Set.copyOf(konular);
    }
}
```

Yazıların altında yorum bırakabilirsiniz. Sorular ve itirazlar, katılmalardan daha çok işime yarar.
