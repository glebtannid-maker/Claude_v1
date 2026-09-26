# Поток 12. Разведка спроса: реальные боли и готовность платить в сообществах creative-tools (motion, видеомонтаж, Figma, DOOH/3D, AI-видео)

Дата: 2026-09-26. Автор: поток «demand_scout».

## 0. Ограничения сбора данных (прочитать до выводов)

Этот поток работал с жёсткими техническими ограничениями, и это влияет на уверенность в выводах:

- **Reddit недоступен.** Поисковый краулер не индексирует reddit.com (ошибка «domains are not accessible to our user agent»), прямое чтение тоже заблокировано. Поэтому **прямых цитат, апвоутов и числа комментариев из r/AfterEffects, r/MotionDesign, r/premiere, r/editors, r/FigmaDesign, r/aivideo, r/StableDiffusion, r/comfyui, r/VFX в отчёте нет.** Вместо них использованы прокси: форумы Adobe Community, Creative COW, форумы LottieFiles/Figma, GitHub (звёзды, issues, число репозиториев), листинги aescripts и Gumroad, отраслевые издания.
- **Большинство первоисточников заблокированы egress-прокси** (aescripts.com, figma.com, adobe.com, producthunt.com, gumroad.com, upwork.com, envato.com, motionarray.com, lottiefiles.com, youtube.com и др.). Доступны только github.com, raw.githubusercontent.com и pypi.org. Цифры с заблокированных сайтов взяты из поисковой выдачи (сниппетов) по указанным URL: это слабее, чем чтение страницы целиком.
- **Лимит веб-поиска сессии (200 запросов на все потоки) закончился**, когда этот поток сделал около 30 поисков. Поэтому остались без данных: топ платных плагинов Figma Community, топ категорий Envato/Motion Array, запуски на Product Hunt, бестселлеры Gumroad, ставки на Upwork и просмотры YouTube-туториалов. В тексте они помечены «нет данных» и заменены прокси.
- Для материалов без видимой даты публикации указана **дата доступа (д.д.) 2026-09-26**.

Как это учесть: общие выводы о **поглощении платформами** и **давлении клонов** опираются на первичные данные (релизы Adobe и Figma, счётчики GitHub), и уверенность в них средняя или высокая. Выводы о **ранжировании болей по частоте** опираются на прокси, уверенность в них низкая или средняя. Перед тем как вкладывать 2–6 недель в любую идею, нужна 1–2-часовая ручная проверка по Reddit и маркетплейсам (чек-лист в разделе 7).

---

## 1. Ключевые факты

**Adobe: что уже встроено в After Effects в 2026 году (то есть больше не продаётся как отдельный плагин)**

