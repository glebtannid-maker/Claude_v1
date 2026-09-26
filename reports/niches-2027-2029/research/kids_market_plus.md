# Поток 10 — дополнение (top-up): «рисунок ребёнка + фото ребёнка → видео». Проверки, исправления, новые данные

*Дата среза: 2026-09-26. Это дополнение к `kids_market.md`: то, что там не изменилось, здесь не повторяется.*

> **Методология и метки.** До исчерпания общего лимита сессии (200 из 200) я успел сделать 34 запроса WebSearch. Прямой WebFetch к сайтам конкурентов, App Store, Google Play, Etsy и Reddit заблокирован прокси (проверено 2026-09-26: `EGRESS_BLOCKED`). Поэтому использованы ещё три источника:
> - **[W]** — факт из поисковой выдачи WebSearch: сводка проиндексированной страницы на 2026-09-26. Саму страницу я не открывал. Если дата страницы в выдаче не видна, пишу «дата н/д».
> - **[CrUX]** — мой расчёт по месячным спискам **Chrome UX Report Top-1M**: глобальный, US, GB, CA, AU ([zakird/crux-top-lists](https://github.com/zakird/crux-top-lists), скачано с raw.githubusercontent.com 2026-09-26). Это публичный рейтинг Google по реальным загрузкам страниц в Chrome. Он даёт корзины ранга: top-1k, 5k, 10k, 50k, 100k, 500k, 1M. **Это прокси веб-трафика.** Трафик внутри мобильных приложений он не видит, а смена корзины означает изменение трафика в разы, а не на проценты.
> - **[Н]** — новостной корпус (копии TechCrunch, The Verge, Ars Technica, Wired и других на GitHub, 2025–2026): даю исходный URL и дату публикации.
> - **[П-с]** — проверено параллельным потоком этой сессии (`consumer_apps.md`) по указанному URL.
>
> «Оценка» — мой расчёт с допущениями и уровнем уверенности.

---

## Проверено и исправлено

### 1. Демо Meta Animated Drawings (sketch.metademolab.com): **живо, но трафик упал примерно на порядок** (в оригинале: «нет данных»)
- [W] Страницы демо (`/canvas`, `/about`, `/terms`, `/usage`) на 2026-09-26 в поисковом индексе. Условия использования: демо исследовательское, **«may not be used for any commercial purpose(s)»**, **недоступно жителям штатов Illinois и Texas** ([Terms](https://sketch.metademolab.com/terms); [главная](https://sketch.metademolab.com/), дата н/д). *Оценка (средняя уверенность):* Illinois и Texas исключены, скорее всего, из-за законов о биометрии (BIPA, CUBI): там есть детекция поз и сегментация. **Для основателя это прямой сигнал:** даже Meta не стала рисковать биометрическими исками, хотя обрабатывает только рисунки. С фото реальных детей юридический риск заметно выше.
- [CrUX] Динамика ранга `https://sketch.metademolab.com`:

| Период | Глобально | US | GB |
|---|---|---|---|
| 2022-12 → 2025-06 | **top-100k** (в 2024-03 и 2024-06 — **top-50k**) | 2025-01/02 и 2025-06: top-100k; 2025-03…05: top-500k | 2025-01…03, 05, 06: top-100k |
| 2025-07 → 2026-08 | **top-500k** все 14 месяцев | top-500k все месяцы | top-500k, **кроме 2025-12: top-100k** (предрождественский всплеск) |

  **Вывод (оценка, средняя уверенность).** Демо работает и в августе 2026 года всё ещё входит в top-500k. Но с июля 2025 года оно опустилось на одну корзину (трафик упал примерно в 3–10 раз). Совпадения по времени: 2025-07-23 вышел бесплатный photo-to-video в Google Photos [П-с], 2025-09-03 репозиторий заархивирован [П, оригинал]. Прогноз оригинала «демо может отключиться, и освободится трафик» пока не подтвердился. Похоже, что **спрос перетёк к генеративным инструментам**, а не ждёт замены демо. Всплеск в UK в декабре 2025 года подтверждает гипотезу оригинала о подарочном сезоне.

### 2. Crayola Color Alive — **оригинал ошибался**, описывая его как действующую AR-категорию
- [W] Приложение Crayola Color Alive **удалено из Google Play 2018-06-05**. До удаления его скачали **2,2 млн раз** ([AppBrain](https://www.appbrain.com/app/crayola-color-alive/com.DAQRI.crayola.coloralive), дата н/д). В сторах его больше нет. Упоминания «Color Alive 2.0» есть только на APK-зеркалах.
- [W] **Quiver**: бесплатная загрузка, 10 AR-раскрасок без подписки, покупки внутри приложения **$0,99–4,99**, подписка открывает 250+ листов и 75+ планов уроков. Образовательные лицензии — пять тарифов, от 10 до 500 мест ([QuiverVision Subscribe](https://quivervision.com/subscribe); [Educational App Store](https://www.educationalappstore.com/app/quiver-education-3d-coloring-app), дата н/д). Рейтинг в Android — **3,04★ при ~18 тыс. оценок**, **2,5 млн+ загрузок** ([AppBrain](https://www.appbrain.com/app/quiver-3d-coloring-app/com.puteko.colarmix), дата н/д). [CrUX] Сайт quivervision.com в US top-1M был только в 2025-09 и 2026-03.
- **Вывод.** AR-раскраски — стареющая категория с низкими рейтингами. Это не растущий конкурент, а пример того, что «оживление» только на своих шаблонах без свободного рисунка удержать не удалось.

### 3. Физические продукты из рисунков: цены подтверждены и уточнены (в оригинале «нет данных» или [БЗ])

| Продукт | Факт | Источник |
|---|---|---|
| **Budsies** (плюш по рисунку) | «regular character drawings **under $150**»; доставка «approximately **6–8 weeks**» (в праздники дольше). Акции: **$59 при номинале $99** за одну игрушку, $109 за две (номинал $198) | [W] [Budsies — cost](https://www.budsies.com/custom-plush-cost/), дата н/д; [CertifiKID](https://www.certifikid.com/deal/10779/59-for-custom-stuffed-animal-designed-by-you-9), дата н/д |
| Budsies, трафик | [CrUX] US **top-500k все 20 месяцев** (2025-01 → 2026-08), GB top-500k/1M. Спрос стабильный, без роста | CrUX |
| **Child's Own Studio** | Мягкие игрушки 16" (стандарт) и 25" (большие), изготовление «normally 4 weeks». Сейчас компания предлагает и оптовое производство. Пресса прошлых лет: **$90–140** за игрушку, **~400 игрушек с 2007 года**: это ремесленный объём, лист ожидания | [W] [childsown.com — Softie Create](https://www.childsown.com/softie-create/); [Daily Meal](https://www.thedailymeal.com/let-childs-own-studio-transform-your-kids-drawing-unique-plush-toy/); [Baby Gizmo](https://babygizmo.com/turn-childs-drawing-stuffed-toy/), даты н/д (старые публикации) |
| **Crayon Creatures** | **€99 (~$130)** за 3D-печать из «песчаника» ~10 см, срок 3 недели. Раньше было $150 + $20 доставка в США. Статус в 2026 году — н/д | [W] [New Atlas](https://newatlas.com/crayon-creatures-childrens-drawings/25700/), 2013; [3DPrint.com](https://3dprint.com/238874/turn-your-kids-2d-drawing-into-a-3d-printed-sculpture/), 2019 |
| **Artkive** (домен **artkiveapp.com**, в оригинале ошибочно artkive.com) | Коробка-кит **$14,99** по вводной цене (стандартно $39); книга **от $75 за 25 изображений**; мозаика в раме $99 / $249; оцифровка $45. Минимальный реальный чек — **~$89,99** | [W] [ForeverArtKids — Artkive alternatives (2026)](https://foreverartkids.com/guides/artkive-alternative/); [Artkive FAQ](https://faq.artkiveapp.com/hc/en-us/articles/360025758991-How-does-pricing-work-for-the-Artkive-Box), 2026 |
| Artkive, трафик | [CrUX] www.artkiveapp.com: US top-100k в 2025-02 и 2025-04…12; **top-500k в 2026-01…06 и 2026-08** (в 2026-07 — 100k). *Оценка (низкая):* веб-трафик в 2026 году ниже, чем в 2025-м. Часть трафика могла уйти на account.artkiveapp.com: там с 2025-11 устойчиво top-500k | CrUX |
| **Plum Print** | Твёрдая обложка 10×8" — **$175** (первые 20 работ включены), 13×11" — **$210**; каждая следующая работа $2,60 / $2,85; депозит $49,99 за кит | [W] [Plum Print — Pricing](https://www.plumprint.com/pages/pricing), 2026 |
| **Keepy** | Бесплатно до 7 «воспоминаний» в месяц; подписка Unlimited (месячная или годовая, триал 7 дней). Текущая цена — н/д (старые источники называют $5,99 в месяц, не подтверждено) | [W] [App Store](https://apps.apple.com/us/app/keepy-artwork-schoolwork/id647088205); [ArtShow](https://artshow.app/blog/save-your-kids-art-here-are-the-best-apps-to-try/), 2025 |

**Вывод, усиливает оригинал.** Физические «хранилища» детского творчества держат чек **$90–210** (Artkive, Plum Print) и **$99–150** (плюш, 3D). Цифровые «оживлялки» продаются за **$35–80 в год** (см. п. 6). Разница в чеке — 3–5 раз в пользу физики.

### 4. Школьные арт-фандрайзеры: цены, доли и масштаб (в оригинале «нет данных»; **моя оценка доли школы 15–25% была занижена**)

| Компания | Доля школы | Цены | Масштаб | Источник |
|---|---|---|---|---|
| **Square 1 Art** (США, с 2000) | **25% / 33% / 38%**. 33% при участии ≥20% или продажах ≥$3 300 (минимум 150 работ); 38% при участии ≥45%; 25% при <150 работ или участии <20%. Тарифы действуют для программ, стартующих после 2026-01-01 | Товары **$5–60**; бумага, постеры и планы уроков бесплатно; чек школе через 10–14 дней | «Each year… raise **nearly $7 million** for partner schools» | [W] [Free Product Program](https://www.square1art.com/free-product-program/); [FAQ](https://www.square1art.com/faq/); [About](https://www.square1art.com/about-us/), 2026 |
| **Original Works** (США) | **33–50%** в зависимости от программы | «many priced **under $15**»: кружки, магниты, плитки | **$50 млн** прибыли школам за всё время | [W] [Top reasons](https://www.originalworks.com/top-reasons-to-choose-original-works/); [All products](https://www.originalworks.com/all-products/), дата н/д |
| **Artsonia** (онлайн-галерея) | **20%** с каждой покупки | Кружка **от $18,95**, ёлочная игрушка **$14,95**, типично $10–30 | **50 000+ школ K-12 в США**; опубликовано **138 675 512 работ**, **10 млн+ в год**. 11 897 школ загрузили ≥1 000 работ, 3 689 — ≥10 000, 270 — ≥50 000 | [W] [About](https://www.artsonia.com/about/); [Teachers](https://www.artsonia.com/teachers/); [Awards](https://www.artsonia.com/schools/awards/); [Gift Shop](https://www.artsonia.com/gifts/), 2025–2026 |
| **Art to Remember** | Базово **25%**, до **38%** | н/д (популярный товар — магнит 4×5") | **$45 млн+** с 1995 года, **11 545 школ**, 9 225 665 работ | [W] [About / Fundraisers](https://atr.arttoremember.com/fundraisers/), дата н/д |
| **Created by Kids** (Канада) | «fee-free» | н/д | н/д | [W] [createdbykids.ca](https://createdbykids.ca/), дата н/д |

- **Проверка на согласованность (оценка, средняя).** ZoomInfo оценивает выручку Square 1 Art в **$7,1 млн (2026)** ([ZoomInfo](https://www.zoominfo.com/c/square-1-art-llc/112886203)). Но если школы получают ~$7 млн в год при доле 25–38%, валовые продажи должны составлять **~$18–28 млн в год**. Оценка ZoomInfo, по-видимому, занижена: сторонним оценкам выручки не доверять.
- **Юнит-экономика программы (оценка, средняя).** Порог $3 300 и минимум 150 работ у Square 1 Art задают типичный масштаб. Школа на 400 детей × 30% участия × $30 среднего заказа ≈ **$3 600 продаж**, из них школе ~$1 200. Для одиночного основателя: **20 школ в сезон ≈ $70 тыс. валовых продаж** — только если продукт вообще продаётся через школу.
- **Анимации или видео в предложениях этих компаний поиском не найдено** ([W], запрос «school art fundraiser animated video… 2026», 2026-09-26). Это отсутствие доказательств, а не доказательство отсутствия.
- **Трафик [CrUX].** artsonia.com в **US top-5k** почти все месяцы 2025–2026 годов; летом проседает: июнь — 10k, июль — 50k. **Это на 1–2 порядка больше, чем у любого AI-«оживителя».** Artsonia — самый сильный инкумбент по каналу «рисунок ребёнка → покупка семьи».

### 5. Платформенные факты из [БЗ] подтверждены (по `consumer_apps.md` и новостному корпусу)
- **TikTok AI Alive** запущен **2025-05-13**: image-to-video в Story Camera, бесплатно, с метками AI и C2PA ([TechCrunch](https://techcrunch.com/2025/05/13/tiktok-launches-tiktok-ai-alive-a-new-image-to-video-tool/), 2025-05-13) [П-с]. Оригинал указывал «май 2025» — **верно**.
- **Google Photos**: photo-to-video на Veo 2 (6 с), Remix и вкладка Create — бесплатно с **2025-07-23** ([9to5Google](https://9to5google.com/2025/07/23/google-photos-photo-to-video/)). Текстовые промпты для photo-to-video — с **2026-01-26** ([The Verge](https://www.theverge.com/news/868510/google-photos-image-to-video-text-prompt-support), 2026-01-27). **Video Remix** на Gemini Omni (переосвещение, замена фона, стили) — с **2026-07-08** для подписчиков AI Plus/Pro/Ultra ([TechCrunch](https://techcrunch.com/2026/07/08/google-photos-adds-a-new-ai-video-remix-tool/), 2026-07-08) [П-с]. Оригинал указывал «июль 2025» — **верно**.
- **Apple.** Image Wand из iOS 18.2 в этой сессии по-прежнему **не перепроверен**. Новое: на WWDC **2026-06-08** Image Playground получил **фотореалистичную** генерацию на модели в Private Cloud Compute; всё сгенерированное помечается SynthID; **о видео ничего** ([PetaPixel](https://petapixel.com/2026/06/08/apples-all-new-image-playground-promises-more-than-cartoons/), 2026-06-08) [Н]. Apple по-прежнему делает только статичную картинку.
- **Sora.** Закрытие объявлено **2026-03-24** (пост «Goodbye to Sora», [X/@soraofficialapp](https://twitter.com/soraofficialapp/status/2036532795984715896)). Disney отменила инвестицию в OpenAI на $1 млрд ([Ars Technica](https://arstechnica.com/ai/2026/03/the-end-of-sora-also-means-the-end-of-disneys-1-billion-openai-investment/), 2026-03-25) [Н]. Даты закрытия приложения и API в оригинале согласуются с этим.

### 6. Оценка «20–50+ конкурентов» **подтверждена и, скорее, занижена**
Поиск нашёл **не менее 16 названных продуктов**, которых нет в оригинальной таблице (п. «Новые факты», таблица А). Вместе с 13 запусками из WebsiteLaunches получается **~30 известных игроков** только в англоязычном сегменте «детский рисунок → AI-арт, видео или 3D». Урок Oblique («за полгода с 2 до 6+ конкурентов») здесь уже пройден: рынок переполнен.

### 7. Etsy и Fiverr (в оригинале «нет данных») — заполнено частично
- [W] На Etsy есть листинги ручной или полуавтоматической работы: «**Custom Kids' Drawing Animation | Turn Kids' Artwork and Audio Into Personalized Animated Videos**» ([Etsy 1763280459](https://www.etsy.com/listing/1763280459/custom-kids-drawing-animation-turn-kids)) и «Bringing Kids' Art to Life: Child Drawing Animation Kit» ([Etsy 1558930212](https://www.etsy.com/listing/1558930212/bringing-kids-art-to-life-child-drawing)). Плюш по рисунку — десятки листингов, в том числе с «Budsies» в заголовке ([Etsy 236677801](https://www.etsy.com/listing/236677801/custom-plush-from-drawing-custom-plush); [Etsy 508819199](https://www.etsy.com/listing/508819199/stuffed-animal-from-drawing-budsies)). **Цены и число продаж — н/д**: Etsy закрыт прокси, а сводки выдачи их не содержат.
- [W] Fiverr: гиги «2D animation for kids» **от $15**; типичная цена «cartoon animator» — **$120–140** ([Fiverr — cartoon animation](https://www.fiverr.com/gigs/cartoon-animation); [пример гига $15](https://www.fiverr.com/qosain_ali/do-animated-content-2d-cartoon-animation-video-character-2d-animation-for-kids), дата н/д). Это **прокси потолка цены** ручной анимации, а не спроса на анимацию именно детских рисунков.

---

## Новые факты

### А. Прямые конкуренты, которых не было в оригинале: приложения и сайты «рисунок ребёнка → видео / AI-арт / 3D»

| Название | Формат | Что делает | Цена | Рейтинг / тяга | URL | Заметки |
|---|---|---|---|---|---|---|
| **DrawToLife** | iOS, Android, веб | Рисунок → AI-арт в 6 стилях, **книжка с озвучкой на 9 языках**, **говорящее видео**, «Movie Director»; Kids Mode, родительский кабинет, 3–8 лет, без рекламы и соцфункций | iOS: **$4,99 в месяц / $34,99 в год / $79,99 навсегда**; Android: **$9,99 в месяц (40 кредитов) / $79,99 в год (500)**; кредиты $2,99 за 10, $4,99 за 30, $14,99 за 100; первое преобразование бесплатно, триал 3 дня | н/д; [CrUX] вне top-1M | [draw-to-life.com](https://draw-to-life.com/); [App Store](https://apps.apple.com/us/app/draw-to-life-kids-ai-art/id6752760587); [Google Play](https://play.google.com/store/apps/details?id=com.nomadlink.drawtolife&hl=en-US) | Ведёт SEO-блог и страницы сравнения с конкурентами: «7 Best Apps…» ([блог](https://draw-to-life.com/blog/best-apps-bring-kids-drawings-to-life/), 2026) |
| **Gimba** | Android, iOS | Рисунок → AI-арт (anime, cartoon, pixel, clay, watercolor), **мультики и короткие видео** | 3 бесплатные картинки; пакеты кредитов; **Gimba Pro** (месячная подписка): видео, все стили, **до 6 профилей детей**, **1 000 кредитов в месяц**; цена н/д | н/д; [CrUX] вне top-1M | [gimba.app](https://gimba.app/); [Google Play](https://play.google.com/store/apps/details?id=com.yellowsquirrel.gimba&hl=en_US) | Главный аргумент — **приватная галерея без публичной ленты** |
| **KidsAI** | веб | Раскраска рисунка (1 кредит, 20+ стилей) и **анимация 5–22 кредита** в зависимости от длины и разрешения; 3–12 лет | 10 бесплатных кредитов, далее платно (цены кредитов н/д) | н/д | [kidsai.art](https://kidsai.art/); [гайд](https://kidsai.art/animate-drawing.html) | Прозрачная кредитная модель |
| **Animomo** | Android (и сайт) | Фото рисунка или раскраски → короткое анимированное видео, «save a memory, share with family» | н/д | Отзывы: «сын сразу захотел рисовать ещё», «дети развлекались часами» [W] | [animomo.app](https://www.animomo.app/); [Google Play](https://play.google.com/store/apps/details?id=com.igloola.Animomo&hl=en) | — |
| **Drawings Alive** | iOS, Android | Рисунок → реалистичная или мультяшная картинка, **видео**, **3D-модель (.glb/.usdz) в AR** | Подписка; по словам конкурента DrawToLife — **без триала, $10–70** (источник предвзятый) | Заявлено «**20 000+ семей**»; в App Store «not enough ratings» [W]; [CrUX] drawingsalive.com в GB top-1M только в 2025-05…07 | [drawingsalive.com](https://drawingsalive.com/); [App Store](https://apps.apple.com/us/app/drawings-alive-ai-doodle-art/id6749238166) | Сочетает 3D и AR |
| **Doodle Dreams** | веб | Рисунок → анимированное видео «preserving every creative detail», 3–5 минут; **архив с именем автора и его возрастом на момент рисунка** | Токены: 5 с без звука = 1 токен, звук = 2, 10 с = 2; **от $3,75 в месяц за 5 роликов**; 1 анимация бесплатно | Show HN **2024-12-29** | [doodledreams.cc](https://doodledreams.cc/); [HN](https://news.ycombinator.com/item?id=42524848) | Самый низкий ценовой ориентир |
| **AniMagic: Animate Drawings** | iOS | Скелетная анимация в стиле Meta: танцы, волна, «jumping jacks»; **всё на устройстве, данные не собираются**; экспорт в TikTok, Reels, Shorts | н/д | **4,7★, 5 000+ оценок** (App Store, на дату индексации) [W] | [App Store](https://apps.apple.com/us/app/animagic-animate-drawings/id6448135645); [MWM](https://mwm.ai/apps/animagic-animate-drawings/6448135645) | **Единственный найденный с существенным числом оценок.** Нишевая, но реальная тяга у бесплатной приватной скелетной анимации |
| **Revid.ai** (страница инструмента) | веб | Рисунок → **видеоистория** с сюжетом, озвучкой, музыкой, где герои рисунка — главные персонажи | Тарифы общей платформы (н/д) | [CrUX] revid.ai: US top-100k в 2025-03…2026-03, **top-500k с 2026-04** | [revid.ai/tools/animate-kids-drawing](https://www.revid.ai/tools/animate-kids-drawing) | Горизонтальная AI-видеоплатформа делает «детскую» SEO-страницу: пример поглощения ниши широкими игроками |
| **Drawmingo** | веб | Загрузка рисунка → автоматическое распознавание и анимация | н/д | [CrUX] вне top-1M | [drawmingo.com](https://drawmingo.com/) | — |
| **Dodoboo** | iOS, Android, веб | Каракули → AI-арт, детский интерфейс | Freemium + подписка (н/д) | Product Hunt: в целом хвалят; **жалоба на неожиданные списания после обновления** | [Product Hunt](https://www.producthunt.com/products/dodoboo/reviews) | Подтверждает гипотезу оригинала: монетизация — главный источник жалоб |
| **Homiwork AI Clips** | веб | «Animate Drawing Online Free» | бесплатно (фримиум) | [CrUX] homiwork.com: глобально top-500k, GB top-500k–1M (общий AI-сайт) | [homiwork.com](https://homiwork.com/en/app/aiclips/create/animate-drawing) | Бесплатный SEO-конкурент |
| doodlar | веб | «make drawing real» | н/д | вне top-1M | [doodlar.co](https://doodlar.co/) | — |
| Todrawn | веб | Рисунок → арт (детали н/д) | тарифная страница есть (н/д) | вне top-1M | [todrawn.com/pricing](https://todrawn.com/pricing) | — |
| Animated Drawing (клон Meta) | Android, iOS | Скелетная анимация | н/д | н/д | [Google Play](https://play.google.com/store/apps/details?id=com.companyname.animateddrawings); [App Store](https://apps.apple.com/us/app/animated-drawing/id6469684346) | Обёртки открытого кода Meta (MIT) |
| Ai Motions: Animate Drawings; AniToon | iOS | Анимация рисунков | н/д | н/д | [Ai Motions](https://apps.apple.com/us/app/ai-motions-animate-drawings/id6461773689); [AniToon](https://apps.apple.com/us/app/anitoon-draw-art-animate/id6476550987) | — |

Обзор KidsAiTools «AI Animation Tools for Kids: 6 Apps Compared» (~2026-08) ставит в топ не «оживлялки», а **Toontastic** (Google, 4,6/5, бесплатно, без аккаунта) и Animaker ([KidsAiTools](https://www.kidsaitools.com/en/articles/ai-animation-tools-for-kids), ~2026-08) [W]. Бесплатные инструменты от крупных компаний уже занимают «экспертные» подборки.

**Главный вывод по конкурентам (оценка, средняя–высокая уверенность).** [CrUX] Проверены 22 домена AI-новичков (все из оригинала плюс новые). **Ни один не входит в top-1M по веб-трафику** ни в US, ни в GB, ни глобально за 2025-01 → 2026-08. Исключения: drawingsalive.com (GB, три месяца 2025 года) и горизонтальные revid.ai и homiwork.com. Для сравнения, artsonia.com держится в US top-5k, budsies.com — в US top-500k. **Цифровые «оживлялки» не набрали заметного веб-трафика.** Ограничение: у мобильных приложений (AniMagic, Gimba, Animomo) трафик внутри приложения, CrUX его не видит.

### Б. Цены цифровых конкурентов: нижняя граница рынка
- Подписки и пакеты: **$3,75 в месяц** (Doodle Dreams), **$4,99 в месяц / $34,99 в год** (DrawToLife iOS), $9,99 в месяц (DrawToLife Android), разовые пакеты от **$2,99** ([W], источники в таблице А).
- **Оценка (средняя).** Стоимость ролика в рознице уже **$0,5–3**, а себестоимость — $0,2–1,4 (`kids_ops.md`). Потребительский цифровой ролик почти не оставляет маржи на CAC $3+ за установку (оригинал, п. 26).

### В. Сезонность: прокси через CrUX (в оригинале были только оценки)

| Сайт (US) | Обычный месяц | Пик | Когда |
|---|---|---|---|
| **shop.square1art.com** | top-500k | **top-50k** (≈ на порядок выше) | **март–апрель** и **октябрь–декабрь** 2025; снова март–апрель 2026; май — 100k. Глобально top-100k каждый **ноябрь** (2023, 2024, 2025) |
| **arttoremember.com** | top-500k–1M | **top-50k** — октябрь–ноябрь 2025; top-100k — март–апрель 2025 и 2026 | осень и весна |
| **store.originalworks.com** | top-500k–1M | top-50k — ноябрь 2025; top-100k — апрель 2026 | осень и весна |
| **artsonia.com** | **top-5k** | — (провал летом: июнь 10k, июль 50k) | учебный год |
| **lifetouch.com** (школьная фотография) | top-50k | — (провал в июле: 500k) | учебный год |
| **shutterfly.com** | top-5k | **top-1k** | ноябрь–декабрь 2025 |
| **postable.com** (открытки) | top-50k | **top-10k / top-5k** | ноябрь / декабрь 2025 |
| **auraframes.com** (цифровые рамки для бабушек и дедушек) | top-50k | **top-10k** | декабрь 2025 |
| **chatbooks.com** | top-100k | top-50k | декабрь 2025 |
| budsies.com | top-500k | заметного пика в пределах корзины нет | — |

Источник всех строк: [CrUX] ([zakird/crux-top-lists](https://github.com/zakird/crux-top-lists), US-списки 2025-01 → 2026-08).

**Выводы.**
1. **У школьного B2B два равных сезона**: весна (март–апрель) и осень (октябрь–ноябрь, доставка к праздникам). Оригинал писал «осень, реже весна» — **весна не слабее**. Окно весны 2027 года реально, но школы, по-видимому, записываются в январе–феврале (оценка, низкая уверенность).
2. **Потребительский подарочный пик — ноябрь–декабрь**, у открыток и цифровых рамок он резкий (рост на 1–2 корзины). Это согласуется с оценкой оригинала «Рождество — максимум».
3. Budsies не показывает сезонного пика на уровне корзин. Физический плюш продаётся круглый год, в том числе на дни рождения.

### Г. Платформы и дистрибуция: новое за 2026 год
- **CapCut** получил Dreamina **Seedance 2.0** (2026-03-26) со встроенной **защитой от генерации видео с реальных лиц** ([TechCrunch](https://techcrunch.com/2026/03/26/bytedances-new-ai-video-generation-model-dreamina-seedance-2-0-comes-to-capcut/), 2026-03-26) [Н]. У CapCut 736 млн MAU (a16z, через `consumer_apps.md`) [П-с]. **Вывод:** крупнейший массовый видеоредактор тоже не будет делать «реального ребёнка в кадре». Это подкрепляет п. 19 оригинала: окно для «ребёнок + рисунок» есть, но только с полной ответственностью на себе.
- **Meta Muse Image** позволял генерировать картинки с фото из публичных Instagram-аккаунтов других людей. Его **выключили через три дня** после запуска из-за общественного протеста ([TechCrunch](https://techcrunch.com/2026/07/09/how-to-stop-metas-ai-image-generator-from-using-your-instagram-photos/), 2026-07-09; [The Next Web](https://thenextweb.com/news/meta-muse-image-instagram-privacy-backlash-pulled), 2026-07-13) [Н]. Даже Meta отступает, когда AI трогает изображения реальных людей.
- **YouTube Shorts Remix** на Gemini Omni позволяет вставить себя в чужие ролики ([The Verge](https://www.theverge.com/tech/934704/google-gemini-omni-youtub-shorts-remix-ai), 2026-05-20). **Google TV** умеет трансформировать фото с Nano Banana и Veo ([TechCrunch](https://techcrunch.com/2026/04/29/more-gemini-features-are-coming-to-google-tv/), 2026-04-29) [Н]. «Оживить картинку» есть уже даже в телевизоре.
- **Дистрибуция AI-контента дорожает.** **Snapchat** больше не рекомендует полностью сгенерированный AI-контент в Spotlight ([TechCrunch](https://techcrunch.com/2026/07/31/snapchat-no-longer-rewards-fully-ai-generated-spotlight-content/), 2026-07-31). **Instagram** ограничивает охват AI-профилей без маркировки ([TechCrunch](https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/), 2026-08-31) [Н]. *Оценка (средняя):* вирусная петля «ролик → соцсети → новые пользователи» для AI-роликов слабеет. Это ещё один аргумент за частный шеринг (QR, ссылка бабушке) и институциональные каналы.

### Д. Регуляторика вокруг детей и AI-изображений: резкое ужесточение в 2026 году
- **TikTok заплатит $400 млн** по иску DOJ о нарушении **COPPA** (сбор данных детей без уведомления родителей) ([The Verge](https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa), 2026-08-21).
- Мировое соглашение **Meta на $18 млрд** с 29 штатами касается в том числе данных детей до 13 лет ([TechCrunch](https://techcrunch.com/2026/08/27/buried-in-metas-18b-settlement-is-a-legal-pass-on-kids-data/), 2026-08-27).
- **Minnesota** запретила nudify-приложения, штраф для разработчиков до **$500 тыс.** ([Ars Technica](https://arstechnica.com/tech-policy/2026/05/minnesota-set-to-be-first-state-to-ban-nudification-apps/), 2026-05-01). Суд отказал xAI в блокировке запрета ([TechCrunch](https://techcrunch.com/2026/08/01/judge-denies-xais-request-to-block-minnesota-ban-on-nudify-apps/), 2026-08-01). **San Francisco** потребовал от Apple и Google удалить такие приложения из сторов ([TechCrunch](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/), 2026-07-17). В рекламе Meta нашли **реальные фото девочек-подростков** в объявлениях nudify-приложений ([Ars Technica](https://arstechnica.com/tech-policy/2026/09/real-photos-of-young-girls-were-in-nudify-app-ads-on-facebook-instagram/), 2026-09-08).
- **EU Kids Act**: планируется запрет соцсетей до 13 лет и ограничения для чат-ботов, работающих с несовершеннолетними ([Wired](https://www.wired.com/story/the-eu-bans-social-media-for-under-13s/), 2026-09-16; [Wired](https://www.wired.com/story/the-eu-wants-to-break-up-kids-and-their-chatbots/), 2026-09-17). В США — законопроект **KIDS Act** с проверкой возраста ([EFF](https://www.eff.org/deeplinks/2026/06/kids-act-would-require-age-checks-get-online), 2026-06-28) и финальные правила **NY SAFE for Kids Act** ([The Verge](https://www.theverge.com/policy/972007/new-york-safe-for-kids-act-age-verification), 2026-07-28) [Н].
- **Вывод (оценка, высокая уверенность).** «Медленный сценарий» оригинала («инцидент → ужесточение») **уже частично реализуется**. Продукт, где на вход подаётся фото реального ребёнка, в 2027–2029 годах будет в зоне повышенного внимания регуляторов, сторов и платёжных систем. Продукт, работающий только с рисунками, — нет.

---

## Заполненные пробелы (по пунктам брифа)

| Пункт брифа | Было в оригинале | Стало |
|---|---|---|
| Meta Animated Drawings: лицензия, звёзды, статус демо | Всё, кроме статуса демо | **Демо живо**: top-500k CrUX в 2026-08, падение с top-100k с 2025-07; условия — некоммерческое использование, без IL и TX (п. 1) |
| Приложения «animate drawing / drawing to life / doodle to video…» | 13 сайтов из WebsiteLaunches, рейтингов нет | +16 продуктов с ценами (таблица А); рейтинг есть только у AniMagic (4,7★, 5 000+) и Quiver (3,04★, 18 тыс. в Android). **Рейтинги и загрузки остальных — по-прежнему н/д** |
| AR-раскраски (Quiver, Color Alive) | [БЗ] | Color Alive **снят в 2018 году** (исправление); Quiver — цены и рейтинг (п. 2) |
| Архивы детского творчества (Artkive, Keepy, Plum Print) | Цены н/д | Artkive от $89,99, Plum Print $175/$210, Keepy — бесплатно до 7 в месяц (п. 3) |
| Плюш и фигурки (Budsies, Child's Own, Crayon Creatures) | $69 (2015), остальное н/д | Budsies <$150, 6–8 недель; Child's Own $90–140 (старые данные), ~4 недели; Crayon Creatures €99 (2013) (п. 3) |
| AI-сервисы 2024–2026 «рисунок → реальное / 3D / видео» | 13 из фида | + DrawToLife, Gimba, KidsAI, Animomo, Drawings Alive (3D/AR), Doodle Dreams (HN 2024-12-29) и др. (таблица А) |
| Вирусные тренды TikTok, Instagram, Reddit | Tom's Guide (статика) | **нет данных**: Reddit и TikTok не индексируются инструментом. Прокси: пик UK в декабре 2025 у демо Meta [CrUX]; сторонние данные об AI Alive и «трибьют-видео» — в `consumer_apps.md` |
| Etsy и Fiverr: цены и отзывы | н/д | Листинги существуют (ID), цены Etsy — **н/д**; Fiverr — детская 2D-анимация от $15, типично $120–140 (п. 7) |
| Google Trends и прокси поискового объёма | Backlinko 2020 | **CrUX-прокси трафика и сезонности** за 2025–2026 годы (раздел В); Google Trends — по-прежнему н/д |
| Сезоны подарков | Оценки | Подтверждены через CrUX: ноябрь–декабрь для подарков, март–апрель и октябрь–ноябрь для школ |
| B2B: школьные фандрайзеры | Существование [БЗ] | Доли 20–50%, цены $5–60, масштаб: $7 млн в год, 50 тыс. школ, 11,5 тыс. школ (п. 4) |
| Детсадовские фотографы | н/д | Косвенно: lifetouch.com в US top-50k с годовым циклом учебного года [CrUX]. Цены и готовность покупать апселл — **н/д** |
| Риск поглощения платформами | Частично [БЗ] | TikTok AI Alive и Google Photos подтверждены; CapCut Seedance с защитой от реальных лиц; Apple — только статика; Meta откатила Muse Image (раздел Г) |

---

## Обновлённые сценарии и сигналы

Новые данные **меняют вероятности**. Регуляторное ужесточение уже идёт (раздел Д). Дистрибуция AI-контента дорожает (раздел Г). Рынок цифровых «оживлялок» переполнен и без тяги (таблица А и CrUX). Инкумбенты школьного канала сильны (п. 4).

| Сценарий | Было | Стало | Что изменилось |
|---|---|---|---|
| **Базовый: «функция, а не продукт»** | 55% | **50%** | По сути без изменений; уточнение: к 09.2028 **вероятность, что хотя бы один из Artsonia, Square 1 Art, Original Works или Art to Remember добавит анимацию, — 40–60%** (оценка, низкая уверенность). У них канал, рисунки уже оцифрованы (у Artsonia 138 млн работ), а себестоимость ролика < $1 |
| **Быстрый: «платформы съедают всё»** | 25% | **20%** | Платформы демонстративно отказываются от реальных лиц: CapCut Seedance, откат Meta Muse Image, блок детей в Veo. «Рисунок оживает» они съедят, а «ребёнок + рисунок» — вряд ли |
| **Медленный: «регуляторика тормозит»** | 20% | **30%** | TikTok $400 млн по COPPA, EU Kids Act, запреты штатов, давление на сторы — всё это уже в 2026 году |

**Новые или уточнённые опережающие сигналы (как мониторить).**
1. **CrUX ежемесячно** (второй вторник месяца, [zakird/crux-top-lists](https://github.com/zakird/crux-top-lists), бесплатно, 5 минут скриптом): (а) вошёл ли кто-то из AI-«оживителей» в US или GB top-1M — значит, появился победитель с тягой; (б) sketch.metademolab.com — выпал из top-1M, значит, демо закрыто; (в) пики shop.square1art.com, arttoremember.com и artsonia.com как календарь B2B-сезонов.
2. **Сайты Artsonia, Square 1 Art, Original Works, Art to Remember**: появились ли «animated», «video», «AR» в каталоге товаров. Проверять раз в квартал, перед сезонами — в январе и августе.
3. **Регуляторика**: FTC и DOJ по COPPA, судьба EU Kids Act и KIDS Act, законы штатов о биометрии (IL BIPA, TX CUBI). Мониторить новостные дайджесты с фильтром «COPPA | Kids Act | biometric».
4. **Дистрибуция**: правила рекомендаций для AI-контента в Snapchat, Instagram, TikTok. Если в TikTok появится аналогичное понижение AI-контента, ставка на органический охват неверна.

---

## Идеи-кандидаты: новые и уточнённые

### 1. (Уточнено) «Оживший вернисаж» — школьный и детсадовский фандрайзер, только рисунки
- **Суть:** учитель загружает рисунки класса. Родители и бабушки с дедушками покупают по ссылке ролик, открытку с QR или «фильм выставки». Школа получает долю.
- **Тип:** AB. **Формат:** веб-каталог для родителей + печать через PoD + личный кабинет учителя.
- **Покупатель и боль:** арт-учитель или PTA хотят фандрайзер без возни; родители — сувенир с работой ребёнка.
- **Доказательства спроса:** Square 1 Art приносит школам ~$7 млн в год; Artsonia — 50 000+ школ, 10 млн+ работ в год, US top-5k по трафику; Art to Remember — 11 545 школ; пики трафика в марте–апреле и октябре–ноябре (п. 4, раздел В).
- **Экономика (оценка):** рынок уже задал долю школы **25–38% (до 50%)**, а не 15–25%, как в оригинале. Продукт за $10–20 с долей 30% и себестоимостью ролика ~$1,4 оставляет ~55–60% валовой маржи до печати (оценка, средняя).
- **Конкуренты:** Square 1 Art (товары $5–60), Original Works (многие < $15), Artsonia (кружка $18,95+, 20% школе), Art to Remember, Created by Kids. Видео ни у кого не найдено.
- **Моат:** отношения с учреждениями, согласия и приватность только для рисунков, сезонный ритуал.
- **Главный риск:** **инкумбенты сами добавят анимацию** (40–60% к 09.2028, оценка). Кроме того, это продажи в школы США из Бали: длинный цикл и минимум 150 работ на программу.

### 2. (Новое) White-label модуль «animated keepsake» для арт-фандрайзеров и сервисов детских книг
- **Суть:** не конкурировать с Artsonia и Square 1 Art, а **продать им модуль**: API или встраиваемый виджет «оживить рисунок» + страница с QR + шаблоны уровня моушн-дизайна. Оплата за ролик ($0,5–2) или доля выручки.
- **Тип:** AB. **Формат:** B2B2C API + админка + библиотека AE-шаблонов.
- **Покупатель и боль:** продуктовые команды фандрайзеров и сервисов архивов (Artkive, Plum Print, Chatbooks). Им нужен новый SKU с высокой маржой к сезону, а экспертизы по генеративному видео и детской приватности нет.
- **Доказательства спроса:** у покупателей уже есть поток оцифрованных детских работ (138,7 млн у Artsonia; 9,2 млн у Art to Remember) и сезонные пики (раздел В). Прямого спроса на такой модуль **нет данных**, нужны 3–5 интервью.
- **Конкуренты:** их собственные команды с AI-кодингом; горизонтальные API (fal, Replicate, Higgsfield, Magnific), где нет готового детского пресета [П, оригинал].
- **Моат:** контракты и интеграции, качество «рисунок остаётся рисунком» (гибрид риг-анимации и генерации), соответствие COPPA и GDPR-K, скорость обновления шаблонов под сезоны.
- **Главный риск:** покупателей всего 5–10, у каждого длинный цикл решения, и каждый может собрать то же сам за месяц. Для основателя с 2–4 часами в неделю B2B-интеграции — высокая нагрузка на поддержку.

### 3. (Уточнено) «Письмо от внука» — физическая открытка, постер или мини-книга с QR → видео, только рисунки
- **Тип:** A. **Формат:** веб (оплата через MoR) + печать через PoD + страница с видео без приложения.
- **Покупатель и боль:** родители покупают, бабушки и дедушки получают. Хочется подарок «с ребёнком внутри» без технических сложностей.
- **Доказательства спроса и ценовые ориентиры:** Artkive от $89,99, Plum Print $175–210, Budsies до $150, Crayon Creatures €99 (п. 3). Подарочный пик в ноябре–декабре: Shutterfly — US top-1k, Postable — top-5k, Aura Frames — top-10k в декабре 2025 [CrUX]. У Storyworth (подарок «память семьи») — US top-5k–10k круглый год [CrUX].
- **Конкуренты:** Draw & Animate и Once Upon a Drawing (печать + видео, цены н/д) [П, оригинал]; DrawToLife ($34,99 в год, цифровой продукт); Etsy-листинги «Custom Kids' Drawing Animation» (цены н/д).
- **Моат:** средний: бренд, упаковка, операционная надёжность, отзывы. Вариант с **цифровыми рамками** (Aura, Skylight, Nixplay) как каналом доставки видео бабушкам — **гипотеза**: поддержку видео и API в сессии не проверял.
- **Главный риск:** до окна Рождества 2026 года осталось ~5–7 недель на сборку (заказы с ~1 ноября). Цифровые конкуренты дешевле в 3–5 раз. Логистика PoD и возвраты.

### 4. (Понижено) Потребительское приложение «загрузи рисунок → получи клип»
- **Статус:** **не делать как отдельный продукт.** Около 30 известных игроков, цены $3,75 в месяц — $35 в год, ни у одного веб-сайта нет трафика уровня top-1M. Бесплатные альтернативы: демо Meta, Toontastic, homiwork, Google Photos, TikTok AI Alive. Органическая дистрибуция AI-контента дорожает (Snapchat, Instagram).
- Имеет смысл только как **входная воронка** для идей 1–3.

---

## Источники

1. Animated Drawings — Terms of Service (некоммерческое использование, без IL и TX), https://sketch.metademolab.com/terms — проиндексировано 2026-09-26 (дата страницы н/д)
2. Animated Drawings — главная и canvas, https://sketch.metademolab.com/ ; https://sketch.metademolab.com/canvas — проиндексировано 2026-09-26
3. zakird/crux-top-lists — Chrome UX Report Top-1M, глобальные (2022-12 → 2026-08) и по странам (US 2025-01 → 2026-08; GB, CA, AU), https://github.com/zakird/crux-top-lists — скачано 2026-09-26
4. Animomo — сайт и Google Play, https://www.animomo.app/ ; https://play.google.com/store/apps/details?id=com.igloola.Animomo&hl=en — проиндексировано 2026-09
5. DrawToLife — сайт, сравнение, блог, https://draw-to-life.com/ ; https://draw-to-life.com/compare/ ; https://draw-to-life.com/blog/best-apps-bring-kids-drawings-to-life/ — 2026
6. DrawToLife — App Store и Google Play, https://apps.apple.com/us/app/draw-to-life-kids-ai-art/id6752760587 ; https://play.google.com/store/apps/details?id=com.nomadlink.drawtolife&hl=en-US — проиндексировано 2026-09
7. Gimba — сайт и Google Play, https://gimba.app/ ; https://play.google.com/store/apps/details?id=com.yellowsquirrel.gimba&hl=en_US — проиндексировано 2026-09
8. KidsAI, https://kidsai.art/ ; https://kidsai.art/animate-drawing.html — проиндексировано 2026-09
9. Revid.ai — Animate kids drawing, https://www.revid.ai/tools/animate-kids-drawing — проиндексировано 2026-09
10. Drawings Alive — сайт и App Store, https://drawingsalive.com/ ; https://apps.apple.com/us/app/drawings-alive-ai-doodle-art/id6749238166 — проиндексировано 2026-09
11. Drawmingo, https://drawmingo.com/ — проиндексировано 2026-09
12. Doodle Dreams, https://doodledreams.cc/ — проиндексировано 2026-09; Show HN, https://news.ycombinator.com/item?id=42524848 — 2024-12-29
13. AniMagic — App Store и MWM, https://apps.apple.com/us/app/animagic-animate-drawings/id6448135645 ; https://mwm.ai/apps/animagic-animate-drawings/6448135645 — проиндексировано 2026-09
14. Dodoboo — отзывы на Product Hunt, https://www.producthunt.com/products/dodoboo/reviews — 2026
15. Homiwork — Animate Drawing, https://homiwork.com/en/app/aiclips/create/animate-drawing — проиндексировано 2026-09
16. doodlar, https://doodlar.co/ ; Todrawn pricing, https://todrawn.com/pricing — проиндексировано 2026-09
17. Animated Drawing (клоны), https://play.google.com/store/apps/details?id=com.companyname.animateddrawings ; https://apps.apple.com/us/app/animated-drawing/id6469684346 — проиндексировано 2026-09
18. Ai Motions, https://apps.apple.com/us/app/ai-motions-animate-drawings/id6461773689 ; AniToon, https://apps.apple.com/us/app/anitoon-draw-art-animate/id6476550987 — проиндексировано 2026-09
19. KidsAiTools — AI Animation Tools for Kids: 6 Apps Compared (2026), https://www.kidsaitools.com/en/articles/ai-animation-tools-for-kids — ~2026-08
20. Budsies — How much does a custom plush cost, https://www.budsies.com/custom-plush-cost/ ; Pricing, https://www.budsies.com/pricing/ — проиндексировано 2026-09
21. CertifiKID — Budsies deal $59 ($99 value), https://www.certifikid.com/deal/10779/59-for-custom-stuffed-animal-designed-by-you-9 — дата н/д
22. Child's Own — Softie Create и Pricing, https://www.childsown.com/softie-create/ ; https://www.childsown.com/pricing/ — проиндексировано 2026-09
23. Daily Meal — Child's Own Studio, https://www.thedailymeal.com/let-childs-own-studio-transform-your-kids-drawing-unique-plush-toy/ — дата н/д; Baby Gizmo, https://babygizmo.com/turn-childs-drawing-stuffed-toy/ — дата н/д
24. New Atlas — Crayon Creatures, https://newatlas.com/crayon-creatures-childrens-drawings/25700/ — 2013; 3DPrint.com, https://3dprint.com/238874/turn-your-kids-2d-drawing-into-a-3d-printed-sculpture/ — 2019
25. ForeverArtKids — Artkive Alternatives (2026), https://foreverartkids.com/guides/artkive-alternative/ — 2026
26. Artkive FAQ — pricing, https://faq.artkiveapp.com/hc/en-us/articles/360025758991-How-does-pricing-work-for-the-Artkive-Box — проиндексировано 2026-09
27. Plum Print — Pricing, https://www.plumprint.com/pages/pricing — 2026
28. Keepy — App Store, https://apps.apple.com/us/app/keepy-artwork-schoolwork/id647088205 ; ArtShow blog, https://artshow.app/blog/save-your-kids-art-here-are-the-best-apps-to-try/ — 2025
29. QuiverVision — Subscribe, https://quivervision.com/subscribe ; AppBrain Quiver, https://www.appbrain.com/app/quiver-3d-coloring-app/com.puteko.colarmix ; Educational App Store, https://www.educationalappstore.com/app/quiver-education-3d-coloring-app — проиндексировано 2026-09
30. AppBrain — Crayola Color Alive (снят 2018-06-05, 2,2 млн загрузок), https://www.appbrain.com/app/crayola-color-alive/com.DAQRI.crayola.coloralive — проиндексировано 2026-09
31. Square 1 Art — Free Product Program (тарифы с 2026-01-01), https://www.square1art.com/free-product-program/ ; FAQ, https://www.square1art.com/faq/ ; About Us, https://www.square1art.com/about-us/ — 2026
32. ZoomInfo — Square 1 Art (выручка $7,1 млн, оценка третьей стороны), https://www.zoominfo.com/c/square-1-art-llc/112886203 — 2026
33. Original Works — Top reasons, https://www.originalworks.com/top-reasons-to-choose-original-works/ ; All products, https://www.originalworks.com/all-products/ — дата н/д
34. Artsonia — About, Teachers, Awards, Gift Shop, https://www.artsonia.com/about/ ; https://www.artsonia.com/teachers/ ; https://www.artsonia.com/schools/awards/ ; https://www.artsonia.com/gifts/ — проиндексировано 2026-09
35. Artsonia Help — Fundraising Promotion (20%), https://help.artsonia.com/hc/en-us/articles/115000423273-What-is-the-Artsonia-Fundraising-Promotion — дата н/д
36. Art to Remember — Fundraisers, https://atr.arttoremember.com/fundraisers/ ; https://arttoremember.com/about/fundraisers/ — дата н/д
37. Created by Kids (Канада), https://createdbykids.ca/ — дата н/д
38. Etsy — Custom Kids' Drawing Animation, https://www.etsy.com/listing/1763280459/custom-kids-drawing-animation-turn-kids ; Child Drawing Animation Kit, https://www.etsy.com/listing/1558930212/bringing-kids-art-to-life-child-drawing ; плюш по рисунку, https://www.etsy.com/listing/236677801/custom-plush-from-drawing-custom-plush ; https://www.etsy.com/listing/508819199/stuffed-animal-from-drawing-budsies — проиндексировано 2026-09
39. Fiverr — Cartoon animation, https://www.fiverr.com/gigs/cartoon-animation ; гиг за $15, https://www.fiverr.com/qosain_ali/do-animated-content-2d-cartoon-animation-video-character-2d-animation-for-kids — проиндексировано 2026-09
40. TechCrunch — Seedance 2.0 comes to CapCut (защита от реальных лиц), https://techcrunch.com/2026/03/26/bytedances-new-ai-video-generation-model-dreamina-seedance-2-0-comes-to-capcut/ — 2026-03-26
41. TechCrunch — How to stop Meta's AI image generator (Muse Image), https://techcrunch.com/2026/07/09/how-to-stop-metas-ai-image-generator-from-using-your-instagram-photos/ — 2026-07-09; The Next Web — Meta killed Muse Image, https://thenextweb.com/news/meta-muse-image-instagram-privacy-backlash-pulled — 2026-07-13
42. PetaPixel — Apple's all-new Image Playground, https://petapixel.com/2026/06/08/apples-all-new-image-playground-promises-more-than-cartoons/ — 2026-06-08
43. TechCrunch — Google Photos Video Remix, https://techcrunch.com/2026/07/08/google-photos-adds-a-new-ai-video-remix-tool/ — 2026-07-08
44. TechCrunch — TikTok AI Alive, https://techcrunch.com/2025/05/13/tiktok-launches-tiktok-ai-alive-a-new-image-to-video-tool/ — 2025-05-13 (через `consumer_apps.md`)
45. 9to5Google — Google Photos photo-to-video, https://9to5google.com/2025/07/23/google-photos-photo-to-video/ — 2025-07-23; The Verge — text prompts, https://www.theverge.com/news/868510/google-photos-image-to-video-text-prompt-support — 2026-01-27 (через `consumer_apps.md`)
46. X/@soraofficialapp — Goodbye to Sora, https://twitter.com/soraofficialapp/status/2036532795984715896 — 2026-03-24; Ars Technica — Disney $1B, https://arstechnica.com/ai/2026/03/the-end-of-sora-also-means-the-end-of-disneys-1-billion-openai-investment/ — 2026-03-25
47. The Verge — YouTube Shorts Remix на Gemini Omni, https://www.theverge.com/tech/934704/google-gemini-omni-youtub-shorts-remix-ai — 2026-05-20
48. TechCrunch — Gemini features on Google TV (Nano Banana, Veo), https://techcrunch.com/2026/04/29/more-gemini-features-are-coming-to-google-tv/ — 2026-04-29
49. TechCrunch — Snapchat no longer rewards fully AI-generated Spotlight content, https://techcrunch.com/2026/07/31/snapchat-no-longer-rewards-fully-ai-generated-spotlight-content/ — 2026-07-31
50. TechCrunch — Instagram limits undisclosed AI profiles, https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/ — 2026-08-31
51. The Verge — TikTok $400M COPPA settlement, https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa — 2026-08-21
52. TechCrunch — Meta $18B settlement and kids' data, https://techcrunch.com/2026/08/27/buried-in-metas-18b-settlement-is-a-legal-pass-on-kids-data/ — 2026-08-27
53. Ars Technica — Minnesota nudify ban ($500K), https://arstechnica.com/tech-policy/2026/05/minnesota-set-to-be-first-state-to-ban-nudification-apps/ — 2026-05-01; TechCrunch — judge denies xAI, https://techcrunch.com/2026/08/01/judge-denies-xais-request-to-block-minnesota-ban-on-nudify-apps/ — 2026-08-01
54. TechCrunch — San Francisco orders Apple and Google to purge nudify apps, https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/ — 2026-07-17
55. Ars Technica — Meta ads with real photos of teen girls, https://arstechnica.com/tech-policy/2026/09/real-photos-of-young-girls-were-in-nudify-app-ads-on-facebook-instagram/ — 2026-09-08
56. Wired — EU Kids Act (соцсети до 13 лет), https://www.wired.com/story/the-eu-bans-social-media-for-under-13s/ — 2026-09-16; Wired — EU Kids Act и чат-боты, https://www.wired.com/story/the-eu-wants-to-break-up-kids-and-their-chatbots/ — 2026-09-17
57. EFF — KIDS Act age checks, https://www.eff.org/deeplinks/2026/06/kids-act-would-require-age-checks-get-online — 2026-06-28
58. The Verge — NY SAFE for Kids Act rules, https://www.theverge.com/policy/972007/new-york-safe-for-kids-act-age-verification — 2026-07-28
59. WebsiteLaunches — 2026-09-24 (новых сайтов «детский рисунок» нет), https://raw.githubusercontent.com/WebsiteLaunches/daily-website-launches/main/2026/09/2026-09-24.md — 2026-09-24
60. Параллельный поток `consumer_apps.md` (платформенные факты, RevenueCat и Adapty, a16z), 2026-09-26
