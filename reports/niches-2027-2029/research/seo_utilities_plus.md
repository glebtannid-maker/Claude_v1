# Поток 7: дополнение. SEO и утилитарные сайты под AI-поиском, модель «калькуляторных сайтов»

*Срез: 2026-09-26. Дополняет файл `seo_utilities.md`; то, что там не изменилось, здесь не повторяется.*

> **Методология этого прохода.**
> - В этом проходе сделано ~88 запросов WebSearch. Цифры взяты из сниппетов и сводок страниц; ссылка всегда ведёт на страницу-первоисточник.
> - WebFetch недоступен (прокси), поэтому страницы Similarweb и Semrush не открывались. Их цифры — модельные оценки вендоров, не счётчики.
> - Сделан **повторный прогон кэша CrUX** (Chrome UX Report top-lists, файлы из прошлого прохода) по 110 доменам: новые конкуренты, «фермы» калькуляторов, креативные инструменты. Такие данные помечены [П, CrUX]. Корзина — порядок рейтинга (1k = топ-1000 сайтов страны); меньшее число лучше; «—» — сайт вне топ-1M.
> - В конце прохода лимит поиска сессии (200 запросов) был исчерпан. **Не успели проверить:** цены на анаморфные билборды и калькуляторы стоимости моушн-роликов, калькуляторы аренды LED-экранов, агрегаторы цен AI-изображений. Для этих тем действуют данные соседних потоков.

---

## Проверено и исправлено

