# Поток 12, дополнение: разведка спроса, проверка и новые данные

Дата: 2026-09-26. Дополняет файл `demand_scout.md`. Неизменённое содержание оригинала здесь не повторяется.

**Как собирались данные.** Лимит веб-поиска всей сессии (200 запросов) закончился после ~45 запросов этого дополнения. Дальше использовались три канала: GitHub MCP (поиск репозиториев и кода, точные счётчики), WebFetch к github.com и raw.githubusercontent.com, а также read-only каталоги моделей Magnific и Higgsfield через MCP (список моделей и `simulate_cost` без списания кредитов). Reddit, Upwork, YouTube и страницы товаров aescripts, Figma, Gumroad и Envato напрямую не читались. Цифры с этих сайтов взяты из поисковых сниппетов по указанным URL. «д.д.» означает дату доступа, если на странице нет даты публикации.

---

## Проверено и исправлено

### Исправлено (в оригинале была ошибка или устаревшие данные)

1. **«Переноса анимации Figma Motion в AE у конкурентов не найдено» (идея 1 оригинала) — ОШИБКА.**
   - **UXLink** на aescripts переносит «дизайн и моушн между Figma и After Effects в два клика, в обе стороны, сохраняя структуру и анимацию» ([aescripts UXLink](https://aescripts.com/uxlink/), д.д. 2026-09-26). Официальный пост aescripts анонсирует: «UXLink now supports Figma Motion — send your anima[tion]…» ([Facebook aescripts](https://www.facebook.com/aescripts/videos/made-with-uxlink-by-pathlink2025-uxlink-now-supports-figma-motionsend-your-anima/2881170892264345/), 2026).
   - Плагин LottieFiles экспортирует работы Figma Motion в Lottie/dotLottie ([LottieFiles docs](https://docs.lottiefiles.com/en/integrations/figma/04_figma-to-lottie/figma-motion-export), 2026). В Figma Community есть отдельный плагин «Figma Motion to Lottie (Beta)» ([Figma Community](https://www.figma.com/community/plugin/1653028369274786320/figma-motion-to-lottie-beta), 2026).
   - **Вывод:** ниша «Figma Motion → AE» занята примерно через 2–3 месяца после запуска Figma Motion (24.06.2026). Уникальность идеи 1 в исходной формулировке исчезла.

2. **«Plugin API Figma может не давать доступа к таймлайну Motion (нет данных)» — ЗАКРЫТО, доступ есть.**
   - С Version 1, Update 127/130 (23.06.2026) Plugin API позволяет «читать и обновлять данные Motion: стили анимации, таймлайны, анимации и ручные треки ключей» ([Figma Dev Docs, Update 127](https://developers.figma.com/docs/plugins/updates/2026/06/23/version-1-update-127/), 2026-06-23; [figma.motion](https://developers.figma.com/docs/plugins/api/figma-motion/), д.д. 2026-09-26). API помечен как **Beta**.
   - Ограничения из официального навыка Figma MCP ([figma/mcp-server-guide, motion-patterns.md](https://raw.githubusercontent.com/figma/mcp-server-guide/main/skills/figma-use-motion/references/motion-patterns.md), д.д. 2026-09-26):
     - «node.animations reflects manual-keyframe tracks only at present»: пресеты (animation styles) пока не разворачиваются в ключи;
     - анимируются только SOLID-заливки;
     - 3D-трансформы и `VARIANT_PROPERTIES` намеренно выдают ошибку;
     - нельзя анимировать фреймы верхнего уровня.
   - **Важно для Oblique:** в allowlist входят параметры эффектов, в том числе стекла: `REFRACTION_RADIUS`, `REFRACTION_INTENSITY`, `SPECULAR_ANGLE/INTENSITY`, `CHROMATIC_ABERRATION`, `SPLAY`, `RADIUS`, `NOISE_SIZE`, `DENSITY`. **Анимацию стекла, блюров и теней из Figma технически можно прочитать и перенести.** Это единственное найденное место, где у Oblique ещё может быть техническая глубина (см. идею N1).

3. **Overlord: «ранее $45» — неточно.** Цена v1 была **$55** (Toolfarm $52,25). При выходе v2 Battle Axe объявила повышение на **$20**, то есть ≈ **$75** (оценка, средняя уверенность: на страницу оформления заказа попасть не удалось). Overlord 2 — отдельное приложение, в анонсе: «скоро будет работать с Figma» ([Toolfarm](https://www.toolfarm.com/news/battle-axe-overlord-2-coming/), 2024; [X Battle Axe](https://x.com/battleaxedotco/status/1815816822903451995), 2024-07; [Battle Axe Lore](https://lore.battleaxe.co/overlord-2-is-here/), д.д.).

4. **«Около 6 конкурентов Oblique» — занижено.** На 26.09.2026 насчитывается **не менее 9 коммерческих или freemium-инструментов и не менее 11 open-source-репозиториев, созданных в 2026 году** (полная таблица в разделе «Новые факты», блок A). Нижняя граница цены опустилась с $39 до **бесплатно и ≈$6,5** (AEShiper, оценка по курсу). Исходный тезис оригинала подтверждается и даже усиливается: мост Figma→AE **уже** стал товаром (commodity), а не станет им «через 12 месяцев».

5. **Цена Convertify «не получена» → получена.** Convertify Pro (Hypermatic) стоит **$49/мес за пользователя**, есть бесплатный план. Пакет всех плагинов Hypermatic — **$83 за пользователя в месяц** ([Hypermatic Gumroad](https://hypermatic.gumroad.com/l/convertify), д.д.; [Hypermatic Bundle](https://www.hypermatic.com/bundle/), д.д. 2026-09-26). Это единственный подписочный игрок в категории.

### Подтверждено с уточнениями

6. **Figma Motion и HD-экспорт за Full seat — подтверждено и уточнено.**
   - Motion экспортирует MP4, WebM, GIF и анимированный SVG. В открытой бете функция доступна всем с правом редактирования, на любом плане.
   - Бесплатно размер ограничен **1080×1080 при 30 fps**. Большие разрешения и частоты, публикация анимированных компонентов и генерация агентом требуют **Full seat** ([Figma Help: Export animations](https://help.figma.com/hc/en-us/articles/41307983648407-Export-animations-from-Figma), д.д.; [Medium, Sina Rad](https://medium.com/@sinarad.me/figma-motion-the-5-minute-guide-4e3560c3b7f1), 2026-09; [AlternativeTo](https://alternativeto.net/news/2026/6/figma-launches-a-new-integrated-motion-design-tool-alongside-code-layers-and-new-ai-features/), 2026-06).
   - Нативный экспорт в Lottie Figma обещает «в будущем» ([Figma Help](https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta), д.д.).

7. **Рост числа новых AE-репозиториев — подтверждён, и рост ускоряется.** Поквартально (GitHub search `"after effects" created:`, д.д. 2026-09-26):
   - Q1 2026 — **218**, Q2 — **518**, Q3 (по 26.09) — **596**, в сумме ~1 332 (оригинал: ~1,3 тыс., совпадает);
   - Q3 2025 — **111**, то есть за год **×5,4**;
   - по «figma plugin»: Q3 2026 — **394** против **226** в Q3 2025 (**×1,7**).
   - Поправка: часть репозиториев — SEO-спам и кряки. Самый «звёздный» AE-репозиторий Q2 2026 (580 звёзд) — страница с топиками `after-effects-2026-crack` ([GitHub](https://github.com/StuccoFlame85/Adobe-After-Effects), 2026-06).

8. **Число MCP-серверов для AE — подтверждено:** 67 по имени и описанию (в оригинале 72 по более широкому запросу). Лидер Dakkshin/after-effects-mcp — 657 звёзд. В августе 2026 появился kumoproductions/mcp-aftereffects (69 звёзд за 7 недель, умеет рендер отдельных кадров). Для Premiere Pro — **48 MCP-репозиториев**, лидер hetpatel-11 набрал 609 звёзд, а ayushozha заявляет «1 027 инструментов» ([GitHub search](https://github.com/search?q=after+effects+mcp&type=repositories); [Premiere MCP](https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP), д.д. 2026-09-26).

9. **Анаморфные инструменты на GitHub — подтверждено:** по-прежнему **1 репозиторий** (anamorphic-mask-service, 0 звёзд, 08.2026). По «forced perspective / 3d billboard / naked eye 3d» находится 63 репозитория, почти все про игры и демо, производственных инструментов нет ([GitHub](https://github.com/Thomasine723/anamorphic-mask-service), д.д. 2026-09-26).

### Не перепроверено (лимит поиска)

Релизы AE 26.0–26.5, статус AI Assistant, цены Plainly, Nexrender и Templater, цены на субтитры. Источники оригинала (CG Channel, Adobe Community, Capterra) остаются в силе.

---

## Новые факты

### A. Мост Figma → AE: полная карта на 26.09.2026

| Инструмент | Модель и цена | Что важно | Источник |
|---|---|---|---|
| AEUX (Google) | бесплатно, **архив с 06.2025** | бывший стандарт | оригинал, факт 9 |
| Overlord 2 (Battle Axe) | v1 $55 → v2 ≈$75 (оценка) | отдельное приложение, AI/PS/Figma | [Toolfarm](https://www.toolfarm.com/news/battle-axe-overlord-2-coming/), 2024 |
| Prism (Next Horizon) | **от $39** разово (Starter — 1 машина; Duo, Team) | Figma, PS, AI, AE и Resolve | [Next Horizon](https://nexthorizon.art/store/figma-to-ae), д.д. |
| Convertify (Hypermatic) | **$49/мес**, есть free | подписка | [Hypermatic](https://hypermatic.gumroad.com/l/convertify), д.д. |
| **UXLink** (aescripts) | цена не получена | **в обе стороны + Figma Motion** | [aescripts](https://aescripts.com/uxlink/), 2026 |
| **UI Flow** (aeflowtools) | **10 экспортов в день бесплатно** + lifetime на Gumroad (цена не получена) | v22 от **09.09.2026**: часто обновляется | [Figma Community](https://www.figma.com/community/plugin/1605150908629430996/ui-flow-figma-to-after-effects), 2026-09-09; [Gumroad](https://aeflowtools.gumroad.com/l/uiflowkey) |
| DEmotion | разовая оплата (цена не получена) | ведёт SEO-блог «AEUX vs DEmotion» | [trydemotion.com](https://trydemotion.com/), д.д. |
| MotionPotion | free: 5 импортов и 5 экспортов в мес; Wizard — годовая подписка | 5 плагинов + 168 «рецептов» для AE и Figma | [motionpotion.co/pricing](https://motionpotion.co/pricing), д.д. |
| AEShiper | **799 BDT** разово (≈$6,5, оценка по курсу ~122 BDT/$) | ценовой демпинг из Бангладеш | [aeshiper.com](https://aeshiper.com/), д.д. |
| Oblique (основатель) | $59 → $69 | стекло, блюры, эффекты | — |

**Open-source-клоны, созданные в 2026 году** (GitHub, д.д. 2026-09-26):
- fae (03.2026);
- UI-FLow (04.2026);
- figma-ae-bridge (05.2026, в обе стороны);
- karly-herrera/after-effects-mcp (05.2026, «Figma → AE pipelines»);
- figma-to-after-effect (06.2026);
- svg-splitter (07.2026);
- OverAE (08.2026);
- evotechly-motion-os (09.2026);
- transporter-app (09.2026);
- Luma (09.2026);
- **LazyLord (16.09.2026): «A full replacement for Overlord, free forever»**.

Итого 11 репозиториев, из них **4 в одном сентябре** ([GitHub search](https://github.com/search?q=figma+after+effects+created%3A%3E2026-01-01&type=repositories); [LazyLord](https://github.com/raisulsohan/LazyLord)). У всех 0–2 звезды: продукты сырые, но ценовой якорь «бесплатно» уже существует.

### B. Экосистема Figma Motion за 3 месяца

- **65 репозиториев** со словами «figma motion», созданных после 20.06.2026. Большинство — Claude/Codex-навыки: figma-motion-director, figma-motion-storyboard, awesome-ui-motion-skills. Есть «Bounce» (физика и пружины в Figma) ([GitHub search](https://github.com/search?q=figma+motion+created%3A%3E2026-06-20&type=repositories), д.д. 2026-09-26).
- Официальный репозиторий Figma **mcp-server-guide (≈2 тыс. звёзд)** содержит навык `figma-use-motion`: AI-агент анимирует прямо в Figma ([GitHub](https://github.com/figma/mcp-server-guide/tree/main/skills/figma-use-motion), д.д.). Спрос на «экспорт в AE ради анимации UI» будет сокращаться (оценка, средняя уверенность).
- Конкуренты-плагины внутри Figma:
  - Motionkit — бесплатный, MP4/GIF/PNG/Lottie ([Medium](https://medium.com/@codeideal/the-secret-free-motion-design-animation-plugin-inside-figma-1578f527ce98), 2026);
  - Motion Export — анимации в код и видео ([motionexport.com](https://motionexport.com/), д.д.);
  - TinyImage от Hypermatic — пакетный экспорт слоёв Figma Motion в GIF/MP4 ([Hypermatic](https://www.hypermatic.com/tutorials/how-to-bulk-export-figma-motion-layers-to-gif-and-mp4-video-using-tiny-image/), 2026).

### C. Экономика маркетплейсов: цены «вечнозелёных» продуктов (закрывает «нет данных» оригинала)

| Продукт | Цена | Модель | Источник |
|---|---|---|---|
| Plexus 3 (Rowbyte) | **$249,99**; апгрейд с v2 $99,99, с v1 $149,99 | разово + платные мажорные версии | [aescripts](https://aescripts.com/plexus/), д.д. |
| GEOlayers 3 | апгрейд с v2 **$205** (SUL), с v1 $255; новая лицензия — нет данных | разово + платный апгрейд; есть floating и подписка у реселлеров | [aescripts](https://aescripts.com/geolayers/); [Insight](https://www.insight.com/en_US/shop/product/MB-GEO-FL/aescripts/MB-GEO-FL/Aescripts-GEOlayers-3-for-After-Effects-subscription-license-3-floating-license/) |
| Lockdown 4 | апгрейд с v3 **$100**, бесплатно для купивших после 03.02.2026 | теперь AE + C4D + Blender + Maya + Houdini | [aescripts](https://aescripts.com/lockdown/), 2026-02 |
| Newton 4 | апгрейд с v3 **$99,99**, студентам −50% | разово | [aescripts](https://aescripts.com/newton/), д.д. |
| Deep Glow 2 | $99,95 (V1 — $49,95) | см. оригинал | оригинал, факт 18 |

**Вывод.** Самые дорогие продукты aescripts стоят $100–250, их зарабатывающая модель — **платные мажорные апгрейды каждые 2–4 года** ($99–205). Lockdown 4 вышел за пределы AE в 5 3D-программ. Рост идёт за счёт **кросс-DCC-охвата**, а не новых функций в одной программе.

**Videohive (Envato Market):**
- лидеры продаж среди AE-скриптов стоят **$22–35**, product-promo-шаблоны — **$14–49** ([Videohive scripts](https://videohive.net/popular_item/by_category?category=add-ons%2Fafter-effects-scripts); [Videohive promo](https://videohive.net/popular_item/by_category?category=after-effects-project-files%2Fproduct-promo), д.д. 2026-09-26);
- в категории AE Scripts всего **154 позиции**, в Scripts & Presets — 500+. Это небольшой рынок по сравнению с aescripts.

### D. Envato и Motion Array: какие шаблоны нужны (закрывает «нет данных»)

- **Самый скачиваемый видеошаблон Envato 2025 года** — «The Most Useful Transitions Pack for Premiere Pro» (Premiumilk), **106 000 скачиваний** ([Envato Unpacked 2025](https://elements.envato.com/learn/envato-unpacked), 2025-12; [Author Hub](https://author.envato.com/hub/most-popular-items-of-2025/), 2025-12). Лидер рынка — **Premiere-пакет простых переходов**, а не сложный AE-проект.
- **Главный разрыв спроса и предложения по данным Envato:** поиск «stylish packages» вырос на **+410%** (среднесуточные поиски за квартал), при этом до скачивания доходят лишь **6,2%**. Клиенты ищут **наборы в одном дизайн-языке** (переходы, интро, lower thirds, оверлеи) — «a branded world rather than standalone assets». Устойчиво высокий интерес к «vertical», «Instagram», «Reel», «TikTok» ([Envato Author Hub, Video Templates insights Dec 2025](https://hub.author.envato.com/video-templates-content-insights-december-2025/), 2025-12).
- **Envato урезает AI внутри подписки.**
  - До 25.02.2026 генерации были безлимитными. После этой даты введены лимиты: Core — 10 в месяц, Plus — 100 в месяц.
  - С 17.08.2026 действует система кредитов: Core — 20 в месяц, Plus — 200 в месяц.
  - В апреле 2026 в VideoGen добавлен **Seedance 2.0**.
  - Источники: [Envato Help](https://help.elements.envato.com/hc/en-us/articles/60055181647513-Updates-to-Envato-s-AI-Credit-Structure), 2026-08; [Envato Help](https://help.elements.envato.com/hc/en-us/articles/53370106288281-Updates-to-Gen-AI-Access-in-Your-Envato-Subscription), 2026-02.
  - Вывод: AI-генерация дорога даже для платформ, а стоковые шаблоны остаются основным продуктом подписки.
- **Motion Array (принадлежит Artlist):**
  - Everything — **$24,99/мес** при годовой оплате ($39,99 помесячно);
  - Video Templates — **$15,99/мес**;
  - Teams — $323,99 в год за человека;
  - Artlist — $39,99/мес.
  - Источник: [Photutorial](https://photutorial.com/motion-array-pricing/), 2026.
  - Шаблон как отдельная единица почти ничего не стоит для покупателя: $16–25 в месяц за весь каталог.

### E. Figma Community и Product Hunt (частично закрывает «нет данных»)

- **Комиссия Figma Community — 15%.** Модель (разовая покупка или подписка) выбирается при публикации и **потом не меняется** ([Kelviq](https://www.kelviq.com/blog/figma-plugin-monetization/), 2026; [Dodo Payments](https://dodopayments.com/blogs/sell-figma-plugins), 2026). Для сравнения: у aescripts 30%.
- Топ платных плагинов Figma по выручке или установкам: **нет данных**. Прокси (старый датасет без даты, вероятно 2021–2022, низкая уверенность): 98 из 1 079 плагинов были платными (9%), на них приходилось 14,7% установок и 17,7% лайков ([GitHub yuanqing](https://github.com/yuanqing/figma-plugins-monetization-stats), д.д.). Платные плагины получают непропорционально больше вовлечённости.
- **Product Hunt 2026** ([LaunchList](https://getlaunchlist.com/blog/how-to-launch-on-product-hunt-2026), 2026; [TrendGap](https://trendgap.io/blog/product-hunt-launch-upvotes-rank-2026), 2026):
  - для топ-5 дня нужно ~300–500 апвоутов в будний день (500–900 в 2025 году), для #1 — 1 200–1 800;
  - алгоритм в 2026 году сильнее штрафует низкую вовлечённость.
  - Запусков AE- или Figma-to-AE-инструментов с данными об апвоутах найти не удалось (**нет данных**). Для нишевого плагина PH — слабый канал (оценка).

### F. AI-видео: платформы поглощают «подготовку плейтов» (важно для идеи 5 оригинала)

- В каталоге **Higgsfield** (MCP, запрос 2026-09-26) есть:
  - **Video Deflicker**;
  - **Topaz** (1080p/2160p с опциональной интерполяцией кадров);
  - **Bytedance Video Upscale** с пресетом **«aigc»** до 4K и 24–60 fps;
  - **удаление фона по видео (SAM 3)**;
  - Kling 3.0 Omni Edit;
  - FLUX 3 Video Edit;
  - «**Ad Multiplier**» (варианты рекламы на базе Seedance 2.5).
- В каталоге **Magnific** (MCP, 2026-09-26) — **46 видеомоделей**, а также инструменты video_upscale, video_hdr, video_relight, video_color_grade, video_color_transfer, video_motion_shake и **design_auto_resize**.
- **Вывод:** дефликер, апскейл, интерполяция, color transfer и ротоскоп-альфа — уже функции «в один клик» внутри генеративных платформ. Идея «AI Plate Prep» в оригинале оценивалась как «частично решат за 24 мес (50%)». По новым данным частично решено **уже сейчас**. Понижаю: вероятность нативного решения в течение 24 месяцев — ~75% (оценка, средняя уверенность).

### G. Цены AI-видео непрозрачны (данные для B-идеи «калькулятор»)

- Кредиты Magnific через `simulate_cost` на 26.09.2026, точные значения:

  | Модель | Параметры | Кредиты | Кредитов в секунду |
  |---|---|---|---|
  | Seedance 2.0 Pro | 1080p, 5 с | **3 500** | 700 |
  | Veo 3.1 | 1080p, 8 с | **1 600** | 200 |
  | Wan 3.0 | 1080p, 5 с | **1 000** | 200 |
  | Kling 3.0 | 5 с, по умолчанию | **450** | 90 |

  Разброс цены секунды — **×7,8** внутри одной платформы. Перевод кредитов в доллары — нет данных.
- **Бесплатные сравнения уже существуют:** Anil-matcha/awesome-ai-video-models («which model, via which API, at what price, and how fast», 195 звёзд, обновлялся 25.09.2026) и fal-model-atlas («нормализованные цены + матрица возможностей: 332 эндпоинта, 83 семейства», 08.2026) ([GitHub](https://github.com/Anil-matcha/awesome-ai-video-models); [GitHub](https://github.com/egocen-vivideo/fal-model-atlas), д.д. 2026-09-26). Идея 7 оригинала получает названных конкурентов, а её защита слабеет.

### H. Спрос на знания об AI-генерации огромен, но он бесплатный

- Звёзды библиотек промптов на GitHub (д.д. 2026-09-26):
  - awesome-gpt-image-2-API-and-Prompts — **17,2 тыс.** (создан 18.04.2026);
  - awesome-nano-banana-pro-prompts — **13,5 тыс.**;
  - awesome-gpt-image-2 — **9,9 тыс.**;
  - GPT-Image2-Skill — **5,6 тыс.**;
  - awesome-seedance-2-prompts — 2,0 тыс.;
  - higgsfield-ai-prompt-skill — **637** (03.2026);
  - higgsfield-claude-skills — 377.
- Open-Generative-AI («open-source-альтернатива AI-видео-платформам, 600+ моделей») — **29,2 тыс.** звёзд.
- **Вывод:** внимание к рецептам и промптам на порядок выше, чем к любому AE-инструменту (у лидера AE-MCP 657 звёзд). Но всё это бесплатно. Монетизируется аудитория (канал, рассылка, воронка на платный продукт), а не сам контент.
- Навыки Claude для моушн-дизайнеров пока малы: motion-design-skills — 33 звезды, motion-design-with-claude — 19, AI-SKILL-adobe-products — 6 ([GitHub](https://github.com/iart-ai/motion-design-skills), д.д.).

### I. Прочие сигналы с GitHub

- **Рендер-менеджеры на aerender:** в 2026 году создано 11 репозиториев, максимум 22 звезды (aftr, «Puppeteer for After Effects. Use AE with Claude Code», 07.2026) ([GitHub](https://github.com/Arman-Luthra/aftr), д.д.). Разрыв «менеджер сдачи» (боль 3 оригинала) по-прежнему не закрыт, но сигнал слабый.
- **Предэкспортная проверка Lottie:** 19 репозиториев, популярных нет. Свежий lottie-workbench-ae (07.2026) — 1 звезда. Скачивают **конвертеры** Lottie и TGS: lottie-converter — **1 038** звёзд, LottieViewConvert — **634**, LottieFiles/tgskit — 76 ([GitHub](https://github.com/ed-asriyan/lottie-converter), д.д.). Спрос на конвертацию стикеров Telegram заметен. Готовность платить — нет данных.
- **Спецификации DOOH:** единственный профильный репозиторий — vistarmedia/dynamic-creative-spec (10 звёзд), спецификация HTML-креатива для DOOH-стеков ([GitHub](https://github.com/vistarmedia/dynamic-creative-spec), д.д.). Открытой базы спецификаций экранов нет.
- **Мультиформатные рекламные версии:** по запросу «after effects template csv batch render versions» среди репозиториев с 06.2025 — **0 результатов**. Open-source-конкуренции у локального конвейера версий почти нет. Но у Higgsfield есть «Ad Multiplier», а у Magnific — design_auto_resize (блок F): AI-платформы заходят в ту же задачу с другой стороны.

---

## Заполненные пробелы (по пунктам исходного брифа)

| Пункт брифа | Статус после дополнения | Лучшие данные или прокси |
|---|---|---|
| Reddit (r/AfterEffects, r/MotionDesign, r/aivideo и др.) | **нет данных** (не индексируется, чтение заблокировано) | Прокси: счётчики GitHub (блоки A, H, I), инсайты Envato (блок D) |
| Бестселлеры aescripts | **частично**: цены 5 «вечнозелёных» продуктов, модель платных апгрейдов (блок C) | Официального списка «Best Sellers» и числа отзывов нет |
| Новинки aescripts 2025–2026 | **частично**: UXLink (Figma↔AE + Motion), Lockdown 4 (02.2026, кросс-DCC) | — |
| Топ платных плагинов Figma Community | **нет данных**; есть комиссия 15%, правило «модель не меняется», старый прокси 9% платных | блок E |
| Топ категорий Envato и Motion Array | **заполнено**: 106 тыс. скачиваний у лидера 2025 года, разрыв «stylish packages» +410% / 6,2%, вертикальные форматы, цены Motion Array | блок D |
| Product Hunt 2025–2026 | **частично**: пороги апвоутов 2026 года; данных по креативным запускам нет | блок E |
| Бестселлеры Gumroad | **нет данных о продажах**; на Gumroad продаются UI Flow (lifetime), Convertify, DynaCap | блок A |
| YouTube-туториалы (просмотры) | **нет данных** | — |
| Upwork: «template customization», «resize video ads» | **нет данных** (лимит поиска исчерпан до этих запросов) | Прокси: стоимость шаблона у покупателя $16–25/мес за каталог (Motion Array) |
| Боли AI-видео: консистентность, апскейл, интерполяция, промпты, стоимость | **заполнено**: платформы встроили дефликер, апскейл, интерполяцию и удаление фона (F); цены непрозрачны, разброс ×7,8 (G); знание о промптах бесплатно и востребовано (H) | блоки F–H |
| Figma Plugin API для Motion | **заполнено**: API есть (beta), список анимируемых полей включает параметры стекла; ограничение — только ручные ключи | «Проверено», п. 2 |
| Конкуренты Figma→AE с ценами | **заполнено**: 9+ коммерческих, 11 OSS за 2026 год | блок A |

---

## Обновлённые сценарии и сигналы

Новые данные меняют две вещи: **сроки товаризации** и **темп клонирования**. Вероятности корректирую так:

| Сценарий | Было | Стало | Почему |
|---|---|---|---|
| Базовый | 55% | **50%** | То, что оригинал ждал к 12-му месяцу («мост Figma→AE становится товаром», «на каждую идею 5–10 клонов»), **уже произошло** к месяцу 0: 9+ коммерческих, 11 OSS и бесплатный LazyLord |
| Быстрый («агенты съедают инструментальный слой») | 25% | **32%** | Число новых AE-репозиториев ×5,4 за год и растёт каждый квартал (218 → 518 → 596). 67 AE-MCP и 48 Premiere-MCP. Официальный навык Figma для анимации агентом. Платформы AI-видео встроили подготовку плейтов |
| Медленный | 20% | **18%** | Сдвигается только за счёт перераспределения вероятностей |

**Новые или уточнённые опережающие сигналы:**
1. **Figma→AE: переход на цену «ноль».** Появление бесплатного продукта с 1 000+ пользователей в Figma Community или поддержки Figma Motion в Overlord 2 и Prism. Как следить: раз в месяц открывать страницы UI Flow, Overlord и LazyLord (звёзды, версии), GitHub `figma after effects created:>ГГГГ-ММ-01`.
2. **Figma Motion API выходит из беты, и `node.animations` начинает разворачивать animation styles.** Тогда перенос пресетной анимации станет тривиальным для всех. Как следить: [Figma Plugin API updates](https://developers.figma.com/docs/plugins/updates/), раз в две недели.
3. **Нативный Lottie-экспорт в Figma Motion.** Figma обещала его «в будущем». Как следить: Help-статья «Export animations from Figma».
4. **Встроенная «AI-постобработка» в генеративных платформах.** Число инструментов в каталогах Higgsfield и Magnific: сейчас дефликер, апскейл, интерполяция, relight, color transfer, удаление фона. Как следить: раз в квартал запрос `models_explore list type=video` и `video_models_list` через MCP. Сейчас 46 моделей у Magnific и около 37 видеоинструментов у Higgsfield.
5. **Envato: разрыв «поиск/скачивание» по пакетам.** Как следить: ежемесячные «Video Templates insights» и «Content opportunities» на author.envato.com.

---

## Идеи-кандидаты: новые и уточнённые

### Уточнение идеи 1 оригинала: «Oblique Motion Bridge» → понизить до «Oblique FX-Motion»: узкая ниша анимированных эффектов Figma (стекло, блюры, тени) в калиброванные стеки AE
- **Суть:** не конкурировать в переносе слоёв и базовой анимации: здесь уже 9+ коммерческих игроков, UXLink умеет Figma Motion, LazyLord бесплатен. Вместо этого сделать **единственный** мост, который переносит **анимированные параметры эффектов Figma** (`REFRACTION_*`, `SPECULAR_*`, `CHROMATIC_ABERRATION`, `SPLAY`, `RADIUS` блюров и теней) в визуально совпадающие стеки эффектов AE. Пружинные изинги Figma запекаются в AE-ключи.
- **Тип:** A.
- **Формат:** апдейт Oblique (v2) на aescripts за $69–89 и бандл с пакетом «glass looks».
- **Покупатель и боль:** моушн-дизайнеры SaaS- и app-промо, которым в Figma нарисовали «liquid glass», а в AE приходится подбирать эффекты на глаз.
- **Доказательства спроса:** средние для технической возможности (эти параметры есть в allowlist API, [motion-patterns.md](https://raw.githubusercontent.com/figma/mcp-server-guide/main/skills/figma-use-motion/references/motion-patterns.md), 2026). Слабые для объёма: прямых данных о продажах в категории нет.
- **Конкуренты и цены:** UXLink (цена не получена; поддерживает Figma Motion, глубина переноса эффектов неизвестна), Overlord 2 ≈$75, Prism от $39, Convertify $49/мес, UI Flow (freemium), DEmotion, MotionPotion (freemium), AEShiper ≈$6,5, LazyLord бесплатно.
- **Гипотеза защиты:** библиотека калибровок «Figma-эффект → AE-стек», которую основатель собирает руками как моушн-дизайнер. Это данные и вкус, а не код. Плюс скорость реакции на новые эффекты Figma (shader fills).
- **Главный риск:** UXLink или Overlord повторят функцию за 4–8 недель, Figma Motion API в бете может измениться. **Рекомендация:** вложить не больше 1–2 недель и использовать Oblique прежде всего как **канал**: список покупателей и email-база для следующих продуктов.

### Новая идея N1: «Branded World Packs»: системы шаблонов в едином дизайн-языке для вертикальных соцсетей (Premiere + AE + MOGRT)
- **Суть:** не отдельные шаблоны, а **миры**: 40–80 элементов (переходы, титры, lower thirds, оверлеи, end cards) в одном стиле. Каждый в 9:16, 4:5, 1:1 и 16:9, с управлением цветом бренда из одного контроллера. Выпуск раз в 1–2 месяца. Стили берутся из работы студии основателя: анаморф- и DOOH-эстетика, glass.
- **Тип:** A (вкус и арт-дирекция как дефицитный навык, AI помогает производить).
- **Формат:** пакеты на Envato Elements (доход по подписочному пулу) и Videohive ($29–49 за пакет), параллельно — прямые продажи и Gumroad.
- **Покупатель и боль:** монтажёры, SMM и маленькие агентства. Клиенты ищут согласованные наборы и не находят их.
- **Доказательства спроса:**
  - Envato: «stylish packages» +410% поисков, но всего 6,2% доходят до скачивания; запрос на «branded world rather than standalone assets» ([Author Hub](https://hub.author.envato.com/video-templates-content-insights-december-2025/), 2025-12);
  - лидер 2025 года — пакет переходов для Premiere со **106 000 скачиваний** ([Envato Unpacked 2025](https://elements.envato.com/learn/envato-unpacked), 2025-12);
  - устойчивый спрос на vertical, Reel и TikTok.
- **Конкуренты и цены:** тысячи авторов Envato; Motion Array $15,99–24,99/мес за весь каталог; Videohive $14–49 за позицию; Animation Composer (Mister Horse) как библиотека пресетов.
- **Гипотеза защиты:** узнаваемый авторский стиль и регулярность выпуска (накопленный контент), а не код. Каждый пакет продолжает продаваться на Envato годами.
- **Главный риск:** низкая выручка за одно скачивание в подписочном пуле Envato (точный размер выплаты — нет данных). Генеративный AI снижает ценность стоковых шаблонов. Нужно проверить, работает ли выплата Envato на Payoneer для UK LTD (не проверено).

### Новая идея N2: «Figma Motion Presets + AE twin»: пакеты анимационных пресетов, которые одинаково работают в Figma Motion и в AE
- **Суть:** набор из 50–150 UI-анимаций (появления, микро-взаимодействия, «glass reveal»). В Figma они ставятся через плагин как ручные треки ключей: авторинг собственных animation styles через API вне доступа, это прямо указано в документации навыка. В AE те же движения поставляются как `.ffx` с идентичными изингами. Дизайнер прототипирует в Figma, а финальный ролик собирает в AE с тем же ощущением движения.
- **Тип:** A.
- **Формат:** платный плагин в Figma Community (подписка или разовая покупка, комиссия 15%) плюс пакет пресетов на aescripts или Gumroad за $29–49.
- **Покупатель и боль:** продуктовые дизайнеры, которые с 06.2026 анимируют в Figma и не имеют библиотеки качественных движений, а также моушн-дизайнеры, которым нужно «как в прототипе».
- **Доказательства спроса:**
  - 65 репозиториев «figma motion» за 3 месяца (блок B);
  - MotionPotion монетизирует ровно эту модель («AE & Figma plugin for instant motion templates», 168 рецептов, freemium) ([motionpotion.co](https://motionpotion.co/), д.д.);
  - Figma Motion бесплатен в бете на всех планах, база пользователей потенциально огромная (оценка).
- **Конкуренты и цены:** MotionPotion (free 5 в мес, платный Wizard — цена не получена), Motionkit (бесплатно), встроенные пресеты Figma (`figmaAnimationStyles`), Bounce (OSS).
- **Гипотеза защиты:** вкус и качество изингов от практикующего моушн-дизайнера, пара «Figma + AE» (у большинства только одна сторона), регулярные дропы.
- **Главный риск:** Figma расширит встроенные пресеты и агента (навык `figma-use-motion`), и тогда пресеты станут бесплатной функцией. Beta-API может измениться.

### Уточнение идеи 5 оригинала: «AI Plate Prep» → **понизить приоритет**
- **Новые данные:** дефликер, апскейл до 4K с пресетом «aigc», интерполяция (Topaz), удаление фона (SAM 3), color transfer и relight уже встроены в Higgsfield и Magnific (блок F). Нативное решение в течение 24 месяцев — ~75% (оценка).
- **Что остаётся:** узкий шаг **внутри AE**: согласовать зерно и цвет AI-плейта с брендовым футажом и перевести в рабочее пространство (ACES/OCIO). Это сделать платформы не могут, так как не видят остальной ролик. Как отдельный продукт на 12–18 месяцев — сомнительно. Лучше как пакет пресетов за $19–29 внутри воронки.

### Уточнение идеи 7 оригинала: «AI Video Price Tracker» (тип B) → **конкуренты найдены, защита слабая**
- **Новые данные:**
  - разброс цены секунды у одной платформы — ×7,8 (Magnific, 90–700 кредитов/с при 1080p);
  - моделей 46 и больше;
  - бесплатные сравнения уже есть: awesome-ai-video-models (195 звёзд) и fal-model-atlas (332 эндпоинта).
- **Если делать:** не «таблица цен», а **калькулятор стоимости готовой секунды ролика с учётом перегенераций и апскейла** по платформам с подписками (Higgsfield, Magnific, Kling, Runway, Envato с кредитами с 17.08.2026). Данные можно обновлять полуавтоматически через MCP-каталоги (`simulate_cost`). Это единственный найденный технически дешёвый канал регулярного сбора цен.
- **Главный риск:** низкий поисковый спрос (нет данных). Непрозрачный курс «кредит → $». Аффилиатные программы для UK LTD с Payoneer не проверены.

### Новая идея N3 (гипотеза, слабые данные): «Sticker/Emoji Lottie Kit» для Telegram-стикеров из AE
- **Суть:** preflight-скрипт для AE плюс шаблоны, чтобы проходить жёсткие ограничения анимированных стикеров и эмодзи Telegram (TGS/Lottie). Точные лимиты в этом потоке не проверялись.
- **Тип:** AB.
- **Формат:** скрипт за $15–25 и пакет шаблонов.
- **Доказательства:** есть спрос на конвертеры: lottie-converter — 1 038 звёзд, LottieViewConvert — 634 (создан 06.2025); в 06.2026 появился форк bodymovin-for-tgs ([GitHub](https://github.com/ed-asriyan/lottie-converter); [GitHub](https://github.com/SwaggyMacro/LottieViewConvert), д.д.). Готовность платить — нет данных.
- **Конкуренты:** LottieFiles/tgskit (76 звёзд, бесплатно), официальные инструменты Telegram (не проверено).
- **Главный риск:** низкие чеки и бесплатные альтернативы. Держать как побочный продукт к идее 6 оригинала (Lottie Preflight), не как самостоятельный.

### Без изменений по данным, но подтверждена пустота рынка
- **Anamorphic Kit (идея 2) и DOOH Spec Atlas (идея 3):** на GitHub по-прежнему 1 анаморфный репозиторий и ни одной открытой базы спецификаций DOOH (только HTML-спецификация Vistar, 10 звёзд). Продаваемых инструментов нет. Спрос остаётся непроверенным: нужны интервью со студиями. Это по-прежнему самые «некопируемые» идеи благодаря студии и её данным, но и самые рискованные по объёму рынка.
- **Variant Factory Lite (идея 4):** OSS-конкурентов для CSV → AE → пакетный рендер за год не появилось (0 репозиториев). Зато AI-платформы заходят с другой стороны: Higgsfield Ad Multiplier, Magnific design_auto_resize. Риск для «перформанс-вариантов» выше, чем в оригинале. Для **брендовых** версий в точном фирменном стиле (где нужен AE) разрыв сохраняется.

---

## Источники

1. aescripts — UXLink: https://aescripts.com/uxlink/ (д.д. 2026-09-26)
2. Facebook aescripts — «UXLink now supports Figma Motion»: https://www.facebook.com/aescripts/videos/made-with-uxlink-by-pathlink2025-uxlink-now-supports-figma-motionsend-your-anima/2881170892264345/ (2026)
3. LottieFiles Docs — Figma Motion export: https://docs.lottiefiles.com/en/integrations/figma/04_figma-to-lottie/figma-motion-export (2026)
4. Figma Community — Figma Motion to Lottie (Beta): https://www.figma.com/community/plugin/1653028369274786320/figma-motion-to-lottie-beta (2026)
5. Figma Dev Docs — Version 1, Update 127: https://developers.figma.com/docs/plugins/updates/2026/06/23/version-1-update-127/ (2026-06-23)
6. Figma Dev Docs — Version 1, Update 130: https://developers.figma.com/docs/plugins/updates/2026/06/23/version-1-update-130/ (2026-06-23)
7. Figma Dev Docs — figma.motion: https://developers.figma.com/docs/plugins/api/figma-motion/ (д.д. 2026-09-26)
8. figma/mcp-server-guide — figma-use-motion SKILL.md: https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use-motion/SKILL.md (д.д. 2026-09-26)
9. figma/mcp-server-guide — motion-patterns.md (allowlist полей): https://raw.githubusercontent.com/figma/mcp-server-guide/main/skills/figma-use-motion/references/motion-patterns.md (д.д. 2026-09-26)
10. Figma Help — Export animations from Figma: https://help.figma.com/hc/en-us/articles/41307983648407-Export-animations-from-Figma (д.д. 2026-09-26)
11. Figma Help — What Figma features are in beta: https://help.figma.com/hc/en-us/articles/4406787442711-What-Figma-features-are-in-beta (д.д. 2026-09-26)
12. Medium (Sina Rad) — Figma Motion: The 5-Minute Guide: https://medium.com/@sinarad.me/figma-motion-the-5-minute-guide-4e3560c3b7f1 (2026-09)
13. AlternativeTo — Figma launches Motion: https://alternativeto.net/news/2026/6/figma-launches-a-new-integrated-motion-design-tool-alongside-code-layers-and-new-ai-features/ (2026-06)
14. Toolfarm — Overlord 2 coming, v1 price: https://www.toolfarm.com/news/battle-axe-overlord-2-coming/ (2024)
15. X (Battle Axe) — Overlord 2 и повышение цены: https://x.com/battleaxedotco/status/1815816822903451995 (2024-07)
16. Battle Axe Lore — Overlord 2 is here: https://lore.battleaxe.co/overlord-2-is-here/ (д.д. 2026-09-26)
17. Next Horizon — Prism Figma to AE: https://nexthorizon.art/store/figma-to-ae (д.д. 2026-09-26)
18. Hypermatic — Convertify на Gumroad: https://hypermatic.gumroad.com/l/convertify (д.д. 2026-09-26)
19. Hypermatic — Pro Bundle $83: https://www.hypermatic.com/bundle/ (д.д. 2026-09-26)
20. Figma Community — UI Flow (v22, 2026-09-09): https://www.figma.com/community/plugin/1605150908629430996/ui-flow-figma-to-after-effects (2026-09-09)
21. Gumroad — UI Flow lifetime: https://aeflowtools.gumroad.com/l/uiflowkey (д.д. 2026-09-26)
22. DEmotion: https://trydemotion.com/ (д.д. 2026-09-26)
23. DEmotion — Figmotion review 2026: https://trydemotion.com/blog/figmotion-animation-tool (2026)
24. MotionPotion — главная: https://motionpotion.co/ (д.д. 2026-09-26)
25. MotionPotion — Pricing: https://motionpotion.co/pricing (д.д. 2026-09-26)
26. AEShiper: https://aeshiper.com/ (д.д. 2026-09-26)
27. GitHub — LazyLord: https://github.com/raisulsohan/LazyLord (2026-09-16)
28. GitHub — поиск Figma→AE, созданные в 2026: https://github.com/search?q=figma+after+effects+created%3A%3E2026-01-01&type=repositories (д.д. 2026-09-26)
29. GitHub — поиск «figma motion» после 2026-06-20: https://github.com/search?q=figma+motion+created%3A%3E2026-06-20&type=repositories (д.д. 2026-09-26)
30. GitHub — figma/mcp-server-guide (figma-use-motion): https://github.com/figma/mcp-server-guide/tree/main/skills/figma-use-motion (д.д. 2026-09-26)
31. Medium (CodeIdeal) — Motionkit: https://medium.com/@codeideal/the-secret-free-motion-design-animation-plugin-inside-figma-1578f527ce98 (2026)
32. Motion Export: https://motionexport.com/ (д.д. 2026-09-26)
33. Hypermatic — TinyImage, экспорт Figma Motion: https://www.hypermatic.com/tutorials/how-to-bulk-export-figma-motion-layers-to-gif-and-mp4-video-using-tiny-image/ (2026)
34. aescripts — Plexus 3: https://aescripts.com/plexus/ (д.д. 2026-09-26)
35. aescripts — GEOlayers 3: https://aescripts.com/geolayers/ (д.д. 2026-09-26)
36. Insight — GEOlayers 3 subscription floating: https://www.insight.com/en_US/shop/product/MB-GEO-FL/aescripts/MB-GEO-FL/Aescripts-GEOlayers-3-for-After-Effects-subscription-license-3-floating-license/ (д.д. 2026-09-26)
37. aescripts — Lockdown 4: https://aescripts.com/lockdown/ (2026-02)
38. aescripts — Newton 4: https://aescripts.com/newton/ (д.д. 2026-09-26)
39. Videohive — лидеры продаж AE-скриптов: https://videohive.net/popular_item/by_category?category=add-ons%2Fafter-effects-scripts (д.д. 2026-09-26)
40. Videohive — лидеры продаж promo-шаблонов: https://videohive.net/popular_item/by_category?category=after-effects-project-files%2Fproduct-promo (д.д. 2026-09-26)
41. Envato — Unpacked 2025: https://elements.envato.com/learn/envato-unpacked (2025-12)
42. Envato Author Hub — Most popular items of 2025: https://author.envato.com/hub/most-popular-items-of-2025/ (2025-12)
43. Envato Author Hub — Video Templates insights December 2025: https://hub.author.envato.com/video-templates-content-insights-december-2025/ (2025-12)
44. Envato Help — AI Credit Structure: https://help.elements.envato.com/hc/en-us/articles/60055181647513-Updates-to-Envato-s-AI-Credit-Structure (2026-08)
45. Envato Help — Gen AI Access changes: https://help.elements.envato.com/hc/en-us/articles/53370106288281-Updates-to-Gen-AI-Access-in-Your-Envato-Subscription (2026-02)
46. Photutorial — Motion Array pricing: https://photutorial.com/motion-array-pricing/ (2026)
47. Kelviq — Figma plugin monetization 2026: https://www.kelviq.com/blog/figma-plugin-monetization/ (2026)
48. Dodo Payments — How to Monetize Figma Plugins in 2026: https://dodopayments.com/blogs/sell-figma-plugins (2026)
49. GitHub — yuanqing/figma-plugins-monetization-stats: https://github.com/yuanqing/figma-plugins-monetization-stats (дата данных не указана)
50. LaunchList — Product Hunt 2026 guide: https://getlaunchlist.com/blog/how-to-launch-on-product-hunt-2026 (2026)
51. TrendGap — Product Hunt upvotes 2026: https://trendgap.io/blog/product-hunt-launch-upvotes-rank-2026 (2026)
52. GitHub — поиск «after effects» по кварталам (Q1–Q3 2026, Q3 2025): https://github.com/search?q=%22after+effects%22+created%3A2026-07-01..2026-09-26&type=repositories (д.д. 2026-09-26)
53. GitHub — пример кряк-SEO-репозитория: https://github.com/StuccoFlame85/Adobe-After-Effects (2026-06)
54. GitHub — поиск «figma plugin», Q3 2026 и Q3 2025: https://github.com/search?q=%22figma+plugin%22+created%3A2026-07-01..2026-09-26&type=repositories (д.д. 2026-09-26)
55. GitHub — after effects mcp: https://github.com/search?q=after+effects+mcp&type=repositories (д.д. 2026-09-26)
56. GitHub — kumoproductions/mcp-aftereffects: https://github.com/kumoproductions/mcp-aftereffects (2026-08)
57. GitHub — hetpatel-11/Adobe_Premiere_Pro_MCP: https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP (д.д. 2026-09-26)
58. GitHub — ayushozha/AdobePremiereProMCP: https://github.com/ayushozha/AdobePremiereProMCP (2026-03)
59. GitHub — anamorphic-mask-service: https://github.com/Thomasine723/anamorphic-mask-service (2026-08)
60. GitHub — vistarmedia/dynamic-creative-spec: https://github.com/vistarmedia/dynamic-creative-spec (д.д. 2026-09-26)
61. GitHub — Anil-matcha/awesome-ai-video-models: https://github.com/Anil-matcha/awesome-ai-video-models (обновлён 2026-09-25)
62. GitHub — egocen-vivideo/fal-model-atlas: https://github.com/egocen-vivideo/fal-model-atlas (2026-08)
63. GitHub — awesome-gpt-image-2-API-and-Prompts: https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts (2026-04)
64. GitHub — awesome-nano-banana-pro-prompts: https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts (д.д. 2026-09-26)
65. GitHub — Open-Generative-AI: https://github.com/Anil-matcha/Open-Generative-AI (д.д. 2026-09-26)
66. GitHub — higgsfield-ai-prompt-skill: https://github.com/OSideMedia/higgsfield-ai-prompt-skill (2026-03)
67. GitHub — iart-ai/motion-design-skills: https://github.com/iart-ai/motion-design-skills (2026-06)
68. GitHub — aftr (Puppeteer for AE): https://github.com/Arman-Luthra/aftr (2026-07)
69. GitHub — ed-asriyan/lottie-converter: https://github.com/ed-asriyan/lottie-converter (д.д. 2026-09-26)
70. GitHub — SwaggyMacro/LottieViewConvert: https://github.com/SwaggyMacro/LottieViewConvert (д.д. 2026-09-26)
71. GitHub — LottieFiles/tgskit: https://github.com/LottieFiles/tgskit (д.д. 2026-09-26)
72. MCP-каталог Higgsfield (`models_explore`, type=video): запрос 2026-09-26, URL нет (внутренний каталог платформы)
73. MCP-каталог Magnific (`video_models_list`: 46 моделей; `simulate_cost`: Seedance 2.0 Pro, Veo 3.1, Wan 3.0, Kling 3.0): запрос 2026-09-26, URL нет
