---
title: "Kodlama asistanı deneyimlerim"
date: 2024-12-22
description: "GitHub Copilot ve Cursor ile çalışırken edindiğim izlenimler ve kodlama asistanlarının bugünkü sınırları."
tags: ["yapay-zeka", "araçlar"]
---

Yazılım mühendislerinden işlerini tek kelimeyle tanımlamalarını istesek çoğu insanın **kodlama** diyeceğini tahmin ediyorum. Yazılım geliştirmek özünde bir ya da birden çok probleme etkili çözümler üretmek olsa da kod yazmak ve sistemler kurmak, aktif çalışma saatlerimizin önemli bir kısmını kapsıyor. 2024 yılında bu sürecin geri dönülemez biçimde değiştiğini düşünüyorum. Bu değişimin en önemli parçası da hayatımıza giren kodlama asistanları.

ChatGPT'nin tüm dünyaya ücretsiz olarak sunulması insanları oldukça etkiledi. Kullanıcıların bir kısmı onu bir eğlence aracı olarak gördü ve kısa süre sonra ilgisini kaybetti. Kimisi hayatına entegre etti ve ufak araştırmalar için Google'ın reklam çöplüğünden kurtulmayı amaçladı. Yazılım dünyasının aklındaki ilk soru ise bu aracı kod geliştirme süreçlerine nasıl entegre edeceğimiz oldu. Çünkü bizim elimizde, farklı mesleklerden insanların sahip olmadığı çok önemli bir avantaj var: internet üzerinde hayatını sürdüren, yıllara yayılmış muazzam bir topluluk ve bilgi bankası. Bunların çoğu da halka açık durumda. Stack Overflow, GitHub gibi birçok site bir yazılımcı için oldukça fazla bilgi barındırıyor. Bu verilerin işlenmesi ve uygun kullanım senaryolarıyla chatbot uygulamalarının eğitiminde kullanılması sonucunda kısa sürede ürünler görmeye başladık.

## GitHub Copilot ve Cursor

Şüphesiz ki 2018 yılında GitHub'ın Microsoft tarafından satın alınması, yapay zeka uygulamaları çağına baktığımızda büyük anlam ifade ediyor. O zamanlar çoğu kullanıcı haklı olarak GitHub'ın bu satışının ürünü kötüye götüreceğini, kurumsallaşmayla budanacağını düşünüyordu. Ancak bugün geldiğimiz noktada GitHub aracılığıyla Microsoft kendisine yeni bir ürün katmayı başardı. GitHub Copilot'un kod asistanlarının ilk örneklerinden olmasının çeşitli avantajları var: pazarı erken domine etti ve bir kullanıcı kitlesi oluşturdu. Kendisine kullanıcı deneyimi açısından bir yol seçti, ve unutmamak lazım ki her seçim bir vazgeçiştir.

Cursor ise yola ufak çaplı bir startup olarak başladı ve kullanıcılara baştan itibaren alışık oldukları ve sevdikleri bir deneyim verebilmek için VS Code'un bir fork'u ile yoluna devam etti. Bunun üzerine kendi özelliklerini eklediler ve ortaya kullanıcı açısından özel bir deneyim çıktı.

## Benim deneyimim

Bu uzun anlatımdan sonra kendi deneyimlerime gelecek olursam, GitHub Copilot deneyimim ile Cursor deneyimimin aynı projeler üzerinde olmadığını söyleyerek başlayabilirim. Cursor'u ücretsiz olarak, daha özgür bir ortamda denedim. GitHub Copilot'u ise IntelliJ IDEA 2024 ve VS Code ile deneme şansı yakaladım. Her iki ürünün de kullanıcıya yardımcı olmak için tasarladığı senaryolar birbirinden biraz farklı olduğu için benim kullanım şeklim de üründen ürüne değişti. Copilot'u projelerde karşılaştığım bir probleme, yalnızca orayla sınırlı kalacak şekilde çözüm üretmesi için kullandım. Cursor'da yazarken ise belirli bir problemin değil, genel olarak projede yapmak istediğim kapsamlı bir değişikliği yazdırırken kullandım.

Cursor'da daha kapsamlı değişiklikler yapmasını istememin sebebi, bence Cursor'un birden çok dosyayı etkileyecek değişiklikleri yapmakta daha iyi olmasıdır. IDE'ye ekledikleri seçeneklerle asistanın sunduğu çözümü anında tamamen uygulayabilirsin ya da dosya dosya inceleyip evet/hayır diyerek de uygulayabilirsin. Bu özelliğin geliştirmeyi kolaylaştırdığını düşünüyorum. Çünkü ben genelde kodlama asistanını farklı bir yazılımcı, kendimi de onun kodunu inceleyip onay veren başka bir yazılımcı olarak senaryolaştırıyorum. Böylece yazdığı tüm kodların üzerinden geçiyor ve kendim çalışacağını düşünürsem onay veriyorum.

