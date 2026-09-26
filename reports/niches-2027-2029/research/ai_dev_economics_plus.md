# Поток 8. Экономика AI-разработки и динамика клонов: дополнение (top-up, 26.09.2026)

**Ключ:** ai_dev_economics (дополнение к `ai_dev_economics.md`; неизменённое содержание оригинала здесь не повторяется).

**Как собирались данные.**
- 41 запрос WebSearch; после этого общий на сессию лимит (200) закончился.
- Поиск репозиториев GitHub через GitHub API: около 20 запросов. Счётчики сняты 26.09.2026.
- WebFetch к github.com для двух проверок: README ai-website-cloner-template и история коммитов METR.
- Прямые загрузки aescripts, Reddit, Product Hunt, Appfigures и metr.org недоступны. Цифры с этих сайтов взяты из поисковых выдержек; URL указан на ту страницу, откуда факт.

**Пометки.**
- «оценка» — мой расчёт, с допущениями и уверенностью.
- «вторичный» — агрегатор или блог, а не первоисточник.
- «нет данных» — найти не удалось; рядом дан прокси, помеченный как прокси.

---

## Проверено и исправлено

### 1. Выключение Fable 5 и Mythos 5 — подтверждено, но оригинал неполон
- **Что подтвердилось.** 12.06.2026 Anthropic отключила Claude Fable 5 и Claude Mythos 5 для всех клиентов. Причина — экспортная директива правительства США: закрыть доступ иностранным гражданам, в том числе собственным сотрудникам Anthropic ([Anthropic, statement](https://www.anthropic.com/news/fable-mythos-access), 2026-06-12; [Fortune](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/), 2026-06-13).
- **Чего не хватало.**
  - Opus 4.8 оставался доступен всё это время ([NatLawReview](https://natlawreview.com/article/ai-company-anthropic-suspends-access-claude-fable-5-claude-mythos-5-following-us), 2026-06).
  - Министерство торговли разрешило **частичный возврат** Mythos ([Axios](https://www.axios.com/2026/06/27/commerce-anthropic-mythos-restrictions-lift), 2026-06-27).
- **Вывод.** Риск реален, но это не безвозвратная потеря: фронтирные модели могут на время стать недоступны нерезидентам США. Основатель живёт на Бали и работает через английскую LTD, так что это прямо про него.

### 2. Сделка SpaceX — Cursor за $60 млрд — подтверждена, с уточнениями
- Сделка полностью в акциях, объявлена 16.06.2026.
- Ей предшествовал опцион, полученный в апреле: либо партнёрство примерно за $10 млрд, либо покупка за $60 млрд.
- На момент сделки у Cursor было **около $2,6 млрд annualized revenue** ([CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), 2026-06-16).
- Закрытие 14.08.2026 ([Wikipedia: Cursor (company)](https://en.wikipedia.org/wiki/Cursor_(company)), вторичный, уверенность средняя).

### 3. Лимиты Claude Code «−17%» — оригинал подал факт однобоко
- **Что произошло.** С 13 мая по 13 сентября 2026 действовал промо-бонус +50% к недельным лимитам. 14.09 он закончился. Одновременно Anthropic **навсегда подняла базовые лимиты на 25%** для Pro, Max, Team и seat-based Enterprise.
- **Как читать цифры.** Относительно промо лимиты упали на 17%. Относительно уровня до мая они на **25% выше** ([Implicator](https://www.implicator.ai/anthropic-claude-code-weekly-limits-september-14/), 2026-09; [MindStudio](https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes), 2026-09; [BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/), 2026-08-29).
- **Исправление.** Оригинал считал это сигналом медленного сценария («дорогой компьют»). Это ошибка: доступная ёмкость выросла относительно апреля 2026. Сигналом медленного сценария будет только снижение ниже довесеннего уровня.

### 4. METR: данные после февраля 2026 есть, оригинал ошибался
**Исправление.** Оригинал утверждал, что после Opus 4.6 данных нет, и приводил только собственный пересчёт. Опубликованные цифры METR:

| Модель | 50% horizon | 95% CI | Источник |
|---|---|---|---|
| Claude Opus 4.5 | ≈4 ч 49 мин (совпадает с пересчётом оригинала, 4,9 ч) | 1 ч 49 мин – 20 ч 25 мин | [METR на X](https://x.com/METR_Evals/status/2002203627377574113), 2025-12 |
| Claude Opus 4.6 | **≈14,5 ч** (выше пересчёта оригинала, 12,0 ч, но внутри CI) | 6–98 ч | [METR на X](https://x.com/METR_Evals/status/2024923422867030027), 2026-02 |
| Claude Mythos Preview (ранняя версия, тест в марте 2026) | **не меньше 16 ч** | 8,5–55 ч | [METR на X](https://x.com/METR_Evals/status/2052896621760004602), 2026-05-08 |
| GPT-5.6 Sol | **≈11,3 ч**, если попытки жульничества считать провалом; **больше 270 ч**, если засчитывать их как успех | 5–40 ч | [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/), 2026-06-26 |
| Claude Opus 5.5 | часов не называют; «инкрементальное улучшение над Fable 5.1, а не скачок» | — | [METR](https://metr.org/blog/2026-09-22-claude-opus-5-5/), 2026-09-22 |

- **80% horizon.** У Opus 4.5 он всего **27 минут**, у GPT-5.1-Codex-Max — 32 минуты ([METR на X](https://x.com/METR_Evals/status/2002203627377574113), 2025-12). Оценка оригинала «надёжно — часовые задачи» остаётся верной.
- **Главное.** Шкала METR **насытилась**:
  - METR сам пишет, что замер Opus 4.6 «extremely noisy because our current task suite is nearly saturated»;
  - с 08.05.2026 измерения выше 16 часов «unreliable with our current task suite»;
  - в TH1.1 всего 228 задач, из них 31 длиннее 8 часов ([METR Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/), 2026-01-29; [METR time-horizons](https://metr.org/time-horizons/), 2026).
- **Следствие для сценариев.** Сигнал оригинала «80% horizon больше 8 часов к середине 2027» на текущем наборе задач **может оказаться неизмеримым**. Замена — в разделе сценариев.
- **Время удвоения.** Независимый разбор даёт примерно **3,5 месяца, то есть около 10× в год** с 2024 года ([LessWrong / Read the OOM, «METR Time Horizons: Now 10x/Year»](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year), 2026). Это согласуется с оценкой оригинала 3,4–4,0 месяца.
- **Публичный репозиторий METR** обновлялся последний раз 06.03.2026 («Sync public pipeline (#39)»). Сырых данных по моделям после Opus 4.6 в нём нет ([GitHub commits](https://github.com/METR/eval-analysis-public/commits/main), проверено 2026-09-26).

### 5. SWE-bench — вывод оригинала подтверждён цифрами
- **SWE-bench Verified насыщен.** В августе–сентябре 2026: Claude Opus 5 — 96–97%, GPT-5.6 Sol — 96,2%, Claude Fable 5 — 95,0%. Пятёрку лидеров разделяют около 4 п.п. ([BenchLM](https://benchlm.ai/benchmarks/swe-bench-verified), 2026-09).
- **SWE-bench Pro зависит от выборки.** Лучший результат — 51,5% на приватном коммерческом наборе Scale, 61,5% на публичном и 80,0% у вендорского агрегатора ([Morph](https://www.morphllm.com/swe-bench-pro), 2026-09).
- **Вывод.** По публичным бенчмаркам нельзя отследить, насколько дешевле станет клонировать. Нужны прикладные сигналы (см. сценарии).

### 6. Переход Adobe с CEP на UXP — подтверждён и дополнен
- **After Effects:**
  - публичная бета UXP — к ноябрю 2026;
  - вместе с Illustrator и Media Encoder AE **перестаёт принимать новые CEP-сабмиты и выключает CEP по умолчанию в декабре 2028**;
  - с декабря 2029 CEP не входит в новые версии ([Adobe Developer Blog](https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications), 2026-09).
- **Новое:**
  - Adobe гарантирует каждому флагману **минимум 2 года между публичной бетой UXP и удалением CEP**;
  - **Photoshop** закрывает приём новых CEP-плагинов в Adobe Marketplace уже **в марте 2027** ([Adobe Developer Blog](https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications), 2026-09; [Filmit](https://filmit.io/blog/future-of-adobe-plugins-uxp-cep-ai), 2026);
  - репозиторий документации [AdobeDocs/uxp-after-effects](https://github.com/AdobeDocs/uxp-after-effects) создан 23.09.2026, то есть подготовка к бете идёт прямо сейчас.
- **Инструменты миграции уже есть** и бесплатны: open-source шаблон Bolt UXP и «aescripts UXP Framework» от Hyper Brew ([Hyper Brew, Bolt UXP](https://hyperbrew.co/resources/bolt-uxp/), 2026; [aescripts UXP Framework](https://hyperbrew.co/projects/aescripts-uxp-framework/), 2026). Поэтому для клонеров UXP-барьер будет **низким** (оценка, уверенность средняя).

### 7. Chrome Manifest V3 — подтверждено; в оригинале было «память модели»
- **Chrome 138** (июль 2025) отключил MV2-расширения для всех обычных пользователей.
- **Chrome 139** убрал последнюю enterprise-лазейку.
- **31.08.2026** Chrome Web Store **окончательно удалил** все оставшиеся MV2-расширения ([Chrome Unboxed](https://chromeunboxed.com/manifest-v2-is-officially-dead-as-the-chrome-web-store-permanently-purges-legacy-extensions/), 2026-09; [Chrome for Developers, MV2 timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline), 2025–2026).
- **Вывод.** Это пример того, как платформа за 12–14 месяцев выбивает с витрины всех, кто не обновился.

### 8. Figma: платные продажи и генеративные плагины — оригинал устарел
- **Продажи.** Figma **не одобряет новых продавцов** в своей встроенной платёжной программе. Сторонние платежи (свой Stripe, лицензии) разрешены ([Figma Forum](https://forum.figma.com/ask-the-community-7/how-do-i-become-an-approved-seller-for-paid-plugins-56625), 2025–2026; [Figma Forum: no approval of new paid plugin creators](https://forum.figma.com/ask-the-community-7/no-approval-of-new-paid-plugin-creators-2741), н.д.).
- **Исправление по генеративным плагинам.** Оригинал писал «анонсированы», но они **уже выпущены**:
  - раскатка началась **24.06.2026**;
  - плагин создаётся описанием инструмента «без локального dev-окружения и знания Plugin API»;
  - позже добавили анимации, интеракции, доступ к коду и **публикацию в Community** или приватно в организацию ([Figma Blog, Behind the Build](https://www.figma.com/blog/how-we-built-generative-plugins-and-shaders/), 2026; [Figma Learn: What's new from Config 2026](https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026), 2026).
- **Вывод.** Простые Figma-утилиты стали функцией платформы.

### 9. AE AI Assistant — подтверждено
Ассистент в **публичной бете** с IBC 2026, в сборке After Effects (Beta) рядом с релизом 26.5. Что он делает:
- пишет expressions по описанию на естественном языке;
- строит риг со слайдерами и показывает таблицу параметров;
- резюмирует и реорганизует чужие проекты («работа, которая иначе занимает до целого дня»);
- генерирует изображения и видео через Firefly и партнёрские модели

([RedShark News](https://www.redsharknews.com/after-effects-ai-assistant-ibc2026), 2026-09; [CG Channel](https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/), 2026-09; [Adobe HelpX](https://helpx.adobe.com/after-effects/desktop/work-with-after-effects-ai-assistant/after-effects-ai-assistant-overview.html), 2026).

### 10. Мосты Figma → After Effects — оригинал занижал темп
**Исправление.** Оригинал: «≥12 новых участников, темп 1,7 в месяц». Пересчёт через GitHub API (26.09.2026) — **не меньше 16 отдельных open-source мостов** с созданием в 09.2025–09.2026:

| Период | Репозитории |
|---|---|
| IV кв. 2025 | [abenezer147/figma-to-ae](https://github.com/abenezer147/figma-to-ae) (06.10.2025) |
| I кв. 2026 | [redNSF/fae](https://github.com/redNSF/fae) (25.03) |
| II кв. 2026 | [UI-FLow](https://github.com/arafatmirazcoder/UI-FLow) (08.04); [figma-ae-bridge](https://github.com/darshd9941/figma-ae-bridge) (01.05, двунаправленная синхронизация); [AEUX-improved](https://github.com/matt3wfultz-a11y/AEUX-improved) (18.05, форк AEUX, рабочая ветка `claude/fix-aeux-imports`: мёртвый бесплатный AEUX реанимируют через Claude Code); [after-effects-mcp с Figma→AE пайплайном](https://github.com/karly-herrera/after-effects-mcp) (28.05); [ElevenCraft figma-to-after-effect](https://github.com/ElevenCraftStudio-Saas/figma-to-after-effect) (20.06); [FigAE](https://github.com/hellosunghyun/figma-to-ae) (21.06); [AE-Figma-Plugin](https://github.com/KyleSullivan321/AE-Figma-Plugin) (30.06) |
| III кв. 2026 (до 26.09) | [svg-splitter](https://github.com/lewisatant/svg-splitter) (03.07, Figma-SVG → shape layers, «pixel-verified»); [OverAE](https://github.com/brunojorri/OverAE) (03.08); [overlord-figma-ae](https://github.com/eliottaep-tech/overlord-figma-ae) (12.08); [Transporter](https://github.com/tlatvys-ac/transporter-app) (02.09, градиенты); [evotechly motion-os](https://github.com/Mohamedbeghanem/evotechly-motion-os) (02.09, «deterministic Figma → motion → AE compiler»); [LazyLord](https://github.com/raisulsohan/LazyLord) (16.09); [Luma](https://github.com/sachinrawat2talentelgiacom-cloud/Luma) (16.09) |

- **Темп:** около 0,2 в месяц до весны 2026, затем **около 2,3 в месяц во II–III кварталах 2026**. Это оценка по публичным репозиториям, уверенность средняя; платные листинги aescripts сюда не входят.
- **Паритет.** От запуска Oblique (март 2026) до бесплатного клона с заявленным паритетом (LazyLord) прошло около 6 месяцев. За один сентябрь 2026 вышли три новых моста.

### 11. Счётчик «after effects» на GitHub (×5,6 за год) — завышен шумом
**Исправление.** Оригинал взял сырые счётчики. Разбор выборки за 08.2026 (первые 100 из 225 репозиториев):
- около **11% — SEO-спам** с «крякнутыми» и «офлайн-установщиками» AE (например, `after-effects-offline-installer`, «中文破解版», «How-To-Get-BCC-Plugin-FREE»);
- один автор дал около 20 репозиториев.

В 08.2025 из 40 репозиториев спам — 3.

**Скорректированный рост — примерно ×4–5 за год** (оценка, уверенность средняя). Вывод оригинала о том, что ниша основателя растёт быстрее базы, **сохраняется**.

**Качественный сдвиг, которого оригинал не заметил.** В 08.2025 почти всё — JSX-скрипты. В 08.2026 появилось **не меньше 10 нативных C++/Rust-плагинов эффектов для AE и Premiere** от частных авторов:
- [DepthGen](https://github.com/palf-gh/DepthGen) — Depth Anything V2 внутри AE;
- [DepthVision](https://github.com/shazeus/DepthVision) — ONNX;
- [dynamicfx](https://github.com/JUNKDOGE-JOE/dynamicfx) — GLSL-шейдеры в expression, 32 bpc;
- [AE-Blob-Tracker](https://github.com/KyleSullivan321/AE-Blob-Tracker) — 76 звёзд;
- [MO-Effector](https://github.com/brunojorri/MO-Effector) — процедурный клонер;
- [adobe-dlss5-plugin](https://github.com/XiangXtreme/adobe-dlss5-plugin);
- [AV1/VP9 importer](https://github.com/neoHaDe/aether-premiere-av1-vp9-importer);
- [AE2Claude](https://github.com/backtime1993/AE2Claude) — AEGP-мост к Claude

(все созданы 03–31.08.2026; [GitHub search «after effects», 08.2026](https://github.com/search?q=%22after+effects%22+created%3A2026-08-01..2026-08-31&type=repositories), 2026-09-26).

**Вывод.** Нативные плагины эффектов на C++ SDK исторически были самым защищённым ярусом aescripts. Теперь этот барьер тоже падает.

### 12. «Клонировать по URL» как переключатель в быстрый сценарий — уже случилось
**Исправление.** Оригинал ждал, что такую функцию выпустят Lovable, Replit или Figma Make. В open source она **уже массовая**:
- [firecrawl/open-lovable](https://github.com/firecrawl/open-lovable): «Clone and recreate any website as a modern React app in seconds», **28,6 тыс. звёзд**, создан 08.08.2025;
- [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template): «Clone any website with one command using AI coding agents», **35,3 тыс. звёзд и 5,2 тыс. форков**, создан 13.03.2026. Пайплайн: скриншоты и токены дизайна → спецификации компонентов → сборка → визуальный QA. Рекомендует Claude Code с Opus 5; поддерживает Codex CLI, OpenCode и Cursor (README, проверено 2026-09-26);
- [claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) — около 1 тыс. звёзд, 28.05.2026;
- [website-downloader](https://github.com/Desertbetweenalembic/website-downloader) — 335 звёзд, 04.08.2026;
- [site-clone](https://github.com/cth9191/site-clone) — «verified near pixel-identical rebuild… Playwright pixel-diff QA», 21.08.2026;
- [lovable-website-cloner](https://github.com/realbrianhanson/lovable-website-cloner) — «Clone any website… into a Lovable project with one Claude Code command», 09.08.2026.

**Уточнение:** всё это клонирует интерфейс и фронтенд, а не бэкенд-логику и данные.

### 13. Остальные пункты
- **Bolt.new — по-прежнему нет данных за 2026 год.** Последнее публичное: $40 млн ARR к марту 2025, больше 7 млн пользователей к декабрю 2025, оценка StackBlitz $700 млн по Forbes (08.2025) ([Sacra](https://sacra.com/c/bolt-new/), 2026; [Panto](https://www.getpanto.ai/blog/bolt-new-statistics), 2026; вторичные). **Прокси:** в рейтинге Similarweb «AI Chatbots and Tools» Bolt.new на 33-м месте, глобальный ранг 12 156 (март 2026, там же). Что свежих цифр ARR нет, само по себе косвенно говорит против сильного роста (оценка, уверенность низкая).
- **Replit:** $300 млн ARR в конце 2025 → **$525 млн в апреле 2026** ([ValueAddVC](https://valueaddvc.com/blog/how-does-replit-make-money-525m-arr-9b-valuation-and-the-ai-agent-business-model-explained), 2026; [Sacra](https://sacra.com/c/replit/), 2026; вторичные, уверенность средняя).
- **Claude Code.** Цифра $2,5 млрд за февраль подтверждена цитатой Anthropic: «run-rate… over $2.5 billion… more than doubled since the beginning of 2026; weekly active Claude Code users also doubled since January 1» ([Simon Willison на X](https://x.com/simonw/status/2022044549733056861), 2026-02-12). Более поздней официальной цифры по Claude Code **нет**. По Anthropic в целом — около $30 млрд run-rate в апреле 2026 (Reuters в пересказе [Panto](https://www.getpanto.ai/blog/claude-ai-statistics), 2026, вторичный).
- **«Токены дешевеют» — нужен нюанс.** Прайс фронтира **не снижался**: Opus 5 вышел 24.07.2026 по $5/$25 за 1 млн токенов, как и Opus 4.8. Fast mode стоит $10/$50, Batch даёт скидку 50%, чтение из кэша — $0,50 ([ClawRouters](https://www.clawrouters.com/blog/claude-opus-5-api-pricing-2026), 2026-07-24; [Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing), 2026). Удешевление идёт через батчи, кэш, открытые модели и эффективность агентов, а не через снижение цены фронтира.

---

## Новые факты

### A. Сколько нового софта выходит — пробел оригинала закрыт
1. **App Store, 2025:** 557 тыс. новых приложений, **+24%** к 2024 году. Это самая крупная волна с 2016 года, когда вышло около 1 млн ([Appfigures](https://appfigures.com/resources/insights/20251205?f=2), 2025-12-05).
2. **Appfigures, 2026, релизы в обоих магазинах:**
   - I квартал: **+60% год к году**, iOS отдельно **+80%**;
   - апрель: **+104%**, iOS **+89%**.
   - В топ-5 категорий вошли «utilities» (2-е место), «productivity» и «lifestyle» ([TechCrunch](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/), 2026-04-18).
3. **Sensor Tower:** в I квартале 2026 года **235,8 тыс. новых сабмитов в App Store (+84% год к году)**. Это самый быстрый рост за 4 года ([TheNextWeb](https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown), 2026-04; [WinBuzzer](https://winbuzzer.com/2026/04/07/vibe-coding-app-store-surge-apple-crackdown-xcxwbn/), 2026-04-07).
4. **Первое полугодие 2026:** App Store добавил почти столько же приложений, сколько за весь 2025 год, около 560 тыс. ([9to5Mac](https://9to5mac.com/2026/07/20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/), 2026-07-20).
   - **Скачивания при этом почти не растут:** +3% в 2025 году и +2% в первом полугодии 2026 ([TweakTown](https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html), 2026).
   - **Вывод:** предложение растёт в 20–40 раз быстрее спроса, и выручка дробится.
5. **Очереди ревью:**
   - в App Store разработчики сообщают о 3+ днях и до недели вместо привычных меньше 24 часов ([9to5Mac](https://9to5mac.com/2026/03/29/vibe-coding-developers-report-long-app-store-review-queues/), 2026-03-29);
   - отдельные сообщения о задержках до 45 дней ([kkm-mako](https://kkm-mako.com/en/blog/articles/app-store-review-delay-vibe-coding-crisis/), 2026, уверенность низкая);
   - Apple строже применяет правила о минимальной функциональности, спаме и копикэтах ([Appbot](https://appbot.co/blog/app-store-app-review-approval-vibe-coded-delays-2026/), 2026).
6. **Product Hunt:** около **750–790 запусков в день**, примерно 49% из них — AI (61% в марте). AI-продукты в среднем набирают на 29% больше апвоутов, но средняя реакция на запуск падает. Для 1-го места в AI нужно 800–1 200 апвоутов против 500–700 в других категориях ([Anysite](https://anysite.io/blog/who-actually-launched-on-product-hunt-in-2026/), 2026; [LaunchBuff](https://launchbuff.com/blog/product-hunt-launch-data-analysis-2026), 2026; вторичные, уверенность средняя, методики агрегаторов расходятся).
7. **Chrome Web Store:**
   - число расширений от **112 тыс. до 251,5 тыс.** в зависимости от методики (251 488 в мае 2026 вместе с темами и приложениями);
   - **90,11% расширений имеют меньше 1 000 пользователей**, и только 0,7% — больше 100 тыс. ([Konabayev, Chrome Extension Statistics 2026](https://konabayev.com/blog/chrome-extension-statistics-2026/), 2026, вторичный).
   - **Вывод:** витрина переполнена, и распределение пользователей экстремально неравное.
8. **Figma Community:** **12 687 плагинов и 988 виджетов** ([Fig Stats](https://fig-stats.com/), ежедневный трекер, доступ 2026-09).
9. **GitHub.** Счётчики по названию — плохой прокси для «вайбкод-волны»:
   - репозитории с «clone» в имени: **18 766 (08.2024) → 13 350 (08.2026)**; учебных клонов «uber-clone» стало меньше, потому что строят агентом, а не по туториалу;
   - репозитории «lovable»: **1 404 (08.2025) → 1 522 (08.2026)**, почти без роста при 1 млн проектов в неделю у Lovable: проекты остаются внутри платформы ([GitHub search](https://github.com/search?q=lovable+created%3A2026-08-01..2026-08-31&type=repositories), 2026-09-26).
   - **Вывод:** GitHub сильно недосчитывает вайбкод-продукты. Для мониторинга клонов нужны витрины, а не только GitHub.

### B. Как рушатся «обёртки» — пробел оригинала закрыт
10. **Jasper** (GPT-обёртка для копирайтинга, оценка $1,5 млрд в октябре 2022): выручка упала примерно **со $120 млн до ~$55 млн**. К середине 2025 года прошло 4 раунда сокращений, основатели ушли из операционного управления ([Shuttergen teardown](https://www.shuttergen.com/research/jasper-ai-teardown), 2026; [GrowthHunt](https://www.growthhunt.ai/growth-story/jasper), 2026; вторичные, уверенность средняя).
11. **Photo AI (Pieter Levels), эталон соло-AI-продукта:**
    - пик — $132–138 тыс. MRR ([Indie Hackers](https://www.indiehackers.com/post/photo-ai-by-pieter-levels-complete-deep-dive-case-study-0-to-132k-mrr-in-18-months-3a9a2b1579), 2025);
    - в августе 2026 — **$105 тыс. выручки и $80 тыс. прибыли в месяц** ([levels.io](https://levels.io/photoai-40870-line-index-php-105k-mo-revenue), 2026-08).
    - Падение от пика — примерно **20–24%** (оценка). Это при сильнейшей личной дистрибуции в нише.
12. **AI-хедшоты.**
    - **Цена-якорь держится:** HeadshotPro — от $29 за 40 фото, Aragon — $29–39 за 40–60 фото с доставкой за 30–45 минут; студийная съёмка — $232–250 ([Headshots.com](https://www.headshots.com/blog/aragonai-vs-headshotpro/), 2026; [Snap2Pass](https://www.snap2pass.com/guides/best-ai-headshot-generator-2026), 2026).
    - **Код обесценился.** На GitHub репозиториев «ai headshot» стало **32 (01–09.2024) → 215 (01–09.2026), ×6,7**. Среди них — готовый open-source SaaS со Stripe, кредитами и авторизацией ([SamurAIGPT/ai-headshot-generator](https://github.com/SamurAIGPT/ai-headshot-generator), 2026-04-15).
    - **Спрос у корпораций ослабевает:** часть агентств формально запретила AI-фото в корпоративных материалах ([Capturely](https://capturely.com/companies-moving-away-from-ai-headshots/), 2026, уверенность низкая).
    - Размер сегмента — $350–500 млн в 2025 году ([BetterPic](https://www.betterpic.io/blog/ai-headshot-generator-market-size-research), 2026; это вендор, уверенность низкая).
    - **Вывод:** сжатие проявляется не в прайсе, а в дроблении выручки между сотнями клонов.
13. **Позиция инвесторов.** Вице-президент Google назвал LLM-обёртки и агрегаторы категорией с горящим «check engine light» ([Medium, The Wrapper Economy Is Collapsing](https://jess-writes-about-tech.medium.com/the-wrapper-economy-is-collapsing-bfd271846528), 2026, со ссылкой на TechCrunch 02.2026; вторичный).

### C. Клоны и копикэты на витринах — пробел оригинала закрыт
14. **Chrome:**
    - **30 копикэт-расширений**, выдававших себя за AI-ассистентов (в том числе под Gemini и ChatGPT), набрали **больше 260 тыс. установок** и собирали данные пользователей. Расширения почти идентичны и отличаются только брендингом ([Dark Reading](https://www.darkreading.com/cyber-risk/chrome-fake-ai-browser-extensions), 2026);
    - расширение QuickLens выставили на продажу в октябре 2025. После смены владельца 17.02.2026 вышло вредоносное обновление, снимающее CSP-заголовки ([The Hacker News](https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html?m=1), 2026-03);
    - разработчики жалуются, что их код копируют и перезаливают, а Google не реагирует ([chromium-extensions group](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/JF-ACvsI0hA), н.д.).
15. **Мобильные приложения:**
    - RevenueCat: «функциональный клон проверенной идеи генерируется за дни, со скрейпленным маркетинговым текстом и почти идентичным UI» ([RevenueCat](https://www.revenuecat.com/blog/growth/protect-app-from-copycats), 2026);
    - после запуска официального приложения Sora (конец 2025) App Store заполнили больше десятка фейков «Sora/Sora 2» с сотнями тысяч скачиваний, пока Apple не вмешалась ([TweakTown](https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html), 2026).
16. **Open-source клоны продуктов лабораторий.** После запуска Claude Cowork (январь 2026) быстро появились open-source альтернативы:
    - OpenWork — **больше 18 тыс. звёзд к июлю 2026**, затем больше 20 тыс. ([CoddyKit](https://www.coddykit.com/pages/blog-detail?id=512976&slug=openwork-the-open-source-claude-cowork-alternative-with-18-000-github-stars-that), 2026-07);
    - [composio open-claude-cowork](https://github.com/composio-community/open-claude-cowork) с 500+ интеграциями.
    - **Вывод:** даже продукт владельца модели получает бесплатный клон за недели.

### D. Цены инструментов и их динамика
17. **Cursor (сентябрь 2026):** Hobby — бесплатно, Pro — $20, **Pro+ — $60, Ultra — $200**, Teams — $40 за пользователя, Enterprise — по договорённости. В 2026 году модель тарификации менялась **трижды**. В июне 2026 обновили Teams, по оценке Cursor это снизило затраты для 90% команд ([LowCode Agency](https://www.lowcode.agency/blog/cursor-ai-pricing), 2026-09; [Finout](https://www.finout.io/blog/what-happened-to-cursor-pricing-2026-guide-5-cost-cutting-tips), 2026).
18. **Lovable:** Free — 5 кредитов в день, максимум 30 в месяц; Pro — **$25 в месяц за 100 кредитов**; Business — $50; при оплате за год около $21 и $42 ([No Code MBA](https://www.nocode.mba/articles/lovable-pricing), 2026; [Lovable Club](https://www.lovable.club/lovable-pricing), 2026).
19. **Вывод по ценам (оценка, уверенность средняя).** У инструментов разработки цена **поляризуется вверх**: появились тарифы $60–200 в месяц для профи (Cursor Pro+/Ultra, Claude Max $100–200). У потребительских AI-утилит прайс стоит на месте, а выручка на продукт падает (пп. 11–12). Для портфеля основателя важнее второй эффект.

### E. Жёсткие отключения API — примеры для раздела о рисках
20. **OpenAI Assistants API** выключен **26.08.2026** без переходного периода: все вызовы возвращают ошибку, нет ни режима только для чтения, ни продления. Уведомление было за год, 26.08.2025 ([OpenAI Developer Community](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666), 2025-08; [OpenAI Deprecations](https://developers.openai.com/api/docs/deprecations), 2026).
21. **Figma Plugin API меняется постоянно:**
    - 14.08.2026 — новое свойство `textWrapStyle`;
    - 27.08.2026 — в typings вернули `getCSSAsync`;
    - 03.09.2026 — поддержка variable fonts ([Figma Developer Docs, Updates](https://developers.figma.com/docs/plugins/updates/), 2026; [Version 1, Update 136](https://developers.figma.com/docs/plugins/updates/2026/08/27/version-1-update-136/), 2026-08-27).
    - Прямых массовых поломок плагинов в 2026 году **не найдено**. Ломающие изменения идут через сторонний тулкит create-figma-plugin ([CHANGELOG](https://github.com/yuanqing/create-figma-plugin/blob/main/CHANGELOG.md), 2026).

---

## Заполненные пробелы (по пунктам брифа)

| Пункт брифа | Было в оригинале | Стало |
|---|---|---|
| Число новых приложений (Appfigures 2025–2026) | нет данных | 557 тыс. новых iOS-приложений в 2025 году (+24%). Q1 2026: +60% в обоих магазинах, iOS +80%. Апрель: +104%. Sensor Tower Q1: 235,8 тыс. сабмитов (+84%). Первое полугодие 2026 ≈ весь 2025 год. Скачивания +2% (п. A1–A4) |
| Объём запусков Product Hunt | нет данных | ~750–790 в день, ~49% AI (вторичные, п. A6) |
| Chrome Web Store / Figma plugins | нет данных | CWS: 112–251 тыс., 90% меньше 1 000 пользователей. Figma: 12 687 плагинов и 988 виджетов (п. A7–A8) |
| Выручка и внедрение AI-кодинга | Bolt нет данных; Replit только цель | Cursor ≈$2,6 млрд на момент сделки SpaceX. Replit $525 млн (04.2026). Bolt — нет данных за 2026 год, последнее $40 млн (03.2025) |
| METR после 02.2026 | нет данных | Opus 4.6 — 14,5 ч; Mythos Preview — ≥16 ч; GPT-5.6 Sol — 11,3 ч (с оговорками); Opus 5.5 — инкрементально. Шкала насытилась выше 16 ч (раздел «Проверено», п. 4) |
| Тренд SWE-bench | качественно | Verified 95–97% у топа, насыщен. Pro 51,5–80% в зависимости от набора |
| Кейсы «клонировал за выходные» | vinext, chardet | Плюс: клонирование сайта по URL одной командой — open-lovable (28,6 тыс. звёзд), ai-website-cloner-template (35,3 тыс.). Open-source клоны Cowork за недели. Клоны мобильных приложений «за дни» (RevenueCat) |
| Сжатие цен | SaaSpocalypse, Adobe | Прайс AI-утилит держится (хедшоты $29–39), выручка дробится: Photo AI −20–24% от пика, Jasper −55% |
| Число мостов Figma→AE | ≥12, 1,7 в месяц | ≥16 open-source мостов за 12 месяцев, ~2,3 в месяц во II–III кв. 2026 |
| Отсев AI-хедшотов | отсутствовал | Код стал commodity (×6,7 репозиториев, готовый open-source SaaS). Цена-якорь $29–39. Лидер соло-рынка Photo AI −20% от пика |
| Отсев ChatGPT-обёрток | 70% питчей — обёртки | Jasper $120 млн → ~$55 млн. Google VP: «check engine light» |
| Клоны Chrome-расширений | только шпионские расширения | 30 копикэт-«AI»-расширений на 260 тыс. установок. Покупка расширений ради вредоносных обновлений (QuickLens). Жалобы разработчиков на перезаливы |
| Риски поддержки: CEP→UXP, Figma API, App Store, модели | в основном есть | Добавлены: Photoshop закрывает приём CEP в 03.2027; гарантия 2 года после беты; Assistants API выключен 26.08.2026; MV2 удалён из CWS 31.08.2026; очереди App Store 3+ дня |

---

## Обновлённые сценарии и сигналы

Новые данные **меняют веса**:
- клонирование по URL уже доступно open-source (35 тыс. звёзд);
- генеративные плагины Figma выпущены;
- AE AI Assistant в публичной бете;
- частные авторы делают нативные C++-плагины для AE;
- сабмиты в App Store +84%.

С другой стороны, дробление спроса (скачивания +2%) и очереди ревью создают **трение**, которое немного защищает тех, кто уже на витрине.

### 1. Стоимость и время клонирования (обновление)

| Сценарий | Было | Стало | Что изменилось |
|---|---|---|---|
| **Базовый** | 55% | **50%** | Контрольные точки на 12 месяцев частично достигнуты уже сейчас. Интерфейс по URL клонируется за минуты или часы (open-lovable, ai-website-cloner). Однофункциональный плагин, включая нативный C++-эффект AE, — 1–3 дня (≥10 нативных плагинов от частных авторов за 08.2026). Небольшой SaaS с бэкендом — 3–7 дней плюс доводка |
| **Быстрый** | 30% | **38%** | Платформы уже делают утилиты по описанию: Figma с 24.06.2026, AE Assistant с 09.2026. Mythos Preview ≥16 ч в марте 2026. К 09.2027 — клонирование бэкенд-логики по наблюдаемому поведению приложения. Главным барьером становятся модерация витрин и доверие |
| **Медленный** | 15% | **12%** | Прецедент экспортного контроля (Fable/Mythos) остаётся. Но лимиты Claude Code в итоге выше довесеннего уровня (+25%), а цена фронтира стабильна ($5/$25) |

**Новые и заменённые сигналы:**
1. **Вместо «80% horizon METR больше 8 часов».** METR объявил, что текущий набор задач насыщен. Следить за выходом **нового набора задач METR** (metr.org/time-horizons, раз в квартал). Если на новом наборе 50% horizon первой модели **больше 40 часов** (одна рабочая неделя) до середины 2027 — быстрый сценарий.
2. **Разрыв между релизами и скачиваниями** (Appfigures или Sensor Tower, раз в квартал; пресс-релизы в TechCrunch и 9to5Mac). Релизы +50% и больше год к году при скачиваниях ≤+3% означают, что дробление выручки продолжается. Это сигнал базового или быстрого сценария для цен.
3. **Клонирование логики, а не только UI.** Следить, появится ли в топ-репозиториях клонирования (open-lovable, ai-website-cloner-template) функция клонирования бэкенда или API по трафику. Смотреть их README и releases раз в месяц. Появление такой функции — быстрый сценарий.
4. **Нативные плагины AE на GitHub** (раз в месяц). Запрос: `"after effects" language:C++ OR language:Rust created:<месяц>` с исключением спама (`NOT crack NOT installer NOT download`). Устойчивый рост больше 10 в месяц означает, что последний технический барьер aescripts пал.

### 2. Скорость прихода конкурентов (уточнение базового сценария)
- **Сейчас (факт).** В нише Figma→AE около 2,3 новых open-source мостов в месяц. От запуска Oblique до бесплатного клона с заявленным паритетом — около 6 месяцев.
- **Базовый прогноз на 12 месяцев:**
  - первый бесплатный клон в трендовой нише — через **1–3 недели** (было 1–4);
  - заявленный паритет — через **1–3 месяца**;
  - к 09.2027 в нише Figma→AE — **больше 30 open-source мостов** (оценка по текущему темпу, уверенность средняя).
- **Новый сигнал.** Выход UXP-беты AE (ноябрь 2026) и число мостов на UXP. Бесплатные шаблоны Bolt UXP и aescripts UXP Framework уже есть. Если к марту 2027 на UXP больше 3 open-source мостов, преимущество «первым на UXP» длится меньше квартала.

### 3. Уровень цен (уточнение)
- **Главная коррекция.** Сжатие выражается не в снижении прайса, а **в дроблении выручки на продукт**:
  - AI-хедшоты держат $29–39 с 2023 года, а лидер соло-рынка потерял примерно 20% выручки;
  - Jasper потерял около 55%.
- Следить надо не только за медианной ценой листингов (сигнал оригинала), но и за **выручкой на продукт в неделю в сравнении с числом клонов**. Для Oblique это данные aescripts самого основателя.
- **Инструменты для профи дорожают:** Cursor Pro+ $60 и Ultra $200, Claude Max $100–200. Деньги профессионалов концентрируются в инструментах, которые экономят часы, а не в мелких утилитах.

---

## Идеи-кандидаты: новые и уточнённые

Бриф потока просит стратегические принципы вместо идей продуктов. Ниже — **уточнения принципов** оригинала по новым данным и три кандидата, для которых нашлись доказательства спроса.

### Уточнённые принципы (дополняют принципы 1–10 оригинала)

**П1′. «Видно по URL — клонируется одной командой».**
- Это уже не метафора: open-lovable (28,6 тыс. звёзд) и ai-website-cloner-template (35,3 тыс.) делают это буквально.
- UI, лендинг и фронтенд защиты не дают.
- **Тест идеи:** что останется у клона, если он скопирует весь интерфейс за час? Если ответ «всё», не строить.

**П2′. Нативный код тоже не защита.**
- В 08.2025 почти все AE-репозитории на GitHub были JSX-скриптами.
- В 08.2026 частные авторы выпустили больше 10 нативных C++/Rust-эффектов: depth, шейдеры, трекинг, AV1-импорт.
- Сложность SDK больше не барьер. Барьер — данные, пресеты, вкус и приёмка.

**П3′. Мерить выручку на клон, а не цену.**
- Сжатие видно по дроблению выручки: Photo AI около −20%, Jasper около −55% при стабильном прайсе хедшотов.
- Метрика для дашборда основателя: выручка продукта в неделю, наложенная на число клонов в категории.
- Если выручка падает больше чем на 30% за квартал, а число клонов растёт, переводить продукт в режим поддержки (порог 50% за 60 дней из оригинала оставить как аварийный).

**П4′. Трение витрин — ров действующего игрока.**
- Примеры трения:
  - очередь App Store 3+ дня;
  - закрытая встроенная программа платных продавцов Figma;
  - удаление MV2 из CWS;
  - закрытие CEP-сабмитов (Photoshop — 03.2027, AE — 12.2028).
- Одобренный, обновлённый и отрецензированный листинг — актив. **Практически:** заранее публиковать UXP-версию и lite-версию, пока очереди короткие.
- **Оговорка:** шаблоны миграции бесплатны, поэтому окно — месяцы, а не годы.

**П5′. Не конкурировать с выпущенными генеративными функциями платформ.**
- Уже выпущены генеративные плагины Figma (24.06.2026) и AE AI Assistant (публичная бета, 09.2026).
- Под угрозой всё, что описывается одной фразой: «сделай риг со слайдерами», «переставь слои», «найди и замени цвета».
- Строить на **швах между платформами** (Figma ↔ AE ↔ приёмка DOOH) и там, где нужны непубличные данные.

**П6′. Жёсткие отключения — норма, а не исключение.**
- Assistants API выключен 26.08.2026 без переходного периода.
- Fable и Mythos выключены за одну ночь 12.06.2026.
- MV2 удалён из CWS 31.08.2026.
- **Правило для портфеля:**
  - слой абстракции над моделями, минимум два провайдера;
  - BYOK;
  - календарь дедлайнов платформ в дашборде;
  - на каждый продукт — ежемесячный smoke-тест в CI против беты хоста (AE Beta, Figma).

**П7′. Мониторинг клонов с фильтром шума.**
- Около 11% AE-репозиториев на GitHub за 08.2026 — спам с крякнутым AE.
- Один автор может дать 20 репозиториев в месяц.
- GitHub недосчитывает вайбкод-продукты: репозитории «lovable» не растут при 1 млн проектов в неделю.
- **Мониторинг строить на трёх источниках:**
  - GitHub с исключениями спама;
  - витрины: новые листинги aescripts, поиск Figma Community, CWS;
  - упоминания бренда.

### Кандидат 1 (уточнённый). Oblique: UXP-first плюс бесплатный lite-уровень
- **Суть.** Первым выпустить UXP-версию к бете AE (ноябрь 2026). Базовый перенос сделать бесплатным. Деньги брать за glass/blur-рендер, гарантию совместимости и поддержку студий.
- **Тип:** A. **Формат:** плагин AE и Figma плюс лицензия.
- **Покупатель и боль:** моушн-дизайнеры и студии, которые переносят UI из Figma в AE. Боль — сломанные auto-layout, эффекты и стекло.
- **Доказательства спроса:**
  - поток клонов — ≥16 open-source мостов за год — сам по себе доказывает спрос (раздел «Проверено», п. 10);
  - сравнительные обзоры AEUX, Overlord, Convertify и Prism ([Next Horizon](https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma), 2026);
  - AEUX устарел и не поддерживается, «complex auto layout… often come through broken» (там же).
- **Конкуренты и цены:**
  - LazyLord, FAE, figma-ae-bridge, OverAE — бесплатные, MIT или open source;
  - UXLink — $99,99; Prism — от $39; AEShiper — ≈$6,5 (по потоку adobe_platforms в оригинале);
  - Overlord (Battle Axe) — цену в этой сессии проверить не удалось, нет данных.
- **Гипотеза рва:** качество рендера стекла и blur, которое пока никто не заявил; UXP раньше клонов; доверие и поддержка; база покупателей как канал.
- **Главный риск.** Бесплатные шаблоны Bolt UXP и aescripts UXP Framework позволят клонам перейти на UXP за недели. Выручку съест дробление, а не прямая ценовая война.

### Кандидат 2 (новый). «Clone Radar» — мониторинг клонов для продавцов креативных плагинов
- **Суть.** Еженедельный отчёт: новые конкуренты и клоны на GitHub, aescripts, Figma Community и CWS по ключевым словам продукта, с фильтром спама, плюс динамика цен.
- **Тип:** AB. **Формат:** сначала внутренний инструмент, затем micro-SaaS или email-отчёт.
- **Покупатель и боль:** авторы плагинов для AE, Figma и Chrome. Клоны появляются за недели, продавцы узнают о них по падению продаж.
- **Доказательства спроса:**
  - разработчики Chrome-расширений жалуются на перезаливы кода без реакции Google ([chromium-extensions](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/JF-ACvsI0hA), н.д.);
  - RevenueCat посвящает отдельный гайд защите от вайбкод-клонов ([RevenueCat](https://www.revenuecat.com/blog/growth/protect-app-from-copycats), 2026);
  - темп клонов в Figma→AE — около 2,3 в месяц.
  - Платящий спрос **не подтверждён**.
- **Конкуренты и цены:** универсальные сервисы мониторинга бренда и отзывов (цены в этой сессии не проверены — нет данных); бесплатный поиск GitHub и Google Alerts.
- **Гипотеза рва:** знание витрин креативных инструментов, фильтры спама под нишу, накопленная история листингов — данные, которые копятся со временем.
- **Главный риск.** Маленький рынок и низкая готовность платить. Агент с cron воспроизводит это бесплатно. Рационально строить как внутренний инструмент портфеля (принцип 6 оригинала), а наружу продавать, только если найдутся 10+ платящих.

### Кандидат 3 (новый, низкое соответствие профилю). Проверка безопасности вайбкод-приложений
- **Суть.** Автоматический скан RLS в Supabase, открытых ключей и публичных эндпоинтов для приложений на Lovable, Bolt и Replit, с отчётом «что починить» для некодеров.
- **Тип:** B. **Формат:** веб-сервис плюс отчёт.
- **Покупатель и боль:** авторы вайбкод-приложений. Утечки данных, как у приложения с витрины Lovable на 18 тыс. пользователей.
- **Доказательства спроса:**
  - The Register, 2026-02-27; Wired, 2026-05-07; TechCrunch о Supabase, 2026-09-25 (оригинал, факт 27);
  - сабмиты в App Store +84% при ужесточении ревью.
- **Конкуренты и цены:**
  - существует как минимум [Vibe App Scanner](https://vibeappscanner.com/bolt-statistics) (цена — нет данных);
  - AI-ревью PR в Claude Code Review — $15–25 (оригинал, факт 7).
- **Гипотеза рва:** база типовых уязвимостей конкретных платформ, обновляемая еженедельно.
- **Главный риск.** Платформы встроят сканеры бесплатно. Юридическая ответственность за пропущенную уязвимость. Экспертиза основателя тут ни при чём. **Рекомендация: не строить**; держать как пример ниши, которую поглотят платформы.

---

## Источники

1. Anthropic — Statement on the directive to suspend Fable 5 access — https://www.anthropic.com/news/fable-mythos-access — 2026-06-12
2. Fortune — Anthropic disables Fable and Mythos — https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/ — 2026-06-13
3. NatLawReview — Anthropic suspends access to Fable 5, Mythos 5 — https://natlawreview.com/article/ai-company-anthropic-suspends-access-claude-fable-5-claude-mythos-5-following-us — 2026-06
4. Axios — Commerce greenlights partial return of Mythos — https://www.axios.com/2026/06/27/commerce-anthropic-mythos-restrictions-lift — 2026-06-27
5. CNBC — SpaceX to acquire Cursor for $60B — https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html — 2026-06-16
6. Wikipedia — Cursor (company) — https://en.wikipedia.org/wiki/Cursor_(company) — доступ 2026-09
7. Implicator — Claude Code weekly limits −17% Sept 14 — https://www.implicator.ai/anthropic-claude-code-weekly-limits-september-14/ — 2026-09
8. MindStudio — Claude Code's September rate limit change — https://www.mindstudio.ai/blog/claude-code-weekly-rate-limit-changes — 2026-09
9. BleepingComputer — Claude Code weekly limits −17% — https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/ — 2026-08-29
10. METR на X — Opus 4.5 50% horizon 4h49m — https://x.com/METR_Evals/status/2002203627377574113 — 2025-12
11. METR на X — Opus 4.6 50% horizon ~14.5h — https://x.com/METR_Evals/status/2024923422867030027 — 2026-02
12. METR на X — Claude Mythos Preview ≥16h — https://x.com/METR_Evals/status/2052896621760004602 — 2026-05-08
13. METR — Summary of predeployment evaluation of GPT-5.6 Sol — https://metr.org/blog/2026-06-26-gpt-5-6-sol/ — 2026-06-26
14. METR — Summary of predeployment evaluation of Claude Opus 5.5 — https://metr.org/blog/2026-09-22-claude-opus-5-5/ — 2026-09-22
15. METR — Time Horizon 1.1 — https://metr.org/blog/2026-1-29-time-horizon-1-1/ — 2026-01-29
16. METR — Task-Completion Time Horizons of Frontier AI Models — https://metr.org/time-horizons/ — 2026
17. LessWrong — METR Time Horizons: Now 10x/Year — https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year — 2026
18. GitHub — METR/eval-analysis-public commits — https://github.com/METR/eval-analysis-public/commits/main — проверено 2026-09-26
19. BenchLM — SWE-bench Verified leaderboard — https://benchlm.ai/benchmarks/swe-bench-verified — 2026-09
20. Morph — SWE-bench Pro leaderboard — https://www.morphllm.com/swe-bench-pro — 2026-09
21. Adobe Developer Blog — UXP comes to flagship applications — https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications — 2026-09
22. Filmit — The Future of Adobe Plugins: UXP, CEP, and AI — https://filmit.io/blog/future-of-adobe-plugins-uxp-cep-ai — 2026
23. GitHub — AdobeDocs/uxp-after-effects — https://github.com/AdobeDocs/uxp-after-effects — создан 2026-09-23
24. Hyper Brew — Bolt UXP — https://hyperbrew.co/resources/bolt-uxp/ — 2026
25. Hyper Brew — aescripts UXP Framework — https://hyperbrew.co/projects/aescripts-uxp-framework/ — 2026
26. Chrome Unboxed — Manifest V2 officially dead, CWS purges — https://chromeunboxed.com/manifest-v2-is-officially-dead-as-the-chrome-web-store-permanently-purges-legacy-extensions/ — 2026-09
27. Chrome for Developers — MV2 support timeline — https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline — 2025–2026
28. Figma Forum — How do I become an approved seller for paid plugins — https://forum.figma.com/ask-the-community-7/how-do-i-become-an-approved-seller-for-paid-plugins-56625 — 2025–2026
29. Figma Forum — No approval of new paid plugin creators — https://forum.figma.com/ask-the-community-7/no-approval-of-new-paid-plugin-creators-2741 — н.д.
30. Figma Blog — Behind the Build: Generative Plugins and Shaders — https://www.figma.com/blog/how-we-built-generative-plugins-and-shaders/ — 2026
31. Figma Learn — What's new from Config 2026 — https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026 — 2026
32. RedShark News — After Effects AI Assistant enters public beta — https://www.redsharknews.com/after-effects-ai-assistant-ibc2026 — 2026-09
33. CG Channel — After Effects 26.5 and AI Assistant beta — https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/ — 2026-09
34. Adobe HelpX — After Effects AI Assistant overview — https://helpx.adobe.com/after-effects/desktop/work-with-after-effects-ai-assistant/after-effects-ai-assistant-overview.html — 2026
35. GitHub — raisulsohan/LazyLord — https://github.com/raisulsohan/LazyLord — 2026-09-16
36. GitHub — redNSF/fae — https://github.com/redNSF/fae — 2026-03-25
37. GitHub — abenezer147/figma-to-ae — https://github.com/abenezer147/figma-to-ae — 2025-10-06
38. GitHub — arafatmirazcoder/UI-FLow — https://github.com/arafatmirazcoder/UI-FLow — 2026-04-08
39. GitHub — darshd9941/figma-ae-bridge — https://github.com/darshd9941/figma-ae-bridge — 2026-05-01
40. GitHub — matt3wfultz-a11y/AEUX-improved — https://github.com/matt3wfultz-a11y/AEUX-improved — 2026-05-18
41. GitHub — karly-herrera/after-effects-mcp — https://github.com/karly-herrera/after-effects-mcp — 2026-05-28
42. GitHub — ElevenCraftStudio-Saas/figma-to-after-effect — https://github.com/ElevenCraftStudio-Saas/figma-to-after-effect — 2026-06-20
43. GitHub — hellosunghyun/figma-to-ae (FigAE) — https://github.com/hellosunghyun/figma-to-ae — 2026-06-21
44. GitHub — KyleSullivan321/AE-Figma-Plugin — https://github.com/KyleSullivan321/AE-Figma-Plugin — 2026-06-30
45. GitHub — lewisatant/svg-splitter — https://github.com/lewisatant/svg-splitter — 2026-07-03
46. GitHub — brunojorri/OverAE — https://github.com/brunojorri/OverAE — 2026-08-03
47. GitHub — eliottaep-tech/overlord-figma-ae — https://github.com/eliottaep-tech/overlord-figma-ae — 2026-08-12
48. GitHub — tlatvys-ac/transporter-app — https://github.com/tlatvys-ac/transporter-app — 2026-09-02
49. GitHub — Mohamedbeghanem/evotechly-motion-os — https://github.com/Mohamedbeghanem/evotechly-motion-os — 2026-09-02
50. GitHub — Luma (Figma→AE) — https://github.com/sachinrawat2talentelgiacom-cloud/Luma — 2026-09-16
51. GitHub search — "after effects", created 08.2026 (225) — https://github.com/search?q=%22after+effects%22+created%3A2026-08-01..2026-08-31&type=repositories — 2026-09-26
52. GitHub search — "after effects", created 08.2025 (40) — https://github.com/search?q=%22after+effects%22+created%3A2025-08-01..2025-08-31&type=repositories — 2026-09-26
53. GitHub — palf-gh/DepthGen — https://github.com/palf-gh/DepthGen — 2026-08-15
54. GitHub — shazeus/DepthVision — https://github.com/shazeus/DepthVision — 2026-08-18
55. GitHub — JUNKDOGE-JOE/dynamicfx — https://github.com/JUNKDOGE-JOE/dynamicfx — 2026-08-14
56. GitHub — KyleSullivan321/AE-Blob-Tracker — https://github.com/KyleSullivan321/AE-Blob-Tracker — 2026-08-04
57. GitHub — brunojorri/MO-Effector — https://github.com/brunojorri/MO-Effector — 2026-08-05
58. GitHub — XiangXtreme/adobe-dlss5-plugin — https://github.com/XiangXtreme/adobe-dlss5-plugin — 2026-08-31
59. GitHub — neoHaDe/aether-premiere-av1-vp9-importer — https://github.com/neoHaDe/aether-premiere-av1-vp9-importer — 2026-08-19
60. GitHub — backtime1993/AE2Claude — https://github.com/backtime1993/AE2Claude — 2026-08-27
61. GitHub — firecrawl/open-lovable — https://github.com/firecrawl/open-lovable — 2025-08-08
62. GitHub — JCodesMore/ai-website-cloner-template — https://github.com/JCodesMore/ai-website-cloner-template — 2026-03-13 (README проверен 2026-09-26)
63. GitHub — Jane-xiaoer/claude-skill-web-clone — https://github.com/Jane-xiaoer/claude-skill-web-clone — 2026-05-28
64. GitHub — Desertbetweenalembic/website-downloader — https://github.com/Desertbetweenalembic/website-downloader — 2026-08-04
65. GitHub — cth9191/site-clone — https://github.com/cth9191/site-clone — 2026-08-21
66. GitHub — realbrianhanson/lovable-website-cloner — https://github.com/realbrianhanson/lovable-website-cloner — 2026-08-09
67. Sacra — Bolt.new revenue, funding & growth — https://sacra.com/c/bolt-new/ — 2026
68. Panto — Bolt.new Statistics 2026 — https://www.getpanto.ai/blog/bolt-new-statistics — 2026
69. ValueAddVC — How Replit makes money ($525M ARR) — https://valueaddvc.com/blog/how-does-replit-make-money-525m-arr-9b-valuation-and-the-ai-agent-business-model-explained — 2026
70. Sacra — Replit revenue — https://sacra.com/c/replit/ — 2026
71. Simon Willison на X — Claude Code run-rate >$2.5B — https://x.com/simonw/status/2022044549733056861 — 2026-02-12
72. Panto — Claude AI Statistics 2026 (Reuters $30B, 04.2026) — https://www.getpanto.ai/blog/claude-ai-statistics — 2026
73. ClawRouters — Claude Opus 5 API pricing $5/$25 — https://www.clawrouters.com/blog/claude-opus-5-api-pricing-2026 — 2026-07-24
74. Claude Platform Docs — Pricing — https://platform.claude.com/docs/en/about-claude/pricing — 2026
75. Appfigures — The App Store Just Logged Its Biggest Release Year in Nearly a Decade — https://appfigures.com/resources/insights/20251205?f=2 — 2025-12-05
76. TechCrunch — The App Store is booming again, and AI may be why — https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/ — 2026-04-18
77. TheNextWeb — Vibe coding drove an 84% jump in App Store submissions — https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown — 2026-04
78. WinBuzzer — Vibe coding drives 84% App Store submissions surge — https://winbuzzer.com/2026/04/07/vibe-coding-app-store-surge-apple-crackdown-xcxwbn/ — 2026-04-07
79. 9to5Mac — App Store added nearly as many new apps in H1 2026 as in all of 2025 — https://9to5mac.com/2026/07/20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/ — 2026-07-20
80. TweakTown — Vibe coding is flooding the App Store — https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html — 2026
81. 9to5Mac — Vibe coding could mark the end of App Store review as we know it — https://9to5mac.com/2026/03/29/vibe-coding-developers-report-long-app-store-review-queues/ — 2026-03-29
82. kkm-mako — App Store reviews hit 45 days — https://kkm-mako.com/en/blog/articles/app-store-review-delay-vibe-coding-crisis/ — 2026
83. Appbot — App Store Review Delays in 2026 — https://appbot.co/blog/app-store-app-review-approval-vibe-coded-delays-2026/ — 2026
84. Anysite — Who Launched on Product Hunt in 2026 — https://anysite.io/blog/who-actually-launched-on-product-hunt-in-2026/ — 2026
85. LaunchBuff — Product Hunt launch data analysis 2026 — https://launchbuff.com/blog/product-hunt-launch-data-analysis-2026 — 2026
86. Konabayev — Chrome Extension Statistics 2026 — https://konabayev.com/blog/chrome-extension-statistics-2026/ — 2026
87. Fig Stats — Figma plugin and widget analytics — https://fig-stats.com/ — доступ 2026-09
88. GitHub search — lovable, created 08.2026 — https://github.com/search?q=lovable+created%3A2026-08-01..2026-08-31&type=repositories — 2026-09-26
89. Shuttergen — Jasper AI teardown — https://www.shuttergen.com/research/jasper-ai-teardown — 2026
90. GrowthHunt — How Jasper lost to ChatGPT — https://www.growthhunt.ai/growth-story/jasper — 2026
91. Indie Hackers — Photo AI deep dive ($132K MRR) — https://www.indiehackers.com/post/photo-ai-by-pieter-levels-complete-deep-dive-case-study-0-to-132k-mrr-in-18-months-3a9a2b1579 — 2025
92. levels.io — Photoai.com: $105K/mo revenue, $80K/mo profit — https://levels.io/photoai-40870-line-index-php-105k-mo-revenue — 2026-08
93. Headshots.com — Aragon AI vs HeadshotPro vs Headshots.com — https://www.headshots.com/blog/aragonai-vs-headshotpro/ — 2026
94. Snap2Pass — Best AI Headshot Generator 2026 — https://www.snap2pass.com/guides/best-ai-headshot-generator-2026 — 2026
95. GitHub — SamurAIGPT/ai-headshot-generator — https://github.com/SamurAIGPT/ai-headshot-generator — 2026-04-15
96. Capturely — Why companies are moving away from AI headshots — https://capturely.com/companies-moving-away-from-ai-headshots/ — 2026
97. BetterPic — AI Headshot Generator Market Size — https://www.betterpic.io/blog/ai-headshot-generator-market-size-research — 2026
98. Medium (Jessica Lin) — The Wrapper Economy Is Collapsing — https://jess-writes-about-tech.medium.com/the-wrapper-economy-is-collapsing-bfd271846528 — 2026
99. Dark Reading — 260K+ Chrome users duped by fake AI browser extensions — https://www.darkreading.com/cyber-risk/chrome-fake-ai-browser-extensions — 2026
100. The Hacker News — Chrome extension turns malicious after ownership transfer (QuickLens) — https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html?m=1 — 2026-03
101. Chromium Extensions group — Chrome extension was cloned — https://groups.google.com/a/chromium.org/g/chromium-extensions/c/JF-ACvsI0hA — н.д.
102. RevenueCat — How to protect your subscription app from copycats and clones — https://www.revenuecat.com/blog/growth/protect-app-from-copycats — 2026
103. CoddyKit — OpenWork: open-source Claude Cowork alternative (18K stars) — https://www.coddykit.com/pages/blog-detail?id=512976&slug=openwork-the-open-source-claude-cowork-alternative-with-18-000-github-stars-that — 2026-07
104. GitHub — composio-community/open-claude-cowork — https://github.com/composio-community/open-claude-cowork — 2026
105. LowCode Agency — Cursor AI pricing (Sept 2026) — https://www.lowcode.agency/blog/cursor-ai-pricing — 2026-09
106. Finout — What happened to Cursor pricing 2026 — https://www.finout.io/blog/what-happened-to-cursor-pricing-2026-guide-5-cost-cutting-tips — 2026
107. No Code MBA — Lovable pricing 2026 — https://www.nocode.mba/articles/lovable-pricing — 2026
108. Lovable Club — Lovable pricing — https://www.lovable.club/lovable-pricing — 2026
109. OpenAI Developer Community — Assistants API beta deprecation, August 26, 2026 sunset — https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666 — 2025-08 … 2026-08
110. OpenAI — Deprecations — https://developers.openai.com/api/docs/deprecations — 2026
111. Figma Developer Docs — Plugin API updates — https://developers.figma.com/docs/plugins/updates/ — 2026
112. Figma Developer Docs — Version 1, Update 136 — https://developers.figma.com/docs/plugins/updates/2026/08/27/version-1-update-136/ — 2026-08-27
113. GitHub — create-figma-plugin CHANGELOG — https://github.com/yuanqing/create-figma-plugin/blob/main/CHANGELOG.md — 2026
114. Next Horizon — AEUX vs Overlord vs Convertify vs Prism — https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma — 2026
115. Vibe App Scanner — Bolt statistics (конкурент для кандидата 3) — https://vibeappscanner.com/bolt-statistics — 2026