1. AE 26.0 (январь 2026): нативные 3D-параметрические меши (куб, сфера, конус, тор и т. п.), поддержка Substance-материалов с библиотекой из 1300+ бесплатных материалов, импорт SVG сразу в редактируемые shape-слои (с градиентами), анимация вариативных шрифтов, эффект Unmult ([CG Channel](https://www.cgchannel.com/2026/01/adobe-releases-after-effects-26-0-with-native-substance-support/), 2026-01; [postPerspective](https://postperspective.com/quick-look-adobes-premiere-and-after-effects-2026-updates/), д.д. 2026-09-26; [VFXer](https://www.vfxer.com/after-effects-2026-new-features-technical-breakdown/), д.д. 2026-09-26).
2. AE 26.2 (апрель 2026): **Object Matte**, AI-маски по клику с трекингом объекта (замена Roto Brush). Добавлены displacement для 3D-материалов и **Quick Apply**: поиск и применение любого эффекта, пресета или команды меню из одного окна ([CG Channel](https://www.cgchannel.com/2026/04/adobe-releases-after-effects-26-2/), 2026-04; [ProVideo Coalition](https://www.provideocoalition.com/after-effect-26-2-april-2026-release/), 2026-04). Quick Apply закрывает нишу «лаунчеров» вроде FX Console и Quick Menu.
3. AE 26.3 (июнь 2026): глубина резкости (DoF) в Advanced 3D-рендерере и эффект Curl Noise ([CG Channel](https://www.cgchannel.com/2026/06/adobe-releases-after-effects-26-3/), 2026-06).
4. AE 26.5 (сентябрь 2026): гайды в процентах с привязкой к краям, дисковый кэш Object Matte, цветовые метки эффектов, обновлённая панель Effect Controls. **В бете появился агентный AI Assistant**: управление проектом и композициями на естественном языке. Пока доступ только по приглашениям, в публичную бету обещан «в своё время» ([CG Channel](https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/), 2026-09; [Adobe Community](https://community.adobe.com/announcements-527/after-effects-26-5-is-here-1641108), 2026-09; [Adobe Community, анонс беты](https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658), 2026).
5. На Creative COW ассистент описан как «AI Assistant (MCP)» в приватной бете AE ([Creative COW](https://creativecow.net/forums/thread/adobe-adds-an-ai-assistant-mcp-to-after-effects-beta-private-beta/), 2026). Adobe заявляет, что распространит агентные возможности на другие приложения CC. Premiere тоже получает AI Assistant ([ProVideo Coalition](https://www.provideocoalition.com/premiere-ai-assistant/), 2026; [Broadcast](https://www.broadcastnow.co.uk/production-and-post/adobe-rolls-out-ai-agent-on-premiere/5217912.article), 2026).
6. **Сигнал о смене платформы расширений.** 23.09.2026 Adobe создала на GitHub репозиторий документации `AdobeDocs/uxp-after-effects`. Сейчас в нём только шаблон и initial commit ([GitHub](https://github.com/AdobeDocs/uxp-after-effects/commits/main), 2026-09-23). Оценка (средняя уверенность): UXP для AE анонсируют в ближайшие 6–12 месяцев. Для CEP/ExtendScript-панелей это означает риск миграции и одновременно окно «первым на UXP».

**Figma: из Figma в AE теперь уходит меньше анимации**

7. **Figma Motion** запущен на Config 2026 (24.06.2026). В нём есть таймлайн, ключи позиции, масштаба, поворота и прозрачности, пресеты, генерация анимации агентом Figma, просмотр анимации в Dev Mode с копированием в CSS/JSON/React и передача контекста через Figma MCP. На время открытой беты функция бесплатна на всех планах. Публикация анимированных компонентов и **HD-экспорт видео требуют платного Full seat** ([CMSWire](https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/), 2026-06; [Figma Blog](https://www.figma.com/blog/introducing-figma-motion/), 2026-06; [Figma Help](https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026), 2026-06).
8. На том же Config 2026 показали code layers, **shader fills и эффекты**, генеративные плагины, инструменты Weave и обновлённого агента Figma ([CMSWire](https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/), 2026-06). Каждая новая визуальная сущность Figma (shader fills, стекло, блюры) — это новая работа для любого Figma→AE-моста, которую приходится поддерживать.

**Мост Figma → AE: откуда взялись 6 конкурентов Oblique**

9. **AEUX**, бесплатный стандарт Figma/Sketch→AE от моушн-дизайнеров Google, **заархивирован 21.06.2025** (560 звёзд, 42 открытых issue, репозиторий только для чтения) ([GitHub](https://github.com/google/AEUX), 2025-06-21). Бесплатный лидер ушёл, освободилось место для платных инструментов.
10. Платные и бесплатные альтернативы: **Prism от $39**, Overlord (Battle Axe; «ранее $45», есть Figma-плагин), Convertify, AEUX (бесплатный, заархивирован) ([Next Horizon](https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma), д.д. 2026-09-26; [Battle Axe Overlord](https://battleaxe.co/overlord), д.д.; [Figma Community: Overlord](https://www.figma.com/community/plugin/1433559588746637449/overlord), д.д.). Oblique за $59–69 **дороже нижней границы рынка ($39)**.
11. На GitHub 33 репозитория по запросу «figma after effects». Несколько новых обновлялись в сентябре 2026: LazyLord («бесплатная альтернатива» для переноса Figma/PS/AI→AE), OverAE, transporter-app («градиенты из Figma в AE»), evotechly-motion-os («детерминированный компилятор Figma→motion→AE») ([GitHub search](https://github.com/search?q=figma+after+effects&type=repositories&s=updated&o=desc), д.д. 2026-09-26). **Бесплатные клоны уже появляются**, это подтверждает опыт основателя (было 2 конкурента, стало около 6).

**Давление клонов в цифрах (первичные данные GitHub)**

12. Новых репозиториев со словами «After Effects», созданных с 1 января по 26 сентября: **339 в 2025 году против ~1,3 тыс. в 2026 году (≈3,8×)** ([GitHub 2025](https://github.com/search?q=%22after+effects%22+created%3A2025-01-01..2025-09-26&type=repositories); [GitHub 2026](https://github.com/search?q=%22after+effects%22+created%3A%3E2026-01-01&type=repositories), д.д. 2026-09-26). Счётчики GitHub приблизительные, но порядок роста надёжный. Это прокси удешевления разработки благодаря AI.
13. Новых репозиториев «figma plugin» за те же периоды: **597 (2025) против ~1,4 тыс. (2026), ≈2,3×**. Среди топовых — MCP-мосты: figma-mcp-bridge (671 звезда), bridge для Claude Code (156) ([GitHub 2025](https://github.com/search?q=%22figma+plugin%22+created%3A2025-01-01..2025-09-26&type=repositories); [GitHub 2026](https://github.com/search?q=%22figma+plugin%22+created%3A%3E2026-01-01&type=repositories), д.д. 2026-09-26).
14. По запросу «after effects mcp» находится **72 MCP-сервера для AE**, лидер Dakkshin/after-effects-mcp набрал 657 звёзд и 127 форков ([GitHub](https://github.com/search?q=after+effects+mcp&type=repositories); [GitHub](https://github.com/Dakkshin/after-effects-mcp), д.д. 2026-09-26). Управлять AE через LLM уже можно бесплатно, а скоро это станет нативной функцией (факт 4).
15. На aescripts продаётся **Claude Scripter**: AI-ассистент для скриптинга в AE со своим ключом Anthropic API ([aescripts](https://aescripts.com/claude-scripter/), д.д. 2026-09-26). Категория «AI пишет выражения и скрипты» уже на маркетплейсе и одновременно встраивается в сам AE.

**Экономика маркетплейсов**

16. Комиссия aescripts составляет **30%**, автор получает 70%. Пример из интервью: при продажах на $120k разработчик получил $70k с учётом распродаж и аффилиатов ([aescripts FAQ](https://aescripts.com/faq/article/view/faq/become-an-author/), д.д.; [School of Motion](https://schoolofmotion.com/blog/how-much-do-after-effects-script-developers-make-a-chat-with-zack-lovatt), д.д.).
17. Ценовые коридоры aescripts: утилиты около $5–15, продвинутые плагины $30–150+, в основном разовые покупки ([Easyweb](https://www.easyweb-agency.fr/en/outils-comparatifs/aescripts), 2026). С мая по август 2026 шла распродажа «Summer of Sales 2026» со скидкой 25% на сотни продуктов ([aescripts](https://aescripts.com/learn/post/summer-of-sales-2026), 2026-05). Скидка 25% режет выручку автора с $59 до ~$31 чистыми за продажу (оценка: $59 × 0,75 × 0,70).
18. **Deep Glow 2 стоит $99,95, у V1 было $49,95.** Цена выросла вдвое на премиальном «лук»-эффекте: GPU-качество и бренд позволяют повышать цену ([aescripts](https://aescripts.com/deep-glow/), д.д. 2026-09-26).
19. Сторонние обзоры 2026 года чаще всего называют одни и те же «вечнозелёные» продукты: Plexus, GEOlayers, Helium, Lockdown, Newton, Deep Glow, Flow, Stardust, Limber, Animation Composer, RSMB, Trapcode, Element 3D, Saber, FX Console ([Toolfarm](https://www.toolfarm.com/products/subcategory/aescripts_aeplug_ins/), д.д.; [Maxon](https://www.maxon.net/en/article/best-after-effects-plugins), 2026; [Vagon](https://vagon.io/blog/top-10-plugins-for-after-effects), 2026; [School of Motion](https://schoolofmotion.com/blog/best-after-effects-plugins-and-effect-packs-you-need-in-2026), 2026). Это прокси бестселлеров: официальный список «most popular» получить не удалось.
20. **Пиратство распространено массово.** В выдаче по Deep Glow 2 и Overlord соседствуют FileCR, INTRO HD, GFXPACK, psdly, riztagar ([FileCR](https://filecr.com/macos/aescripts-deep-glow2/); [INTRO HD](https://intro-hd.net/battle-axe-overlord-for-after-effects-illustrator/); [riztagar](https://riztagar.com/battle-axe-overlord-for-after-effects/), д.д. 2026-09-26). На GitHub есть SEO-спам-репозитории вида «AEScripts … Full Toolbox 2026» ([GitHub](https://github.com/search?q=aescripts&type=repositories&s=updated&o=desc), д.д.). Чисто десктопный разовый продукт частично «утекает».
21. Battle Axe перевёл продажи с Gumroad на собственный сайт battleaxe.co ([Gumroad → battleaxe.co](https://battleaxe.gumroad.com/l/timelord), д.д.). Сильные авторы уходят в прямые продажи, свой канал ценится выше маркетплейса.

**Автоматизация и версионирование: где уже платят подпиской**

22. **Plainly** (облачный рендер AE-шаблонов по данным): Starter $69/мес за 50 минут рендера, Explorer $134 за 100, Team $259 за 200, Pro $649 за 600 ([Capterra](https://www.capterra.com/p/10026817/Plainly/), 2026; [ColdIQ](https://coldiq.com/tools/plainly), 2026).
23. **Nexrender Cloud**: pay-as-you-go от €99/мес, выделенные ноды от €350/мес. Open-source ядро nexrender: 1,9 тыс. звёзд, 347 форков ([Nexrender Pricing](https://www.nexrender.com/pricing), 2026; [GitHub](https://github.com/inlife/nexrender), д.д.).
24. **Templater (Dataclay)**: от $67,50, только регулярные подписки (upfront отменены), годовая оплата по цене 10 месяцев, есть модель QUE Meter с оплатой за выход ([SourceForge](https://sourceforge.net/software/product/Dataclay-Templater/), 2026; [Dataclay](https://dataclay.com/blog/templater-licensing-guide/), д.д.).
25. Ресайз под соцсети в AE: Smart Resize 2 за $15, COMP Tool за $19, Flip Aspect Ratio, бесплатный скрипт на Creative COW, бесплатный шаблон на Gumroad ([aescripts Smart Resize](https://aescripts.com/smart-resize/); [Pixflow](https://pixflow.net/blog/adapt-your-after-effects-videos-seamlessly-for-any-platform/); [Creative COW](https://creativecow.net/how-i-automated-social-media-resizing-in-after-effects-free-script/); [Gumroad davemh](https://davemh.gumroad.com/l/multiple-aspect-ratio-after-effects-template), д.д. 2026-09-26). Разовые ресайз-скрипты дешёвые и соседствуют с бесплатными, а платят подпиской за **конвейер** (факты 22–24).

**Субтитры: ниша уже массовая и дешёвая**

26. AutoCaption стоит $8/мес, $80/год или $150 бессрочно. Есть Captioneer (подписка и бессрочная лицензия), Voice2Captions (99+ языков), AEJuice Auto Captions (10 бесплатных минут в месяц) и DynaCap за $6,99/мес на Gumroad ([aescripts AutoCaption](https://aescripts.com/autocaption/); [Captioneer](https://aescripts.com/captioneer/); [Voice2Captions](https://aescripts.com/voice2captions/); [AEJuice](https://aejuice.com/product/auto-captions/); [DynaCap](https://acceleratecreative.gumroad.com/l/dynacapmonthly), д.д. 2026-09-26).
27. **auto-subs**: бесплатный офлайн-генератор субтитров для Resolve, Premiere и AE (1000+ языков), 4,3 тыс. звёзд, 287 форков, живёт на донатах ([GitHub](https://github.com/tmoroney/auto-subs), д.д. 2026-09-26).

**Lottie и веб-экспорт**

28. В lottie-web 32,1 тыс. звёзд, **788 открытых issues**, из них **108 открытых с фразой «not supported»** ([GitHub](https://github.com/airbnb/lottie-web); [issue search](https://github.com/search?q=repo%3Aairbnb%2Flottie-web+is%3Aissue+is%3Aopen+not+supported&type=issues), д.д. 2026-09-26). Не поддерживаются или проблемны 3D-слои, layer effects (тени, glow), часть blend modes и сложные выражения ([LottieFiles Help](https://help.lottiefiles.com/supported-after-effects-features); [LottieFiles forum](https://forum.lottiefiles.com/t/issues-with-figmas-export-to-lottie/4744), д.д.).
29. Цены LottieFiles: Individual $19,99/мес (при годовой оплате), Team $24,99 за пользователя в месяц, Enterprise $119,99 ([TrustRadius](https://www.trustradius.com/products/lottiefiles-platform/pricing); [LottieFiles](https://lottiefiles.com/pricing), 2026). Rive: бесплатный план, Cadet $9, Voyager $32, Enterprise $120 за место в месяц ([Gappsy](https://www.gappsy.com/tools/rive/); [SaasHunter](https://saashunter.pro/compare/lottie-vs-rive), 2026).

**AI-видео: боли креаторов (прокси через GitHub)**

30. Консистентность персонажей: 69 репозиториев по запросу «character consistency video». Лидер — **awesome-seedance-2-prompts (~2 тыс. звёзд, 2000+ промптов для Seedance 2.0)**, также story-shot-agent (204). Встречаются проекты под Seedance 2.5 и Veo 4 ([GitHub](https://github.com/search?q=character+consistency+video&type=repositories&s=stars&o=desc), д.д. 2026-09-26). Спрос на **знания** (промпты, референсы) высокий, но решение принадлежит вендорам моделей.
31. Управление генерациями (DAM и промпты): SmartGallery DAM — 383 звезды, **Image-MetaHub — 322 звезды, Pro за $39 разово**, ComfyUI_PromptManager — 172 ([GitHub search](https://github.com/search?q=comfyui+prompt+manager&type=repositories&s=stars&o=desc); [Image-MetaHub](https://github.com/LuqP2/Image-MetaHub), д.д. 2026-09-26). Боль реальная, готовность платить низкая, open-source-конкуренция сильная.
32. Апскейл, интерполяция и дефликер: Video2X — 21,8 тыс. звёзд (бесплатный, v6.4.0), Flowframes — 2,0 тыс. (бесплатно старые сборки, свежие беты только для Patreon), Upscale-A-Video — 1,5 тыс., All-In-One-Deflicker — 764 ([Video2X](https://github.com/k4yt3x/video2x); [Flowframes](https://github.com/n00mkrad/flowframes); [deflicker search](https://github.com/search?q=deflicker&type=repositories&s=stars&o=desc), д.д. 2026-09-26). Массовый спрос есть, но он закрыт бесплатным софтом и встроенными апскейлерами генеративных платформ.
33. Трекинг стоимости AI-генераций: всего 5 репозиториев, у всех ≤10 звёзд ([GitHub](https://github.com/search?q=ai+video+generation+cost+tracker+OR+credits+tracker&type=repositories&s=stars&o=desc), д.д.). **Слабый сигнал спроса**: как самостоятельная боль выражена плохо.
34. ComfyUI: 135 тыс. звёзд, 4,3 тыс. открытых issues. comfy-cli 1.21.0 вышел 24.09.2026 и уже даёт доступ к партнёрским облачным моделям ([GitHub](https://github.com/comfyanonymous/ComfyUI); [PyPI](https://pypi.org/project/comfy-cli/), 2026-09-24). Экосистема огромная и бесплатная, при этом быстро вбирает платные облачные модели.

**DOOH и анаморфные билборды**

35. На GitHub 662 репозитория по «DOOH», почти все про ad-tech, плееры и signage, а по «anamorphic billboard» нашёлся **1 репозиторий** (сервис масок для анаморфного креатива, 0 звёзд) ([GitHub DOOH](https://github.com/search?q=dooh&type=repositories&s=updated&o=desc); [GitHub anamorphic](https://github.com/search?q=anamorphic+billboard&type=repositories), д.д. 2026-09-26). Инструментов для **производства** анаморфного контента почти нет. Это либо пустая ниша, либо ниша без массового спроса (оценка; проверять интервью со студиями).

**Рынок труда и навыки**

36. По гайду School of Motion 2026, моушн-дизайнеры со свободным владением AI получают на **15–50% больше**, спрос на AI-специализацию вырос на 49% за год, «нормальная» зарплата штатного моушн-дизайнера — $80–110k ([School of Motion](https://schoolofmotion.com/blog/motion-design-salaries-in-2026-your-complete-guide-to-what-you-can-earn-and-how-to-earn-more), 2026). В итоговом обзоре SoM за 2025 год главным дефицитным активом названы **вкус и кураторство** ([School of Motion EOY 2025](https://schoolofmotion.com/blog/eoy2025), 2025-12).

**Хронические боли AE (прокси через форумы Adobe)**

37. На Adobe Community повторяются темы с Media Encoder: не создаётся dynamic link, композиции не добавляются в очередь, AME падает при рабочем Render Queue, рендер замедляется при 200+ композициях в очереди ([Adobe Community 1](https://community.adobe.com/bug-reports-505/media-encoder-failing-to-render-when-direct-render-queue-is-ok-why-1213473); [2](https://community.adobe.com/bug-reports-510/media-encoder-will-not-add-compositions-to-queue-905118); [3](https://community.adobe.com/questions-506/render-time-slows-down-when-200-or-more-ae-comps-are-queued-995925); [4](https://community.adobe.com/questions-506/too-many-troubles-between-after-effects-and-media-encoder-996427), треды 2021–2024, д.д. 2026-09-26). GUI-обёртки над aerender на GitHub заброшены: лидер AErender-Launcher (55 звёзд) последний раз обновлялся в 2021 году ([GitHub](https://github.com/search?q=aerender&type=repositories&s=stars&o=desc), д.д.).
38. Потерянные шрифты и футаж: официальный воркфлоу Adobe — поиск «missing» и Collect Files в режиме «Generate Report Only». Пользователи жалуются, что поиск пропавших файлов в новых версиях не работает ([Adobe HelpX](https://helpx.adobe.com/sa_ar/after-effects/how-to/find-missing-footage-fonts-aftereffects.html); [Adobe Community](https://community.adobe.com/questions-529/search-for-alerted-missing-files-in-the-project-search-bar-comes-up-with-no-results-missing-23989), д.д.).

---

## 2. Сценарии: 12 / 24 / 36 месяцев (сентябрь 2026 → конец 2029)

Все вероятности — оценка потока, уверенность низкая или средняя.

| Сценарий | Вероятность | 12 мес (сент. 2027) | 24 мес (сент. 2028) | 36 мес (конец 2029) |
|---|---|---|---|---|
| **Базовый: «агент внутри AE, утилиты дешевеют, деньги в конвейерах и луках»** | 55% | AI Assistant выходит в публичную бету или GA для AE и Premiere. Figma Motion вне беты, простой UI-моушн уходит из AE. На aescripts на каждую популярную идею приходится 5–10 клонов, цены утилит падают до $10–29. Мост Figma→AE становится товаром | UXP для AE в бете или GA, старые CEP-панели нужно переписывать. Разовые утилиты (переименование, организация, выражения) почти бесплатны через агента. Устойчивы B2B-конвейеры версий (Plainly/Nexrender-класс), премиальные эффекты с «луком», пакеты контента с регулярными обновлениями | AE остаётся стандартом бренд- и рекламного моушна, но доля «ручного» моушна для соцсетей падает. Выигрывают авторы со своим каналом (YouTube, рассылка, сообщество) и продуктами «данные + шаблоны + сервис» |
| **Быстрый: «агенты съедают инструментальный слой»** | 25% | Adobe открывает MCP/агента для всех и отдаёт генерацию шаблонов текстом. Figma Motion получает экспорт видео и Lottie для всех. Продажи мелких скриптов падают на 50%+ (оценка) | Большинство задач «скрипт за $15–40» решаются промптом. Маркетплейсы переходят на бандлы и подписки. AI-видео даёт 30–50% соцконтента брендов (оценка, низкая уверенность) | В цене только доступ к данным и каналам (спецификации экранов, шаблоны брендов, клиентская база), вкус и физический мир (DOOH, ивенты) |
| **Медленный: «бета надолго»** | 20% | AI Assistant остаётся приватной бетой, UXP для AE откладывается. Спрос на утилиты стабилен, давление идёт только от клонов | Цены утилит снижаются на 20–30%, но объёмы держатся. Мост Figma→AE ещё продаётся | Рынок похож на 2025 год, только с большим числом продавцов |

**Опережающие сигналы (что мониторить и как):**
1. **Статус AI Assistant в AE и Premiere:** переход из приватной беты в публичную, затем GA. Смотреть анонсы на community.adobe.com (раздел Announcements), release notes AE, итоги Adobe MAX (октябрь 2026 и октябрь 2027). Проверять раз в месяц.
2. **UXP для AE:** появление реального контента в `AdobeDocs/uxp-after-effects` (API, гайды, минимальная версия AE) и объявление о прекращении поддержки CEP. Подписаться на Watch → Releases/Commits на GitHub.
3. **Скорость клонирования:** число новых GitHub-репозиториев «After Effects» и «figma plugin» по месяцам (поиск `created:YYYY-MM`) и число Figma→AE-инструментов на aescripts и в Figma Community. Проверять раз в квартал. Рост выше ×2 в год означает, что утилиты не защищаются кодом.
4. **Figma Motion:** появление экспорта Lottie/MP4 для всех планов, доступ плагинов к таймлайну через Plugin API, выход из беты. Следить за changelog Figma и help-центром. Если плагины получат доступ к таймлайну, открывается окно для моста «Figma Motion → AE» (идея 1 в разделе 6).
5. **Цены автоматизации:** изменения тарифов Plainly и Nexrender (снижение порога входа ниже $69 и €99 означает конкуренцию снизу). Проверять раз в квартал.

---

## 3. Ответы на ключевые вопросы

- **Что станет массовым и дешёвым (12–24 мес):** субтитры (уже есть бесплатный auto-subs на 4,3 тыс. звёзд и платные за $7–8/мес), ресайз под соцсети ($15–19 плюс бесплатные скрипты), ротоскоп (Object Matte), простой 3D в AE (меши, Substance, DoF), написание выражений и скриптов (Claude Scripter, 72 MCP-сервера, AI Assistant), апскейл и интерполяция (Video2X, Flowframes, встроенные апскейлеры генеративных платформ), простой UI-моушн (Figma Motion). Уверенность высокая.
- **Что поглотят платформы:** Adobe уже встроил Quick Apply, Object Matte, SVG→shape, Unmult, вариативные шрифты и 3D-меши, а к 2028 году (оценка) через агента заберёт организацию проектов, переименование и пакетные правки. Figma забирает UI-анимацию и хендофф моушн-спецификаций разработчикам (Dev Mode → CSS/JSON/React). Вендоры моделей (Veo, Seedance, Kling и др.) забирают консистентность персонажей и апскейл.
- **Где останутся деньги:**
  1. **Конвейеры версий для брендов** с подпиской и расходом по рендер-минутам: Plainly берёт $69–649/мес, Nexrender от €99/мес.
  2. **Премиальные «лук»-эффекты** с брендом: Deep Glow 2 поднял цену с $49,95 до $99,95.
  3. **Узкие межпрограммные мосты с быстрыми обновлениями.** Figma→AE сейчас стоит $39–69, но быстро превращается в товар.
  4. **Данные и спецификации** (DOOH-экраны, форматы площадок) и **накопленный контент** (пресеты, шаблоны, обучающие материалы).
  5. **Физический мир**: анаморфные и DOOH-проекты, где код вторичен.
- **У кого будут инструменты:** у массового пользователя через агента Adobe (при подписке CC) и через Figma (Full seat для HD-экспорта). У профессионалов останутся premium-плагины, конвейеры автоматизации и пайплайны «AI-плейт → композ». Инструментов для анаморфного 3D пока нет ни у кого (факт 35).
- **Какие навыки обесценятся:** знание меню и горячих клавиш, написание выражений вручную, базовый ротоскоп, ручной ресайз и версионирование, базовый UI-моушн, простой 3D-текст.
- **Какие станут дефицитом:** вкус и арт-дирекция (SoM EOY 2025), интеграция AI-плейтов в брендовый композ (премия за AI-навыки 15–50%, SoM 2026), проектирование систем шаблонов и данных для версий, знание физических форматов (DOOH, анаморф, LED), доверие и собственный канал дистрибуции.

---

## 4. Топ-боли (ранжированы по привлекательности для основателя)

Ранг = сила боли × доказанная готовность платить × низкая вероятность нативного решения × совпадение с профилем основателя. «Сила доказательств» — насколько подтверждено этим потоком (см. раздел 0).

### 1. Версионирование рекламного моушна: форматы, языки, варианты
- **Кто:** моушн-дизайнеры и студии, работающие на бренды, in-house-команды перформанс-маркетинга.
- **Частота:** почти каждый рекламный проект (16:9 → 9:16/4:5/1:1, плюс локализация и A/B-варианты). Оценка, средняя уверенность.
- **Как решают и сколько платят:** вручную или скриптами за $15–19. При объёмах платят подписку: Plainly $69–649/мес, Nexrender от €99/мес, Templater от $67,50 (факты 22–25).
- **Доказательства:** средние. Прямых тредов с Reddit нет. Прокси: три платных SaaS с подписочной моделью и открытым ценником, 1,9 тыс. звёзд у nexrender, множество бесплатных ресайз-скриптов (признак массовой боли).
- **Разрыв:** между «скриптом за $15» и «SaaS за $69+/мес». Нет простого локального инструмента для небольших студий: Google Sheet → шаблон AE → пакетный рендер + пресеты соцформатов + safe zones + субтитры, без облака и поминутной оплаты.
- **Решат ли Adobe/Figma нативно за 24 мес:** частично (вероятность 40%, оценка). Агент AE сможет «сделать 9:16 из этой композиции», но вряд ли станет конвейером данных с очередью рендера. У Adobe есть корпоративный стек для вариаций, но он дорогой (нет данных о ценах в этой сессии).

### 2. Мост Figma → AE с высокой точностью (эффекты, стекло, блюры, текст, auto-layout) и новым контентом Figma
- **Кто:** UI/продуктовые моушн-дизайнеры, агентства, промо приложений и SaaS.
- **Частота:** каждый UI-промо-проект. Оценка, средняя уверенность.
- **Как решают и сколько платят:** AEUX (бесплатный, заархивирован 06.2025), Overlord (ранее $45), Prism от $39, Convertify, Oblique $59–69, бесплатные клоны на GitHub (факты 9–11).
- **Доказательства:** сильные для конкуренции (6+ игроков), средние для объёма спроса.
- **Разрыв:** поддержка **новых сущностей Figma** (shader fills, code layers, Figma Motion) и **перенос анимации** из Figma Motion в AE, а не только слоёв.
- **Решат ли нативно за 24 мес:** Figma частично закрывает потребность: простой моушн делают прямо в Figma (факт 7). Adobe пока движется к SVG-импорту (факт 1). Полноценный импорт .fig в AE — вероятность 20–30% (оценка). **Главный риск: товаризация клонами, а не платформа.**

### 3. Надёжный рендер и пакетная сдача (AME, очередь, уведомления, спецификации площадок)
- **Кто:** все пользователи AE, особенно фрилансеры с ночными рендерами и студии с десятками вариантов.
- **Частота:** еженедельно. Оценка.
- **Как решают и сколько платят:** Multi-Frame Rendering в AE, AME, самописные aerender-обёртки (заброшены с 2019–2021 годов), облачные фермы, Plainly/Nexrender для масштаба.
- **Доказательства:** средние (повторяющиеся треды Adobe Community, факт 37).
- **Разрыв:** локальный «менеджер сдачи»: очередь через aerender + пресеты спецификаций (Meta, TikTok, YouTube, DOOH-операторы) + проверка результата (длительность, битрейт, громкость, safe zones) + уведомления в Telegram/Slack.
- **Решат ли нативно за 24 мес:** частично (35%, оценка). Adobe улучшает рендер, но проверка по спецификациям площадок — не его приоритет.

### 4. Анаморфные и DOOH-креативы: спецификации экранов, настройка форсированной перспективы, превью с точки зрителя, форматы сдачи
- **Кто:** 3D/моушн-студии, агентства, девелоперы и ритейл с LED-фасадами.
- **Частота:** редко в целом, но каждый проект дорогой. Оценка.
- **Как решают и сколько платят:** вручную в C4D, Blender и AE. Спецификации запрашивают у операторов экранов. Продаваемых инструментов не найдено (факт 35).
- **Доказательства:** слабые (отсутствие инструментов может означать и пустую нишу, и отсутствие спроса).
- **Разрыв:** библиотека спецификаций реальных анаморфных и DOOH-экранов, риги камеры для AE/Blender, симулятор «взгляда с улицы», чек-лист сдачи.
- **Решат ли нативно за 24 мес:** нет (<10%, оценка). Слишком узко для Adobe и Figma.

### 5. Интеграция AI-плейтов в композ (дефликер, зерно, цвет, края и альфа, апскейл, частота кадров)
- **Кто:** моушн-дизайнеры и композеры, которые вставляют кадры Veo, Kling, Seedance или Higgsfield в брендовый ролик.
- **Частота:** растёт, уже встречается в рекламных проектах. Оценка, низкая уверенность.
- **Как решают и сколько платят:** Video2X и Flowframes (бесплатно или по донатам), встроенные апскейлеры платформ, Topaz (нет данных о цене в этой сессии), в AE — ручной композ, Unmult и Object Matte (факты 1–2, 32).
- **Доказательства:** средние (десятки тысяч звёзд у апскейлеров и дефликеров).
- **Разрыв:** «AI Plate Prep» внутри AE: однокнопочная подготовка плейта (дефликер, согласование зерна с кадром, color transfer, чистка краёв, конформ частоты кадров) + пресеты под конкретные модели.
- **Решат ли нативно за 24 мес:** частично (50%). Adobe уже добавил Unmult и Object Matte, генеративные платформы улучшают выход (ProRes/альфа).

### 6. Каталог и повторное использование AI-генераций (промпты, сиды, референсы, стоимость) в разных сервисах
- **Кто:** AI-видео-креаторы и студии, работающие одновременно с 3–6 сервисами.
- **Частота:** ежедневно у активных креаторов.
- **Как решают и сколько платят:** open-source-DAM (SmartGallery 383, Image-MetaHub 322 звезды, Pro $39), папки, Notion (факт 31).
- **Доказательства:** средние для боли, слабые для готовности платить.
- **Разрыв:** нейтральная библиотека для видео с согласованием с клиентом и переносом «рецепта» между вендорами.
- **Решат ли нативно за 24 мес:** внутри своих экосистем — да: Magnific Spaces, Higgsfield, Adobe Firefly Boards (оценка). Кросс-вендорную библиотеку — нет.

### 7. Совместимость Lottie и веб-экспорта
- **Кто:** UI/продуктовые моушн-дизайнеры, передающие анимацию разработчикам.
- **Частота:** часто в продуктовых командах.
- **Как решают и сколько платят:** Bodymovin (бесплатный), плагин LottieFiles (бесплатный, платформа $19,99+/мес), Rive ($9–120/место), ручная переделка (факты 28–29).
- **Доказательства:** сильные для боли (788 открытых issues, 108 «not supported»), слабые для денег.
- **Разрыв:** проверка перед экспортом (preflight) с автоисправлением: запекание эффектов в shape-слои, замена неподдерживаемого.
- **Решат ли нативно за 24 мес:** Figma Motion экспортирует в CSS/JSON/React (факт 7) и забирает простые UI-анимации. Вероятность, что боль сильно уменьшится, 50–60% (оценка).

### 8. Гигиена проекта и передача другому человеку: потерянные шрифты и футаж, упаковка, чистка
- **Кто:** все, особенно при передаче проектов между фрилансерами и студиями.
- **Частота:** еженедельно.
- **Как решают и сколько платят:** нативный Collect Files, Dependencies, ручная работа. Платят мало: утилиты стоят $5–15.
- **Доказательства:** средние (факт 38; OPERATOR с модулем «Asset Doctor» — пока план, 0 звёзд).
- **Разрыв:** проверка лицензий шрифтов, автоматический релинк, облачная упаковка.
- **Решат ли нативно за 24 мес:** в основном да (60–70%, оценка). Агент AE закроет поиск, релинк и чистку.

### 9. Анимированные субтитры для соцсетей
- **Кто:** монтажёры, SMM, креаторы.
- **Частота:** ежедневно.
- **Сколько платят:** $6,99–8/мес, $80/год, $150 бессрочно, есть бесплатные варианты (факты 26–27).
- **Разрыв:** почти нет, ниша переполнена.
- **Решат ли нативно за 24 мес:** уже во многом решено (транскрипция в Premiere, бесплатный auto-subs). **Не заходить.**

### 10. Написание выражений и скриптов
- **Кто:** моушн-дизайнеры без навыков программирования.
- **Сколько платят:** Claude Scripter работает со своим API-ключом; 72 бесплатных MCP-сервера.
- **Решат ли нативно за 24 мес:** да (80%+, оценка), через AI Assistant. **Не заходить.**

### 11. Рутинные операции: переименование, сортировка, применение эффектов, пакетные правки
- **Сколько платят:** $5–15 за утилиту.
- **Решат ли нативно за 24 мес:** да. Quick Apply уже есть (26.2), агент в бете (26.5). **Не заходить.**

### 12. Консистентность персонажей и стиля в AI-видео
- **Доказательства:** сильные для боли (2 тыс. звёзд у репозитория промптов Seedance 2.0).
- **Решат ли за 24 мес:** решают вендоры моделей (референсы, «элементы» персонажей). Инструментом не заходить. **Возможен контентный продукт** (библиотеки промптов и референсов), но его легко скопировать.

### 13. Контроль стоимости AI-генераций
- **Доказательства:** слабые (5 репозиториев, ≤10 звёзд, факт 33).
- **Вывод:** как SaaS не заходить. Как B-тип (калькулятор и SEO) — только после проверки поискового спроса (нет данных).

### 14. Риггинг персонажей
- **Состояние:** рынок зрелый и занятый (Limber, Duik, RubberHose и др., факт 19). Adobe вряд ли встроит риггинг, но вход поздний. **Не приоритет.**

### 15. 3D внутри AE
- **Состояние:** поглощено Adobe в 26.0–26.5 (меши, Substance, displacement, DoF, 3D-текст с материалами в бете). **Не заходить** с общими 3D-инструментами.

### 16. Ротоскоп и маски
- **Состояние:** поглощено (Object Matte 26.2 с кэшем в 26.5). **Не заходить.**

### 17. Прайсинг и сметы фрилансера-моушн-дизайнера
- **Доказательства:** слабые для готовности платить. Есть информационный спрос: гайды по зарплатам SoM (факт 36).
- **Вывод:** подходит для B-типа (SEO-калькулятор) как лидогенерация для других продуктов, а не как самостоятельная выручка.

### 18. Ревью и согласование версий с клиентом
- **Состояние:** закрывает Frame.io, принадлежащий Adobe (в этой сессии не перепроверено). Вероятность поглощения высокая. **Не заходить.**

### 19. Передача моушн-спецификаций разработчикам
- **Состояние:** поглощено Figma Motion (Dev Mode → CSS/JSON/React, MCP), факт 7. **Не заходить.**

### 20. Пиратство (боль продавца, а не пользователя)
- **Доказательства:** сильные (факт 20).
- **Вывод для дизайна продукта:** закладывать онлайн-компонент (обновляемая библиотека спецификаций или пресетов, облачная проверка, лицензия с сервером), иначе заметная часть спроса уходит на варезные сайты.

---

## 5. Что продаётся на маркетплейсах

**aescripts + aeplugins (главный канал для AE-инструментов):**

| Продукт / категория | Цена | Что показывает | Источник |
|---|---|---|---|
| Deep Glow 2 (свечение, GPU) | $99,95 (V1 стоил $49,95) | Премиальный «лук» с брендом позволяет удвоить цену | [aescripts](https://aescripts.com/deep-glow/) |
| AutoCaption | $8/мес, $80/год, $150 бессрочно | Даже в переполненной нише есть подписочная модель | [aescripts](https://aescripts.com/autocaption/) |
| Captioneer, Voice2Captions | подписка и бессрочная лицензия (точные цены не получены) | Субтитры — переполненная категория | [Captioneer](https://aescripts.com/captioneer/), [Voice2Captions](https://aescripts.com/voice2captions/) |
| Smart Resize 2 | $15 | Ресайз — дешёвая утилита | [aescripts](https://aescripts.com/smart-resize/) |
| COMP Tool | $19 | То же | [Pixflow](https://pixflow.net/blog/adapt-your-after-effects-videos-seamlessly-for-any-platform/) |
| Templater Pro / Bot | подписка, от $67,50 | Автоматизация продаётся подпиской даже через aescripts | [aescripts Templater Bot](https://aescripts.com/templater-bot/), [SourceForge](https://sourceforge.net/software/product/Dataclay-Templater/) |
| Claude Scripter | свой ключ API (цена лицензии не получена) | AI-скриптинг уже продаётся на маркетплейсе | [aescripts](https://aescripts.com/claude-scripter/) |
| LottieFiles for AE | бесплатно (платформа от $19,99/мес) | Плагин как воронка в SaaS | [aescripts](https://aescripts.com/lottiefiles/) |
| OneClickExport PRO (Premiere) | нет данных | Новый продукт 2026 года в нише «экспорт в один клик» | [GitHub landing](https://github.com/birdofscript/oce-landing) |
| «Вечнозелёные» продукты по сторонним обзорам 2026 года | нет данных по ценам в этой сессии | Plexus, GEOlayers, Helium, Lockdown, Newton, Flow, Stardust, Limber, Animation Composer, RSMB, Trapcode, Element 3D, Saber, FX Console | [Toolfarm](https://www.toolfarm.com/products/subcategory/aescripts_aeplug_ins/), [Maxon](https://www.maxon.net/en/article/best-after-effects-plugins), [SoM](https://schoolofmotion.com/blog/best-after-effects-plugins-and-effect-packs-you-need-in-2026) |

Чем прокси-бестселлеры отличаются от утилит: у каждого из них есть либо **сложный рендер или симуляция** (Plexus, Stardust, Newton, Deep Glow, Trapcode), либо **данные и контент** (GEOlayers — карты, Animation Composer — библиотека пресетов), либо **глубина в узком воркфлоу** (Flow — кривые, Limber — риг, Lockdown — трекинг деформаций). Утилит уровня «переименовать слои» среди них нет. Это совпадает с тезисом, что выигрывает не код.

**Figma → AE (прямые конкуренты Oblique):** Prism от $39, Overlord (ранее $45; с Figma-плагином), Convertify (цена не получена), AEUX (бесплатный, заархивирован), бесплатные клоны на GitHub (LazyLord, OverAE и др.). Нижняя граница рынка ($39) на 34% ниже стартовой цены Oblique ($59).

**Автоматизация и SaaS (вне маркетплейсов):** Plainly $69–649/мес, Nexrender Cloud от €99 до €350+/мес, Templater от $67,50. Рендер-минуты — главная единица тарификации.

**Lottie и интерактивный моушн:** LottieFiles $19,99–119,99/мес, Rive $9–120 за место в месяц.

**AI-воркфлоу:** Image-MetaHub Pro $39 разово. Flowframes монетизирует свежие беты через Patreon. Остальные решения open-source.

**Gumroad:** DynaCap $6,99/мес (субтитры), бесплатные шаблоны под несколько соотношений сторон. Battle Axe ушёл с Gumroad на свой сайт.

**Figma Community (топ платных плагинов), Envato Elements и Motion Array (топ категорий), Product Hunt (запуски 2025–2026 с апвоутами), Upwork (ставки и объём заказов «template customization» и «resize video ads»), YouTube (просмотры туториалов):** **нет данных.** Источники заблокированы, лимит поиска исчерпан. Лучший доступный прокси для Figma — рост числа новых репозиториев «figma plugin» в 2,3 раза за год и доминирование MCP-мостов среди них (факт 13). Для Envato и Motion Array прокси нет. Рекомендация — ручная проверка по чек-листу в разделе 7.

---

## 6. Возможности для основателя

Фильтры: запуск за 2–6 недель с Claude Code, поддержка 2–4 часа в неделю, защита не кодом. Отдельно учитывается, что UK LTD + Payoneer + Бали могут ограничить некоторые платёжные и аффилиатные программы.

### Идея 1. «Oblique Motion Bridge»: из моста для слоёв в мост для анимации и новых эффектов Figma (развитие текущего продукта)
- **Суть:** переносить в AE не только слои, но и **анимацию Figma Motion** (ключи, изинги, пресеты), а также новые **shader fills и эффекты Figma**, с библиотекой AE-пресетов, откалиброванных под «стекло», блюры и шейдеры Figma.
- **Тип:** A.
- **Формат:** расширение существующего плагина (Figma-плагин + CEP/UXP-панель AE). Платный апгрейд или версия 2.0 на aescripts за $69–99, продажи напрямую и бандлом с пресетами.
- **Покупатель и боль:** UI-моушн-дизайнеры и агентства. Анимацию теперь прототипируют в Figma Motion (с 24.06.2026), а финальный рекламный ролик собирают в AE. Сейчас такую анимацию приходится переделывать вручную.
- **Доказательства спроса:** средние. Вокруг мостов Figma→AE уже 6+ платных и бесплатных инструментов (факты 9–11), бесплатный лидер ушёл (факт 9), Figma запустила Motion (факт 7). Прямых данных об объёме продаж нет.
- **Конкуренты и цены:** Prism от $39, Overlord (ранее $45), Convertify, бесплатные клоны. Переноса именно анимации Figma Motion в AE у конкурентов не найдено (по данным этого потока; нужно проверить).
- **Гипотеза защиты:** скорость обновлений после каждого релиза Figma, глубина воркфлоу (основатель сам делает такие проекты), бренд и сообщество вокруг Oblique, ранний переход на UXP.
- **Главный риск:** Plugin API Figma может не давать доступа к данным таймлайна Motion (**нет данных**, проверить в первую очередь). Кроме того, клоны появятся через 2–3 месяца. Если Figma откроет экспорт Lottie или видео для всех, часть сценариев отпадёт.

### Идея 2. «Anamorphic Kit»: риги, превью и спецификации для анаморфных 3D-билбордов
- **Суть:** набор для AE и Blender (C4D опционально): камера с форсированной перспективой, построенная по геометрии конкретного углового экрана, превью «взгляд пешехода», пресеты рендера под популярные анаморфные экраны, чек-лист сдачи оператору.
- **Тип:** A (прямое преимущество за счёт студии и 3D-команды).
- **Формат:** пакет шаблонов и скриптов на aescripts или Gumroad за $79–149 плюс воронка на услуги студии.
- **Покупатель и боль:** небольшие 3D/моушн-студии и агентства, которым впервые заказали анаморф. Каждый раз с нуля выясняют спецификации и строят перспективу, а ошибка ломает иллюзию объёма.
- **Доказательства спроса:** слабые. Готовых инструментов практически нет (1 репозиторий на GitHub, факт 35). Объём рынка — нет данных. Проверить: интервью с 5–10 студиями, поиск «anamorphic billboard tutorial» на YouTube и Gumroad.
- **Конкуренты и цены:** продаваемых аналогов не найдено. Бесплатные туториалы на YouTube (нет данных по просмотрам).
- **Гипотеза защиты:** реальные спецификации из проектов студии, связи с операторами экранов, портфолио студии как доверие. Продукт работает на две цели: выручку и лидогенерацию для студии.
- **Главный риск:** слишком маленький рынок покупателей инструмента. Выручка может оказаться только от лидогенерации.

### Идея 3. «DOOH Spec Atlas»: база спецификаций DOOH и анаморфных экранов + пресеты экспорта
- **Суть:** SEO-сайт или каталог спецификаций экранов (разрешение, соотношение, длительность, fps, кодек, safe areas, контакт оператора) по городам и сетям. Бесплатная часть — поиск, платная — пакет пресетов AE, AME и Premiere под сети и проверка файла перед сдачей.
- **Тип:** AB (данные + автоматизация, синергия со студией).
- **Формат:** сайт (Claude Code) + загружаемые пресеты за $29–49 + лидогенерация для студии.
- **Покупатель и боль:** моушн-дизайнеры и агентства, которым прислали «макет на 3 экрана в 3 странах»: спецификации разбросаны по PDF операторов.
- **Доказательства спроса:** нет данных о поисковом спросе. Прокси: 662 DOOH-репозитория по ad-tech, но почти нет творческих инструментов (факт 35). Проверить через Keyword Planner или Ahrefs объёмы «[сеть] specs», «billboard dimensions [город]».
- **Конкуренты и цены:** спецификации публикуют сами операторы и SSP (нет данных в этой сессии).
- **Гипотеза защиты:** накопленные и регулярно обновляемые данные, SEO-позиции, доверие со стороны студии.
- **Главный риск:** низкая монетизация (пользователи заходят на сайт по разу на проект). Сбор и поддержка данных может занять больше 4 часов в неделю.

### Идея 4. «Variant Factory Lite»: локальный конвейер версий для малых студий
- **Суть:** CEP/UXP-панель: Google Sheet или CSV → слоты шаблона AE (тексты, медиа, цвета, языки) → автоматические форматы 9:16, 4:5, 1:1 и 16:9 с safe zones → пакетный рендер через aerender на собственной машине с проверкой результата и отчётом.
- **Тип:** A.
- **Формат:** разовая лицензия $99–149 или $15–19/мес. Каналы — aescripts и прямые продажи.
- **Покупатель и боль:** фрилансеры и студии из 1–10 человек, которым нужно 20–200 вариантов на кампанию. Plainly со своими $69/мес за 50 минут для них дорог или избыточен, а скрипт за $15 не решает задачу целиком.
- **Доказательства спроса:** средние. Три SaaS продают это же корпорациям подпиской (факты 22–24), ресайз-скриптов много (факт 25), в Adobe Community повторяются боли с рендером (факт 37).
- **Конкуренты и цены:** Plainly $69–649/мес, Nexrender €99+/мес (open-source ядро бесплатно), Templater от $67,50, скрипты ресайза $15–19.
- **Гипотеза защиты:** набор готовых рекламных шаблонов-систем и пресетов площадок от практикующего моушн-дизайнера, то есть контент, а не код.
- **Главный риск:** поддержка разных машин и версий AE может превысить 4 часа в неделю. Агент Adobe может закрыть сценарий «сделай 9:16» (вероятность частичного решения 40%). Open-source nexrender бесплатен.

### Идея 5. «AI Plate Prep»: подготовка AI-плейтов для композа в AE
- **Суть:** панель плюс пресеты: импорт плейта из Higgsfield, Kling, Veo или Seedance → конформ частоты кадров → дефликер → согласование зерна с проектом → color transfer под референс → чистка краёв и Unmult → опционально апскейл через API. Пресеты под «характер» конкретных моделей.
- **Тип:** A.
- **Формат:** скрипт и пакет пресетов за $39–59, с бесплатным обновлением пресетов под новые модели.
- **Покупатель и боль:** моушн-дизайнеры, которые вставляют AI-кадры в брендовые ролики. AI-кадры мерцают, не совпадают по зерну и цвету и имеют «грязные» края.
- **Доказательства спроса:** средние (Video2X 21,8 тыс., Upscale-A-Video 1,5 тыс., Deflicker 764 звезды, факт 32; премия за AI-навыки 15–50%, факт 36).
- **Конкуренты и цены:** Video2X и Flowframes бесплатно, Topaz (нет данных), встроенные апскейлеры платформ, нативные Unmult и Object Matte в AE.
- **Гипотеза защиты:** скорость обновления пресетов под новые модели и экспертиза основателя в композе.
- **Главный риск:** платформы улучшают качество и форматы выхода, Adobe добавляет AI-очистку. Срок жизни продукта может оказаться 12–18 месяцев.

### Идея 6. «Lottie Preflight»: проверка и автоисправление перед экспортом Lottie
- **Суть:** скрипт для AE находит неподдерживаемые в Lottie функции (эффекты, blend modes, 3D, выражения), предлагает запечь их в shape-слои или заменить, показывает прогноз размера JSON и превью.
- **Тип:** A.
- **Формат:** $19–29 на aescripts.
- **Покупатель и боль:** продуктовые моушн-дизайнеры. Анимация «ломается» у разработчиков.
- **Доказательства спроса:** сильные для боли (788 открытых issues, 108 «not supported», факт 28), слабые для готовности платить.
- **Конкуренты и цены:** Bodymovin и плагин LottieFiles (бесплатно), Rive, Figma Motion.
- **Гипотеза защиты:** глубина в узкой задаче. Слабая.
- **Главный риск:** Figma Motion и LottieFiles закрывают сценарий. Низкий чек.

### Идея 7 (тип B). «AI Video Price Tracker»: калькулятор стоимости секунды AI-видео по моделям и платформам
- **Суть:** SEO-сайт с актуальными ценами генерации (за секунду, за кредит, по разрешению) у Veo, Kling, Seedance, Runway, Higgsfield, Magnific и др. Калькулятор бюджета проекта. Монетизация — аффилиатные программы и реклама.
- **Тип:** B.
- **Формат:** сайт с еженедельным обновлением данных; сбор автоматизирует Claude Code.
- **Покупатель и боль:** креаторы и студии, которые считают бюджет AI-ролика.
- **Доказательства спроса:** **слабые** (5 репозиториев, ≤10 звёзд, факт 33). Поисковый спрос — нет данных.
- **Конкуренты:** агрегаторы и обзорные блоги (нет данных в этой сессии).
- **Гипотеза защиты:** скорость обновления данных и SEO-история.
- **Главный риск:** низкий спрос. Доступность аффилиатных программ для UK LTD с выплатой на Payoneer не проверена. Google AI Overviews перехватывают трафик.

### Идея 8 (тип B). «Motion Rate Calculator»: калькулятор ставок и смет для моушн-проектов по странам и форматам
- **Суть:** SEO-калькулятор «сколько стоит 30-секундный моушн-ролик, анимированный логотип, 3D-анаморф в [стране]». Лидогенерация для студии и точка кросс-продаж шаблонов.
- **Тип:** B (с синергией A через студию).
- **Доказательства спроса:** информационный спрос подтверждают зарплатные гайды SoM (факт 36). Готовность платить низкая.
- **Главный риск:** данные о ставках трудно проверить, в нише сильные игроки контента (SoM).

### Что не делать (по данным потока)
Субтитры, ассистенты для выражений и скриптов, утилиты организации проекта, ротоскоп, общий 3D в AE, инструменты консистентности персонажей, ревью и согласование. Всё это уже массово и дёшево или поглощено Adobe, Figma либо вендорами моделей (разделы 1 и 4).

---

## 7. Что проверить руками до запуска (1–2 часа, закрывает пробелы этого потока)

1. **Reddit** (r/AfterEffects, r/MotionDesign, r/aivideo, r/FigmaDesign): поиск «figma motion after effects», «anamorphic», «resize versions», «AI footage flicker», «lottie not working» за 2026 год. Выписать 10 тредов с числом апвоутов и комментариев.
2. **aescripts:** сортировки «Best Sellers» и «Newest» в категориях Scripts и Extensions. Выписать топ-30 с ценой и числом отзывов, отдельно посчитать все Figma→AE-инструменты.
3. **Plugin API Figma:** есть ли доступ к данным таймлайна Figma Motion. От этого зависит, жива ли идея 1.
4. **Figma Community → Plugins → Paid:** топ-20 по числу пользователей.
5. **Envato Elements и Motion Array:** топ категорий AE-шаблонов за 2026 год (соцсети, титры, лого, переходы, AI-ориентированные).
6. **Upwork:** число открытых заказов «After Effects template customization» и «resize video ads», медианный бюджет.
7. **Keyword Planner или Ahrefs:** объёмы запросов «anamorphic billboard», «DOOH specs», «billboard size [город]», «AI video cost per second».

---

## 8. Источники

1. CG Channel — AE 26.0 с нативным Substance: https://www.cgchannel.com/2026/01/adobe-releases-after-effects-26-0-with-native-substance-support/ (2026-01)
2. postPerspective — Premiere и AE 2026: https://postperspective.com/quick-look-adobes-premiere-and-after-effects-2026-updates/ (д.д. 2026-09-26)
3. VFXer — разбор AE 2026: https://www.vfxer.com/after-effects-2026-new-features-technical-breakdown/ (д.д. 2026-09-26)
4. CG Channel — AE 26.2: https://www.cgchannel.com/2026/04/adobe-releases-after-effects-26-2/ (2026-04)
5. ProVideo Coalition — AE 26.2: https://www.provideocoalition.com/after-effect-26-2-april-2026-release/ (2026-04)
6. CG Channel — AE 26.3: https://www.cgchannel.com/2026/06/adobe-releases-after-effects-26-3/ (2026-06)
7. CG Channel — AE 26.5 и AI Assistant: https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/ (2026-09)
8. Adobe Community — AE 26.5: https://community.adobe.com/announcements-527/after-effects-26-5-is-here-1641108 (2026-09)
9. Adobe Community — бета AI Assistant: https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658 (2026)
10. Creative COW — AI Assistant (MCP) в бете AE: https://creativecow.net/forums/thread/adobe-adds-an-ai-assistant-mcp-to-after-effects-beta-private-beta/ (2026)
11. Adobe Exchange — AI Assistant for After Effects: https://exchange.adobe.com/apps/cc/203667/ai-assistant-for-after-effects (д.д. 2026-09-26)
12. ProVideo Coalition — AI Assistant в Premiere: https://www.provideocoalition.com/premiere-ai-assistant/ (2026)
13. Broadcast — AI-агент в Premiere: https://www.broadcastnow.co.uk/production-and-post/adobe-rolls-out-ai-agent-on-premiere/5217912.article (2026)
14. GitHub — AdobeDocs/uxp-after-effects (коммиты): https://github.com/AdobeDocs/uxp-after-effects/commits/main (2026-09-23)
15. CMSWire — Config 2026 (Code Layers, Motion): https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/ (2026-06)
16. Figma Blog — Introducing Figma Motion: https://www.figma.com/blog/introducing-figma-motion/ (2026-06-24)
17. Figma Help — What's new from Config 2026: https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026 (2026-06)
18. GitHub — google/AEUX (архив): https://github.com/google/AEUX (2025-06-21)
19. Next Horizon — AEUX vs Overlord vs Convertify vs Prism: https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma (д.д. 2026-09-26)
20. Battle Axe — Overlord: https://battleaxe.co/overlord (д.д. 2026-09-26)
21. Figma Community — Overlord: https://www.figma.com/community/plugin/1433559588746637449/overlord (д.д. 2026-09-26)
22. Gumroad — Timelord переехал на battleaxe.co: https://battleaxe.gumroad.com/l/timelord (д.д. 2026-09-26)
23. GitHub search «figma after effects»: https://github.com/search?q=figma+after+effects&type=repositories&s=updated&o=desc (д.д. 2026-09-26)
24. GitHub search «After Effects», созданные в 2025: https://github.com/search?q=%22after+effects%22+created%3A2025-01-01..2025-09-26&type=repositories (д.д. 2026-09-26)
25. GitHub search «After Effects», созданные в 2026: https://github.com/search?q=%22after+effects%22+created%3A%3E2026-01-01&type=repositories (д.д. 2026-09-26)
26. GitHub search «figma plugin», 2025: https://github.com/search?q=%22figma+plugin%22+created%3A2025-01-01..2025-09-26&type=repositories (д.д. 2026-09-26)
27. GitHub search «figma plugin», 2026: https://github.com/search?q=%22figma+plugin%22+created%3A%3E2026-01-01&type=repositories (д.д. 2026-09-26)
28. GitHub search «after effects mcp»: https://github.com/search?q=after+effects+mcp&type=repositories (д.д. 2026-09-26)
29. GitHub — Dakkshin/after-effects-mcp: https://github.com/Dakkshin/after-effects-mcp (д.д. 2026-09-26)
30. aescripts — Claude Scripter: https://aescripts.com/claude-scripter/ (д.д. 2026-09-26)
31. aescripts — Become an Author (комиссия): https://aescripts.com/faq/article/view/faq/become-an-author/ (д.д. 2026-09-26)
32. School of Motion — сколько зарабатывают разработчики скриптов (Zack Lovatt): https://schoolofmotion.com/blog/how-much-do-after-effects-script-developers-make-a-chat-with-zack-lovatt (д.д. 2026-09-26)
33. Easyweb — обзор aescripts 2026: https://www.easyweb-agency.fr/en/outils-comparatifs/aescripts (2026)
34. aescripts — Summer of Sales 2026: https://aescripts.com/learn/post/summer-of-sales-2026 (2026-05)
35. aescripts — Deep Glow 2: https://aescripts.com/deep-glow/ (д.д. 2026-09-26)
36. Toolfarm — продукты aescripts + aeplugins: https://www.toolfarm.com/products/subcategory/aescripts_aeplug_ins/ (д.д. 2026-09-26)
37. Maxon — лучшие плагины AE 2026: https://www.maxon.net/en/article/best-after-effects-plugins (2026)
38. Vagon — лучшие плагины AE 2026: https://vagon.io/blog/top-10-plugins-for-after-effects (2026)
39. School of Motion — лучшие плагины 2026: https://schoolofmotion.com/blog/best-after-effects-plugins-and-effect-packs-you-need-in-2026 (2026)
40. FileCR — пиратский Deep Glow 2: https://filecr.com/macos/aescripts-deep-glow2/ (д.д. 2026-09-26)
41. INTRO HD — пиратский Overlord: https://intro-hd.net/battle-axe-overlord-for-after-effects-illustrator/ (д.д. 2026-09-26)
42. riztagar — пиратский Overlord: https://riztagar.com/battle-axe-overlord-for-after-effects/ (д.д. 2026-09-26)
43. GitHub search «aescripts» (SEO и варез-репозитории): https://github.com/search?q=aescripts&type=repositories&s=updated&o=desc (д.д. 2026-09-26)
44. Capterra — Plainly: https://www.capterra.com/p/10026817/Plainly/ (2026)
45. ColdIQ — Plainly: https://coldiq.com/tools/plainly (2026)
46. Nexrender — Pricing: https://www.nexrender.com/pricing (2026)
47. GitHub — inlife/nexrender: https://github.com/inlife/nexrender (д.д. 2026-09-26)
48. SourceForge — Dataclay Templater: https://sourceforge.net/software/product/Dataclay-Templater/ (2026)
49. Dataclay — Templater Licensing Guide: https://dataclay.com/blog/templater-licensing-guide/ (д.д. 2026-09-26)
50. aescripts — Templater Bot: https://aescripts.com/templater-bot/ (д.д. 2026-09-26)
51. aescripts — Smart Resize: https://aescripts.com/smart-resize/ (д.д. 2026-09-26)
52. Pixflow — ресайз под соцсети в AE: https://pixflow.net/blog/adapt-your-after-effects-videos-seamlessly-for-any-platform/ (д.д. 2026-09-26)
53. Creative COW — бесплатный скрипт ресайза: https://creativecow.net/how-i-automated-social-media-resizing-in-after-effects-free-script/ (д.д. 2026-09-26)
54. Gumroad — шаблон под несколько соотношений сторон: https://davemh.gumroad.com/l/multiple-aspect-ratio-after-effects-template (д.д. 2026-09-26)
55. aescripts — AutoCaption: https://aescripts.com/autocaption/ (д.д. 2026-09-26)
56. aescripts — Captioneer: https://aescripts.com/captioneer/ (д.д. 2026-09-26)
57. aescripts — Voice2Captions: https://aescripts.com/voice2captions/ (д.д. 2026-09-26)
58. AEJuice — Auto Captions: https://aejuice.com/product/auto-captions/ (д.д. 2026-09-26)
59. Gumroad — DynaCap: https://acceleratecreative.gumroad.com/l/dynacapmonthly (д.д. 2026-09-26)
60. GitHub — tmoroney/auto-subs: https://github.com/tmoroney/auto-subs (д.д. 2026-09-26)
61. GitHub — airbnb/lottie-web: https://github.com/airbnb/lottie-web (д.д. 2026-09-26)
62. GitHub — issues lottie-web «not supported»: https://github.com/search?q=repo%3Aairbnb%2Flottie-web+is%3Aissue+is%3Aopen+not+supported&type=issues (д.д. 2026-09-26)
63. LottieFiles — поддерживаемые функции AE: https://help.lottiefiles.com/supported-after-effects-features (д.д. 2026-09-26)
64. LottieFiles Forum — проблемы экспорта из Figma: https://forum.lottiefiles.com/t/issues-with-figmas-export-to-lottie/4744 (д.д. 2026-09-26)
65. LottieFiles — Pricing: https://lottiefiles.com/pricing (2026)
66. TrustRadius — цены LottieFiles: https://www.trustradius.com/products/lottiefiles-platform/pricing (2026)
67. aescripts — LottieFiles for AE: https://aescripts.com/lottiefiles/ (д.д. 2026-09-26)
68. Gappsy — Rive: https://www.gappsy.com/tools/rive/ (2026)
69. SaasHunter — Lottie vs Rive: https://saashunter.pro/compare/lottie-vs-rive (2026)
70. GitHub search «character consistency video»: https://github.com/search?q=character+consistency+video&type=repositories&s=stars&o=desc (д.д. 2026-09-26)
71. GitHub search «comfyui prompt manager»: https://github.com/search?q=comfyui+prompt+manager&type=repositories&s=stars&o=desc (д.д. 2026-09-26)
72. GitHub — Image-MetaHub: https://github.com/LuqP2/Image-MetaHub (д.д. 2026-09-26)
73. GitHub — k4yt3x/video2x: https://github.com/k4yt3x/video2x (д.д. 2026-09-26)
74. GitHub — n00mkrad/flowframes: https://github.com/n00mkrad/flowframes (д.д. 2026-09-26)
75. GitHub search «deflicker»: https://github.com/search?q=deflicker&type=repositories&s=stars&o=desc (д.д. 2026-09-26)
76. GitHub search — трекинг стоимости AI-видео: https://github.com/search?q=ai+video+generation+cost+tracker+OR+credits+tracker&type=repositories&s=stars&o=desc (д.д. 2026-09-26)
77. GitHub — ComfyUI: https://github.com/comfyanonymous/ComfyUI (д.д. 2026-09-26)
78. PyPI — comfy-cli 1.21.0: https://pypi.org/project/comfy-cli/ (2026-09-24)
79. GitHub search «dooh»: https://github.com/search?q=dooh&type=repositories&s=updated&o=desc (д.д. 2026-09-26)
80. GitHub search «anamorphic billboard»: https://github.com/search?q=anamorphic+billboard&type=repositories (д.д. 2026-09-26)
81. School of Motion — зарплаты в моушн-дизайне 2026: https://schoolofmotion.com/blog/motion-design-salaries-in-2026-your-complete-guide-to-what-you-can-earn-and-how-to-earn-more (2026)
82. School of Motion — итоги 2025 года: https://schoolofmotion.com/blog/eoy2025 (2025-12)
83. Adobe Community — Media Encoder падает при рабочем Render Queue: https://community.adobe.com/bug-reports-505/media-encoder-failing-to-render-when-direct-render-queue-is-ok-why-1213473 (д.д. 2026-09-26)
84. Adobe Community — AME не добавляет композиции в очередь: https://community.adobe.com/bug-reports-510/media-encoder-will-not-add-compositions-to-queue-905118 (д.д. 2026-09-26)
85. Adobe Community — замедление при 200+ композициях в очереди: https://community.adobe.com/questions-506/render-time-slows-down-when-200-or-more-ae-comps-are-queued-995925 (д.д. 2026-09-26)
86. Adobe Community — проблемы связки AE и AME: https://community.adobe.com/questions-506/too-many-troubles-between-after-effects-and-media-encoder-996427 (д.д. 2026-09-26)
87. GitHub search «aerender»: https://github.com/search?q=aerender&type=repositories&s=stars&o=desc (д.д. 2026-09-26)
88. Adobe HelpX — поиск потерянных шрифтов и футажа: https://helpx.adobe.com/sa_ar/after-effects/how-to/find-missing-footage-fonts-aftereffects.html (д.д. 2026-09-26)
89. Adobe Community — не работает поиск потерянных файлов: https://community.adobe.com/questions-529/search-for-alerted-missing-files-in-the-project-search-bar-comes-up-with-no-results-missing-23989 (д.д. 2026-09-26)
90. GitHub — OPERATOR для AE (в стадии планирования): https://github.com/runeveilstudio/operatorae (д.д. 2026-09-26)
91. GitHub — лендинг OneClickExport PRO: https://github.com/birdofscript/oce-landing (д.д. 2026-09-26)