| # | Утверждение оригинала | Статус | Что показала проверка (источник, дата) |
|---|---|---|---|
| 1 | Pew: клик по обычному результату в 8% визитов с AI-сводкой против 15% без неё; по ссылке в сводке — 1% | **Подтверждено** | Дополнительно: после страницы со сводкой сессия заканчивается в 26% случаев против 16% без неё ([Pew](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/), 2025-07-22). Полная научная версия вышла на arXiv 2026-08-05. AIO чаще появляется на длинных запросах, на запросах с вопросительным словом и на запросах «существительное + глагол» ([arXiv 2608.04831](https://arxiv.org/abs/2608.04831), 2026-08). |
| 2 | Ahrefs: CTR первой позиции −34,5% (04.2025), затем −58% | **Подтверждено** | Сравнивались данные GSC за 12.2023 и 12.2025, 300 тыс. ключей. Новое: бренды, процитированные в AIO, получают на 35% больше кликов, чем органика под сводкой ([Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update), 2026-02; [BusinessWire](https://www.businesswire.com/news/home/20260518322756/en/New-Research-Googles-AI-Overviews-Now-Cost-Websites-58-of-Their-Clicks), 2026-05-18). |
| 3 | Seer: процитированные в AIO страницы получают ~+120% CTR | **Уточнено** | 2,1% против 0,9% — это **×2,3, то есть +133%**. CTR на AIO-запросах: 1,3% в 12.2025 → 2,4% в 02.2026. Выборка: 53 бренда, 5,47 млн запросов, 2,43 млрд показов, 01.2025–02.2026 ([SEL](https://searchengineland.com/google-ai-overviews-ctr-recovery-study-475566), 2026-04; [Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update), 2026-04). |
| 4 | SparkToro: 68,01% поисков без клика (01–04.2026) | **Подтверждено** | База сравнения — 60,45% в 2024 году. Панель Similarweb, США, допущение «2/3 мобайл» ([SEL](https://searchengineland.com/google-zero-click-searches-2026-study-479717), 2026). |
| 5 | Semrush: доля запросов с AIO 6,49% → 24,61% → 15,69% | **Подтверждено** | Новое и важное для калькуляторов: у 95% AIO-ключей нет рекламы или она минимальна. Коммерческие ключи с CPC > $2 «в основном не затронуты». ~60% AIO-ключей имеют ≤100 запросов в месяц ([Semrush](https://www.semrush.com/blog/semrush-ai-overviews-study/), 2025-12). |
| 6 | I/O 2026: AI Mode — больше 1 млрд пользователей в месяц, Gemini 3.5 Flash | **Подтверждено** | Дополнительно: у AI Overviews больше 2,5 млрд пользователей в месяц; ~200 стран и 98 языков ([Google](https://blog.google/products-and-platforms/products/search/search-io-2026/), 2026-05-19; [tech-insider](https://tech-insider.org/google-ai-mode-1-billion-users-io-2026/), 2026-05). |
| 7 | Generative UI пришёл в AI Overviews (дата не указана) | **Уточнено** | Выкатка в AIO началась в августе 2026 года, «полная доступность — в ближайшие недели». На I/O Google обещал generative UI «всем в Поиске этим летом, бесплатно». SEJ прямо называет под угрозой сайты калькуляторов, конвертеров и сравнений ([SEJ](https://www.searchenginejournal.com/google-expands-generative-ui-beyond-ai-mode-into-ai-overviews/586452/), 2026-08-19). |
| 8 | Виджет «Character Counter» в AIO | **Подтверждено + CrUX** | Виджет есть ([SERoundtable](https://www.seroundtable.com/google-ai-overviews-character-counter-42026.html), ~2026-09). По CrUX `wordcounter.net` упал **ещё до виджета**: GB 10k → 50k в 06.2026, US 10k → 50k к 08.2026 [П, CrUX]. По Semrush в 03.2026 у сайта ещё было 14,19 млн визитов ([Semrush](https://www.semrush.com/website/wordcounter.net/overview/), 2026-03). |
| 9 | «Исследований о частоте AIO на калькуляторных запросах не найдено (нет данных)» | **Исправлено: данные есть** | BrightEdge: **AIO появляется только на 9% финансовых калькуляторных запросов** («401k calculator», «mortgage calculator», «compound interest calculator»). На YMYL — 11% против ~30% в среднем. На образовательных финансовых запросах («what is an IRA») — до 91% ([SEJ по данным BrightEdge](https://www.searchenginejournal.com/ai-overviews-disappears-on-certain-kinds-of-finance-queries/565389/), 2026-01-20; [BrightEdge](https://www.brightedge.com/resources/weekly-ai-search-insights/google-ymyl-finance-ai-overviews), 2026). |
| 10 | Политика от 2026-05-15 «теперь прямо называет» генеративный AI и перевод как scaled content abuse | **Частично неверно** | 15.05.2026 изменилось другое: спам-политики распространили на попытки **манипулировать ответами AI Overviews и AI Mode** ([SEL](https://searchengineland.com/google-updates-search-spam-policies-to-clarify-it-applies-to-generative-ai-responses-477657), 2026-05; [ppc.land](https://ppc.land/google-spam-policies-now-officially-cover-ai-overviews-and-ai-mode-in-search/), 2026-05). Примеры про генеративный AI и «автоматические преобразования, включая перевод» есть в политике scaled content abuse с марта 2024 года [З; текущая редакция подтверждена]. Риск «шаблон × 20 стран × перевод» существует **два с половиной года**, а не с мая 2026. |
| 11 | Календарь апдейтов 2026: 4 спам-апдейта | **Подтверждено** | Длительность спам-апдейтов: март — 19 ч 30 мин, июнь — 24–26.06, август — 18–21.08 (2 дня 16 ч). **Сентябрь (с 24.09) — до двух недель, самый долгий.** 2026 год — самый активный по спам-апдейтам с 2021-го ([SEJ](https://www.searchenginejournal.com/google-september-2026-spam-update/590828/), 2026-09-24; [SEJ](https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/), 2026-06). Core-апдейты: 27.03–08.04 и 21.05–02.06.2026; декабрь 2025 — 11–29.12, 18 дней ([Amsive](https://www.amsive.com/insights/seo/google-march-2026-core-update-winners-losers-analysis/), 2026-04; [Sistrix](https://www.sistrix.com/blog/google-december-2025-core-update-information-and-analysis/), 2025-12). |
| 12 | Мартовская волна 2026: удар по data-template страницам | **Подтверждено (практики)** | Падение трафика на 50–80% без сообщений в GSC: ранжирование просело алгоритмически, полный эффект виден через 14 дней после начала апдейта ([Digital Applied](https://www.digitalapplied.com/blog/scaled-content-abuse-google-march-update-ai-pages-decimated), 2026-03). GSQi (август 2026): сайт потерял **200 тыс.+ запросов целиком** — программатик-страницы в разных странах, где кроме шаблона был только AI-текст ([GSQi](https://www.gsqi.com/marketing-blog/august-2026-google-spam-update-case-studies/), 2026-08). |
| 13 | Mediavine: основной уровень от $5 тыс. годового дохода, Journey — от 1 000 сессий | **Подтверждено** | Journey — с 15.01.2026, от 1 000 сессий в месяц из Tier-1, доля издателя 70%. Official — от $5 тыс. в год, 75%. Select — $100–250 тыс. в год, 80% ([Jupiter](https://www.jupiter.co/blog/mediavine-requirements-2026-how-to-qualify), 2026; [Mediavine](https://www.mediavine.com/mediavine-requirements/), 2026). |
| 14 | Raptive: порог 25 тыс. просмотров | **Подтверждено** | Действует с **16.10.2025**. Для сайтов с 25–99,9 тыс. просмотров ≥50% трафика должно идти из US, UK, CA, NZ или AU ([SEJ](https://www.searchenginejournal.com/raptive-drops-traffic-requirement-by-75-to-25000-views/558780/), 2025-10). |
| 15 | Ezoic поднял порог до 250 тыс. (низкая уверенность) | **Подтверждено** | 250 тыс. пользователей в месяц для новых сайтов с **19.02.2026**. Исключения: программа Access Now (без минимума), Incubator и «дедушкина оговорка» для старых издателей ([Ezoic Support](https://support.ezoic.com/kb/article/getting-started-ezoics-requirements), 2026). |
| 16 | MyPayCalculator: ~$7,5 тыс. в год при ~150 тыс. посетителей, «~$4 RPM» | **Исправлено** | Обе цифры — **оценки третьих лиц** (трафик по инструментам, доход по «AdSense calculator»), а не отчёт владельца ([Goodreads mirror](https://www.goodreads.com/author_blog_posts/25154711-10-month-old-calculator-website-already-earning-7-5k-year?tab=book), 2024). Как замер RPM использовать нельзя. CrUX: `mypaycalculator.co.uk` в GB колеблется между 50k и 100k [П, CrUX]. |
| 17 | Omni: ~17 млн визитов, ~70 сотрудников | **Уточнено** | Semrush: 14,29 млн визитов в 06.2026 (−12,2% к маю); 53% — органика Google, 34% — прямой трафик ([Semrush](https://www.semrush.com/website/omnicalculator.com/overview/), 2026-06). Сотрудников 62 ([PitchBook](https://pitchbook.com/profiles/company/106982-56), 2026). Выручка +28,4% в 2024 году ([EMIS](https://www.emis.com/php/company-profile/PL/Omni_Calculator_Sp_z_oo_en_4463647.html)). |
| 18 | calculator.net: ~59,8 млн визитов | **Подтверждено** | 59,76 млн в 08.2026 ([Semrush](https://www.semrush.com/website/calculator.net/overview/), 2026-08); Similarweb — #1 135 в мире ([Similarweb](https://www.similarweb.com/website/calculator.net/), 2026-08). |
| 19 | `salaryaftertax.com` — «проигравший» мультистрановой сайт | **Уточнено (вывод был слишком общим)** | Сайт потерял периферийные рынки: GB 100k → 500k, NZ 50k → 500k. Но держит **топ-5k в Ирландии** и 50k в Канаде [П, CrUX]. Semrush: 502 тыс. визитов в 06.2026, +19,6% к маю, основная аудитория — Ирландия ([Semrush](https://www.semrush.com/website/salaryaftertax.com/overview/), 2026-06). У talent.com тот же паттерн: канадский `ca.talent.com` держится на 5k → 10k CA, а `ie.talent.com` упал 5k → 50k, `nz.talent.com` — 10k → 50k [П, CrUX]. **Правильный вывод: сеть сохраняет рынок, где она локальный лидер, и теряет остальные.** |
| 20 | WebFX: инструменты и калькуляторы получают от AI меньше, чем от органики | **Подтверждено** | 600 тыс. AI-сессий, 2 500 URL, 05.2025–05.2026. AI Lift у tools/calculators — **−3,0 п.п.** Главные получатели AI-трафика: домашние страницы (31,3%) и страницы стадии решения (55,3%) ([WebFX](https://www.webfx.com/blog/ai/what-content-earns-ai-traffic/), 2026-07). Цифру «98% из ChatGPT» повторно проверить не удалось. |
| 21 | Доля ChatGPT в AI-трафике 76% → 53% | **Подтверждено** | Gemini — 27–28%, Claude — ~9% (06.2025 → 05.2026) ([Similarweb](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/), 2026-05). |
| 22 | Консент: CMP обязательна с 16.01.2024 | **Подтверждено + новое** | С **01.03.2026 обязателен TCF v2.3**; новые строки v2.2 Google перестал принимать 28.02.2026. Иначе запрос уходит в Limited Ads, а это минус выручка ([ppc.land](https://ppc.land/google-mandates-tcf-v2-3-migration-by-february-2026/), 2025–2026). |
| 23 | Выплата AdSense на Payoneer для UK Ltd не подтверждена | **Частично закрыто** | Payoneer официально поддерживает приём AdSense на счета в USD, EUR и GBP ([Payoneer](https://www.payoneer.com/resources/how-to-use-payoneer/adsense-payments/)). Mediavine платит через Tipalti, среди методов есть Payoneer ([Mediavine Help](https://help.mediavine.com/mediavine-payment-methods)). AdSense допускает организационный аккаунт на юрлицо ([AdSense Help](https://support.google.com/adsense/answer/32750?hl=en-GB)). Директор-резидент Индонезии — **нет данных**. |
| 24 | «Специализированного калькулятора оплаты для съёмочных групп не найдено» | **Неверно** | Такие калькуляторы есть:<br>– **TimeMachine** — APA-калькулятор дня и табель для UK-рекламы, бесплатный, iPhone и веб ([timemachineapp.co.uk](https://timemachineapp.co.uk/), 2026);<br>– **CineLog** — оплата по Bectu HETV/MMP, iOS ([cinelog.co.uk](https://cinelog.co.uk/), 2026);<br>– **CineHours** — $89, iOS;<br>– FilmBiz Rate, Crew Time Card (правила IATSE);<br>– **Tools for Film** и **Production Slate** — бесплатные калькуляторы переработок ([toolsforfilm.com](https://www.toolsforfilm.com/tools/overtime-cost); [prodslate.com](https://www.prodslate.com/tools/overtime-calculator), 2026). |
| 25 | Сроки перехода с CEP на UXP | **Подтверждено** | Публичная бета UXP в AE — к 11.2026. AE, Illustrator и Media Encoder перестают принимать новые CEP-сабмиты, CEP отключён по умолчанию — 12.2028. Premiere перестаёт принимать CEP в 12.2027. CEP выводится из эксплуатации в конце 2029. Маркетплейс Photoshop не принимает новые CEP с 03.2027 ([Adobe Dev Blog](https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications), 2026-09). Публичного трекера совместимости поиск по-прежнему не нашёл. |
| 26 | Минфин Австрии выпустил Brutto-Netto-Rechner | **Подтверждено** | Калькулятор обновлён под 2026 год 30.12.2025: шкала +1,73%, изменения по пендлерам ([OTS](https://www.ots.at/presseaussendung/OTS_20251230_OTS0009/aktualisierter-brutto-netto-rechner-des-finanzministeriums-fuer-2026-online), 2025-12-30). В Германии есть официальный BMF-Steuerrechner ([bmf-steuerrechner.de](https://www.bmf-steuerrechner.de/)), в Австралии — Fair Work Pay Calculator ([calculate.fairwork.gov.au](https://calculate.fairwork.gov.au/)). |
| 27 | AIO и AI Mode цитируют разное (13,7% пересечения) | **Подтверждено** | При этом выводы совпадают в 86% случаев. Ответ AI Mode длиннее в 4 раза ([SEJ](https://www.searchenginejournal.com/google-ai-mode-ai-overviews-cite-different-urls-per-ahrefs-report/563364/), 2025-12). |
| 28 | Отчёты GSC по показам в AIO и AI Mode | **Подтверждено + детали** | В отчётах **только показы, без кликов и CTR**. Данные — с 18.05.2026. Выкатка на все сайты завершена 31.08.2026 ([Google](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports), 2026-06-03; [SEJ](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/), 2026-09). |

---

## Новые факты

### A. AI-поиск: охват, точность, регуляторика

1. **По Similarweb, AIO показывается в 43% поисков в США против 15% годом ранее.** Визиты в AI Mode: 126 млн (06.2025) → 279 млн (05.2026). Методика публично не раскрыта ([TechCrunch](https://techcrunch.com/2026/07/27/googles-ai-search-is-rapidly-becoming-the-default-new-data-shows/), 2026-07-27; критика — [MLQ](https://mlq.ai/news/google-ai-overviews-reached-43-of-us-searches-in-similarweb-data-but-methodology-is-thin/), 2026-07). Разброс оценок доли AIO в 2026 году у разных трекеров — от ~21% до ~60% ([Digital Bloom](https://thedigitalbloom.com/learn/ai-citation-position-revenue-report-2026/), 2026).
2. **Кто показывает AIO (Ahrefs, 146 млн SERP).**
   - AIO есть на 20,5% SERP; 99,9% триггеров — информационные запросы.
   - Запросы-вопросы: AIO в 57,9% случаев. Однословные запросы — 9,5%, запросы из 7+ слов — 46,4%.
   - Меньше всего AIO в «Shopping» (3,2%) и «Real Estate» (5,8%).
   - Источник: [Ahrefs](https://ahrefs.com/blog/ai-overview-triggers/), 2025. **Вывод:** запрос «45000 after tax» — короткий, без вопросительного слова, с числом — структурно реже вызывает AIO.
3. **BrightEdge (05.2025):** за год с запуска AIO показы выросли на 49%, CTR упал примерно на 30%. К началу 2026 года AIO стоял примерно на 48% отслеживаемых запросов в 9 отраслях ([BrightEdge](https://www.brightedge.com/news/press-releases/one-year-google-ai-overviews-brightedge-data-reveals-google-search-usage), 2025-05-14; [SEL](https://searchengineland.com/google-ai-overviews-search-clicks-fell-report-455498), 2025-05).
4. **Authoritas (новости UK-издателей, данные 16–22.04.2025):** при AIO CTR ниже на 47,5% на десктопе и на 37,7% на мобайле. ~70% страниц, процитированных в AIO, меняются за 2–3 месяца. Отчёт приложен к жалобе в CMA ([Press Gazette](https://pressgazette.co.uk/media-audience-and-business-data/google-ai-overviews-publishers-report-clickthroughs-authoritas-report/), 2025).
5. **Similarweb (отчёт о новостных издателях):** доля поисков без клика выросла с 56% до 69% (05.2024 → 05.2025). Органический трафик новостных сайтов упал с 2,3 млрд до 1,7 млрд визитов ([SERoundtable](https://www.seroundtable.com/similarweb-google-zero-click-search-growth-39706.html), 2025).
6. **Точность AI на финансах и налогах — эмпирика в пользу калькуляторов.**
   - The College Investor: 37% ответов AIO на 101 финансовый запрос вводят в заблуждение или неточны (в 2024 году — 43%). Хуже всего — налоги, страхование и финпомощь ([College Investor](https://thecollegeinvestor.com/66208/37-of-google-ai-finance-answers-are-inaccurate-in-2025/), 2025).
   - **TaxCalcBench:** лучшие модели правильно считают **меньше трети** федеральных деклараций США даже на упрощённой выборке ([arXiv 2507.16126](https://arxiv.org/pdf/2507.16126), 2025-07).
   - The Finance Buff: ChatGPT, Claude, Gemini и Grok все ошиблись в сложном кейсе с первой попытки ([Finance Buff](https://thefinancebuff.com/ai-tax-calculator.html), 2026).
7. **CMA (UK) обязала Google дать опт-аут из AIO и AI Mode без потери позиций** (2026-06-03).
   - Переключатель в GSC учитывается с 17.06.2026; Google обещал выкатить его глобально ([TechCrunch](https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/), 2026-06-03; [MediaPost](https://www.mediapost.com/publications/article/416681/google-gives-publishers-opt-out-for-ai.html), 2026-07-21).
   - Издатели говорят, что без данных о кликах опт-аутом «нельзя безопасно пользоваться». People Inc потерял 800 млн Google-сессий с Q1 2024 по Q1 2026 ([Digiday](https://digiday.com/media/googles-ai-opt-out-leaves-publishers-with-a-choice-they-cant-safely-use/), 2026).
8. **Давление в ЕС:** European Publishers Council подал антимонопольную жалобу на AIO ([RTÉ](https://www.rte.ie/news/business/2026/0210/1557746-google-ai-publishers/), 2026-02-10). Во Франции AIO и AI Mode включены с 22.07.2026 ([Digital Applied](https://www.digitalapplied.com/blog/google-ai-mode-france-launch-eu-publishers-seo-2026), 2026). В Германии AIO работает с 26.03.2025 ([Google](https://blog.google/feed/were-bringing-the-helpfulness-of-ai-overviews-to-more-countries-in-europe/), 2025-03).
9. **Агентный слой усиливается.**
   - «Information agents» в AI Mode — летом 2026 для подписчиков AI Pro и Ultra в США ([9to5Google](https://9to5google.com/2026/06/12/google-information-agents/), 2026-06-12).
   - ChatGPT запустил персональные финансы с подключением счетов: US, Plus и Pro, 2026-06-25 ([OpenAI](https://openai.com/index/personal-finance-chatgpt/), 2026-06).
   - В каталоге приложений ChatGPT было 1 624 приложения на 02.07.2026; 09.07.2026 каталог перенесён в Plugin directory (средняя уверенность, [awesome-chatgpt-apps](https://github.com/rdmgator12/awesome-chatgpt-apps), 2026-07).
   - CalcFleet уже продаёт калькуляторы (в т.ч. US take-home) через web, API и **MCP** с «проверяемыми квитанциями» расчёта ([Glama](https://glama.ai/mcp/connectors/com.calcfleet/calculators/tools/take_home_pay_calculator); [calcfleet.com](https://calcfleet.com/), 2026).

### B. LLM-рефералы: канал всё ещё крошечный

10. **Cloudflare Radar (05.2026):** Google даёт **87,63%** поисковых рефералов, а **все AI-чатботы вместе — 0,29%** ([TechnologyChecker](https://technologychecker.io/blog/search-engine-market-share), 2026-09).
11. **SE Ranking:** рефералы из ChatGPT выросли на 36,7% в мае 2026 года после того, как 07.05.2026 в ответах появились кликабельные бренд-ссылки. Доля переходов на **домашние страницы** выросла с 26–29% до 62–63% ([SE Ranking](https://seranking.com/blog/chatgpt-referral-traffic-may-2026/), 2026-06). **Вывод:** ChatGPT ведёт на бренд, а не на глубокую страницу калькулятора.
12. Perplexity в среднем даёт 21,9 цитаты на ответ против 10,4 у ChatGPT. Publisher Program — пул $42,5 млн, раздел 80/20 ([getpanto](https://www.getpanto.ai/blog/perplexity-ai-statistics); [Digital Strategy Force](https://digitalstrategyforce.com/journal/perplexitys-2026-publisher-program-what-it-means-for-content-creators/), 2026).
13. `llms.txt` **не влияет на цитирование**. Корреляции нет на выборке ~300 тыс. доменов; AI-краулеры почти не запрашивают этот файл ([SE Ranking](https://seranking.com/blog/llms-txt/), 2026; [Rankability](https://www.rankability.com/data/llms-txt-adoption/), 2026-06).

### C. Трафик калькуляторных сайтов: снимок из сниппетов Similarweb и Semrush (оценки вендоров)

| Сайт | Визиты (месяц, инструмент) | Динамика / комментарий |
|---|---|---|
| calculator.net | 59,76 млн (08.2026, Semrush) | CrUX: мир 1k стабильно |
| omnicalculator.com | 14,29 млн (06.2026, Semrush) | −12,2% м/м; CrUX US 5k → 10k (08.2026) |
| inchcalculator.com | 4,7 млн (05.2026, Semrush) против 7,79 млн (10.2025) | ~−40% за 7 мес.; CrUX GB 10k → 50k (08.2026) |
| thecalculatorsite.com | 4,7 млн (08.2026, [Exploding Topics](https://analytics.explodingtopics.com/website/thecalculatorsite.com)) | CrUX US 10k → 50k (12.2025); GB 5k стабильно |
| rapidtables.com | ~10,9 млн (01.2026, [Exploding Topics](https://analytics.explodingtopics.com/website/rapidtables.com)); 3 млн «search visits» (08.2026, [Similarweb/Semrush-сниппет](https://www.similarweb.com/website/rapidtables.com/)) | Метрики разные, сравнивать нельзя; CrUX US 5k → 10k |
| unitconverters.net | 2,4 млн (08.2026, [Semrush](https://www.semrush.com/website/unitconverters.net/overview/)) | CrUX стабильно 50k |
| convertunits.com | 862 тыс. (07.2026, [AhrefsTop](https://ahrefstop.com/websites/convertunits.com)) | CrUX US и GB 50k → **500k** (07–08.2026) |
| thesalarycalculator.co.uk | 1,3 млн поисковых (04.2026, [AhrefsTop](https://ahrefstop.com/websites/thesalarycalculator.co.uk)); 3,06 млн всего (12.2025, [Similarweb](https://www.similarweb.com/website/thesalarycalculator.co.uk/)) | 69% десктопа — органика; CrUX GB 1k |
| listentotaxman.com | **283 тыс.**, #7 367 в UK (04.2026, [Similarweb](https://www.similarweb.com/website/listentotaxman.com/)) | CrUX GB 10k — калибровка корзины |
| paycheckcity.com | **611,7 тыс.**, #15 720 в US (05.2026, [Similarweb](https://www.similarweb.com/website/paycheckcity.com/)) | Принадлежит Symmetry (payroll-движок); выручка $10–15 млн (оценка Similarweb) |
| salaryaftertax.com | 502 тыс. (06.2026, Semrush) | см. п. 19 выше |
| talent.com | 14,63 млн (11.2025, [Semrush](https://www.semrush.com/website/talent.com/overview/)) | −9,6% м/м |
| smartasset.com | 8,96 млн (06.2025, [Similarweb](https://www.similarweb.com/website/smartasset.com/)) | Paycheck calculator — главный драйвер органики; CrUX GB 50k → 500k, US 5k → 10k |
| paycalculator.com.au | #44 473 в мире (04.2026, [Similarweb](https://www.similarweb.com/website/paycalculator.com.au/)) | +1,2% м/м |

**Калибровка CrUX по визитам (оценка, средняя уверенность):**

| Корзина CrUX | Визитов в месяц | Эталон |
|---|---|---|
| GB top-1k | ~2–3 млн | thesalarycalculator.co.uk |
| GB top-10k | ~250–300 тыс. | listentotaxman.com |
| US top-50k | ~0,5–0,7 млн | paycheckcity.com |
| GB top-50k | ~50–200 тыс. | вывод из соседних корзин |

Оценка для GB top-50k в оригинале (100–200 тыс.) была на верхней границе.

### D. Новые первичные данные CrUX этого прохода [П, CrUX, 01.2025 → 08.2026]

14. **Программатик-«фермы» калькуляторов проседают на 1–2 порядка корзины. Бренды с прямым трафиком держатся.**
    - `calculator.academy`: US 10k → 100k; мир 50k → 500k.
    - `calculator-online.net`: GB 100k → **500k** сразу после майского core (06.2026).
    - `miniwebtool.com` и `goodcalculators.com`: US 100k → 500k.
    - `calculators.org`: GB 100k → 500k (08.2026).
    - При этом `calculatorsoup.com` (US 5k), `calculator.net` (1k) и `gigacalculator.com` (US 50k) стабильны.
    - Это прямое подтверждение тезиса «ферма из тысяч однотипных калькуляторов умирает» на данных самого Google.
15. **Ни один из ~30 найденных «креативных» калькуляторов не входит в топ-1M** (GB, US, AU, мир):
    - Tools for Film, Kreatli, Postplanify, SocialSizes, Poster.ly, FileFlippers;
    - TimeMachine, CineLog, Production Slate;
    - все freelance-rate-калькуляторы (`freelanceratecalculator.net/.org` и др.);
    - SyncCalc, Music Oracle, Tools 4 Music, Audiodrome;
    - DataCalc, FreeAIVideoHub, BDOOH, DOOH Marketing.
    - Исключения, все на границе топ-1M: `digitalrebellion.com` и `toolstud.io` (500k–1M), `ledwallcentral.com` (US 500k), `cometapi.com` (1M), `lipi.ai` (500k–1M), `creatorflow.so` (500k–1M).
    - **Вывод: рекламная модель друга, перенесённая в креативные ниши, даёт почти нулевой трафик.**
16. **Новые участники британской ниши «UK salary» 2025–2026 застряли внизу.**
    - `uksalarycalculator.io`, `calculatemysalary.co.uk`, `uksalarytakehome.co.uk`, `employerscalculator.co.uk`, `uktaxcal.com`, `ukcalculator.com` — все в корзине 500k–1M GB.
    - Инкумбенты держатся: thesalarycalculator — 1k, listentotaxman — 10k, uktaxcalculators — 50k, mypaycalculator — 50–100k.
    - **Входить генериком в «головную» нишу поздно.**
17. **NHS-ниша: победитель забирает почти всё.**
    - `nhstakehome.co.uk`: 1M (04.2026) → **50k** (08.2026).
    - Остальные клоны (`nhstakehomepaycalculator`, `nhstakehomepay`, `mynhstakehomecalculator`, `nhssalarycalculators`, `employerscalculator`) — 100k–1M.
    - В выдаче по запросу **9+ NHS-калькуляторов** ([SERP-срез](https://nhstakehome.co.uk/), 2026-09).
18. **Эффект «событийных» калькуляторов слабее, чем казалось.**
    - Закон OBBBA (04.07.2025) ввёл вычеты на переработки (до $12 500 / $25 000) и чаевые (до $25 000) на 2025–2028 годы. Вычет за чаевые заявили больше 3,5 млн деклараций к началу марта 2026 года ([Wikipedia](https://en.wikipedia.org/wiki/No_tax_on_tips); [H&R Block](https://www.hrblock.com/tax-center/irs/tax-law-and-policy/one-big-beautiful-bill-no-tax-on-overtime/), 2025–2026).
    - Под закон появились EMD-сайты: `noovertimetax.com`, `notaxovertimecalculator.com`, `notaxonovertimecalculators.org`, `nationaltaxtools.com`. Из них **только один** однажды мелькнул в US топ-1M (12.2025) [П, CrUX].
    - Спрос забрали TurboTax, H&R Block и Fidelity.
    - **Вывод:** смена правил — ров для **существующего бренда**, а не повод запускать отдельный сайт.
19. **AU award-калькуляторы подтверждены:** `fairworkmate.com.au` и `wagecalculator.com.au` — топ-50k AU (08.2026), при наличии официального калькулятора Fair Work.

### E. Монетизация и выход

20. **Реальный кейс калькуляторного сайта на Mediavine (Flippa).**
    - `247calculator.com`: пиковая прибыль **$728 в месяц при 25 тыс.+ просмотров**. Отсюда ~$29 за 1 000 просмотров на пике (оценка). Стабильный доход ~$600 в месяц без обновлений.
    - ~90% трафика — **не из Google**; из Google — до ~100 визитов в день. Калькуляторы частично написаны с AI.
    - Источник: [Flippa](https://flippa.com/12032211-728-peak-monthly-profit-25k-monthly-pageviews-100-margins-passive-calculator-site-earning-with-mediavine-primed-for-seo-growth), дата листинга н/д.
    - Мультипликаторы Flippa для контент-сайтов — 25–40× месячной прибыли, база калькулятора Flippa — 30× ([Flippa](https://flippa.com/blog/how-much-is-my-website-worth/), 2025).
21. **SleepCalculator.com:** ~1,6 млн пользователей в месяц, оценка дохода $30–36 тыс. в месяц — это **оценка** Niche Pursuits, а не отчёт владельца ([X / Niche Pursuits](https://x.com/nichepursuits/status/1904573862244999235), 2025-03). CrUX: мир 100k → 500k (12.2025), GB 50k → 100k [П]. Даже «вечнозелёный» одностраничник теряет трафик.
22. **RPM (вендорские и блогерские цифры, низкая уверенность):**
    - Adstimate: Tier-1 (US, UK, CA, AU, DE) — $15–45 ([Adstimate](https://adstimate.com/blog/adsense-rpm-by-country.html), 2026);
    - Raptive, финансы: $18–50+; один издатель на Raptive — $34–44 RPM в 01–02.2026, ниша не указана ([This Week in Blogging](https://thisweekinblogging.com/mediavine-vs-raptive/), 2026);
    - **Единственная «жёсткая» точка — 247calculator (~$24–29 на пике).**
23. **AdSense:** «Low value content» — самая частая причина отказа. Цифра «85% первых заявок отклоняются» — непроверенная блогерская оценка, низкая уверенность ([ILLUMINATION](https://medium.com/illumination/google-adsense-rejection-fixes-2026-get-approved-after-multiple-rejections-aab43931f654), 2026).
24. **Партнёрка Adobe (Partnerize):** 85% первого месяца для помесячных планов и 8,33% для предоплаченных годовых ([Cuelinks](https://www.cuelinks.com/campaigns/adobe-affiliate-program), 2026-08; [Adobe](https://www.adobe.com/affiliates.html)). Для креативных тул-сайтов это самый жирный аффилиатный слой.
25. **B2B-рынок налоговых движков существует и платит.**
    - Symmetry (владелец PaycheckCity) продаёт Tax Engine и калькуляторы через API и виджеты по индивидуальным квотам ([Symmetry](https://www.symmetry.com/calculators-by-symmetry)).
    - Инди-API **PayrollTaxAPI**: Free — 1 тыс. запросов; **$49 в месяц — 100 тыс.; $299 в месяц — 2 млн**. Сам сервис утверждает, что Symmetry и Vertex берут $17,5–33 тыс. в год — это слова конкурента ([payrolltaxapi.com](https://payrolltaxapi.com/), 2026).
    - Бесплатные виджеты раздают FederalPay и EmployerCost; у EmployerCost white-label за деньги ([FederalPay](https://www.federalpay.org/calculator-widgets); [EmployerCost](https://employercost.com/widget)).
26. **Будущие события смены правил** (спрос на обновления):
    - UK: пороги подоходного налога заморожены **до апреля 2031**; с **06.04.2029** льгота по NIC на salary sacrifice ограничена £2 000 в год ([MoneySavingExpert](https://www.moneysavingexpert.com/news/2025/11/salary-sacrifice-capped-national-insurance-budget/), 2025-11).
    - NHS: повышение 2026/27 — 3,3% ([nhstakehome.co.uk](https://nhstakehome.co.uk/), 2026).
    - US: вычеты OBBBA истекают после 2028 года, а это ещё одна волна запросов.

### F. Контекст «ответных» сайтов (подтверждение коллапса из CrUX)

27. **Chegg:** трафик от не-подписчиков −49% в январе 2025 года, выручка −24% в Q4 2024, иск к Google за AIO ([SEL](https://searchengineland.com/google-sued-by-chegg-over-ai-overviews-hurting-traffic-and-revenue-452518), 2025-02). **Stack Overflow:** вопросов на 76% меньше, чем до ChatGPT ([ppc.land](https://ppc.land/stack-overflow-traffic-collapses-as-ai-tools-reshape-how-developers-code/), 2026). **Forbes Advisor** после санкции за site reputation abuse (09.2024) к 05.2025 вернул лишь ~17% трафика ([BuzzStream](https://www.buzzstream.com/blog/forbes-advisor-analysis/), 2025).

---

## Заполненные пробелы (по пунктам брифа)

1. **Влияние AIO и AI Mode на CTR.** Все цифры оригинала подтверждены. Добавлены:
   - Authoritas: −47,5% / −37,7%;
   - BrightEdge: показы +49%, CTR −30%;
   - Similarweb: доля поисков без клика 56% → 69%, охват AIO 43%;
   - arXiv-версия Pew.

   Seer исправлен (×2,3).
2. **Трафик калькуляторных сайтов.** См. таблицу C. Паттерн: генерики и фермы теряют 20–40% за год (inchcalculator, omni, convertunits, calculator.academy). Лидеры с прямым трафиком стабильны (calculator.net, calculatorsoup). Юрисдикционные лидеры растут (thesalarycalculator, listentotaxman). Данных по incomeaftertax.com **нет**: в выдаче сайт не нашёлся.
3. **Триггерится ли AIO на калькуляторных запросах и удерживают ли клики интерактивные инструменты.**
   - **Да, удерживают, но не все.** Финансовые калькуляторные запросы — AIO в 9% случаев (BrightEdge).
   - Короткие и числовые запросы структурно реже вызывают AIO (Ahrefs).
   - Коммерческие ключи с CPC > $2 почти не затронуты (Semrush).
   - Контр-тренд: **generative UI в AIO с 08.2026** и встроенный счётчик символов. Google сам строит одношаговые инструменты.
   - Прямых данных о CTR калькуляторов после generative UI пока **нет**. Лучший прокси — корзины CrUX (сигнал в разделе сценариев).
4. **Спам-политики и апдейты.**
   - Календарь 2025–2026 подтверждён; сентябрьский спам-апдейт идёт до двух недель.
   - Уточнено: майское изменение политики касалось манипуляции AI-ответами, а не перевода.
   - Кейс GSQi: программатик плюс AI-текст ведёт к полной потере 200 тыс.+ запросов.
5. **LLM-рефералы.**
   - Все AI-чатботы вместе дают 0,29% поисковых рефералов против 87,6% у Google.
   - Калькуляторы получают от AI относительно меньше, чем от органики (WebFX: −3,0 п.п.).
   - ChatGPT ведёт в основном на домашние страницы (62–63%).
   - `llms.txt` бесполезен для цитирования.
   - **Вывод:** до 2028 года это не канал для калькуляторов. Канал — это агентный слой (MCP/API), см. идею N3.
6. **Монетизация.**
   - Пороги Mediavine, Raptive и Ezoic подтверждены (Ezoic — с исключениями).
   - С 03.2026 обязателен TCF v2.3.
   - Реальная точка RPM калькулятора на Mediavine — ~$24–29 на пике (247calculator).
   - Мультипликаторы Flippa — 25–40×.
   - Партнёрка Adobe — 85% первого месяца.
   - RPM по DE, AU, CA раздельно — **нет данных** (только Tier-1 скопом у вендоров).
7. **Модель друга: почему работает и что выживет.**
   - Подтверждено: (а) отдельная страна с брендом и прямым трафиком выживает; (б) у мультистрановых сетей остаётся их «домашний» рынок, периферия отваливается; (в) ниша профессии (NHS) — это гонка, где выживает №1; (г) генерик в занятой нише не пробивается.
   - Опровергнуто: «событийные» EMD-сайты под новый закон в основном не пробились — спрос ушёл к брендам.
8. **8–12 похожих схем в темах основателя.** См. раздел идей. Главная новость — **насыщение.** Почти в каждой креативной «калькуляторной» нише уже есть 5–10 бесплатных AI-собранных инструментов, и никто из них не набрал заметного трафика. Значит, спрос на такие калькуляторы мал сам по себе. Деньги — не в рекламе, а в воронке к платному продукту или в B2B.
9. **Шесть стандартных вопросов: уточнения к оригиналу.**
   - *Массовым и дешёвым станет* ещё и **сам «калькулятор-маркетинг»**. Safe-zone-чекеры, калькуляторы ставок и расчёты стоимости AI-видео раздаются бесплатно как лид-магниты SaaS и API-реселлеров (Kreatli, Postplanify, CometAPI, FreeAIVideoHub).
   - *Платформы поглотят* одношаговые инструменты: generative UI в AIO, виджеты в SERP, персональные финансы в ChatGPT (US).
   - *Деньги останутся* у бренда №1 в юрисдикции, у B2B-движков и API (PayrollTaxAPI $49–299 в месяц, Symmetry) и у платных инструментов внутри рабочих приложений (Safest Zone на aescripts, $99,99).
   - *Доступ к инструментам.* Массовый пользователь получит расчёт в поиске. Профессионалу нужен **аудит-след**: версия правил, источник, квитанция. Этот рынок начинают CalcFleet и MCP-обёртки госкалькуляторов.
   - *Обесценится:* сборка калькуляторов, EMD-домены под новый закон, `llms.txt`/GEO-«хаки».
   - *Дефицитом станут:* статус локального лидера (бренд) в стране или профессии, скорость обновления правил, B2B-доверие.

---

## Обновлённые сценарии и сигналы

Новые данные **меняют картину по сегментам**. Один общий сценарий для «калькуляторов» больше не годится.

**Сегмент 1. Генерики и программатик-фермы.** «Быстрый» сценарий фактически уже идёт:
- calculator.academy −1 порядок корзины;
- convertunits → 500k;
- wordcounter — вниз на корзину ещё до виджета;
- Omni −12% м/м.

Вероятность продолжения падения на −30–60% к 2028 году — **~70% (оценка, средняя уверенность)**.

**Сегмент 2. Юрисдикционные pay/tax-калькуляторы (модель друга).** Вероятности пересмотрены.

| Сценарий | Было | Стало | Почему |
|---|---|---|---|
| Базовый | 55% | **55%** | Без изменений. Трафик на новый сайт сжимается за счёт клонов и generative UI; бренды №1 держатся |
| Быстрый (Google или ChatGPT считают take-home сами, CTR −40%+) | 25% | **20%** | Против: финкалькуляторные запросы — AIO в 9% (BrightEdge, 2026-01); YMYL-осторожность (11%); 37% ошибок AIO в финансах; TaxCalcBench <1/3. За: generative UI в AIO (08.2026); персональные финансы в ChatGPT (06.2026) |
| Медленный (угроза в основном от клонов) | 20% | **25%** | Регуляторика: опт-аут CMA, жалоба EPC, иск Penske. Тренд: лидеры ниши растут в CrUX в 2026 году |

**Сегмент 3. Креативные калькуляторы.** Рекламная модель нежизнеспособна **в любом сценарии**: 0 из ~30 инструментов в топ-1M. Жизнеспособны только как воронка к платному продукту, лидоген или B2B.

**Новые и уточнённые сигналы:**

1. **Доля AIO на финкалькуляторных запросах.**
   - Как мониторить: еженедельные сводки BrightEdge плюс свои 30 контрольных запросов («£45,000 after tax», «take home pay 90000 australia», «brutto netto 4000»).
   - Порог «быстрого» сценария: **>25%** (сейчас 9%) или появление **интерактивного generative UI** на запросах take-home в UK/US.
2. **Распространение generative UI на Tier-1 страны** — в Google-блогах (Keyword, Search Central) и SEJ/SERoundtable. Сигнал: интерактивный расчёт налога в AIO хотя бы в одной стране портфеля.
3. **Персональные финансы в ChatGPT за пределами США** — в релиз-нотах OpenAI. Сигнал: запуск в UK, AU или CA.
4. **Корзины CrUX: три эталонные группы** (скрипт `lookup2.py` на кэше [zakird/crux-top-lists](https://github.com/zakird/crux-top-lists), ежемесячно):
   - лидеры: thesalarycalculator, listentotaxman, brutto-netto-rechner, paycalculator.com.au;
   - фермы: calculator.academy, calculator-online.net, miniwebtool;
   - новички: nhstakehome, fairworkmate.

   Сигнал «быстрого» сценария: лидеры теряют корзину. Сигнал «медленного»: новички продолжают входить в топ-50k.
5. **Доля AI-чатботов в поисковых рефералах** ([Cloudflare Radar](https://radar.cloudflare.com/)) — сейчас 0,29%. Если больше 1%, LLM-оптимизацию страниц пора включать в план.
6. **Показы против кликов в отчётах GSC по AI:** в отчётах только показы. Сигнал — рост AI-показов при падении органических кликов на те же URL более чем на 30%.
7. **Длительность и частота спам-апдейтов** ([Status Dashboard](https://status.search.google.com/)). Пять и больше спам-апдейтов за 2027 год или сохранение двухнедельных выкаток означает давление на любой шаблонный контент.
8. **Пороги премиальных сетей** (Mediavine, Raptive, Ezoic). Снижение порогов — сигнал, что сети борются за издателей на фоне падения трафика. Повышение (Ezoic, 02.2026) отрезает мелкие сайты.

---

## Идеи-кандидаты: новые и уточнённые

### Пересмотр вердиктов по 10 схемам оригинала

| # | Схема | Было | Стало | Причина (новые данные) |
|---|---|---|---|---|
| 1 | CrewRate (оплата кино, ТВ, рекламы) | **Лучший** | **Слабо–средне** | Уже есть TimeMachine (бесплатно, UK APA), CineLog (UK HETV), CineHours ($89), FilmBiz Rate, Tools for Film, Production Slate. Никто из них не в топ-1M, значит спрос мал |
| 2 | Гос. шкалы оплаты AU/NZ/IE/CA | Хорошо, но гонка | **Хорошо, только первым и через конвейер друга** | nhstakehome → 50k за 4 мес.; fairworkmate и wagecalculator → 50k AU. Клоны застревают на 500k–1M |
| 3 | Take-home и дневная ставка для креативных фрилансеров | Хорошо | **Слабо как SEO; средне как отчёт о ставках** | 9+ EMD-калькуляторов ставок, все вне топ-1M; бенчмарки ставок раздают YunoJuno и Malt |
| 4 | Спецификации и safe zones + preflight | Средне | **Средне, только как воронка к платному AE/UXP-продукту** | 10+ бесплатных safe-zone-чекеров, вне топ-1M; на aescripts уже есть Safest Zone ($99,99) и Unsafe Area Overlay |
| 5 | Атлас DOOH и калькулятор LED | Хорошо как лидоген | **Сузить до экранов ЮВА и анаморфной геометрии** | Базу LED-панелей уже держит LED Wall Central (команда ProjectorCentral, 4 000+ панелей, US 500k) |
| 6 | UXP Radar | Хорошо (2027–29) | **Хорошо** (сроки Adobe подтверждены, трекера нет) | — |
| 7 | License Check (шрифты, музыка) | Средне | **Слабо** | 8+ font-license-чекеров, 8+ sync-fee-калькуляторов, почти все вне топ-1M |
| 8 | Стоимость AI-продакшена | Слабо–средне | **Слабо** | Калькуляторы — маркетинг API-реселлеров (CometAPI, FreeAIVideoHub, BuildMVPFast, NodeTool); выигрывает владелец данных (artificialanalysis.ai → 50k GB и US) |
| 9 | Смета моушна и анаморфа | Хорошо как лидоген | Без изменений | Проверить не успели (лимит поиска) |
| 10 | Битрейт и рендер | Слабо | **Слабо** | Digital Rebellion и toolstud.io — 500k–1M; калькуляторы рендер-ферм бесплатны (RebusFarm, Ranch, SuperRenders, TurboRender) |

### N1. «Pay-калькуляторы с первенством в нише» — партнёрство с конвейером друга (тип B; уточнённая схема 2)
- **Суть:** не генерики, а **первый качественный сайт для профессии или региона**, где лидера ещё нет. После выхода в топ-50k — рассылка «ваша оплата изменится с даты X».
- **Формат:** 1 сайт = 1 профессия × 1 юрисдикция. Реальные таблицы соглашений, дата проверки, методология, email-алерты.
- **Покупатель и боль:** бюджетники и работники по отраслевым соглашениям (AU awards, NHS, учителя, IE HSE). Каждый год выходят новые ставки, а официальные PDF неудобны.
- **Доказательства спроса:**
  - `nhstakehome.co.uk`: 1M → **50k GB** с 04 по 08.2026;
  - `fairworkmate.com.au` и `wagecalculator.com.au` → **50k AU** (08.2026), несмотря на официальный калькулятор Fair Work [П, CrUX];
  - listentotaxman (топ-10k GB) ≈ 283 тыс. визитов в месяц (Similarweb, 04.2026).
- **Конкуренты (все бесплатные):** Fair Work Pay Calculator (гос.); в NHS-нише 9+ клонов; в AU ещё PayRate.au; генерики thesalarycalculator и paycalculator.com.au.
- **Гипотеза моата:** быть №1 (победитель берёт почти всё: клоны застревают на 500k–1M) + скорость обновления в день выхода соглашения + email-база. Код — не моат.
- **Главный риск:** гонка клонов (5–9 клонов за 3–6 месяцев) и generative UI. Для основателя без кода есть YMYL-риск ошибок в расчёте. **Делать только в связке с другом**: его конвейер, домены и опыт AdSense; основатель ищет ниши и делает дизайн и бренд.

### N2. «Движок оплаты как API, виджеты и MCP» (тип B, B2B; новая схема)
- **Суть:** взять движки расчёта take-home из N1 (UK, IE, AU, NZ) и продавать их как **API и встраиваемые виджеты** HR-сайтам, рекрутерам и job-бордам. Как **MCP-сервер** — агентам: «зарплата X по правилам 2026/27, квитанция с версией правил».
- **Формат:** API по подписке + white-label-виджет + MCP в каталогах (Glama, Smithery).
- **Покупатель и боль:** рекрутинговые сайты и job-борды (talent.com держит калькуляторы ради SEO); финтех; AI-агенты, которые сами ошибаются в налогах (TaxCalcBench: <1/3 верных расчётов).
- **Доказательства спроса:**
  - PaycheckCity (612 тыс. визитов в месяц) — витрина B2B-движка Symmetry с выручкой $10–15 млн (оценка);
  - PayrollTaxAPI продаёт тарифы $49 и $299 в месяц;
  - CalcFleet продаёт MCP-калькуляторы с квитанциями;
  - MCP-обёртки госкалькуляторов (estv-mcp, irish-tax-mcp — из оригинала).
- **Конкуренты с ценами:** Symmetry (индивидуальная квота; по словам конкурента, $17,5–33 тыс. в год); PayrollTaxAPI (Free / $49 / $299 в месяц, только США); FederalPay и EmployerCost (бесплатные виджеты, white-label — по запросу); CalcFleet (цены н/д).
- **Гипотеза моата:** версионированные правила нескольких стран вне США, аудит-след и SLA на обновление в день изменения. У американских API этого нет.
- **Главный риск:** B2B-продажи и поддержка противоречат режиму 2–4 часов в неделю. Ответственность за ошибки в расчётах. Спрос вне США не подтверждён (**нет данных**).

### N3. «Бесплатный веб-чекер → платный AE/UXP-инструмент» (тип A; уточнённая схема 4)
- **Суть:** веб-проверка ролика (safe zones, длительность, fps, громкость, spec площадки или DOOH-экрана) как **бесплатная воронка**, а монетизация — платная AE/UXP-панель на aescripts, которая делает то же самое внутри AE. Это прямое продолжение аудитории Oblique.
- **Покупатель и боль:** моушн-дизайнер сдаёт 10–30 версий под площадки и экраны; отбраковка по спекам стоит переделок.
- **Доказательства спроса:**
  - на aescripts продаются **Safest Zone ($99,99)** и Unsafe Area Overlay — люди платят за это внутри AE ([aescripts](https://aescripts.com/safest-zone/), 2026);
  - в сообществе Adobe есть запрос «Safezones for current social media platforms» ([Adobe Community](https://community.adobe.com/t5/after-effects-ideas/safezones-for-current-social-media-platforms-pleeeaaaaase/idi-p/15276849));
  - 10+ бесплатных веб-чекеров (Kreatli, Postplanify, Poster.ly, CreatorFlow, Overvisual, FileFlippers) — все вне топ-1M, кроме CreatorFlow, то есть **рекламой SEO-сайт здесь не окупится**.
- **Конкуренты с ценами:** Safest Zone $99,99; бесплатные веб-чекеры; оверлеи PNG бесплатно; пресеты Adobe Media Encoder входят в подписку.
- **Гипотеза моата:** экспертиза AE, бренд Oblique и аудитория aescripts. Спеки DOOH и 3D-экранов студии (у SaaS-чекеров их нет). Ранний выход на UXP в AE (бета с 11.2026).
- **Главный риск:** ниша уже занята платным AE-инструментом; AI-клоны появятся за месяцы (урок Oblique). Реалистичная выручка — как у одного скрипта aescripts, а не как у портфеля.

### N4. «UXP Radar» (тип A; схема 6 подтверждена)
- **Суть:** публичная матрица «плагин × версия AE/Premiere/Photoshop × CEP/UXP» + рассылка «что сломается» + каталог мигрировавших плагинов.
- **Доказательства спроса:**
  - Adobe: UXP-бета в AE к 11.2026;
  - Premiere перестаёт принимать CEP в 12.2027;
  - CEP отключён по умолчанию в AE, Illustrator и AME в 12.2028, выводится в конце 2029;
  - маркетплейс Photoshop закрывает CEP в 03.2027 ([Adobe Dev Blog](https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications), 2026-09);
  - Hyper Brew пишет «часы тикают» ([Hyper Brew](https://hyperbrew.co/blog/uxp-plugins-in-premiere-2026/), 2026);
  - публичного трекера поиск не нашёл.
- **Конкуренты:** блоги Hyper Brew и Filmit, фильтры aescripts, заметки Toolfarm. Цены — н/д (контент бесплатный).
- **Монетизация:** спонсорство разработчиков плагинов; аффилиаты aescripts и Adobe (85% первого месяца помесячной подписки); платный «studio pack» — оценка.
- **Гипотеза моата:** накопленная история совместимости + сеть разработчиков, которые сами присылают данные + доверие к автору Oblique. Слишком мелко для Adobe.
- **Главный риск:** маленькая платящая аудитория; окно ограничено 2027–2029 годами.

### N5. «Годовой отчёт о ставках моушн- и 3D-фрилансеров» (тип A; замена схеме 3)
- **Суть:** не калькулятор, а **собственный датасет** — ежегодный опрос ставок через сообщество основателя и покупателей Oblique. К нему — лёгкий калькулятор «ставка → take-home» (UK, AU, DE) как точка входа.
- **Доказательства спроса:**
  - медиана дневной ставки remote/hybrid моушн-дизайнера в UK — £388 (ITJobsWatch, 6 мес. до 01.05.2025); средняя — £250 в день ([YunoJuno](https://www.yunojuno.com/freelancer-rates-job-role/motion-graphics); [Creativepool](https://creativepool.com/magazine/industry/freelance-day-rates-in-2026-what-creative-talent-should-charge.34695), 2026);
  - `yunojuno.com` вырос в GB 50k → **10k** (01.2025 → 08.2026), интерес к фриланс-ставкам растёт [П, CrUX].
- **Конкуренты:** YunoJuno и Malt (бесплатные таблицы ставок как маркетинг маркетплейсов), School of Motion (зарплатный гайд), 9+ бесплатных калькуляторов ставок.
- **Монетизация:** спонсорство (рендер-фермы, стоки, плагины), лидоген бухгалтерам для UK Ltd (оценка), продвижение собственных продуктов.
- **Гипотеза моата:** первичные данные, которые копятся годами. AI-клон калькулятора не повторит опрос.
- **Главный риск:** низкая прямая выручка. Нужна ежегодная работа по сбору данных (~20–40 ч в год, оценка).

### N6. «Screen Atlas ЮВА» — экраны DOOH и анаморф, лидоген студии (тип A; суженная схема 5)
- **Суть:** не база LED-панелей (её держит LED Wall Central), а **каталог конкретных экранов ЮВА и Ближнего Востока** с реальным разрешением канваса, углом и точкой обзора для анаморфа, спеками файла и сроками согласования. Плюс калькулятор «экран → канвас → бюджет».
- **Доказательства спроса:**
  - нишевые DOOH-справочники вне топ-1M (BDOOH, DOOH Marketing) [П, CrUX]; AdQuick и Blip — US 500k [П]. Спрос есть, но маленький;
  - цены билбордов в США: $250–14 000+ в месяц за статику, $1 200–15 000 за цифровые; CPM $3–10 ([AdQuick](https://www.adquick.com/billboard-cost), 2026).
- **Конкуренты с ценами (все бесплатные):** LED Wall Central (бесплатно, 4 000+ панелей), BDOOH, DOOH Marketing, спек-дашборд Vistar (по запросу через Deal Desk), калькуляторы LED от производителей (Key Digital, Esdlumen, DOIT Vision).
- **Гипотеза моата:** связь с физическим миром — замеры и кейсы студии, отношения с операторами в ЮВА.
- **Главный риск:** SEO-выручка около нуля. Это лидоген студии, а не самоходный продукт.

---

## Источники

1. Pew Research — https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ (2025-07-22)
2. arXiv 2608.04831 (Pew panel, AIO clicks) — https://arxiv.org/abs/2608.04831 (2026-08-05)
3. Ahrefs, AIO reduce clicks update — https://ahrefs.com/blog/ai-overviews-reduce-clicks-update (2026-02)
4. BusinessWire, Ahrefs Q1 2026 benchmark — https://www.businesswire.com/news/home/20260518322756/en/New-Research-Googles-AI-Overviews-Now-Cost-Websites-58-of-Their-Clicks (2026-05-18)
5. Seer Interactive 2026 — https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update (2026-04)
6. Search Engine Land о Seer — https://searchengineland.com/google-ai-overviews-ctr-recovery-study-475566 (2026-04)
7. SEL, zero-click 68% — https://searchengineland.com/google-zero-click-searches-2026-study-479717 (2026)
8. Semrush AI Overviews study — https://www.semrush.com/blog/semrush-ai-overviews-study/ (2025-12)
9. Google I/O 2026 Search — https://blog.google/products-and-platforms/products/search/search-io-2026/ (2026-05-19)
10. tech-insider, AI Mode 1B — https://tech-insider.org/google-ai-mode-1-billion-users-io-2026/ (2026-05)
11. SEJ, generative UI в AIO — https://www.searchenginejournal.com/google-expands-generative-ui-beyond-ai-mode-into-ai-overviews/586452/ (2026-08-19)
12. Google blog, Gemini 3 в Search — https://blog.google/products-and-platforms/products/search/gemini-3-search-ai-mode/ (2025-11-18)
13. SERoundtable, Character Counter — https://www.seroundtable.com/google-ai-overviews-character-counter-42026.html (~2026-09)
14. Semrush, wordcounter.net — https://www.semrush.com/website/wordcounter.net/overview/ (2026-03)
15. SEJ/BrightEdge, finance calculators 9% — https://www.searchenginejournal.com/ai-overviews-disappears-on-certain-kinds-of-finance-queries/565389/ (2026-01-20)
16. BrightEdge, YMYL finance — https://www.brightedge.com/resources/weekly-ai-search-insights/google-ymyl-finance-ai-overviews (2026)
17. SEL, spam policies & AI responses — https://searchengineland.com/google-updates-search-spam-policies-to-clarify-it-applies-to-generative-ai-responses-477657 (2026-05)
18. ppc.land, spam policies cover AIO — https://ppc.land/google-spam-policies-now-officially-cover-ai-overviews-and-ai-mode-in-search/ (2026-05)
19. Google spam policies — https://developers.google.com/search/docs/essentials/spam-policies (ред. 2026-05-15)
20. SEJ, September 2026 spam update — https://www.searchenginejournal.com/google-september-2026-spam-update/590828/ (2026-09-24)
21. SEJ, June 2026 spam update — https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/ (2026-06)
22. Amsive, March 2026 core — https://www.amsive.com/insights/seo/google-march-2026-core-update-winners-losers-analysis/ (2026-04)
23. Sistrix, December 2025 core — https://www.sistrix.com/blog/google-december-2025-core-update-information-and-analysis/ (2025-12)
24. Digital Applied, scaled content abuse March 2026 — https://www.digitalapplied.com/blog/scaled-content-abuse-google-march-update-ai-pages-decimated (2026-03)
25. GSQi, August 2026 spam update case studies — https://www.gsqi.com/marketing-blog/august-2026-google-spam-update-case-studies/ (2026-08)
26. Jupiter, Mediavine requirements 2026 — https://www.jupiter.co/blog/mediavine-requirements-2026-how-to-qualify (2026)
27. Mediavine requirements — https://www.mediavine.com/mediavine-requirements/ (2026)
28. SEJ, Raptive 25K — https://www.searchenginejournal.com/raptive-drops-traffic-requirement-by-75-to-25000-views/558780/ (2025-10)
29. Ezoic Support, requirements — https://support.ezoic.com/kb/article/getting-started-ezoics-requirements (2026)
30. MyPayCalculator (оценка) — https://www.goodreads.com/author_blog_posts/25154711-10-month-old-calculator-website-already-earning-7-5k-year?tab=book (2024)
31. Semrush, omnicalculator.com — https://www.semrush.com/website/omnicalculator.com/overview/ (2026-06)
32. PitchBook, Omni Calculator — https://pitchbook.com/profiles/company/106982-56 (2026)
33. EMIS, Omni Calculator — https://www.emis.com/php/company-profile/PL/Omni_Calculator_Sp_z_oo_en_4463647.html (н/д)
34. Semrush, calculator.net — https://www.semrush.com/website/calculator.net/overview/ (2026-08)
35. Similarweb, calculator.net — https://www.similarweb.com/website/calculator.net/ (2026-08)
36. Semrush, salaryaftertax.com — https://www.semrush.com/website/salaryaftertax.com/overview/ (2026-06)
37. WebFX, 600K AI sessions — https://www.webfx.com/blog/ai/what-content-earns-ai-traffic/ (2026-07)
38. Similarweb, Gen AI stats — https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/ (2026-05)
39. ppc.land, TCF v2.3 — https://ppc.land/google-mandates-tcf-v2-3-migration-by-february-2026/ (2025–2026)
40. Payoneer, AdSense payments — https://www.payoneer.com/resources/how-to-use-payoneer/adsense-payments/ (н/д)
41. Mediavine Help, payment methods — https://help.mediavine.com/mediavine-payment-methods (2026)
42. AdSense Help, account types — https://support.google.com/adsense/answer/32750?hl=en-GB (н/д)
43. TimeMachine (APA crew) — https://timemachineapp.co.uk/ (2026)
44. CineLog — https://cinelog.co.uk/ (2026)
45. Tools for Film, overtime calculator — https://www.toolsforfilm.com/tools/overtime-cost (2026)
46. Production Slate, overtime calculator — https://www.prodslate.com/tools/overtime-calculator (2026)
47. Adobe Dev Blog, CEP → UXP — https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications (2026-09)
48. Hyper Brew, UXP in Premiere 2026 — https://hyperbrew.co/blog/uxp-plugins-in-premiere-2026/ (2026)
49. OTS, BMF Brutto-Netto-Rechner 2026 — https://www.ots.at/presseaussendung/OTS_20251230_OTS0009/aktualisierter-brutto-netto-rechner-des-finanzministeriums-fuer-2026-online (2025-12-30)
50. Fair Work Pay Calculator — https://calculate.fairwork.gov.au/ (2026)
51. SEJ, AIO vs AI Mode citations — https://www.searchenginejournal.com/google-ai-mode-ai-overviews-cite-different-urls-per-ahrefs-report/563364/ (2025-12)
52. Google, Gen AI performance reports — https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports (2026-06-03)
53. SEJ, GSC AI reports worldwide — https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/ (2026-09)
54. TechCrunch, AIO 43% — https://techcrunch.com/2026/07/27/googles-ai-search-is-rapidly-becoming-the-default-new-data-shows/ (2026-07-27)
55. MLQ, методика 43% — https://mlq.ai/news/google-ai-overviews-reached-43-of-us-searches-in-similarweb-data-but-methodology-is-thin/ (2026-07)
56. Digital Bloom, AI citation report 2026 — https://thedigitalbloom.com/learn/ai-citation-position-revenue-report-2026/ (2026)
57. Ahrefs, AIO triggers — https://ahrefs.com/blog/ai-overview-triggers/ (2025)
58. BrightEdge, one year of AIO — https://www.brightedge.com/news/press-releases/one-year-google-ai-overviews-brightedge-data-reveals-google-search-usage (2025-05-14)
59. SEL, BrightEdge clicks −30% — https://searchengineland.com/google-ai-overviews-search-clicks-fell-report-455498 (2025-05)
60. Press Gazette, Authoritas — https://pressgazette.co.uk/media-audience-and-business-data/google-ai-overviews-publishers-report-clickthroughs-authoritas-report/ (2025)
61. SERoundtable, Similarweb zero-click 56→69% — https://www.seroundtable.com/similarweb-google-zero-click-search-growth-39706.html (2025)
62. The College Investor, 37% inaccurate — https://thecollegeinvestor.com/66208/37-of-google-ai-finance-answers-are-inaccurate-in-2025/ (2025)
63. TaxCalcBench — https://arxiv.org/pdf/2507.16126 (2025-07)
64. The Finance Buff, AI tax test — https://thefinancebuff.com/ai-tax-calculator.html (2026)
65. TechCrunch, CMA opt-out — https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/ (2026-06-03)
66. MediaPost, Google opt-out — https://www.mediapost.com/publications/article/416681/google-gives-publishers-opt-out-for-ai.html (2026-07-21)
67. Digiday, opt-out dilemma — https://digiday.com/media/googles-ai-opt-out-leaves-publishers-with-a-choice-they-cant-safely-use/ (2026)
68. RTÉ, EPC complaint — https://www.rte.ie/news/business/2026/0210/1557746-google-ai-publishers/ (2026-02-10)
69. Digital Applied, AI Mode France — https://www.digitalapplied.com/blog/google-ai-mode-france-launch-eu-publishers-seo-2026 (2026)
70. Google, AIO in Europe — https://blog.google/feed/were-bringing-the-helpfulness-of-ai-overviews-to-more-countries-in-europe/ (2025-03)
71. 9to5Google, information agents — https://9to5google.com/2026/06/12/google-information-agents/ (2026-06-12)
72. OpenAI, personal finance in ChatGPT — https://openai.com/index/personal-finance-chatgpt/ (2026-06)
73. awesome-chatgpt-apps — https://github.com/rdmgator12/awesome-chatgpt-apps (2026-07)
74. Glama, CalcFleet take-home MCP — https://glama.ai/mcp/connectors/com.calcfleet/calculators/tools/take_home_pay_calculator (2026)
75. CalcFleet — https://calcfleet.com/ (2026)
76. TechnologyChecker, search referrals (Cloudflare Radar) — https://technologychecker.io/blog/search-engine-market-share (2026-09)
77. SE Ranking, ChatGPT referrals May 2026 — https://seranking.com/blog/chatgpt-referral-traffic-may-2026/ (2026-06)
78. getpanto, Perplexity statistics — https://www.getpanto.ai/blog/perplexity-ai-statistics (2026)
79. Digital Strategy Force, Perplexity publisher program — https://digitalstrategyforce.com/journal/perplexitys-2026-publisher-program-what-it-means-for-content-creators/ (2026)
80. SE Ranking, llms.txt — https://seranking.com/blog/llms-txt/ (2026)
81. Rankability, llms.txt adoption — https://www.rankability.com/data/llms-txt-adoption/ (2026-06)
82. Exploding Topics, thecalculatorsite.com — https://analytics.explodingtopics.com/website/thecalculatorsite.com (2026-08)
83. Exploding Topics, rapidtables.com — https://analytics.explodingtopics.com/website/rapidtables.com (2026-01)
84. Similarweb, rapidtables.com — https://www.similarweb.com/website/rapidtables.com/ (2026-08)
85. Semrush, unitconverters.net — https://www.semrush.com/website/unitconverters.net/overview/ (2026-07/08)
86. AhrefsTop, convertunits.com — https://ahrefstop.com/websites/convertunits.com (2026-07)
87. AhrefsTop, thesalarycalculator.co.uk — https://ahrefstop.com/websites/thesalarycalculator.co.uk (2026-04)
88. Similarweb, thesalarycalculator.co.uk — https://www.similarweb.com/website/thesalarycalculator.co.uk/ (2026-08)
89. Similarweb, listentotaxman.com — https://www.similarweb.com/website/listentotaxman.com/ (2026-04)
90. Similarweb, paycheckcity.com — https://www.similarweb.com/website/paycheckcity.com/ (2026-05)
91. Semrush, talent.com — https://www.semrush.com/website/talent.com/overview/ (2025-12)
92. Similarweb, smartasset.com — https://www.similarweb.com/website/smartasset.com/ (2025-09)
93. Similarweb, paycalculator.com.au — https://www.similarweb.com/website/paycalculator.com.au/ (2026-04)
94. Semrush, inchcalculator.com — https://www.semrush.com/website/inchcalculator.com/overview/ (2025-11 / 2026-05)
95. AhrefsTop, brutto-netto-rechner.info — https://ahrefstop.com/websites/brutto-netto-rechner.info (2026-09)
96. CrUX top-lists (кэш, повторный прогон 110 доменов) — https://github.com/zakird/crux-top-lists (данные 01.2025–08.2026; доступ 2026-09-26)
97. nhstakehome.co.uk — https://nhstakehome.co.uk/ (2026-09)
98. fairworkmate.com.au tools — https://fairworkmate.com.au/tools (2026)
99. Wikipedia, No tax on tips — https://en.wikipedia.org/wiki/No_tax_on_tips (2026)
100. H&R Block, OBBBA overtime — https://www.hrblock.com/tax-center/irs/tax-law-and-policy/one-big-beautiful-bill-no-tax-on-overtime/ (2025)
101. NoOvertimeTax — https://noovertimetax.com/ (2026)
102. MoneySavingExpert, salary sacrifice cap — https://www.moneysavingexpert.com/news/2025/11/salary-sacrifice-capped-national-insurance-budget/ (2025-11)
103. Flippa, 247 Calculator listing — https://flippa.com/12032211-728-peak-monthly-profit-25k-monthly-pageviews-100-margins-passive-calculator-site-earning-with-mediavine-primed-for-seo-growth (н/д)
104. Flippa, website valuation — https://flippa.com/blog/how-much-is-my-website-worth/ (2025)
105. X / Niche Pursuits, SleepCalculator — https://x.com/nichepursuits/status/1904573862244999235 (2025-03)
106. BoringCashCow, calculators — https://boringcashcow.com/view/online-calculators-generate-millions-a-year (н/д; данные 2023)
107. Adstimate, RPM by country — https://adstimate.com/blog/adsense-rpm-by-country.html (2026)
108. This Week in Blogging, Mediavine vs Raptive — https://thisweekinblogging.com/mediavine-vs-raptive/ (2026)
109. Medium/ILLUMINATION, AdSense rejections — https://medium.com/illumination/google-adsense-rejection-fixes-2026-get-approved-after-multiple-rejections-aab43931f654 (2026)
110. Cuelinks, Adobe affiliate — https://www.cuelinks.com/campaigns/adobe-affiliate-program (2026-08)
111. Adobe affiliates — https://www.adobe.com/affiliates.html (2026)
112. Symmetry, calculators — https://www.symmetry.com/calculators-by-symmetry (2026)
113. PayrollTaxAPI — https://payrolltaxapi.com/ (2026)
114. FederalPay widgets — https://www.federalpay.org/calculator-widgets (2026)
115. EmployerCost widget — https://employercost.com/widget (2026)
116. SEL, Chegg v. Google — https://searchengineland.com/google-sued-by-chegg-over-ai-overviews-hurting-traffic-and-revenue-452518 (2025-02)
117. ppc.land, Stack Overflow — https://ppc.land/stack-overflow-traffic-collapses-as-ai-tools-reshape-how-developers-code/ (2026)
118. BuzzStream, Forbes Advisor — https://www.buzzstream.com/blog/forbes-advisor-analysis/ (2025)
119. aescripts, Safest Zone — https://aescripts.com/safest-zone/ (2026)
120. aescripts, Unsafe Area Overlay — https://aescripts.com/unsafe-area-overlay/ (2026)
121. Adobe Community, safe zones idea — https://community.adobe.com/t5/after-effects-ideas/safezones-for-current-social-media-platforms-pleeeaaaaase/idi-p/15276849 (н/д)
122. Kreatli, safe zone hub — https://kreatli.com/guides/safe-zone-guide (2026)
123. Postplanify, safe zone checkers — https://postplanify.com/blog/social-media-safe-zones-2026-complete-guide (2026)
124. LED Wall Central — https://www.ledwallcentral.com/ (2026); ProjectorCentral launch — https://www.projectorcentral.com/LED-Wall-Central-launch.htm
125. Key Digital, LED calculator — https://www.keydigital.org/tools/led-video-wall-calculator (2026)
126. CometAPI, AI video pricing — https://www.cometapi.com/ai-video-api-pricing/ (2026)
127. FreeAIVideoHub, AI video cost calculator — https://www.freeaivideohub.com/ai-video-cost-calculator (2026)
128. NodeTool, AI video cost — https://nodetool.ai/blog/ai-video-generation-cost (2026)
129. Font license checkers: JustFreeFonts — https://justfreefonts.com/font-license-checker/ ; Lipi.ai — https://www.lipi.ai/copyright ; FontAlternatives — https://fontalternatives.com/licenses/ (2025–2026)
130. Sync fee calculators: SyncCalc — http://synccalc.com/ ; Music Oracle — https://musicoracle.app/ ; Tools 4 Music — https://tools4music.com/calculators/sync-licensing-fee (2026)
131. Render farm calculators: RebusFarm — https://rebusfarm.net/buy/calculator ; TurboRender AE — https://turborender.com/after-effects (2026)
132. Video storage calculators: Digital Rebellion — https://www.digitalrebellion.com/webapps/videocalc ; DataCalc — https://data-calc.com/ ; toolstud.io — https://toolstud.io/video/filesize.php (2026)
133. Freelance rate calculators: https://freelanceratecalculator.net/ ; https://freelanceratecalculator.org/ ; Upwork — https://www.upwork.com/tools/freelance-rate-calculator (2025–2026)
134. YunoJuno, motion graphics rates — https://www.yunojuno.com/freelancer-rates-job-role/motion-graphics (2026)
135. Creativepool, day rates 2026 — https://creativepool.com/magazine/industry/freelance-day-rates-in-2026-what-creative-talent-should-charge.34695 (2026)
136. AdQuick, billboard cost — https://www.adquick.com/billboard-cost (2026)
137. Vistar, creatives best practices — https://help.vistarmedia.com/hc/en-us/articles/360059687631-Creatives-Best-Practices (2026)
