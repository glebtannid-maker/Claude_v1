# Поток 3. Adobe и соседние платформы: что поглотят платформы, где останется место для инди (сентябрь 2026)

**Дата среза:** 2026-09-26. **Ключ:** adobe_platforms.

**Методология и ограничения (важно для доверия к цифрам).** В этой сессии лимит WebSearch (общий на все потоки, 200 запросов) закончился примерно после 37 запросов этого потока. Прямая загрузка страниц (WebFetch) для почти всех доменов заблокирована прокси: adobe.com, sec.gov, aescripts.com, figma.com, gumroad.com и cgchannel.com недоступны; доступен только github.com. Поэтому источники трёх типов:
- (а) выдержки поисковика по первичным страницам, со ссылкой на первичный URL;
- (б) первичные данные GitHub: даты создания репозиториев, README, теги релизов;
- (в) зеркала новостей на GitHub (репозиторий `byte-pipe/tech-news` сохраняет полные тексты TechCrunch, The Verge, Wired с оригинальным URL и датой). В тексте указан оригинальный URL.

Где данных нет, стоит «нет данных». Факты из памяти модели, не перепроверенные в сессии, помечены «память модели — проверить». Оценки помечены «оценка» и снабжены уровнем уверенности.

---

## Ключевые факты

### Adobe: деньги, цены, стратегия