## Yazılımcılar tarihe mi karışıyor?

Asistanların yeteneklerinin artmasıyla birçok kişi artık kodlamayı bilmeyenlerin de hayal ettikleri projeleri bu asistanlara yazdırabileceklerini düşündü. Sürekli sorun çıkaran, teslim tarihini kaçıran, isteklere olmaz diyebilen yazılımcılardan kurtulacağı için umutlanmış olmalılar. Üretilen içeriklerde büyük puntolarla "YAZILIMCILAR TARİHE KARIŞIYOR" gibi başlıklar atıldığını gördük. Ancak ben bunun henüz olmadığını düşünüyorum. Bana bu hissi veren de asistanlarla olan deneyimlerim.

Bir geliştirme isteyene ve çalışan doğru cevabı alana kadar her şey çok güzel. Ancak asistanın size vermiş olduğu kodları uygulayıp çalıştırdığınızda hata aldığınız oldu mu? İşte o durumda kodlamayı bilmeyen biri, antik dilde tabletlere bakan turistler kadar çaresiz kalır. Çünkü bu asistanların sizin için kod yazıyor olması, her şeyi tamamen sizin istediğiniz gibi doğru ve eksiksiz yapacağı anlamına gelmez. Hatayla karşılaştığınızda, diyelim ki şanslısınız ve loglardan hatayı tespit ettiniz ve bu hatayı asistana söylediniz. İşte bu noktada hâlâ bir gelişim alanı olduğunu düşünüyorum. Asistanlar kod yazmak için tasarlanmış. Hataları anlamlandırmak ve yeni çözüm sunmak konusunda o kadar da başarılı olduklarını düşünmüyorum. Buradan sonra asistana bağlı kalmaya devam etmekte ısrar ederseniz ve şanslıysanız çalışan bir kod elde edersiniz. Yoksa muhtemelen arka arkaya alınan hatalardan sonra bir yerde saçma cevaplar verecek ya da aynı cevaplarda ısrarcı olacak.

Hata sonrası başarılı bir çözüm önermesi de sorunları tam anlamıyla çözmüş olmuyor. Çünkü önceki hatalı çözümlerin uygulanmasından sonra ortaya çalışsa bile düzeni bozulmuş, hangi parçasının işe yaradığı belli olmayan bir kara kutu çıkmış oluyor. Bu da yazılan kodların kalitesini düşürüyor. Bu düşünce yalnızca benim değil, yapılan araştırmaların da sonucu. [Uplevel'ın yaptığı araştırmada](https://betanews.com/2024/09/17/genai-tools-dont-increase-coding-efficiency) Copilot'un kullanıcılar açısından verimlilikte hiçbir artış sağlamadığı, ancak hata oranını yüzde 41 artırdığı görülmüş.

## Yarış sürüyor

Asıl konumuz olan Copilot ve Cursor'a dönecek olursak, orada da yeni gelişmeler var. Yukarıda bahsettiğim araştırma ve karamsar düşünceler, bu araçların kötü olduğunu düşündüğüm anlamına gelmiyor. Çünkü bu yarışta henüz sona ulaşmış değiliz ve sektör yeni startup'lar ve araçlarla son sürat büyümeyi sürdürüyor. Geçen gün yapılan [Copilot güncellemesi](https://github.blog/news-insights/product-news/github-copilot-in-vscode-free/) ve GitHub kullanıcılarına ücretsiz Copilot kullanım imkânı verilmesi bu yarışta önemli bir hamleyi temsil ediyor. Hem ücretsiz seçenek geldi hem de Cursor'un alametifarikası olan, farklı chatbotları uygulama içinde kullanabilme seçeneği Copilot'a da gelmiş bulunuyor. VS Code'un bir fork'u olan Cursor'un bu hamlelerle nasıl başa çıkacağını ise gelecekte göreceğiz.

Yukarıda anlattıklarım, benim bu araçlarla olan deneyimlerimin bir sonucu. Gelecekte bizi nelerin beklediği ise ayrı bir konu. *Yapay zeka eldeki kaynaklarla ulaşabileceği en üst platoya ulaştı mı? Asistanlar daha fazla gelişirlerse cidden kodlamayı bitirecekler mi?* gibi sorular hâlâ geçerliliğini koruyor. Şimdilik bekleyip görmek ve gelişmeleri yakından takip ederek adapte olmanın bir yazılımcı için en iyi seçenek olduğunu düşünüyorum.

---

*Bu yazı ilk olarak 22 Aralık 2024'te [LinkedIn'de](https://www.linkedin.com/pulse/kodlama-asistan%C4%B1-deneyimlerim-kenan-g%C3%BClol-pk8of/) yayımlandı.*
