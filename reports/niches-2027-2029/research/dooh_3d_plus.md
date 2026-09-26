# Поток 5 — ДОПОЛНЕНИЕ (top-up): DOOH, 3D-экраны, FOOH

Дата: 2026-09-26. Дополняет файл `dooh_3d.md`. Неизменённое содержание оригинала здесь не повторяется.

> **Как собирались данные.** В этом раунде сделано ~38 веб-поисков; после них общий лимит сессии (200 запросов) был исчерпан. WebFetch и curl к целевым сайтам (aescripts.com, fooh.com, worldooh.org, higgsfield.ai) блокирует прокси (проверено: 403 CONNECT, 2026-09-26). Поэтому цифры взяты из поисковых сниппетов с указанных страниц, из GitHub (доступен напрямую) и из MCP-каталогов Magnific и Higgsfield (запросы 2026-09-26).
>
> Уверенность по источникам:
> - **Высокая** — WOO, OAAA, официальные релизы.
> - **Средняя** — агентские гайды по ценам.
> - **Низкая** — блоги студий со «статистикой» без методологии.
>
> Мои расчёты помечены «оценка».

---

## Проверено и исправлено

### 1. Доля programmatic DOOH — в оригинале ОШИБКА (завышена)

В оригинале (п. 10) со ссылкой на слабый агрегатор amraandelma было «~$2,4 млрд в мире, programmatic ≈ 9–10% DOOH».