1. **Q3 FY2026 (отчёт от 10.09.2026):** выручка $6,76 млрд (+13% г/г), non-GAAP EPS $6,13. Общий ARR Adobe $27,50 млрд (+11,2% г/г). Подписочная выручка Creative & Marketing Professionals $4,65 млрд (+13%). Прогноз выручки на FY26 повышен до $26,576–26,626 млрд ([Adobe IR](https://news.adobe.com/news/2026/09/adobe-q3fy26-financial-results), 2026-09-10; [Investing.com](https://www.investing.com/news/company-news/adobe-q3-fy2026-slides-strong-results-ceo-transition-announced-93CH-4897031), 2026-09).
2. **AI-first ARR больше $650 млн, рост >150% г/г.** MAU Adobe превысил 1 млрд (+20%). «Creative freemium» MAU (Firefly, Express, веб- и мобильные Premiere/Photoshop/Lightroom) больше 100 млн (+70% г/г). ARR Firefly вырос на 40% кв/кв ([Yahoo Finance, итоги звонка](https://finance.yahoo.com/markets/stocks/articles/adobe-inc-adbe-q3-2026-090037567.html), 2026-09). Вывод: рост идёт от AI и бесплатного входа, а не от pro-десктопа.
3. **Смена CEO.** Anil Chakravarthy (сейчас отвечает за Customer Experience Orchestration, то есть за enterprise-маркетинг) станет CEO с 01.12.2026, Шантану Нараен станет executive chair ([Adobe](https://news.adobe.com/news/2026/09/adobe-announces-anil-chakravarthy-to-become-president-and-ceo), 2026-09). Интерпретация, оценка средней уверенности: приоритет смещается к enterprise/marketing-стеку, а pro-инструменты для моушна (AE) не станут центром инвестиций.
4. **Q2 FY26 (июнь 2026): Adobe отложила запланированное повышение цен CC примерно на $500 млн ARR** и ускорила freemium. MAU creative freemium на тот момент >90 млн, ARR Firefly около $300 млн с ростом ~50% кв/кв ([SaaStr](https://www.saastr.com/adobe-just-deferred-a-big-annual-price-increase-its-the-first-big-crack-in-b2b-pricing-power-since-2022/), 2026-06; [Futurum](https://futurumgroup.com/insights/adobe-q2-fy-2026-ai-demand-strengthens-results-as-freemium-strategy-expands/), 2026-06). Это первый публичный признак, что ценовая власть Adobe ограничена.
5. **Акция.** Около −37% с начала 2026 года, P/E около 13 ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/adobe-now-down-37-2026-164456666.html), 2026-09). $239,07 на 24.09.2026, −18% от максимума 31 августа ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/vorboerse/adobe-stock-heads-into-the-open-after-a-0-67-percent-drop/70180123), 2026-09-24; [Trefis](https://www.trefis.com/stock/adbe/articles/616422/adobe-stock-slides-18-value-play-or-falling-knife/2026-09-24), 2026-09-24). Bank of America дала «Underperform» с тезисом «AI тянет рост вниз» ([Barchart](https://www.barchart.com/story/news/3205612/bank-of-america-says-ai-will-drag-down-adobe-stock), 2026). Morgan Stanley в июле понизила до Underweight, целевая цена $240 вместо $365 ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/adobe-now-down-37-2026-164456666.html), 2026).
6. **Цены.** С 17.06.2025 (США) All Apps переименован в Creative Cloud Pro, цена $69,99/мес вместо $59,99. В тариф входят 4 000 премиальных генеративных кредитов. Новый тариф Standard даёт 25 кредитов в месяц ([PhotoshopCAFE](https://photoshopcafe.com/generative-credits-to-be-enforced-adobe-cc-plans-change/), 2025-06). Отдельный AE стоит $34,49/мес ([The Verge](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates), 2026-04-17).
7. **Firefly как агрегатор чужих моделей.** Подключены партнёрские видеомодели Google Veo 3.1, Kling 3.0/3.0 Omni, Runway Gen-4.5, Luma Ray3 и другие. Планы Firefly: от $9,99/мес (2 000 кредитов) до $199,99/мес (50 000 кредитов и безлимит на часть видеомоделей) ([Krea blog](https://www.krea.ai/blog/is-adobe-firefly-free-what-it-is-and-how-it-compares-in-2026), 2026; [Feisworld](https://www.feisworld.com/blog/adobe-firefly-video-generation-partner-models), 2026; [Adobe blog](https://blog.adobe.com/en/publish/2026/03/19/adobe-firefly-expands-video-image-creation-with-new-ai-capabilities-custom-models), 2026-03-19).
8. **Adobe скупает инди-инструменты.** **Topaz Labs** куплен 25.06.2026, «инструменты интегрируют во все приложения» ([TechCrunch](https://techcrunch.com/2026/06/25/adobe-acquires-image-and-video-enhancement-tool-maker-topaz-labs/), 2026-06-25). Rilo (маркетинговая аналитика) куплен 02.09.2026 ([TechCrunch](https://techcrunch.com/2026/09/02/adobe-acquires-indian-market-intelligence-startup-rilo/), 2026-09-02). Upscale, denoise и интерполяция кадров теперь нативная территория Adobe.
9. **Premiere на телефонах бесплатно.** Premiere для Android вышел 22.09.2026 (бесплатно, экспорт до 4K). Premiere Rush перестают поддерживать 30.09.2026. Premiere для iPhone вышел «почти год назад» ([Wired](https://www.wired.com/story/adobe-premiere-now-on-android/), 2026-09-22).

### After Effects и Premiere: что стало нативным (2025–2026)

10. **AE 26.0 (январь 2026):**
    - нативные параметрические 3D-меши (сфера, куб, конус) и 1 300 бесплатных материалов;
    - анимация осей variable fonts;
    - импорт SVG, редактируемые градиенты из Illustrator;
    - новый кеинг, аудиоэффекты (gate, compressor);
    - lossless-кеш превью, нативный WinARM ([Newsshooter](https://www.newsshooter.com/2026/01/22/whats-new-in-adobe-after-effects-26-0/), 2026-01-22; [Digital Production](https://digitalproduction.com/2026/01/23/adobe-after-effects-2026-lands-with-3d-text-and-performance-boosts/), 2026-01-23).
11. **AE 26.3 (июнь 2026):**
    - Depth of Field в Advanced 3D;
    - **вставка контента из Illustrator и SVG как нативных редактируемых shape-слоёв**;
    - трекинг масок до 5× быстрее;
    - копирование кадра в буфер, эффект Curl Noise ([CG Channel](https://www.cgchannel.com/2026/06/adobe-releases-after-effects-26-3/), 2026-06).

    Для Oblique это важно: базовый перенос вектора через SVG-буфер теперь делается без плагинов.
12. **AE 26.5 (сентябрь 2026)** — рабочий релиз: дисковый кеш для Object Matte, новые Guides, цветные метки эффектов, обновлённая панель Effect Controls. **В бете появился агентный AI Assistant.** Он генерирует исполняемый JSX, пишет и отлаживает expressions, чинит сломанные риги и ссылки, переименовывает и реорганизует проект, анализирует весь проект целиком ([CG Channel](https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/), 2026-09; [RedShark](https://www.redsharknews.com/after-effects-ai-assistant-ibc2026), 2026-09; [Adobe Community](https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658), 2026-09). Под прямой удар попадают категории «AI-генератор expressions/скриптов» (например, [AE GPT на aescripts](https://aescripts.com/ae-gpt/)) и «органайзеры проектов».
13. **AI-ротоскоп в AE:** Object Matte (наведение и клик, Refine Edge) и Roto Brush 4.0 на новой нейросети ([Adobe Help](https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html), 2026; [Blue Lightning](https://bluelightningtv.com/2026/01/22/firefly-ai-lands-in-premiere-pro-and-after-effects/), 2026-01-22).
14. **Premiere 26.x.**
    - Object Mask с контролем краёв.
    - Generative Extend: от 360p до 4K, любые пропорции.
    - **Generative Media Tool** (IBC, сентябрь 2026): генерация видео и SFX прямо на таймлайне моделями Firefly и партнёров; Generate Soundscape в бете.
    - Color Mode: публичная бета на NAB (апрель 2026), GA позже в 2026 ([No Film School](https://nofilmschool.com/adobe-generative-media-tool), 2026-09; [Kyler Holland](https://www.kylerholland.com/blog/premiere-pro-september-2026-whats-new/), 2026-09; [No Film School NAB](https://nofilmschool.com/adobe-updates-nab-2026), 2026-04).
15. **Firefly AI Assistant:** публичная бета в апреле 2026, с 18.06.2026 встроен в Premiere, Illustrator, InDesign и Frame.io ([TechCrunch](https://techcrunch.com/2026/06/18/adobe-adds-its-ai-assistant-to-premiere-illustrator-and-indesign/), 2026-06-18).
16. **Sneaks на MAX 2025 (октябрь 2025):**
    - **Project Motion Map** анимирует статичную векторную графику по текстовому промпту, без ключей и ригов;
    - Project Frame Forward переносит правку одного кадра на всё видео;
    - Project Sound Stager генерирует саунд-дизайн ([Adobe Blog](https://blog.adobe.com/en/publish/2025/10/30/adobe-max-2025-sneaks-where-ai-creativity-play-collide), 2025-10-30; [No Film School](https://nofilmschool.com/adobe-max-sneaks-2025), 2025-10).

    Sneaks обычно доходят до продукта за 1–3 года (оценка, средняя уверенность, по истории прошлых sneaks).
17. **MCP-коннектор Adobe × Anthropic «Adobe for Creativity»** вышел 28.04.2026: больше 50 инструментов (Photoshop, Lightroom, Illustrator, Firefly, Premiere, Express, InDesign, Stock) из одного промпта. Работает на уровне Express, а не полного десктопа ([Pillitteri](https://pasqualepillitteri.it/en/news/1558/claude-adobe-creative-cloud-50-tools-single-prompt-2026), 2026; [MindStudio](https://www.mindstudio.ai/blog/claude-mcp-adobe-vs-photoshop-premiere-what-it-does), 2026). Вторичные источники, уверенность средняя.

### Платформа плагинов Adobe: UXP, CEP, Exchange

18. **Официальный график перехода с CEP на UXP (блог разработчиков Adobe, сентябрь 2026):**
    - публичная бета UXP-плагинов в **After Effects к ноябрю 2026**;
    - в Premiere UXP уже GA (с Premiere 2026), доступны гибридные плагины;
    - Illustrator получит бету весной 2027;
    - у каждого флагмана минимум 2 года от UXP-беты до удаления CEP;
    - для AE, Illustrator и Media Encoder CEP перестаёт приниматься в новые сабмиты и **выключается по умолчанию в декабре 2028**;
    - **с декабря 2029 CEP не входит в новые версии** ([Adobe Developer Blog](https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications), 2026-09; [Hyper Brew](https://hyperbrew.co/blog/uxp-plugins-in-premiere-2026/), 2026).

    Даты взяты из выдержек поисковика, а не с самой страницы; уверенность средняя-высокая.
19. **Adobe Developer Distribution (Exchange):** разработчик получает **90%** выручки платного плагина, листинг бесплатный, платежи идут через сторонних провайдеров вроде FastSpring ([Adobe Developer FAQ](https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/faq), н.д.). Трафика и продаж Exchange по категориям нет (нет данных).
20. Hyper Brew продаёт «CEP→UXP Migration Assessment — роадмап за две недели» ([Hyper Brew](https://hyperbrew.co/uxp/), 2026). Это прокси спроса: разработчики платят за миграцию.

### Figma

21. **Config 2026 (24.06.2026):**
    - **Figma Motion** — нативный таймлайн с ключами, кривыми и spring-физикой; открытая бета на всех тарифах; экспорт в CSS, JSON, React, MP4, GIF, WebM, Animated SVG;
    - анимацию можно создать промптом через Figma agent;
    - code layers, shader fills и effects, **генеративные плагины** (плагин описывается словами, код писать не нужно), инструменты Weave прямо на холсте ([CMSWire](https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/), 2026-06; [Figma Help](https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026), 2026-06; [Figma Blog](https://www.figma.com/blog/config-2026-recap/), 2026-06).
22. **Figma Motion → Lottie:** бесплатный экспорт через плагин LottieFiles (transform, opacity, color, trim path, spring). Ограничения: градиенты анимировать нельзя, Background Blur не поддерживается ([LottieFiles docs](https://docs.lottiefiles.com/en/integrations/figma/04_figma-to-lottie/figma-motion-export), 2026). LottieFiles прямо пишет, что Figma Motion не заменяет AE для композитинга и сложной анимации ([LottieFiles blog](https://lottiefiles.com/blog/design-guides-and-tips/best-motion-design-tools-ranked-by-use-case), 2026).
23. **Figma купила Weavy** (нодовый AI-генератор изображений и видео) 30.10.2025, теперь это Figma Weave. Условия сделки не раскрыты ([TechCrunch](https://techcrunch.com/2025/10/30/figma-acquires-ai-powered-media-generation-company-weavy), 2025-10-30). Вторичные источники называют примерно $200 млн, уверенность низкая.
24. **Figma Q2 2026:** выручка $370 млн (+48% г/г), NRR 136%, прогноз на год $1,463–1,467 млрд. Это первый полный квартал монетизации AI-кредитов; больше 80% крупных платящих клиентов используют кредиты еженедельно ([Figma IR](https://investor.figma.com/news-events/news/news-details/2026/Figma-Announces-Second-Quarter-2026-Financial-Results/default.aspx), 2026-08; [GuruFocus](https://www.gurufocus.com/news/9009442/figma-inc-fig-q2-2026-earnings-call-highlights-revenue-surges-48-to-370m-ai-monetization-gains-traction), 2026-08). Акция упала на росте AI-расходов ([Quartz](https://qz.com/figma-stock-earnings-ai-investment-costs-080626), 2026-08-06).
25. **Glass в Figma** вышел из беты 27.01.2026 и теперь применяется к фигурам и тексту (по выдержке поиска; первичная страница — [Figma Help, Effects](https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers)). В AE нативного background blur нет: такая идея висит на Adobe Ideas ([Adobe Community Ideas](https://community.adobe.com/ideas/add-native-background-blur-effect-for-layers-like-figma-s-background-1546738), н.д.). Это ядро ценности Oblique, и оно же может стать нативным.
26. **Figma Community (вторичный источник):** комиссия 15%, при этом «Figma сейчас не одобряет новых продавцов платных файлов» ([appstores.dev, зеркало на GitHub](https://github.com/jessems/appstores.dev/blob/main/content/stores/figma.mdx), дата н.д.). Уверенность средняя, перед решением проверить на figma.com.

### Canva, Maxon, Apple, Blackmagic, CapCut, Blender: давление «бесплатно»

27. **Canva: Affinity стал бесплатным** (перезапуск «Affinity by Canva» 30.10.2025: вектор, растр и вёрстка в одном приложении; раньше $69,99 за приложение или $169,99 за три) ([HN](https://news.ycombinator.com/item?id=45761659), 2025-10-30; [The Verge](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates), 2026-04-17). **Больше 5 млн загрузок** к февралю 2026 ([TechCrunch](https://techcrunch.com/2026/02/23/canva-acquires-startups-working-on-animation-and-marketing/), 2026-02-23).
28. **Canva купила Cavalry** (процедурный 2D-моушн) и MangoAI 23.02.2026, а в апреле 2026 **сделала Cavalry полностью бесплатным** ([TechCrunch](https://techcrunch.com/2026/02/23/canva-acquires-startups-working-on-animation-and-marketing/), 2026-02-23; [Canva Newsroom](https://www.canva.com/newsroom/news/mangoai-cavalry-acquisition/), 2026-02; [The Verge](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates), 2026-04-17). Показатели Canva на конец 2025: 265+ млн пользователей, 31 млн платящих, **$4 млрд годовой выручки** (TechCrunch, там же).
29. **Maxon сделала Autograph** (прямой аналог AE) бесплатным для индивидуальных пользователей в апреле 2026. Раньше он стоил $1 795 бессрочно или $59/мес ([The Verge](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates), 2026-04-17).
30. **Apple Creator Studio** (запуск в начале 2026) стоит $12,99/мес или $129/год и включает Final Cut Pro, Logic Pro, Motion, Compressor и Pixelmator Pro ([JustCreative](https://justcreative.com/adobe-cc-vs-apple-creator-studio/), 2026-02-24).
31. **DaVinci Resolve 21** (апрель 2026): страница Photo, маски, поддержка .af от Affinity в бесплатной версии ([The Verge](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates), 2026-04-17). **Resolve 21.1 (08.09.2026) интегрирует Claude, Claude Code и ChatGPT Codex** через 20 новых scripting API. При этом продвинутый скриптинг перенесли в платную Studio; на HN отмечают, что API пока не умеет простых вещей ([Blackmagic PR](https://www.blackmagicdesign.com/media/release/20260908-03), 2026-09-08; [HN, 398 баллов](https://news.ycombinator.com/item?id=49610181), 2026-09; [конспект на GitHub](https://github.com/ahastudio/til/blob/main/video/davinci-resolve-21-1.md), 2026-09).
32. **CapCut (вторичные источники, уверенность низкая-средняя).** Тарифы Standard около $9,99/мес и Pro около $19,99/мес (1 200 AI-points). В США приложение пропадало из сторов 19.01.2025. Сделка по TikTok USDS JV закрыта 22.01.2026, в ней явно упомянут CapCut ([исследование film-room-oss на GitHub](https://github.com/nino-chavez/film-room-oss/blob/main/research/competitive/2026-07-21-creator-editor-lane.md), 2026-07-21, авторы сами пометили цифры как непроверенные). Открытая альтернатива OpenCut была в трендах GitHub в июле 2025 и июне 2026 ([OpenCut](https://github.com/OpenCut-app/OpenCut), 2025-07).
33. **Blender 5.2.0 вышел 13.07.2026**, 5.2.2 — 14.09.2026; параллельно поддерживается LTS 4.5.x ([GitHub, теги Blender](https://github.com/blender/blender/tags), 2026-09-14).
34. **Remotion** (видео кодом на React) набрал **60,4 тыс. звёзд** и позиционирует себя как «video tools for the agent era», со встроенными agent skills ([GitHub](https://github.com/remotion-dev/remotion), 2026-09). Кодовый моушн через агентов стал реальной альтернативой шаблонам AE для продуктовых видео.

### Коммодитизация «AI управляет креативным приложением» (первичные данные GitHub, 26.09.2026)

35. **MCP-серверы для After Effects:** 72 публичных репозитория с 2025 года. **По периодам: 8 за весь 2025 год, 30 за январь–июнь 2026, 34 за июль–26 сентября 2026.** Темп вырос примерно с 1 до ~12 в месяц. Лидер — Dakkshin/after-effects-mcp (657★, создан 12.04.2025) ([поиск GitHub](https://github.com/search?q=after+effects+mcp&type=repositories), 2026-09-26). Для Premiere таких репозиториев 69 (лидер 609★), для DaVinci Resolve 73 (лидер 3 148★), для Blender 498 (лидер ahujasid/mcp-for-blender, 29 359★).
36. **Пиратство.** Для Glassary, MB Liquid Glass и Overlord (v2.6.4, v2.7.3) взломанные версии появляются на варез-агрегаторах в течение месяцев после релиза (листинги gfxtra, filecr и аналогов в выдаче поиска, 2025–2026; ссылки намеренно не приводятся). Для десктопных плагинов AE это постоянный налог на выручку.

### Маркетплейсы

37. **Getty × Shutterstock: сделка сорвалась.** США её одобрили, а британский регулятор заблокировал ([The Verge, заголовок в зеркале](https://github.com/byte-pipe/tech-news/blob/master/data/2026-07-01/content/newsfeed-amazon-fined-225-million-for-failing-to-help-ident.md), 2026-06-30/07-01). Envato принадлежит Shutterstock: куплен в 2024 году (память модели — проверить).
38. **Envato уходит в AI-генерацию:** GraphicsGen (октябрь 2025) ([DesignWorkLife](https://designworklife.com/i-tried-envatos-graphicsgen-and-i-was-surpised/), 2025-10), собственный «creative AI engine» на FLUX ([BFL blog](https://bfl.ai/blog/how-envato-built-its-creative-ai-engine-on-flux), 2026-06-17). Динамика доходов авторов Envato, Motion Array (принадлежит Artlist, память модели), Storyblocks и MotionElements за 2025–2026: **нет данных** в этой сессии. Косвенный признак: площадки-агрегаторы сами генерируют контент, значит доля выручки, идущая авторам, структурно снижается (оценка, средняя уверенность).
39. **aescripts + aeplugins:** размер каталога, доля разработчика и число релизов в месяц — **нет данных** (сайт недоступен). Прокси для темпа: только категория «стекло» после Liquid Glass от Apple (июнь 2025) дала как минимум 4 AE-плагина: Glassary, MB Liquid Glass, AE Glass, Liquid Glass ([aescripts Glassary](https://aescripts.com/glassary/), 2025–2026, плюс выдача поиска). Трендовая ниша заполняется клонами за считанные месяцы.
40. Отдельный интерфейс «AI-ассистента для AE» уже продаётся на Adobe Exchange ([Exchange](https://exchange.adobe.com/apps/cc/203667/ai-assistant-for-after-effects), н.д.) — ровно та категория, которую Adobe сейчас закрывает нативно (факт №12).

---

## Хронология Figma → After Effects: как быстро появлялись клоны (урок Oblique)

| Дата (создание / релиз) | Продукт | Модель / цена | Что заявлено | Источник |
|---|---|---|---|---|
| 2019–09.2022 (последний релиз 0.8.2, 01.09.2022), **архивирован 21.06.2025** | AEUX (Google, Adam Plouff) | бесплатно, open source | слои Figma/Sketch → shape/text-слои, blur (с v0.8.1) | [GitHub releases](https://github.com/google/AEUX/releases) |
| 11.2024 (v2.4.0 с Figma) | Overlord (Battle Axe) | v1 $55, v2 «+$20» (≈$75 — оценка); вечная лицензия + 1 год обновлений | Figma/PS/AI → AE, live text, градиенты | [X Battle Axe](https://x.com/battleaxedotco/status/1856102276022128859), [Toolfarm](https://www.toolfarm.com/news/battle-axe-overlord-2-coming/) |
| н.д. | Convertify (Hypermatic) | подписка; бандл всех плагинов Hypermatic — «$83/user/month» по заголовку страницы | экспорт Figma в AE и другие форматы | [Hypermatic](https://www.hypermatic.com/convertify/), [Bundle](https://www.hypermatic.com/bundle/) |
| ~осень 2025 (оценка по ID плагина) | AEUX-PLUS (Figma Community) | н.д. | форк или наследник AEUX | [Figma](https://www.figma.com/community/plugin/1558056526591954235/aeux-plus) |
| 06.10.2025 | figma-to-ae (open source) | бесплатно | перенос слоёв | [GitHub](https://github.com/abenezer147/figma-to-ae) |
| ~начало 2026 (оценка по ID); **v22 от 09.09.2026** | UI Flow | freemium: 10 экспортов в день бесплатно + пожизненный ключ на Gumroad (цена н.д.) | Figma → AE, текст, маски | [Figma](https://www.figma.com/community/plugin/1605150908629430996/ui-flow-figma-to-after-effects), [Gumroad](https://aeflowtools.gumroad.com/l/uiflowkey) |
| **03.2026** | **Oblique (основатель)** | aescripts $59 → $69 | лейауты + эффекты, стекло, блюры | — |
| 25.03.2026 | FAE (redNSF) | бесплатно, GPL-3.0 | **двусторонний** обмен Figma ↔ AE | [GitHub](https://github.com/redNSF/fae) |
| 08.04.2026 | UI-FLow (репозиторий) | бесплатно | экспорт фреймов в AE | [GitHub](https://github.com/arafatmirazcoder/UI-FLow) |
| 01.05.2026 | figma-ae-bridge | бесплатно, MIT | auto-layout, компоненты, blend modes, тени; градиентов нет | [GitHub](https://github.com/darshd9941/figma-ae-bridge) |
| 28.05.2026 | after-effects-mcp (karly-herrera) | бесплатно | MCP + «Figma → AE pipelines» для AI-агентов | [GitHub](https://github.com/karly-herrera/after-effects-mcp) |
| 20.06.2026 | figma-to-after-effect (ElevenCraft) | бесплатно | «редактируемые композиции AE», без зависимостей | [GitHub](https://github.com/ElevenCraftStudio-Saas/figma-to-after-effect) |
| **24.06.2026** | **Figma Motion (нативно)** | входит в Figma, открытая бета | анимация в Figma с экспортом в Lottie/MP4/код, AE не нужен | [Figma Help](https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026) |
| 06.2026 | **AE 26.3: вставка SVG/AI как нативных shape-слоёв** | входит в AE | базовый вектор без плагина | [CG Channel](https://www.cgchannel.com/2026/06/adobe-releases-after-effects-26-3/) |
| н.д. (на 2026 уже поддерживает Figma Motion) | UXLink (aescripts) | **$99,99** | двусторонний обмен, анимация, градиенты до 5 стопов, blend modes | [aescripts](https://aescripts.com/uxlink/) |
| н.д. | AEShiper | 799 BDT пожизненно (≈$6,5 — оценка по курсу) | Figma → AE | [aeshiper.com](https://aeshiper.com/) |
| н.д. | magicul.io | веб-конвертер | Figma → AE | [magicul](https://magicul.io/converter/figma-to-after-effects) |
| 03.08.2026 | OverAE | бесплатно | прямая связь Figma ↔ AE | [GitHub](https://github.com/brunojorri/OverAE) |
| 02.09.2026 | Transporter | н.д. | перенос **градиентов** Figma → AE | [GitHub](https://github.com/tlatvys-ac/transporter-app) |
| 02.09.2026 | evotechly motion-os | бесплатно | «детерминированный компилятор Figma → motion → AE» | [GitHub](https://github.com/Mohamedbeghanem/evotechly-motion-os) |
| **16.09.2026** | **LazyLord** | **бесплатно навсегда, MIT** | «полная замена Overlord»: Figma/PS/AI ↔ AE, тени, glow, **blur**, blend modes, маски, компоненты как прекомпы, **update-in-place, live-sync** | [GitHub](https://github.com/raisulsohan/LazyLord) |
| 16.09.2026 | Luma tools | н.д. | Figma → AE transfer | [GitHub](https://github.com/sachinrawat2talentelgiacom-cloud/Luma) |

**Выводы с цифрами:**
- **Скорость появления.** Бесплатные и open-source мосты Figma → AE на GitHub: 1 в IV кв. 2025, 1 в I кв. 2026, 4 во II кв. 2026, 5 в III кв. 2026 (до 26.09). Темп вырос примерно в 5 раз, примерно с 0,3 до 1,7 новых в месяц. Сверху добавились нативный Figma Motion (июнь 2026) и нативная вставка SVG в AE (июнь 2026).
- **Реальное число конкурентов больше, чем «~6», которых видит основатель:** минимум **12 новых участников за 12 месяцев** (сентябрь 2025 — сентябрь 2026), из них ≥9 бесплатные.
- **Цены** на платные решения: от ≈$6,5 (AEShiper) до $99,99 (UXLink), середина $55–75. Бесплатный LazyLord с заявленным паритетом с Overlord появился через ~6 месяцев после старта Oblique. Эффекты (blur/glow/shadows) уже заявлены в бесплатных клонах; не заявлено пока только **Figma Glass** с корректным рендером в AE.
- **Разрыв между лидером и клоном сократился с лет до недель.** AEUX (2019) и Overlord v2 (2023) разделяли годы; между бесплатными клонами 2026 года проходят недели.

---

## DANGER LIST: что платформы с высокой вероятностью сделают нативно в течение 24 месяцев (до осени 2028)

| Функция / ниша | Кто | Доказательства | Вероятность натива за 24 мес. (оценка) | Вывод для инди |
|---|---|---|---|---|
| Генерация expressions/JSX, «скрипт по описанию», починка ригов, реорганизация проекта | Adobe | AI Assistant в бете AE 26.5 (сентябрь 2026) | 90% (высокая) | Не строить AI-генераторы скриптов для AE |
| Агентное управление приложением (MCP/скриптинг) | Adobe, Blackmagic, Figma | Adobe × Anthropic MCP (апрель 2026), Resolve 21.1 с Claude/Codex (сентябрь 2026), Figma agent; 72 бесплатных AE-MCP на GitHub | 85% | «MCP для X» не продаётся: open source и нативные решения |
| Ротоскоп, выделение объектов, маски | Adobe, Blackmagic | Object Matte, Roto Brush 4, Object Mask в Premiere | уже сделано | Уходить |
| Апскейл, денойз, интерполяция, восстановление AI-видео | Adobe | покупка Topaz (июнь 2026) | 85% | Уходить |
| Генеративные extend, fill, SFX, эмбиент на таймлайне | Adobe | Generative Extend 4K, Generative Media Tool (сентябрь 2026) | уже сделано | Уходить |
| Базовое 3D в AE (примитивы, материалы, DoF) | Adobe | AE 26.0/26.3 | уже сделано, дальше будет расширяться | Плагины «простые 3D-формы и материалы» обречены |
| Анимация variable fonts | Adobe | AE 26.0 | уже сделано | Уходить |
| Перенос вектора Illustrator/SVG в AE | Adobe | вставка shape-слоёв в AE 26.3 | уже сделано | Базовый Figma → AE обесценен |
| UI-моушн в дизайн-инструменте + экспорт в код/Lottie | Figma | Figma Motion (июнь 2026) + LottieFiles | уже сделано (бета) | «Figma → Lottie» и пресеты UI-анимации не продаются |
| Прямой экспорт Figma Motion → AE или «Paste from Figma» в AE | Figma / Adobe / сообщество | UXLink уже переносит Figma Motion; CSS/JSON-экспорт упрощает клоны | 50% нативно, 95% бесплатным клоном | Для Oblique это главная угроза |
| Нативный background blur и стекло в AE | Adobe | идея на Adobe Ideas; Figma Glass GA | 35% (низкая-средняя) | Ядро Oblique живёт 1–2 года, потом риск |
| Авто-анимация вектора по промпту | Adobe | Project Motion Map (sneak MAX 2025) | 50% | Пресеты «оживить иллюстрацию» уйдут |
| Цветокоррекция для монтажёров | Adobe | Color Mode в Premiere (бета апрель 2026, GA в 2026) | уже сделано | Простые LUT/грейдинг-плагины для Premiere не делать |
| Анимированные субтитры, автоформаты под соцсети, ресайз | Adobe, CapCut, Blackmagic | MCP-коннектор (ресайз под Reels/Shorts), CapCut AI, мобильный Premiere | уже сделано | Уходить |
| Бесплатные pro-приложения для моушна | Canva, Maxon | Cavalry и Autograph бесплатны с апреля 2026, Affinity с октября 2025 | уже сделано | Платный standalone-софт для моушна не делать |
| Генерация шаблонов и стока | Envato, Adobe, Canva | Envato на FLUX, Firefly + Adobe Stock в Firefly Video Editor | 80% | Классические шаблонные паки дешевеют |

---

## Сценарии: 12 / 24 / 36 месяцев (сентябрь 2026 → конец 2029)

### A. «Платформы поглощают» против «места для инди-разработчиков»

| Сценарий | Вероятность | 12 мес. (IX.2027) | 24 мес. (IX.2028) | 36 мес. (конец 2029) |
|---|---|---|---|---|
| **Базовый: «поглощение по краям»** | 55% | AI Assistant в AE выходит в GA. Простые скрипты, органайзеры и генераторы expressions теряют 50–80% продаж (оценка, средняя). Figma Motion выходит из беты. Мостов Figma → AE больше 20, большинство бесплатные. Первые UXP-плагины для AE | Вокруг Figma Motion ↔ AE окончательно устоялись бесплатные решения. Платные плагины держатся на глубине конкретного пайплайна, поддержке и контенте (пресеты, риги). CEP в AE выключен по умолчанию (декабрь 2028), часть старых плагинов умирает, и выигрывают те, кто портировал | Каталоги плагинов AE поляризуются: 10–20% «глубоких» инструментов с лояльной базой и длинный хвост почти бесплатных AI-клонов. Индивидуальная выручка у середины рынка падает (оценка) |
| **Быстрый: «агенты съедают плагины»** | 25% | AE AI Assistant, Firefly assistant и MCP закрывают большую часть автоматизации. Adobe добавляет импорт из Figma или Figma — экспорт в AE. Агенты вроде Claude пишут одноразовые скрипты под задачу | Рынок платных утилит для AE сокращается вдвое и больше. Ценность остаётся только у данных, контента, физического мира и сервиса | Моушн-дизайнеры в основном работают с агентами поверх AE, Figma, Cavalry и Remotion. Плагины как класс товара в основном бесплатны |
| **Медленный: «инерция профи»** | 20% | Смена CEO и ставка на freemium тормозят pro-функции AE. AI Assistant долго в бете, UXP в AE в 2027 сырой | Студии сидят на CEP до последнего. Платные плагины живут как в 2024–2025 | Индивидуальные нишевые плагины вроде Oblique приносят деньги 2–3 года |

**Опережающие сигналы и как их отслеживать:**
1. **Статус и цена AE AI Assistant** (GA, лимиты генеративных кредитов). Смотреть объявления AE 27.0 (обычно январь) и NAB (апрель) в Adobe Community Announcements. GA без жёстких лимитов кредитов → сдвиг к быстрому сценарию.
2. **Темп клонов на GitHub.** Раз в месяц делать запросы вида `figma "after effects" created:>ГГГГ-ММ-01` и `after effects mcp created:>…`. Рост больше 3 мостов в месяц или появление форков LazyLord со звёздами → быстрый сценарий.
3. **Форматы экспорта Figma Motion.** Отслеживать release notes Figma (раз в неделю) и Config 2027. Появление AE/.aep или «Send to After Effects» → удар по Oblique в течение 3–6 месяцев.
4. **UXP в AE:** выйдет ли бета к ноябрю 2026 и насколько полный у неё API. Задержка больше чем на 6 месяцев → медленный сценарий.

### B. Маркетплейсы (aescripts, Adobe Exchange, Figma Community, Envato/Motion Array/Storyblocks)

| Сценарий | Вероятность | 12 мес. | 24 мес. | 36 мес. |
|---|---|---|---|---|
| **Базовый: «сжатие и поляризация»** | 55% | aescripts растёт по числу релизов (AI удешевил разработку), но выручка на продукт падает. Цены в трендовых категориях снижаются на 20–40% (оценка, низкая-средняя). Exchange получает UXP-волну. Стоковые шаблоны дешевеют из-за AI-генерации внутри Envato и Firefly | Кураторские площадки (aescripts) ценятся как фильтр доверия среди AI-мусора. Envato и Motion Array платят авторам всё меньшую долю | Выживают авторы с аудиторией и собственным каналом. Маркетплейс становится только каналом дистрибуции, а не бизнесом |
| **Быстрое обрушение** | 30% | Поток AI-клонов и бесплатных open-source решений. aescripts ужесточает модерацию. Figma Community не открывает платные продажи новым авторам | Выручка шаблонных авторов падает на 50% и больше (оценка, низкая) | Шаблонный сток как профессия почти исчезает |
| **Ренессанс качества** | 15% | Миграция CEP → UXP и уход части пользователей с Adobe в Cavalry, Autograph и Resolve создают спрос на новые пакеты и порты | Новые маркетплейсы вокруг бесплатных приложений (Canva/Cavalry, Resolve) | Появляются 1–2 новые площадки с хорошей экономикой для авторов |

**Сигналы и мониторинг:** (1) Число новых продуктов на странице «New» aescripts за месяц — считать вручную раз в месяц, базу начать сейчас. (2) Квартальные отчёты Shutterstock (владелец Envato) после срыва сделки с Getty: строки про контрибьюторские выплаты и AI-лицензирование. (3) Откроет ли Figma Community приём новых платных продавцов (страница помощи Figma, раз в квартал). (4) Объявит ли Canva маркетплейс для Cavalry или Affinity (Canva Newsroom).

---

## Ответы на ключевые вопросы

**Что станет массовым и дешёвым (или бесплатным):**
- генерация видео и SFX на таймлайне (Premiere Generative Media Tool);
- ротоскоп и маски;
- апскейл и восстановление (Adobe + Topaz);
- expressions и скрипты (AE AI Assistant);
- перенос вектора и дизайна в AE (вставка SVG в AE 26.3, 12+ мостов, бесплатный LazyLord);
- UI-моушн с экспортом в код (Figma Motion);
- профессиональный вектор, растр и вёрстка (Affinity бесплатно);
- процедурный 2D-моушн (Cavalry бесплатно);
- аналог AE (Autograph бесплатно);
- монтаж на телефоне (Premiere mobile бесплатно);
- набор приложений Apple за $12,99/мес.

**Что поглотят платформы:** всё из Danger List. Особенно автоматизацию через агентов (Adobe × Anthropic, Resolve × Claude/Codex, Figma agent и генеративные плагины) и утилиты «один эффект, одна кнопка». Генеративные плагины Figma означают, что простой плагин для Figma пользователь теперь делает сам словами. Для рынка платных Figma-плагинов это сигнал сильнее любого конкурента.

**Где останутся деньги:**
1. У платформ: Adobe зарабатывает на AI-кредитах и freemium-воронке (AI-first ARR >$650 млн), Figma — на AI-кредитах (NRR 136%).
2. В глубоких pro-пайплайнах, где нужны доверие, поддержка и совместимость: студии, broadcast, DOOH.
3. В данных, которые постоянно обновляются: спецификации, совместимость, цены кредитов.
4. В контенте, который накапливается: риги, пресеты, сцены, библиотеки под конкретные форматы.
5. В связке с физическим миром и услугой: 3D-билборды, превиз под конкретные экраны.
6. В ранних экосистемах, которые только что стали бесплатными: Cavalry, Affinity, Autograph. Пользователи туда приходят массово (у Affinity 5 млн+ загрузок за ~4 месяца), а инструментов и пакетов для них пока мало.

**У кого будет доступ к инструментам.** Массовый пользователь получает pro-функции бесплатно через Canva/Affinity/Cavalry, Resolve, мобильный Premiere и freemium Firefly. Профи отличаются не доступом к софту, а вкусом, пайплайном, клиентами и умением управлять агентами. Adobe сознательно покупает массовую аудиторию и откладывает повышение цен.

**Какие навыки обесценятся:**
- ручной ротоскоп;
- написание expressions и скриптов «с нуля»;
- рутинная подготовка файлов между Figma и AE;
- базовый монтаж и цвет для соцсетей;
- производство шаблонов для стоков;
- «знание кнопок» конкретного приложения: агент знает кнопки лучше.

**Какие станут дефицитом:**
- арт-дирекция и motion-вкус (оценка суждения, а не исполнение);
- постановка задач агентам и приёмка их результата в моушне — это ровно профиль основателя;
- знание узких пайплайнов: DOOH-спецификации, анаморфная геометрия, broadcast-доставка;
- доверие и дистрибуция: своя аудитория, отношения со студиями.

---

## Возможности для основателя (где у инди остаётся место)

### 1. «Plugin Compatibility & UXP Migration Radar» — трекер совместимости плагинов AE/Premiere
- **Суть:** публичная база совместимости плагинов и скриптов AE/Premiere с версиями 26.x, UXP/CEP, WinARM и Apple silicon. Плюс email-алерты «что сломается при апдейте».
- **Тип:** B (данные + автоматизация), частично A (экспертиза в AE).
- **Формат:** SEO-сайт + еженедельная рассылка + платный «Studio pack» (экспорт матрицы, алерты по списку установленных плагинов). Цена $9–19/мес или $99/год на студию (оценка); спонсорские листинги для разработчиков.
- **Покупатель и боль:** пайплайн-TD и фрилансеры боятся обновлять AE, потому что апдейт ломает плагины. Разработчикам нужна видимость «мы UXP-ready».
- **Доказательства спроса:**
  - график перехода: UXP-бета в AE к 11.2026, CEP выключен по умолчанию в 12.2028, удалён в 12.2029 ([Adobe Dev Blog](https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications), 2026-09);
  - на форуме Adobe есть тред «CEP / UXP roadmap: should developers stop building CEP plugins» ([Adobe Community](https://community.adobe.com/questions-606/cep-uxp-roadmap-should-developers-stop-building-cep-plugins-and-what-happens-to-existing-ones-1614807), 2026);
  - Hyper Brew продаёт аудит миграции ([Hyper Brew](https://hyperbrew.co/uxp/), 2026);
  - AEUX заброшен и архивирован (21.06.2025).
- **Конкуренты:** фильтры совместимости на страницах aescripts (цены н.д.), заметки Toolfarm, консалтинг Hyper Brew (цена н.д.). Публичного трекера по всем вендорам не найдено — нет данных, это гипотеза, проверить вручную.
- **Гипотеза моата:** накопленная история совместимости + скорость обновления в день релиза AE + отношения с разработчиками, которые сами отправляют данные. Слишком мелко для Adobe.
- **Главный риск:** маленькая платёжеспособная аудитория; aescripts может сделать то же у себя. Нужно проверить, разрешает ли aescripts партнёрку и сбор данных (нельзя скрейпить в нарушение ToS).

### 2. «Creative AI Credit Calculator» — калькулятор стоимости AI-кредитов и трекер цен моделей
- **Суть:** калькулятор «сколько стоит 1 минута AI-видео или 100 изображений» в Firefly, Figma AI credits, CapCut AI points, Magnific/Freepik, Krea, Higgsfield и других, с историей цен.
- **Тип:** B.
- **Формат:** сеть калькуляторов и сравнительных страниц (программатик-SEO) + API/CSV для агентств + партнёрские ссылки.
- **Покупатель и боль:** продюсеры и фрилансеры считают бюджет AI-продакшена, а тарифы непрозрачны и меняются ежемесячно:
  - Firefly: $9,99 за 2 000 кредитов … $199,99 за 50 000; партнёрские модели тратят кредиты по-разному;
  - в CC Pro 4 000 кредитов, в Standard 25;
  - у Figma AI-кредиты — отдельная статья монетизации;
  - Adobe отложила повышение цен на ~$500 млн ARR.
- **Доказательства спроса (прокси):** конкуренты уже пишут SEO-контент вроде «Adobe Firefly price 2026» ([Krea](https://www.krea.ai/blog/is-adobe-firefly-free-what-it-is-and-how-it-compares-in-2026), 2026; [Feisworld](https://www.feisworld.com/blog/adobe-firefly-video-generation-partner-models), 2026; [XainFlow](https://www.xainflow.com/blog/adobe-firefly-ai-natives-third-party-models-creative-cloud), 2026). Объём поиска — нет данных, нужна проверка в Ahrefs/Semrush.
- **Конкуренты:** блоги самих вендоров (предвзятые), агрегаторы цен LLM (например, litellm) — они не покрывают креативные кредиты. Специализированный калькулятор не найден (нет данных).
- **Гипотеза моата:** скорость обновления + архив цен (графики «как дорожало») + репутация практика. Моат слабый-средний.
- **Главный риск:** AI Overviews и чат-боты забирают клики; вендоры меняют схемы кредитов, и поддержка съедает больше 4 часов в неделю, если не автоматизировать сбор цен.

### 3. «Anamorphic / DOOH Previz Kit» — превиз и сцены под реальные 3D-экраны
- **Суть:** веб-превиз (three.js) и набор сцен для Blender/AE с правильной камерой и точкой обзора под конкретные угловые L-образные экраны, плюс база спецификаций экранов.
- **Тип:** A (студия основателя + 3D-команда).
- **Формат:** платные киты по $49–199 за локацию или $29/мес для агентств (оценка); бесплатный превиз как лидогенерация для студии.
- **Покупатель и боль:** агентства и бренды, которые питчат идею 3D-билборда. Им нужен правдоподобный превиз на конкретной локации без трёх недель продакшена, и нужны точные размеры, кривизна, частота кадров и формат файла экрана.
- **Доказательства спроса:** в этом потоке нет данных по рынку DOOH (см. отдельный поток DOOH). Косвенно: платформы в эту нишу не идут (ни в Danger List, ни в роадмапах Adobe, Figma и Canva ничего похожего нет), а AE 26.x добавил 3D, DoF и материалы, то есть снизил порог для сцены в AE.
- **Конкуренты:** универсальные мокапы билбордов на Envato и Motion Array (цены н.д.), кастомный превиз студий. Специализированный продукт не найден (нет данных).
- **Гипотеза моата:** связь с физическим миром (база экранов, фото и замеры локаций), контент кейсов студии, доверие операторов экранов. Слишком мелко для платформ.
- **Главный риск:** рынок может оказаться маленьким (число анаморфных экранов и кампаний в год нужно подтвердить). Поддержка базы экранов требует ручной работы.

### 4. «Early-ecosystem packs» для бесплатных Cavalry / Autograph / Affinity
- **Суть:** пакеты ригов, пресетов, скриптов и шаблонов + шпаргалки «AE → Cavalry/Autograph» для дизайнеров, которые уходят с Adobe по цене.
- **Тип:** A.
- **Формат:** цифровые пакеты по $19–79 (Gumroad, свой сайт, позже маркетплейс Canva, если появится) + бесплатные туториалы как канал.
- **Покупатель и боль:** дизайнеры и небольшие студии, для которых $69,99 за CC Pro дорого. Бесплатный инструмент уже есть, а готовых рабочих материалов и знаний для него нет.
- **Доказательства спроса:**
  - Affinity: 5 млн+ загрузок за ~4 месяца после перехода в бесплатные ([TechCrunch](https://techcrunch.com/2026/02/23/canva-acquires-startups-working-on-animation-and-marketing/), 2026-02-23);
  - Cavalry и Autograph бесплатны с апреля 2026 ([The Verge](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates), 2026-04-17);
  - у Canva 265 млн пользователей и 31 млн платящих.
- **Конкуренты:** официальные библиотеки Cavalry и Autograph (объём н.д.), немногочисленные инди-авторы (нет данных).
- **Гипотеза моата:** ранний контент и аудитория в молодой экосистеме, доверие AE-эксперта, накопленная библиотека.
- **Главный риск:** пользователи бесплатного софта платят плохо; Canva может раздавать ассеты в Canva Pro; экосистема может не взлететь среди профи.

### 5. «Motion Delivery Preflight» — проверка готового ролика по спецификациям
- **Суть:** UXP-панель для AE/Premiere и веб-чекер, которые проверяют рендер по постоянно обновляемой базе спецификаций: safe zones соцсетей, форматы DOOH-экранов, лимиты размера и кодеков, громкость для broadcast.
- **Тип:** AB.
- **Формат:** $49 бессрочно или $5/мес; бесплатный веб-чекер как канал.
- **Покупатель и боль:** фрилансеры и студии отдают один ролик в 10–20 форматах; ошибка стоит перерендера и отказа площадки.
- **Доказательства спроса:** число форматов растёт (Premiere mobile по умолчанию делает вертикаль, Wired, 2026-09-22; ресайз под Reels/Shorts вынесен в MCP Adobe). Жалоб и объёма поиска в этом потоке нет (нет данных), нужен опрос 10 студий.
- **Конкуренты:** пресеты экспорта Adobe и ревью во Frame.io (цены в составе CC); enterprise-QC для broadcast (цены н.д.).
- **Гипотеза моата:** база спецификаций, обновляемая быстрее вендоров (особенно DOOH через студию основателя) + интеграция в пайплайн. Вход через UXP с ранним стартом (бета AE в 11.2026).
- **Главный риск:** Adobe может добавить «платформенные пресеты с проверкой»; низкая готовность платить за QC у фрилансеров.

### 6. «Maintained successors»: порт заброшенных CEP/ExtendScript-инструментов на UXP с поддержкой
- **Суть:** брать популярные заброшенные MIT/Apache-инструменты AE и портировать их на UXP с помощью Claude Code (с соблюдением лицензии и атрибуции). Продавать «поддерживаемую версию» с гарантией совместимости или порт под ключ для мелких авторов.
- **Тип:** A.
- **Формат:** $15–39 за инструмент или подписка «поддержка всех портов» $5/мес; услуга порта $300–1 500 (оценка).
- **Покупатель и боль:** пользователи старых бесплатных скриптов, которые сломаются, когда CEP выключат по умолчанию (12.2028); авторы без ресурсов на миграцию.
- **Доказательства спроса:** AEUX архивирован (21.06.2025), при этом по нему всё ещё открывают issues ([GitHub](https://github.com/google/AEUX/releases)); Hyper Brew продаёт миграцию ([Hyper Brew](https://hyperbrew.co/uxp/)); у Adobe формальное окно 2026–2029.
- **Конкуренты:** Hyper Brew (консалтинг и фреймворк Bolt; цены н.д.), сами авторы.
- **Гипотеза моата:** доверие («мы поддерживаем») + раннее присутствие на aescripts и Exchange (Exchange оставляет разработчику 90%). Код сам по себе не моат.
- **Главный риск:** AI делает порт тривиальным для всех, а Adobe может выпустить автоконвертер CEP → UXP. Окно ограничено 2027–2029.

**Чего не делать (из Danger List):** AI-генераторы скриптов и expressions для AE; «MCP для приложения X»; апскейл и денойз; простые 3D-плагины; UI-анимацию с экспортом в Lottie; базовые мосты Figma → AE; шаблонные стоки как основной доход.

---

## Что это значит для Oblique (коротко, практично)

1. **Считать Oblique активом для сбора выручки с горизонтом 12–18 месяцев**, а не платформой. Бесплатный LazyLord (16.09.2026) уже заявляет blur, тени, blend modes и update-in-place. UXLink за $99,99 переносит Figma Motion. Figma Motion и вставка SVG в AE закрывают базовый сценарий нативно.
2. **Держать уникальность в том, чего нет у бесплатных:** корректный перенос **Figma Glass** в AE, пиксельное совпадение эффектов, поддержка с быстрым ответом на апдейты AE и Figma (доверие), пресеты и риги как контент.
3. **Первым сделать UXP-версию для AE** после выхода беты (цель ноябрь 2026). Статус «UXP-native, будущая совместимость» — аргумент для студий, пока клоны сидят на CEP (LazyLord, figma-ae-bridge и FAE — CEP/ExtendScript).
4. **Не снижать цену до уровня клонов.** Держать $59–69 и продавать гарантию и поддержку. Иначе начнётся гонка к бесплатному, где инди проигрывает open source.
5. **Раз в месяц мониторить** GitHub-поиск по новым мостам и release notes Figma: признаки «экспорт в AE» и «Glass в Lottie/AE».

---

## Открытые вопросы (проверить до решения)
- Каталог aescripts: число продуктов, релизов в месяц, доля разработчика, наличие партнёрки. Сайт в этой сессии был недоступен.
- Доходы авторов Envato, Motion Array, Storyblocks и MotionElements в 2025–2026, изменения ставок роялти.
- Действительно ли Figma Community закрыта для новых платных продавцов, и какая сейчас комиссия (вторичный источник говорит о 15%).
- Цена и лимиты кредитов для AE AI Assistant после GA.
- Точные даты CEP в AE (декабрь 2028 и 2029) — проверить по первичному блогу Adobe.
- Финансирование и метрики Jitter, Rive и Spline в 2025–2026 — нет данных в этой сессии.
- Официальные цены CapCut 2026 и статус в США/Индонезии — только вторичные данные.
- Выплаты для UK Ltd с Payoneer: поддерживают ли aescripts, Exchange (FastSpring) и Gumroad выплаты на Payoneer или UK-банк.

---

## Источники
1. Adobe — Q3 FY26 results, https://news.adobe.com/news/2026/09/adobe-q3fy26-financial-results (2026-09-10)
2. Investing.com — Adobe Q3 FY2026 slides, https://www.investing.com/news/company-news/adobe-q3-fy2026-slides-strong-results-ceo-transition-announced-93CH-4897031 (2026-09)
3. Yahoo Finance — Adobe Q3 2026 call highlights, https://finance.yahoo.com/markets/stocks/articles/adobe-inc-adbe-q3-2026-090037567.html (2026-09)
4. Adobe — Anil Chakravarthy to become CEO, https://news.adobe.com/news/2026/09/adobe-announces-anil-chakravarthy-to-become-president-and-ceo (2026-09)
5. Motley Fool — Adobe Q3 2026 transcript, https://www.fool.com/earnings/call-transcripts/2026/09/11/adobe-adbe-q3-2026-earnings-call-transcript/ (2026-09-11)
6. SaaStr — Adobe deferred price increase, https://www.saastr.com/adobe-just-deferred-a-big-annual-price-increase-its-the-first-big-crack-in-b2b-pricing-power-since-2022/ (2026-06)
7. Futurum — Adobe Q2 FY2026, https://futurumgroup.com/insights/adobe-q2-fy-2026-ai-demand-strengthens-results-as-freemium-strategy-expands/ (2026-06)
8. Yahoo Finance — Adobe down 37% in 2026, https://finance.yahoo.com/markets/stocks/articles/adobe-now-down-37-2026-164456666.html (2026-09)
9. Barchart — BofA on Adobe, https://www.barchart.com/story/news/3205612/bank-of-america-says-ai-will-drag-down-adobe-stock (2026)
10. Trefis — Adobe stock slides 18%, https://www.trefis.com/stock/adbe/articles/616422/adobe-stock-slides-18-value-play-or-falling-knife/2026-09-24 (2026-09-24)
11. ad-hoc-news — ADBE price, https://www.ad-hoc-news.de/boerse/news/vorboerse/adobe-stock-heads-into-the-open-after-a-0-67-percent-drop/70180123 (2026-09-24)
12. PhotoshopCAFE — CC Pro and generative credits, https://photoshopcafe.com/generative-credits-to-be-enforced-adobe-cc-plans-change/ (2025-06)
13. Krea — Adobe Firefly price 2026, https://www.krea.ai/blog/is-adobe-firefly-free-what-it-is-and-how-it-compares-in-2026 (2026)
14. Feisworld — Firefly partner models, https://www.feisworld.com/blog/adobe-firefly-video-generation-partner-models (2026)
15. Adobe Blog — Firefly expands video/image, https://blog.adobe.com/en/publish/2026/03/19/adobe-firefly-expands-video-image-creation-with-new-ai-capabilities-custom-models (2026-03-19)
16. XainFlow — Firefly partner models list, https://www.xainflow.com/blog/adobe-firefly-ai-natives-third-party-models-creative-cloud (2026)
17. Newsshooter — AE 26.0, https://www.newsshooter.com/2026/01/22/whats-new-in-adobe-after-effects-26-0/ (2026-01-22)
18. Digital Production — AE 2026, https://digitalproduction.com/2026/01/23/adobe-after-effects-2026-lands-with-3d-text-and-performance-boosts/ (2026-01-23)
19. CG Channel — AE 26.3, https://www.cgchannel.com/2026/06/adobe-releases-after-effects-26-3/ (2026-06)
20. CG Channel — AE 26.5 + AI Assistant, https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/ (2026-09)
21. RedShark — AE AI Assistant public beta, https://www.redsharknews.com/after-effects-ai-assistant-ibc2026 (2026-09)
22. Adobe Community — AE AI Assistant beta, https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658 (2026-09)
23. Adobe Help — Object Matte, https://helpx.adobe.com/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/object-matte.html (2026)
24. Blue Lightning — Firefly in Premiere/AE, https://bluelightningtv.com/2026/01/22/firefly-ai-lands-in-premiere-pro-and-after-effects/ (2026-01-22)
25. No Film School — Generative Media Tool, https://nofilmschool.com/adobe-generative-media-tool (2026-09)
26. Kyler Holland — Premiere 26.5, https://www.kylerholland.com/blog/premiere-pro-september-2026-whats-new/ (2026-09)
27. No Film School — NAB 2026 Adobe, https://nofilmschool.com/adobe-updates-nab-2026 (2026-04)
28. CineD — Color Mode, Kling 3.0, Frame.io Drive, https://www.cined.com/adobe-reinvents-color-grading-in-premiere-expands-firefly-with-kling-3-0-and-debuts-frame-io-drive/ (2026-04)
29. TechCrunch — Adobe AI assistant in Premiere/Illustrator/InDesign, https://techcrunch.com/2026/06/18/adobe-adds-its-ai-assistant-to-premiere-illustrator-and-indesign/ (2026-06-18)
30. Adobe Blog — MAX 2025 Sneaks, https://blog.adobe.com/en/publish/2025/10/30/adobe-max-2025-sneaks-where-ai-creativity-play-collide (2025-10-30)
31. No Film School — MAX 2025 sneaks, https://nofilmschool.com/adobe-max-sneaks-2025 (2025-10)
32. Pillitteri — Claude + Adobe (Adobe for Creativity MCP), https://pasqualepillitteri.it/en/news/1558/claude-adobe-creative-cloud-50-tools-single-prompt-2026 (2026)
33. MindStudio — Adobe MCP limits, https://www.mindstudio.ai/blog/claude-mcp-adobe-vs-photoshop-premiere-what-it-does (2026)
34. Adobe Developer Blog — UXP comes to flagship apps, https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications (2026-09)
35. Hyper Brew — UXP in Premiere 2026, https://hyperbrew.co/blog/uxp-plugins-in-premiere-2026/ (2026)
36. Hyper Brew — CEP→UXP migration assessment, https://hyperbrew.co/uxp/ (2026)
37. Adobe Community — CEP/UXP roadmap thread, https://community.adobe.com/questions-606/cep-uxp-roadmap-should-developers-stop-building-cep-plugins-and-what-happens-to-existing-ones-1614807 (2026)
38. Adobe Developer Distribution FAQ (90% revenue), https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/faq (н.д.)
39. Adobe Exchange — AI Assistant for After Effects (third-party), https://exchange.adobe.com/apps/cc/203667/ai-assistant-for-after-effects (н.д.)
40. aescripts — AE GPT, https://aescripts.com/ae-gpt/ (н.д.)
41. TechCrunch — Adobe acquires Topaz Labs, https://techcrunch.com/2026/06/25/adobe-acquires-image-and-video-enhancement-tool-maker-topaz-labs/ (2026-06-25)
42. TechCrunch — Adobe acquires Rilo, https://techcrunch.com/2026/09/02/adobe-acquires-indian-market-intelligence-startup-rilo/ (2026-09-02)
43. Wired — Premiere on Android, https://www.wired.com/story/adobe-premiere-now-on-android/ (2026-09-22)
44. CMSWire — Figma Config 2026, https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/ (2026-06)
45. Figma Help — What's new from Config 2026, https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026 (2026-06)
46. Figma Blog — Config 2026 recap, https://www.figma.com/blog/config-2026-recap/ (2026-06/07)
47. LottieFiles docs — Figma Motion export, https://docs.lottiefiles.com/en/integrations/figma/04_figma-to-lottie/figma-motion-export (2026)
48. LottieFiles blog — best motion tools 2026, https://lottiefiles.com/blog/design-guides-and-tips/best-motion-design-tools-ranked-by-use-case (2026)
49. TechCrunch — Figma acquires Weavy, https://techcrunch.com/2025/10/30/figma-acquires-ai-powered-media-generation-company-weavy (2025-10-30)
50. Figma IR — Q2 2026 results, https://investor.figma.com/news-events/news/news-details/2026/Figma-Announces-Second-Quarter-2026-Financial-Results/default.aspx (2026-08)
51. GuruFocus — Figma Q2 2026 highlights, https://www.gurufocus.com/news/9009442/figma-inc-fig-q2-2026-earnings-call-highlights-revenue-surges-48-to-370m-ai-monetization-gains-traction (2026-08)
52. Quartz — Figma stock on AI costs, https://qz.com/figma-stock-earnings-ai-investment-costs-080626 (2026-08-06)
53. Figma release notes (mirror), https://github.com/byte-pipe/tech-news/blob/master/data/2026-08-17/content/tldr-figma-product-news-and-release-notes.md (2026-08-17)
54. Figma Help — effects/Glass, https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers (2026-01)
55. Adobe Community Ideas — native background blur, https://community.adobe.com/ideas/add-native-background-blur-effect-for-layers-like-figma-s-background-1546738 (н.д.)
56. appstores.dev — Figma store (15%, no new sellers), https://github.com/jessems/appstores.dev/blob/main/content/stores/figma.mdx (н.д.)
57. Figma Community — After Effects tag, https://www.figma.com/community/tag/after%20effects/plugins (2026)
58. Google AEUX releases (archived 2025-06-21), https://github.com/google/AEUX/releases
59. Battle Axe — Overlord, https://battleaxe.co/overlord (н.д.)
60. Battle Axe on X — Overlord for Figma 2.4.0, https://x.com/battleaxedotco/status/1856102276022128859 (2024-11)
61. Toolfarm — Overlord v1 price / v2, https://www.toolfarm.com/news/battle-axe-overlord-2-coming/ (2023)
62. Hypermatic — Convertify, https://www.hypermatic.com/convertify/ ; bundle https://www.hypermatic.com/bundle/ (н.д.)
63. Figma Community — AEUX-PLUS, https://www.figma.com/community/plugin/1558056526591954235/aeux-plus (~2025)
64. Figma Community — UI Flow, https://www.figma.com/community/plugin/1605150908629430996/ui-flow-figma-to-after-effects (v22, 2026-09-09)
65. Gumroad — UI Flow key, https://aeflowtools.gumroad.com/l/uiflowkey (2026)
66. aescripts — UXLink, https://aescripts.com/uxlink/ (н.д.)
67. AEShiper, https://aeshiper.com/ (н.д.)
68. magicul — Figma to AE converter, https://magicul.io/converter/figma-to-after-effects (н.д.)
69. GitHub — LazyLord, https://github.com/raisulsohan/LazyLord (2026-09-16)
70. GitHub — figma-ae-bridge, https://github.com/darshd9941/figma-ae-bridge (2026-05-01)
71. GitHub — FAE, https://github.com/redNSF/fae (2026-03-25)
72. GitHub — figma-to-ae, https://github.com/abenezer147/figma-to-ae (2025-10-06)
73. GitHub — UI-FLow, https://github.com/arafatmirazcoder/UI-FLow (2026-04-08)
74. GitHub — figma-to-after-effect, https://github.com/ElevenCraftStudio-Saas/figma-to-after-effect (2026-06-20)
75. GitHub — OverAE, https://github.com/brunojorri/OverAE (2026-08-03)
76. GitHub — Transporter, https://github.com/tlatvys-ac/transporter-app (2026-09-02)
77. GitHub — evotechly motion-os, https://github.com/Mohamedbeghanem/evotechly-motion-os (2026-09-02)
78. GitHub — Luma tools, https://github.com/sachinrawat2talentelgiacom-cloud/Luma (2026-09-16)
79. GitHub — after-effects-mcp (karly-herrera), https://github.com/karly-herrera/after-effects-mcp (2026-05-28)
80. GitHub search — after effects mcp (72 repos), https://github.com/search?q=after+effects+mcp&type=repositories (2026-09-26)
81. GitHub — Dakkshin/after-effects-mcp, https://github.com/Dakkshin/after-effects-mcp (2025-04-12)
82. GitHub — Adobe_Premiere_Pro_MCP, https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP (2025-07-07)
83. GitHub — davinci-resolve-mcp, https://github.com/samuelgursky/davinci-resolve-mcp (2025-03-18)
84. GitHub — mcp-for-blender, https://github.com/ahujasid/mcp-for-blender (2025-03-07)
85. aescripts — Glassary, https://aescripts.com/glassary/ (2025–2026)
86. The Verge — «The creative software industry has declared war on Adobe», https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates (2026-04-17; прочитано через зеркало https://github.com/byte-pipe/tech-news/blob/master/data/2026-04-20/content/hackernews_api-the-creative-software-industry-has-declared-war-on.md)
87. TechCrunch — Canva acquires Cavalry & MangoAI, https://techcrunch.com/2026/02/23/canva-acquires-startups-working-on-animation-and-marketing/ (2026-02-23)
88. Canva Newsroom — MangoAI & Cavalry acquisition, https://www.canva.com/newsroom/news/mangoai-cavalry-acquisition/ (2026-02)
89. Hacker News — Affinity by Canva, https://news.ycombinator.com/item?id=45761659 (2025-10-30)
90. JustCreative — Adobe CC vs Apple Creator Studio, https://justcreative.com/adobe-cc-vs-apple-creator-studio/ (2026-02-24)
91. Blackmagic — DaVinci Resolve 21.1 release, https://www.blackmagicdesign.com/media/release/20260908-03 (2026-09-08)
92. Hacker News — Resolve 21.1 discussion, https://news.ycombinator.com/item?id=49610181 (2026-09)
93. GitHub (ahastudio/til) — Resolve 21.1 notes, https://github.com/ahastudio/til/blob/main/video/davinci-resolve-21-1.md (2026-09)
94. Blackmagic — DaVinci Resolve Photo page, https://www.blackmagicdesign.com/products/davinciresolve/photo (2026-04)
95. GitHub — Blender tags, https://github.com/blender/blender/tags (2026-09-14)
96. GitHub — Remotion, https://github.com/remotion-dev/remotion (2026-09)
97. GitHub (film-room-oss) — CapCut pricing and ownership notes (secondary), https://github.com/nino-chavez/film-room-oss/blob/main/research/competitive/2026-07-21-creator-editor-lane.md (2026-07-21)
98. GitHub — OpenCut, https://github.com/OpenCut-app/OpenCut (2025-07)
99. The Verge headline «Getty's Shutterstock merger falls apart» (mirror), https://github.com/byte-pipe/tech-news/blob/master/data/2026-07-01/content/newsfeed-amazon-fined-225-million-for-failing-to-help-ident.md (2026-06-30/07-01)
100. BFL — How Envato built its creative AI engine on FLUX, https://bfl.ai/blog/how-envato-built-its-creative-ai-engine-on-flux (2026-06-17)
101. DesignWorkLife — Envato GraphicsGen, https://designworklife.com/i-tried-envatos-graphicsgen-and-i-was-surpised/ (2025-10)
102. TIKR — Adobe near 52-week low, https://www.tikr.com/blog/adobe-stock-is-trading-near-52-week-low-heres-where-shares-could-go-in-2026 (2026)