Это **неверно.** Первое глобальное исследование WOO Global pDOOH Expenditure Study (данные 12 SSP, агрегировал PwC, 40+ рынков) даёт другие цифры:
- **$1,339 млрд за 2025 год, то есть 7,0% мирового DOOH** ([invidis](https://invidis.com/news/2026/09/research-analysis-woo-puts-global-programmatic-dooh-spend-at-us1-34-billion/), 2026-09; [WOO](https://www.worldooh.org/news/woo-global-pdooh-spend-study-2025), 2026; [Brand Communicator](https://brandcom.ng/2026/09/16/global-programmatic-dooh-market-reached-1-339-billion-in-2025-inaugural-woo-study-finds/), 2026-09-16).
- Предварительная цифра, объявленная в июне, была «$1,4 млрд» ([invidis](https://invidis.com/news/2026/06/dooh-woo-study-reveals-1-4-billion-global-programmatic-dooh-market/), 2026-06).

Разбивка по регионам ([The Media Online](https://themediaonline.co.za/2026/09/global-programmatic-dooh-market-reaches-1-339bn-with-emea-leading-adoption/), 2026-09; [WOO](https://www.worldooh.org/news/woo-global-pdooh-spend-study-2025)):

| Регион | pDOOH 2025 | Доля programmatic в DOOH региона | Комментарий |
|---|---|---|---|
| Americas | $667 млн (~50% мирового pDOOH) | 14,1% | Из них США — $545,5 млн |
| EMEA | $521 млн | — | Лидер по проникновению: в Германии 31,8% |
| **APAC** | **$151 млн** | **1,7%** | **61% регионального объёма приходится на Австралию и Новую Зеландию** |
| Восточная Азия (JP/KR/CN) | — | **0,6%** | База DOOH — $7,3 млрд |

**Вывод, существенный для основателя.** В Азии, кроме ANZ, **>98% DOOH продаётся напрямую, а не через программатик.** Премиальные и 3D-экраны ЮВА в 2027–2028 годах будут продаваться через отношения с владельцами. Это **усиливает** ценность «отношений и данных об экранах» (идеи 2 и 5 оригинала) и **ослабляет** угрозу из сценария «Быстрый», где SSP продают 3D-слоты с авто-адаптацией креатива.

Цифра eMarketer (~$1,23 млрд pDOOH в США на 2026 год) методологически несравнима с WOO: у WOO США = $545,5 млн за 2025 год. Для решений использовать WOO.

### 2. «Специализированный коммерческий плагин для анаморфа не найден» — в оригинале ОШИБКА

В оригинале (п. 36, идея 1) сказано, что коммерческих инструментов нет. На деле ниша **уже занята базовыми инструментами:**
- **aescripts «Naked-Eye 3D»** — скрипт для After Effects (ScriptUI-панель), который **подбирает камеру и «разворачивает» LED-экраны** для анаморфных 3D-билбордов. Анонс в соцсетях aescripts: TikTok-пост датирован ~2026-05-30 (дата вычислена из ID поста), обучающее видео — 2026-05-22 ([aescripts Facebook](https://www.facebook.com/aescripts/videos/new-naked-eye-3d-create-camera-matched-anamorphic-naked-eye-3d-billboard-scenes-/1994006781204015/), 2026-05; [aescripts TikTok](https://www.tiktok.com/@aescripts/video/7645827526098439438), 2026-05). **Цена — нет данных:** страница aescripts заблокирована прокси, сниппеты цену не показали.
- **aescripts «LED Architect»** — прямо в AE считает разрешение, раскладку панелей, число кабинетов, мощность и вес по **пресетам реальных поставщиков**. Генерирует композицию с направляющими и тестовыми оверлеями. Плавающая лицензия стоит **$99,99**, цена обычной — нет данных ([aescripts](https://aescripts.com/led-architect/), 2025–2026).
- **Бесплатные пиксель-мап-инструменты:** онлайн-генератор [Ghosteam Pixelmap Tool](https://www.ghosteaminc.com/pixelmap-tool/) для AE и Resolume; шаблон [DVizion LED Pixelmapper](https://dvizion.gumroad.com/l/ledpixelmapper) на Gumroad. На GitHub весной–летом 2026 появились навайбкоженные клоны: [avd-pixelmap](https://github.com/bburris81-cmyk/avd-pixelmap) (2026-04) и [led-test-patterns](https://github.com/oisinryan/led-test-patterns) (2026-08). Та же динамика клонов, что у Oblique.
- **Maxon** официально обучает анаморфу в Cinema 4D: статья «Creating 3D Anamorphic Billboards with Maxon One» и доклад Noseman на NAB 2025 ([Maxon](https://www.maxon.net/en/article/creating-3d-anamorphic-billboards-with-maxon-one), 2025; [Novedge/NAB 2025](https://novedge.com/blogs/design-news/nab-2025-noseman-how-to-make-3d-anamorphic-billboards-in-cinema-4d), 2025). Сетап камеры — задокументированный навык, а не тайное знание.
- **Blender (Superhive, бывший Blender Market):** по запросу «anamorphic billboard / LED corner» находятся только инструменты анаморфных *объективов* — Lens Sim, LensMode, Pro Lens, Jackimorphic Camera Pack. **Специализированного аддона под анаморфные LED-экраны в выдаче нет** ([Superhive](https://superhivemarket.com/products/lens-sim?num=2), 2026-09). Это возможная ниша, но маленькая.

**Итог:** идея «плагин-превиз как продукт» в оригинале переоценена. Слой кода уже коммодитизирован, как и с Oblique. Защищаемым остаётся только слой **данных о конкретных экранах** (см. «Идеи»).

### 3. Каталог 3D-экранов FOOH.com — цифра в оригинале УСТАРЕЛА

Оригинал: «64 экрана при запуске». Сейчас в директории **138–139 DOOH-экранов в 63 городах** ([FOOH.com Screens Directory](https://fooh.com/directories/screens), 2026-09). Среди них:
- Сингапур — The Heeren;
- Милан — Pattari 2, угловой экран на Piazza XXV Aprile, экран Urban Vision на фасаде Дуомо;
- Найроби — Westlands;
- Лас-Вегас — Mandalay Bay;
- несколько экранов Times Square.

([Heeren](https://fooh.com/screens/the-hereen-3d-billboard); [Pattari 2](https://fooh.com/screens/pattari-2-milan-3d-billboard/); [Piazza XXV](https://fooh.com/screens/piazza-xxv-corner-3d-billboard-milan/); [Duomo](https://fooh.com/screens/duomo-di-milano-3d-billboard); [Westlands](https://fooh.com/screens/westlands-3d-anamorphic-led-screen/); 2026.)

FOOH.com также проводит **FOOH Awards 2026: 21 победитель в 7 категориях** ([FOOH.com](https://fooh.com/), 2026). Главный конкурент идеи «SEA 3D Screen Atlas» **удвоил каталог за ~год** и строит сообщество.

### 4. Цены на медиа ЮВА-калькуляторы: «покрытие в ЮВА слабее» — ЧАСТИЧНО НЕВЕРНО

По запросам «harga sewa videotron Jakarta» уже ранжируются как минимум 6 гайдов от операторов и агентств:
- [transads.id](https://transads.id/berapa-harga-iklan-videotron-jakarta-panduan-lengkap-tarif-lokasi-premium-dan-cara-memilih-media-yang-tepat-bagian-1/);
- [Lestari Ads](https://www.lestariads.com/en/blog/dooh/berapa-sih-harga-sewa-videtron-kota-kota-besar-di-indonesia.html);
- [Wicaksana](https://www.wicaksanaindonesia.com/sewa-jasa-videotron-jakarta-2025/);
- [uno.id](https://uno.id/videotron-jakarta-media-iklan-digital/);
- [Firstboard](https://firstboard.com/id/id/blog/harga-billboard-indonesia);
- [nezzan](https://nezzan.edu.eu.org/harga-sewa-videotron-di-jakarta-murah/).

Все — 2025 года. С Дубаем то же: страницы о стоимости Burj Khalifa и Sheikh Zayed Road есть у leadsdubai, datamysite, outdooradvertisinguae и digitalspacedive. С Сингапуром тоже: TPM, marketingagency.sg, Blindspot, AdQuick (2026).

**Поправка к идее 6:** SEO-ниша «сколько стоит LED-реклама в [город]» в ЮВА и ОАЭ **занята самими операторами на местных языках**. Это не пустой рынок, как предполагал оригинал.

### 5. Стандарты: OpenOOH — ссылка в оригинале указывала на форк

Каноничный репозиторий — [openooh/venue-taxonomy](https://github.com/openooh/venue-taxonomy): 54 звезды, 40 форков, обновлён 2026-09-24. Поддерживает OpenOOH; в рабочей группе Vistar, Broadsign, Place Exchange и VIOOH. Актуальная версия — v1.1, в репозитории есть и v1.2.

Проверено по README: **полей для 3D- и анаморфных экранов, геометрии или точки обзора в таксономии нет.** Утверждение оригинала «отдельного стандарта для 3D не найдено» теперь **подтверждено**, а не просто «нет данных».

### 6. Пресеты Higgsfield «Billboard» / «Giant Product» — НЕ ПОДТВЕРЖДЕНЫ через MCP

В MCP-каталоге Higgsfield (2026-09-26) поиск по пресетам «billboard» дал **0 результатов** в галереях Viral и Marketing Studio. Поиск по приложениям Marketplace «billboard» и «3D» — тоже 0. По запросу «giant» нашлись пресеты **«Street colossus»** (субъект становится гигантом в городе) и **«Lacewalker»** («масштабные иллюзии для фэшн-кампаний и продуктовых шоукейсов»). Страницы higgsfield.ai/apps/billboard из оригинала, вероятно, существуют только в веб-интерфейсе. Факт «FOOH-эстетика = пресет одним кликом» **в целом верен**, но конкретные названия требуют ручной проверки.

**Тарифы Higgsfield (в оригинале «нет данных»)**, по данным на сентябрь 2026:

| План | Цена | Кредиты в месяц |
|---|---|---|
| Starter | $19/мес | 270 |
| Plus | $47/мес при оплате за год ($59 помесячно) | 1 200 |
| Ultra | $99/мес при оплате за год ($129 помесячно) | 3 000 |

([Creatify](https://creatify.ai/blog/higgsfield-pricing-(2026)-plans-and-what-you-ll-actually-pay), 2026-09.) Другие обзоры приводят $15 / $39 / $99 ([Layer3labs](https://www.layer3labs.io/guides/higgsfield-ai-pricing), 2026). Тарифы меняются часто, уверенность средняя.

### 7. EU AI Act, маркировка — в оригинале «сроки требуют проверки»; ПРОВЕРЕНО

- **Статья 50 применяется с 2026-08-02.** Штрафы — до €15 млн или 3% мирового оборота ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/transparency-rules-article-50/), 2026; [Stibbe](https://www.stibbe.com/publications-and-insights/the-ai-acts-transparency-obligations-rules-scope-and-timeline), 2026).
- **Определение deepfake включает контент, который «напоминает существующие… объекты, места, события» и ложно выглядит подлинным.** Это прямо описывает ИИ-FOOH на реальной локации: гигантский продукт на реальной улице Парижа.
- **AI Omnibus** даёт отсрочку по машинной маркировке **до декабря 2026** для генеративных систем, выведенных на рынок до 2026-08-02. Контент, опубликованный до 2026-08-02, ретроактивно маркировать не нужно.
- ЕК готовит **Code of Practice on Transparency of AI-generated Content** ([EC](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content), 2026).
- UK ASA: раскрытие факта использования ИИ **не лечит** вводящее в заблуждение сообщение ([ASA](https://www.asa.org.uk/news/disclosure-of-ai-in-advertising-striking-the-balance-between-creativity-and-responsibility.html), 2025–2026).
- Решений регуляторов именно по FOOH не найдено (нет данных).

**Следствие:** для ЕС-клиентов ИИ-FOOH теперь требует дисклеймера. Сигнал «регуляторной маркировки» из сценария «Медленный» уже **материализовался**, но спрос он не останавливает, а лишь добавляет шаг в процесс.

### 8. Прочее

- **MAGNA «+7% OOH в 2025»** в оригинале устарело. На странице MAGNA есть фраза «OOH — самый динамичный из традиционных медиа, **+10% до $36,2 млрд**, DOOH **+18%**», но период из сниппета **не ясен** ([MAGNA](https://magnaglobal.com/ad-forecast-media-innovation-to-propel-the-global-ad-market/)). Использовать как ориентир, не как факт.
- **Cross Shinjuku Vision:** sales sheet от 2025-04 подтверждает сетку ротации:
  - 15 с — 4 раза в час (68 в день);
  - 30 с — 2 раза в час (34 в день);
  - 60 с — 1 раз в час (17 в день).

  Отдельно тарифицируются доплаты за приём контента (¥50 000) и за управление live-трансляцией (¥100 000) ([sales sheet](https://shinjuku.xspace.tokyo/wp-content/uploads/2025/07/%E3%80%90%E3%82%AF%E3%83%AD%E3%82%B9%E6%96%B0%E5%AE%BF%E3%83%93%E3%82%B8%E3%83%A7%E3%83%B3%E3%80%91%E5%AA%92%E4%BD%93%E8%B3%87%E6%96%99-20250702%E4%BF%AE%E6%AD%A3.pdf), 2025-04/07). Тариф ¥800 000 за неделю в этом раунде повторно **не** проверен.
- **Piccadilly Lights:** официальная цена слота по-прежнему не опубликована. Новое: Landsec выставил остров Piccadilly («Lucent») на продажу с ориентиром **£450 млн**. Landsec сохраняет цифровую инфраструктуру на лизхолде на 250 лет и **95% чистого операционного дохода** ([CoStar](https://www.costar.com/article/402827887/us-hedge-fund-doubles-up-at-landsecs-450-million-piccadilly-lights-scheme), 2025–2026; [Completely Retail](https://news.completelyretail.co.uk/piccadilly-circus-island-site-handed-450m-price-tag), 2025). Под экраном открыта площадка для брендовых активаций ([Campaign](https://www.campaignlive.co.uk/article/landsec-creates-brand-experience-venue-piccadilly-lights/1865666), 2025). Иконические экраны — это инфраструктурный актив стоимостью сотни миллионов фунтов, и доступ к ним закрыт.
- **Не удалось перепроверить:** диапазон Times Square ($7–25 тыс. в неделю), прайс Coper/Tridimensi ($2–5 тыс.), цены Daktronics Creative Services, поисковый объём по ЮВА-запросам. Для них остаются оценки оригинала.

---

## Новые факты

### Рынок, 2026 год (ускорение, а не замедление)
1. **США, Q1 2026:** OOH — **$2,12 млрд (+7,1% г/г)**, рекорд для первого квартала. DOOH растёт на **+12,9%**, его доля — **36%**. В заголовке релиза прямо названы драйверы: «digital growth and **AI brands**» ([OAAA](https://oaaa.org/news/ooh-hits-new-first-quarter-high-as-revenue-reaches-2-12-billion-driven-by-digital-growth-and-ai-brands/), 2026-06-03; [GlobeNewswire](https://www.globenewswire.com/news-release/2026/06/03/3306111/0/en/ooh-hits-new-first-quarter-high-as-revenue-reaches-2-12-billion-driven-by-digital-growth-and-ai-brands.html), 2026-06-03).
2. **США, Q2 2026:** OOH — **$3,16 млрд**, впервые больше $3 млрд за квартал, **+10,7% г/г**. DOOH — **38,4%** выручки, **+18,5% г/г** ([PPC Land](https://ppc.land/us-out-of-home-revenue-tops-3-billion-for-first-time-up-10-7/), 2026; [Billboard Insider](https://billboardinsider.com/us-out-of-home-revenue-up-9-percent-in-2q-2026/), 2026). В заголовке Billboard Insider стоит «+9,2%» — расхождение с +10,7%, нужно сверить с первичным релизом OAAA. Расчёт от базы Q2 2025 ($2,86 млрд) даёт ≈+10,5%.
3. OAAA публикует материал «From Coca-Cola to OpenAI, Brands Are Betting Bigger on OOH» ([OAAA](https://oaaa.org/news/from-coca-cola-to-openai-brands-are-betting-bigger-on-ooh/), 2026). **ИИ-компании стали крупными заказчиками наружки.** Это новый сегмент заказчиков спектакулярного и 3D-контента (оценка).

### Локации и цены медиа (закрывают «нет данных» оригинала)
4. **Дубай, Burj Khalifa (LED-фасад):** **AED 250 000 (~$68 тыс.) за 3-минутный показ** в будни с 20:00 до 22:00, **AED 350 000 (~$95 тыс.)** в выходные. Пакеты: AED 500 000 за два показа, **AED 1 млн за пять** показов с 19:00 до полуночи ([Arabian Business](https://www.arabianbusiness.com/industries/media/burj-khalifa-ad-cost), дата публикации н/д; те же цифры в гайдах 2026 — [Leads Dubai](https://www.leadsdubai.com/burj-khalifa-advertisement-cost/)). Оценка: **~$380 за секунду**; курс AED жёстко привязан, 3,6725/$.
5. **Дубай, Sheikh Zayed Road:** премиальные цифровые билборды стоят **AED 80–400 тыс.+ в месяц (~$22–109 тыс.)**, в целом по трассе — AED 35–300 тыс.+ за локацию в месяц. Трафик — 200 тыс.+ машин в день ([outdooradvertisinguae](https://outdooradvertisinguae.com/outdoor-advertising-rates-and-costs-on-sheikh-zayed-road-dubai/), 2026; [Digital Space Dive](https://digitalspacedive.com/billboard-advertising-dubai-abu-dhabi/), 2025–2026). Это агентские гайды, уверенность средняя. Отраслевая пресса пишет о волне naked-eye 3D от SZR до Downtown ([DigiComm](https://digicomm.ae/news/anamorphic-3d-led-dubai-2026/), 2026). Тарифы именно 3D-экранов — нет данных.
6. **Сингапур:** CPM — **от S$10 в programmatic до S$55+ на LED Orchard и Marina Bay**, активация — **от S$2 500** (~$1,9 тыс., оценка) ([AdQuick SG](https://www.adquick.com/dooh-advertising/singapore-sg), 2026). Премиальная статика на Orchard — S$15–35 тыс. в месяц ([TPM](https://theperfectmediagroup.com/billboard-advertising-rates-singapore/), 2026).
   - **ION Orchard Grand Façade LED (JCDecaux):** 189 м², Full HD, 2 млн пикселей, заявлена поддержка 3D, **1,35 млн viewable impressions в месяц**. Первый бренд-партнёр — **Tiffany & Co.** ([JCDecaux SG](https://www.jcdecaux.com.sg/news-and-press-releases/jcdecaux-singapore-and-ion-orchard-unveils-brand-new-ion-grand-facade-led)).
   - **The Heeren:** L-образный экран на 82 м², модернизирован под анаморф, работает с 8:00 до 23:00 ([TPM](https://theperfectmediagroup.com/heeren-orchard-led-screen-the-best-out-of-home-digital-in-the-vicinity/), 2026).
   - Местный 3D-продакшн: [Unicam Studio](https://www.unicamstudio.com/3d-anamorphic-video-singapore/).
7. **Бангкок:** на Siam Paragon и Siam Center работает «Tri 3D Anamorphic» — сдвоенные экраны с видом со входа Parc Paragon и с платформы BTS. Оператор **Plan B Media** заявляет «65 млн eyeballs в месяц» ([Plan B Media](https://www.planbmedia.co.th/ooh/digital/), 2026). **Тарифы не опубликованы** (нет данных).
8. **Джакарта:** средняя аренда videotron — **Rp 5–30 млн в месяц**. **Sudirman — Rp 200–500 млн в месяц (~$12–31 тыс.**; оценка по курсу ~16 300 IDR/$) ([transads.id](https://transads.id/berapa-harga-iklan-videotron-jakarta-panduan-lengkap-tarif-lokasi-premium-dan-cara-memilih-media-yang-tepat-bagian-1/), 2025; [Lestari Ads](https://www.lestariads.com/en/blog/dooh/berapa-sih-harga-sewa-videtron-kota-kota-besar-di-indonesia.html), 2025). Разброс ×2,5 внутри одной улицы.
9. **Бали (прокси):** ивентовая аренда LED — **Rp 3,5–11 млн в день** в помещении и **Rp 4,5–37 млн в день** на улице. Videotron в Табанане — Rp 2 млн за м² ([Mitra LED](https://www.mitra-led.com/sewa-led-videotron-p2-indoor-p2-5-p2-6-p2-9-videotron-wilayah-bali-denpasar-dan-sekitarnya.html), 2025; [86visualpro](https://86visualpro.com/sewa-led-videotron-bali/), 2025). Помесячных тарифов на рекламные DOOH-экраны Бали и данных о 3D-экранах на Бали **нет**. Вероятно, их либо нет, либо они не продвигаются онлайн (оценка).
10. **Стамбул:** Reklam Istanbul в начале 2024 года поставил **L-образный LED в порту Кадыкёй**. Из-за новизны формата **оператор создал собственную 3D-студию**, планирует ещё минимум один крупный 3D-экран и работает на Broadsign ([Broadsign](https://broadsign.com/blog/how-reklam-istanbul-is-building-turkeys-largest-digital-ooh-network-with-broadsign/), 2024–2025). Владельцы экранов на развивающихся рынках **вынуждены сами производить 3D-контент.** Для идеи 5 это и спрос, и риск: они строят in-house.
11. **Милан:** 3D-экраны у Piazza del Duomo — Urban Vision на боковом фасаде собора, изогнутый Pattari 2, угловой на Piazza XXV Aprile (FOOH.com, 2026; см. выше). Тарифы — нет данных.
12. **Сеул, COEX:** тариф K-POP Square по-прежнему не опубликован. Прокси: реклама COEX Brand Avenue стоит **от ₩9 000 000 без НДС** ([Cublic](http://www.cublic.co.kr/index.php/en/our-media/item/106-led-brandave-en), н/д).
13. **Токио, фанатская реклама.** У jeki (JR East Planning) есть отдельный продукт **«Cheering AD» (応援広告)** для Cross Shinjuku Vision: реклама, которую оплачивают фанаты в поддержку айдолов и персонажей ([jeki Cheering AD](https://cheering-ad.jeki.co.jp/en/products/cross-shinjuku-vision), 2026). Это **отдельный класс заказчика 3D-экранов, не бренды.** Объём рынка — нет данных.
14. **Self-serve DOOH:** Blindspot (TPS Engage, портфель Techstars) предлагает самостоятельную покупку DOOH с **оплатой за показ, бронированием по часам и без минимумов**. Заявлено **3 млн+ экранов в 50+ странах**, есть ИИ-планировщик «Blinky» и Pull API для владельцев экранов ([профиль API Evangelist на GitHub](https://github.com/api-evangelist/tps-engage), 2026-08; [Blindspot SG](https://seeblindspot.com/billboards-in-singapore/)). Нижний сегмент (SMB) закрывают self-serve-платформы.

### FOOH и ИИ-видео
15. **Цены FOOH, 2026:**
    - одна сцена — **~$2–8 тыс.**, мультишотная брендовая кампания — **$10–40 тыс.+** (так в источнике, помечено как оценка);
    - готовый FOOH для соцсетей — $4–15 тыс.;
    - Maverick Frame — от $1 800 (≈40 ч × $45).

    ([MAD CGI](https://www.madcgi.com/blog-posts/what-is-fooh-advertising-and-why-every-brand-needs-it-in-2026), 2026; [Maverick Frame](https://maverickframe.com/blog/what-is-fooh/), 2026.) На Fiverr есть гиг «naked-eye 3D для углового LED» за **$95** ([Fiverr opreston](https://www.fiverr.com/opreston/create-3d-anamorphic-illusion-for-corner-led-screen), 2026-09).
16. **Объём FOOH (низкая уверенность):** по блогу MAD CGI, в 2025 году в мире сделано **~1 872 FOOH-ролика**, медианный ролик набирает **~184 тыс.** органических просмотров ([MAD CGI](https://www.madcgi.com/blog-posts/what-is-fooh-advertising-and-why-every-brand-needs-it-in-2026), 2026). Методология не раскрыта. **Оценка:** при среднем чеке $2–8 тыс. рынок заказного FOOH — **~$4–15 млн в год**. Это очень маленький рынок для шаблонов и инструментов (низкая уверенность).
17. **ИИ-генераторы «билборд/FOOH» уже массовые:** [Artificial Studio Billboard Ad](https://app.artificialstudio.ai/tools/billboard-ad), [WaveSpeedAI Billboard Ad](https://wavespeed.ai/apps/ads/billboard-ad), prompt-приложение [PromptBase «Viral FOOH CGI Product Video»](https://promptbase.com/app/viral-fooh-cgi-product-video), пресеты Higgsfield (п. 6 выше); все 2026 года. Для мокапа в стоке есть шаблон [VideoHive «3D Billboard Mockup»](https://videohive.net/item/3d-billboard-mockup/53578416): изогнутый 3D-экран в городе, 4K, 20 с. Цена — нет данных.
18. **Технический потолок ИИ-видео для реальных 3D-экранов** (каталог Magnific MCP, 2026-09-26):
    - **Seedance 2.5** — до **30 с**, до **1080p**;
    - **Seedance 2.0** — до **4K**, 4–15 с;
    - соотношения сторон у всех рекомендованных моделей — **от 9:16 до 21:9** (ограничение входа — 0,4–2,5);
    - стоимость 15 с Seedance 2.5 в 1080p — **11 850 кредитов Magnific** (simulate_cost, точно). Пересчёт в $ — нет данных.

    **Вывод (оценка, средняя уверенность):** премиальные 3D-экраны нестандартны. У COEX 7840×1952 ≈ **4:1**, у Cross Shinjuku 19×7,2 м ≈ 2,6:1 плюс изгиб. **Ни одна массовая модель не выдаёт такую геометрию нативно** и не строит off-axis-проекцию. «Анаморф одним кликом под конкретный экран» в 2026 году невозможен без 3D- и композ-пайплайна. Барьер держится, пока модели не поддерживают соотношения >3:1, 8K и проекцию по заданной камере.

---

## Заполненные пробелы (по пунктам брифа)

| Пункт брифа | Было в оригинале | Что теперь известно |
|---|---|---|
| Programmatic share | $2,4 млрд / 9–10% (слабый источник) | **$1,339 млрд / 7,0%** (WOO+PwC); APAC 1,7%, Восточная Азия 0,6% |
| Рост DOOH 2026 | Прогнозы PQ Media и WOO | **Факт H1 2026 (США): DOOH +12,9% в Q1 и +18,5% в Q2**, доля 36% → 38,4% |
| Дубай | нет данных | Burj Khalifa — AED 250–350 тыс. за 3 мин; SZR digital — AED 80–400 тыс. в месяц |
| Сингапур | нет данных | CPM S$10–55+, активация от S$2 500; ION Grand Façade 189 м², 1,35 млн показов в месяц; Heeren L-образный 82 м² |
| Бангкок | нет данных | Siam Paragon/Center Tri 3D (Plan B); тарифы не опубликованы |
| Бали | нет данных | Только ивентовая аренда (Rp 4,5–37 млн в день на улице); рекламных 3D-экранов не найдено |
| Джакарта | Список операторов | Sudirman — Rp 200–500 млн в месяц (~$12–31 тыс.) |
| Стамбул | нет данных | L-образный экран Reklam Istanbul в Кадыкёе (2024) и собственная 3D-студия оператора |
| Милан | нет данных | 3 экрана с 3D у Duomo (Urban Vision и др.); тарифы — нет данных |
| COEX тарифы | нет данных | Нет данных; прокси — Brand Avenue от ₩9 млн |
| Инструменты для 3D-превиза | «Коммерческих нет» | **Есть:** aescripts Naked-Eye 3D (май 2026), LED Architect; бесплатные pixel-map-инструменты; VideoHive-мокап |
| Стандарт для 3D-экранов | нет данных | Подтверждено: в OpenOOH v1.1/v1.2 полей геометрии нет |
| Тарифы Higgsfield | нет данных | $19 / $47–59 / $99–129 в месяц (270 / 1 200 / 3 000 кредитов) |
| Каталоги 3D-экранов | FOOH.com — 64 | FOOH.com — **138–139 экранов, 63 города** |
| Маркировка ИИ-рекламы | «сроки требуют проверки» | Ст. 50 AI Act действует с 2026-08-02; отсрочка по маркировке до XII-2026 для систем, выпущенных до 2026-08-02 |
| Кто заказывает | Бренды, IP, ТЦ | Плюс **ИИ-компании** (OAAA 2026), **фан-сообщества** (jeki Cheering AD), **сами операторы** через in-house-студии |
| Поисковый объём по ЮВА | нет данных | Нет данных. Прокси: 6+ ценовых гайдов на бахаса по Джакарте (2025), то есть спрос есть и SERP занят |

---

## Обновлённые сценарии и сигналы

Новые данные меняют вероятности умеренно.

| Сценарий | Было | Стало | Почему |
|---|---|---|---|
| Базовый «3D — строка в прайсе» | 55% | **55%** | Подтверждается: DOOH ускоряется, премиум-3D в Азии продаётся напрямую |
| Быстрый «ИИ-анаморф за клик» | 25% | **30%** | **Слой инструментов коммодитизируется быстрее прогноза:** Naked-Eye 3D и LED Architect на aescripts, ИИ-видео до 30 с в 1080p. Но **медиа-сторона в Азии не автоматизируется** (pDOOH в APAC 1,7%), поэтому ускорение касается продакшна, а не продаж |
| Медленный «усталость от вау» | 20% | **15%** | Q2 2026 в США: DOOH +18,5%; WOO прогнозирует долю DOOH 49% в 2026. Маркировка ИИ (ст. 50) уже действует, но выглядит как процессный шаг, а не как стоп-фактор |

**Новые и уточнённые сигналы (что и как мониторить):**
1. **WOO pDOOH Study (ежегодно, сентябрь).** Порог: если проникновение programmatic в APAC вырастет с 1,7% до >5% к 2028, прямые отношения с владельцами обесцениваются, а каталоги уходят в DSP. Смотреть invidis и worldooh.org.
2. **Квартальные релизы OAAA.** База: DOOH +18,5% в Q2 2026. Два квартала подряд ниже +8% — сигнал медленного сценария.
3. **aescripts Naked-Eye 3D и клоны.** Раз в квартал проверять число аналогов на aescripts, Superhive и Gumroad, цены и появление «пресетов экранов». Если кто-то начнёт продавать **пакеты реальных экранов**, окно для идеи Spec Packs закрывается.
4. **Спецификации ИИ-видео.** Появление соотношений сторон >3:1, 8K и управления камерой или проекцией (image-to-video с заданной off-axis-камерой) в Seedance, Kling, Veo или Higgsfield означает, что «Быстрый» сценарий переходит в медиа-продакшн.
5. **Число экранов на FOOH.com.** База — 139, 63 города. Если к IX-2027 будет больше 300 и появятся ЮВА-экраны с ценами, SEA Atlas теряет смысл.
6. **Практика маркировки FOOH в ЕС:** финальный Code of Practice ЕК и первые кейсы санкций. Плюс ASA-решения по «фейковым» наружным кампаниям.

---

## Идеи-кандидаты: новые и уточнённые

### Уточнение 1. «Screen Twin Previz» → разворот в «Screen Spec Packs» (тип A, данные поверх чужих инструментов)
- **Что меняется:** плагин-превиз как самостоятельный продукт **не рекомендуется**. aescripts Naked-Eye 3D (май 2026) и LED Architect уже закрывают сетап камеры, развёртку и раскладку панелей; Maxon учит этому бесплатно. Повторяется ситуация Oblique: 2 конкурента превращаются в 6.
- **Новый формат:** платные **пакеты данных по реальным экранам** ($19–49 за экран или $99–199 за «город»; оценка). Внутри:
  - геометрия и развёртка граней;
  - pixel map;
  - высота и позиция точки обзора;
  - фото и видео плейта с точки обзора;
  - готовые сцены **под существующие инструменты:** AE с Naked-Eye 3D, C4D, Blender;
  - кодек и ограничения плеера;
  - сроки согласования.
- **Покупатель и боль:** фрилансеры с Fiverr ($70–600) и студии среднего сегмента. Им не хватает точных данных экрана: владельцы присылают PDF с ошибками или не присылают ничего.
- **Свидетельства спроса:** появление самого Naked-Eye 3D (aescripts видит спрос); LED Architect продаёт «пресеты поставщиков», значит, пресеты — ценность; FOOH.com публикует размеры и разрешения экранов, но не сцены. Прямых продаж spec-паков нигде не найдено (нет данных).
- **Конкуренты и цены:** Naked-Eye 3D (цена — нет данных); LED Architect (floating $99,99); бесплатные Ghosteam Pixelmap и DVizion; FOOH.com даёт базовые спеки бесплатно.
- **Моат:** данные, которые снимают на месте, и доступ к владельцам. Кодом это не копируется.
- **Главный риск:** правовой статус фото и спек (нужно согласие владельца экрана) и маленький TAM. В оригинале оценка: 500–1 500 3D-экранов вне Китая. Отдельный бизнес из этого, вероятно, $5–30 тыс. в год (оценка, низкая уверенность). Разумно только как **часть идеи 2**.

### Уточнение 2. «SEA 3D Screen Atlas» — усилено данными WOO, но с новым конкурентом
- **Новые доказательства:** проникновение programmatic в APAC — **1,7%**, значит, премиум продаётся через людей. В ЮВА тарифы **не публикуют**: Plan B (Бангкок), COEX, 3D-экраны Сингапура. В Джакарте разброс на одной улице — Rp 200–500 млн в месяц. Новые 3D-экраны: ION Orchard (JCDecaux), The Heeren, Siam Paragon/Center, Menara BCA, GI Kempinski, Pavilion KL.
- **Новые конкуренты:** FOOH.com (139 экранов, 63 города, есть Heeren); AdQuick SG/KL (городские гайды с CPM); Blindspot (self-serve, 3 млн+ экранов, оплата за показ); локальные операторы с SEO-гайдами на бахаса.
- **Уточнённая монетизация:** не SEO-трафик, а **RFQ и лиды в студию** плюс **платные spec-паки** (см. выше). Вход в рынок — **Индонезия** (основатель на Бали) и Сингапур, где 3D-экраны уже продают JCDecaux и TPM.
- **Главный риск:** FOOH.com расширяется на ЮВА быстрее; сделок мало (оценка — десятки в год на страну).

### Новая идея A. «Fan & IP 3D Ads» — продуктовая линия 3D-«поздравлений» для фан-сообществ и IP (тип A)
- **Суть:** фиксированный пакет «3D-анаморф-ролик на 15 с под конкретный экран + подача в оператора». Сценарии: день рождения айдола, юбилей аниме или персонажа, K-pop-камбэк. Шаблонные 3D-сцены адаптируются под 3–5 экранов: Cross Shinjuku, экраны Сеула, Джакарты и Бангкока.
- **Формат:** продуктовая услуга с фиксированной ценой, $500–2 000 за продакшн без медиа (оценка). Лендинг на японском, корейском, бахаса и тайском. Производство — через 3D-ассистентов студии.
- **Покупатель и боль:** фан-клубы и фан-менеджеры, которые уже покупают «cheering ads». У jeki есть отдельный продукт Cheering AD для Cross Shinjuku, на экранах крутятся IP-кампании вроде Chiikawa (оригинал, п. 17). Студийный кастом стоит $8–25 тыс. — фанатам это недоступно.
- **Свидетельства спроса:** продукт [jeki Cheering AD — Cross Shinjuku Vision](https://cheering-ad.jeki.co.jp/en/products/cross-shinjuku-vision) (2026); IP-кампании на 3D-экранах (оригинал). Объёма фан-рекламы и цен — **нет данных**.
- **Конкуренты и цены:** собственные креатив-службы операторов (jeki, Unica); локальные студии Японии и Кореи (цены — нет данных); Fiverr ($70–600) без знания конкретных экранов.
- **Моат:** шаблоны под конкретные экраны, знание правил модерации операторов (особенно японских), доверие в фан-сообществах, накопленная библиотека.
- **Главный риск:** права на изображения айдолов и персонажей (нужно одобрение агентства или правообладателя); языковой барьер; низкий чек при высокой доле ручной работы — противоречит лимиту 2–4 ч/нед. **Уверенность в идее — низкая.** Проверять через 5–10 интервью с организаторами фан-реклам.

### Новая идея B. «3D Content Kit для операторов с in-house-студией» (тип A, B2B-лицензия ассетов)
- **Суть:** это сдвиг идеи 5 оригинала. Операторы вроде Reklam Istanbul **сами создают 3D-студии**, когда запускают первый 3D-экран. Им нужны не готовые ролики, а **библиотека анаморф-ассетов и сцен**: окна, рамы, «аквариумы», объёмные частицы, погодные и праздничные лупы с параметрической геометрией экрана, в форматах C4D, Blender и AE (совместимо с Naked-Eye 3D). Плюс гайд по съёмке плейта и QA.
- **Формат:** годовая лицензия на оператора, $1–5 тыс. в год (оценка); обновления раз в квартал.
- **Покупатель и боль:** операторы на развивающихся рынках (Турция, ЮВА, Ближний Восток, Африка — Westlands в Найроби есть на FOOH.com). Они запускают 3D-экран без продакшн-экспертизы.
- **Свидетельства спроса:** кейс Reklam Istanbul (Broadsign, 2024–2025); у Daktronics есть подразделение Creative Services (оригинал); ТЦ сами запускали 3D-контент (Pavilion KL, оригинал). Цен на подобные лицензии — нет данных.
- **Конкуренты:** стоки (VideoHive, Envato) — в основном мокапы, а не анаморф-сцены; студии производителей LED.
- **Моат:** библиотека, накопленная на реальных проектах студии, и отношения с операторами.
- **Главный риск:** продажа B2B-лицензий занимает много времени; операторов с 3D-экранами — сотни, а не тысячи.

### Понижено в приоритете
- **Идея 6 (калькуляторы стоимости DOOH для ЮВА и Дубая):** SERP уже занят гайдами операторов на местных языках (п. 4 раздела «Проверено»). Переходит из «отдельной ставки типа B» в **«только как SEO-страницы внутри SEA Atlas»**.
- **Идея 7 (FOOH Kit):** рынок заказного FOOH, вероятно, всего ~$4–15 млн в год (оценка, низкая уверенность). ИИ-генераторы доступны от $19 в месяц, в ЕС действует маркировка deepfake. Имеет смысл только как контент-маркетинг студии.
- **Идея 3 (DOOH Export Doctor):** бесплатные пиксель-мап-инструменты уже есть (Ghosteam, клоны на GitHub 2026). Остаётся бесплатной воронкой.
- **Идея 4 (In-Situ 3D Pitch):** появились дешёвые стоковые мокапы (VideoHive «3D Billboard Mockup») и ИИ-генераторы билбордов. Защищён только вариант с **точными цифровыми двойниками реальных экранов**, то есть это снова продолжение идеи 2.

**Итог для портфеля:** единственный защищённый актив в этом потоке — **полевые данные о реальных 3D-экранах ЮВА и доступ к их владельцам**. Все продукты-«обёртки» — плагин, мокап, калькулятор, FOOH-шаблоны — копируются за месяцы и уже имеют конкурентов. Если основатель идёт в этот поток, ставка одна: SEA Atlas плюс Spec Packs плюс заказы студии, а не отдельные инструменты.

---

## Источники

1. invidis — WOO: global pDOOH $1.34bn. https://invidis.com/news/2026/09/research-analysis-woo-puts-global-programmatic-dooh-spend-at-us1-34-billion/ (2026-09)
2. WOO — Global pDOOH Spend Study 2025. https://www.worldooh.org/news/woo-global-pdooh-spend-study-2025 (2026)
3. invidis — WOO study reveals $1.4bn pDOOH. https://invidis.com/news/2026/06/dooh-woo-study-reveals-1-4-billion-global-programmatic-dooh-market/ (2026-06)
4. The Media Online — pDOOH $1.339bn, EMEA leads. https://themediaonline.co.za/2026/09/global-programmatic-dooh-market-reaches-1-339bn-with-emea-leading-adoption/ (2026-09)
5. Brand Communicator — pDOOH $1.339bn. https://brandcom.ng/2026/09/16/global-programmatic-dooh-market-reached-1-339-billion-in-2025-inaugural-woo-study-finds/ (2026-09-16)
6. Media-Marketing — pDOOH growth not in the West. https://www.media-marketing.com/en/news/programmatic-dooh-is-worth-1-339-billion-and-its-greatest-growth-opportunity-is-not-in-the-west/ (2026-09)
7. OAAA — Q1 2026 $2.12B. https://oaaa.org/news/ooh-hits-new-first-quarter-high-as-revenue-reaches-2-12-billion-driven-by-digital-growth-and-ai-brands/ (2026-06-03)
8. GlobeNewswire — Q1 2026 OAAA release. https://www.globenewswire.com/news-release/2026/06/03/3306111/0/en/ooh-hits-new-first-quarter-high-as-revenue-reaches-2-12-billion-driven-by-digital-growth-and-ai-brands.html (2026-06-03)
9. PPC Land — US OOH tops $3B in Q2 2026, +10.7%. https://ppc.land/us-out-of-home-revenue-tops-3-billion-for-first-time-up-10-7/ (2026)
10. Billboard Insider — US OOH up 9.2% in 2Q 2026. https://billboardinsider.com/us-out-of-home-revenue-up-9-percent-in-2q-2026/ (2026)
11. OAAA — From Coca-Cola to OpenAI. https://oaaa.org/news/from-coca-cola-to-openai-brands-are-betting-bigger-on-ooh/ (2026)
12. MAGNA — Ad forecast (OOH +10%, DOOH +18%; период не ясен). https://magnaglobal.com/ad-forecast-media-innovation-to-propel-the-global-ad-market/ (н/д)
13. aescripts — Naked-Eye 3D (Facebook video). https://www.facebook.com/aescripts/videos/new-naked-eye-3d-create-camera-matched-anamorphic-naked-eye-3d-billboard-scenes-/1994006781204015/ (2026-05)
14. aescripts — Naked-Eye 3D (TikTok). https://www.tiktok.com/@aescripts/video/7645827526098439438 (~2026-05-30)
15. aescripts — LED Architect. https://aescripts.com/led-architect/ (2025–2026)
16. Ghosteam — Pixelmap Tool (free). https://www.ghosteaminc.com/pixelmap-tool/ (2026)
17. DVizion — LED Pixelmapper (Gumroad). https://dvizion.gumroad.com/l/ledpixelmapper (н/д)
18. GitHub — bburris81-cmyk/avd-pixelmap. https://github.com/bburris81-cmyk/avd-pixelmap (2026-04)
19. GitHub — oisinryan/led-test-patterns. https://github.com/oisinryan/led-test-patterns (2026-08)
20. Maxon — Creating 3D Anamorphic Billboards with Maxon One. https://www.maxon.net/en/article/creating-3d-anamorphic-billboards-with-maxon-one (2025)
21. Novedge — NAB 2025 Noseman anamorphic billboards in C4D. https://novedge.com/blogs/design-news/nab-2025-noseman-how-to-make-3d-anamorphic-billboards-in-cinema-4d (2025)
22. Superhive — Lens Sim (пример выдачи по «anamorphic»). https://superhivemarket.com/products/lens-sim?num=2 (2026-09)
23. VideoHive — 3D Billboard Mockup. https://videohive.net/item/3d-billboard-mockup/53578416 (н/д)
24. FOOH.com — Screens Directory (138–139 screens, 63 cities). https://fooh.com/directories/screens (2026-09)
25. FOOH.com — The Heeren 3D Billboard, Singapore. https://fooh.com/screens/the-hereen-3d-billboard (2026)
26. FOOH.com — Pattari 2 Milan. https://fooh.com/screens/pattari-2-milan-3d-billboard/ (2026)
27. FOOH.com — Piazza XXV Corner Milan. https://fooh.com/screens/piazza-xxv-corner-3d-billboard-milan/ (2026)
28. FOOH.com — Duomo di Milano 3D Billboard. https://fooh.com/screens/duomo-di-milano-3d-billboard (2026)
29. FOOH.com — Westlands 3D screen (Nairobi). https://fooh.com/screens/westlands-3d-anamorphic-led-screen/ (2026)
30. FOOH.com — homepage / FOOH Awards 2026. https://fooh.com/ (2026)
31. GitHub — openooh/venue-taxonomy. https://github.com/openooh/venue-taxonomy (обновл. 2026-09-24)
32. GitHub — api-evangelist/tps-engage (Blindspot). https://github.com/api-evangelist/tps-engage (2026-08)
33. Blindspot — Billboards in Singapore. https://seeblindspot.com/billboards-in-singapore/ (2026)
34. Arabian Business — Burj Khalifa ad cost. https://www.arabianbusiness.com/industries/media/burj-khalifa-ad-cost (н/д)
35. Leads Dubai — Burj Khalifa advertisement cost 2026. https://www.leadsdubai.com/burj-khalifa-advertisement-cost/ (2026)
36. outdooradvertisinguae — Sheikh Zayed Road rates. https://outdooradvertisinguae.com/outdoor-advertising-rates-and-costs-on-sheikh-zayed-road-dubai/ (2026)
37. Digital Space Dive — Billboard advertising Dubai & Abu Dhabi 2025/2026. https://digitalspacedive.com/billboard-advertising-dubai-abu-dhabi/ (2025–2026)
38. DigiComm — Anamorphic 3D LED Dubai 2026. https://digicomm.ae/news/anamorphic-3d-led-dubai-2026/ (2026)
39. AdQuick — DOOH Singapore 2026. https://www.adquick.com/dooh-advertising/singapore-sg (2026)
40. TPM — Billboard advertising rates Singapore 2026. https://theperfectmediagroup.com/billboard-advertising-rates-singapore/ (2026)
41. JCDecaux Singapore — ION Grand Façade LED. https://www.jcdecaux.com.sg/news-and-press-releases/jcdecaux-singapore-and-ion-orchard-unveils-brand-new-ion-grand-facade-led (н/д)
42. TPM — Heeren Orchard LED screen. https://theperfectmediagroup.com/heeren-orchard-led-screen-the-best-out-of-home-digital-in-the-vicinity/ (2026)
43. Unicam Studio — 3D anamorphic video Singapore. https://www.unicamstudio.com/3d-anamorphic-video-singapore/ (н/д)
44. Plan B Media — Digital OOH Thailand. https://www.planbmedia.co.th/ooh/digital/ (2026)
45. transads.id — Harga iklan videotron Jakarta. https://transads.id/berapa-harga-iklan-videotron-jakarta-panduan-lengkap-tarif-lokasi-premium-dan-cara-memilih-media-yang-tepat-bagian-1/ (2025)
46. Lestari Ads — Harga sewa videotron kota besar. https://www.lestariads.com/en/blog/dooh/berapa-sih-harga-sewa-videtron-kota-kota-besar-di-indonesia.html (2025)
47. Wicaksana Indonesia — Sewa videotron Jakarta 2025. https://www.wicaksanaindonesia.com/sewa-jasa-videotron-jakarta-2025/ (2025)
48. uno.id — Videotron Jakarta. https://uno.id/videotron-jakarta-media-iklan-digital/ (2025)
49. Firstboard — Harga billboard Indonesia. https://firstboard.com/id/id/blog/harga-billboard-indonesia (2025)
50. nezzan — Harga sewa videotron Jakarta 2025. https://nezzan.edu.eu.org/harga-sewa-videotron-di-jakarta-murah/ (2025)
51. Mitra LED — Sewa LED videotron Bali. https://www.mitra-led.com/sewa-led-videotron-p2-indoor-p2-5-p2-6-p2-9-videotron-wilayah-bali-denpasar-dan-sekitarnya.html (2025)
52. 86visualpro — Sewa LED videotron Bali. https://86visualpro.com/sewa-led-videotron-bali/ (2025)
53. Broadsign — Reklam Istanbul case. https://broadsign.com/blog/how-reklam-istanbul-is-building-turkeys-largest-digital-ooh-network-with-broadsign/ (2024–2025)
54. Cublic — COEX Brand Avenue ads. http://www.cublic.co.kr/index.php/en/our-media/item/106-led-brandave-en (н/д)
55. Korea Herald — COEX largest outdoor screen. https://www.koreaherald.com/article/1621275 (н/д)
56. jeki — Cheering AD, Cross Shinjuku Vision. https://cheering-ad.jeki.co.jp/en/products/cross-shinjuku-vision (2026)
57. Cross Shinjuku Vision sales sheet (Unica). https://shinjuku.xspace.tokyo/wp-content/uploads/2025/07/%E3%80%90%E3%82%AF%E3%83%AD%E3%82%B9%E6%96%B0%E5%AE%BF%E3%83%93%E3%82%B8%E3%83%A7%E3%83%B3%E3%80%91%E5%AA%92%E4%BD%93%E8%B3%87%E6%96%99-20250702%E4%BF%AE%E6%AD%A3.pdf (2025-04/07)
58. CoStar — Landsec £450m Piccadilly Lights scheme. https://www.costar.com/article/402827887/us-hedge-fund-doubles-up-at-landsecs-450-million-piccadilly-lights-scheme (2025–2026)
59. Completely Retail — Piccadilly Circus island £450m. https://news.completelyretail.co.uk/piccadilly-circus-island-site-handed-450m-price-tag (2025)
60. Campaign — Landsec brand experience venue under Piccadilly Lights. https://www.campaignlive.co.uk/article/landsec-creates-brand-experience-venue-piccadilly-lights/1865666 (2025)
61. Creatify — Higgsfield pricing 2026. https://creatify.ai/blog/higgsfield-pricing-(2026)-plans-and-what-you-ll-actually-pay (2026-09)
62. Layer3labs — Higgsfield AI pricing 2026. https://www.layer3labs.io/guides/higgsfield-ai-pricing (2026)
63. Artificial Studio — Billboard Ad generator. https://app.artificialstudio.ai/tools/billboard-ad (2026)
64. WaveSpeedAI — Billboard Ad. https://wavespeed.ai/apps/ads/billboard-ad (2026)
65. PromptBase — Viral FOOH CGI product video. https://promptbase.com/app/viral-fooh-cgi-product-video (2026)
66. MAD CGI — What is FOOH advertising 2026. https://www.madcgi.com/blog-posts/what-is-fooh-advertising-and-why-every-brand-needs-it-in-2026 (2026)
67. Maverick Frame — What is FOOH. https://maverickframe.com/blog/what-is-fooh/ (2026)
68. Fiverr — opreston, naked-eye 3D corner LED ($95). https://www.fiverr.com/opreston/create-3d-anamorphic-illusion-for-corner-led-screen (2026-09)
69. artificialintelligenceact.eu — Article 50 practical guide. https://artificialintelligenceact.eu/transparency-rules-article-50/ (2026)
70. Stibbe — AI Act transparency obligations timeline. https://www.stibbe.com/publications-and-insights/the-ai-acts-transparency-obligations-rules-scope-and-timeline (2026)
71. European Commission — Code of Practice on AI-generated content. https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content (2026)
72. ASA — Disclosure of AI in advertising. https://www.asa.org.uk/news/disclosure-of-ai-in-advertising-striking-the-balance-between-creativity-and-responsibility.html (2025–2026)
73. Magnific MCP — video_models_list и simulate_cost (Seedance 2.5 / 2.0, лимиты длительности, разрешения и сторон; 11 850 кредитов за 15 с 1080p). Внутренний каталог, запрос 2026-09-26.
74. Higgsfield MCP — get_presets («billboard» — 0; «giant» — Street colossus, Lacewalker) и apps_search («billboard», «3D» — 0). Запрос 2026-09-26.
