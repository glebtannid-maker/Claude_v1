# Поток 11. Приложение «детский рисунок (+ фото ребёнка) → видео»: экономика, политики провайдеров, регуляторика

Дата: 2026-09-26. Автор: исследовательский поток 11 (deep dive, часть 2).

**Как читать метки достоверности.** В этой сессии сетевой доступ был сильно ограничен: WebFetch к большинству сайтов (openai.com, ai.google.dev, fal.ai, ftc.gov, ico.org.uk, stripe.com, printful.com и т.д.) заблокирован egress-прокси; лимит веб-поиска сессии исчерпан после ~30 запросов этого потока. Поэтому:
- **[П]** — факт подтверждён в этой сессии: результатом веб-поиска с указанным URL, открытой страницей (developer.apple.com), первичными файлами на GitHub (официальный Google Gen AI SDK, Gemini Cookbook, прайс-лист LiteLLM) или калькулятором стоимости Magnific API (simulate_cost, 2026-09-26).
- **[БЗ]** — факт из базы знаний модели (актуальность до ~06.2026), в сессии не перепроверен. URL даны канонические, но в сессии не открывались. Перед юридическими решениями эти пункты нужно перепроверить.
- «оценка» — расчёт/допущение, указаны допущения и уверенность.

---

## Ключевые факты

**Цены: изображения**
1. [П] OpenAI **gpt-image-2** (снапшот `gpt-image-2-2026-04-21`): 1024×1024 low $0.006, medium $0.053, high $0.211 за изображение; batch дешевле на 50% ([aifreeapi, проверено 2026-09-06](https://www.aifreeapi.com/en/posts/openai-image-generation-api-pricing); [LiteLLM price list, 2026-09-26](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json)). Для **edit** (с входным фото) на fal: medium 1024² $0.061, high $0.219 ([LiteLLM, fal-записи, 2026-09-26](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json)).
2. [П] **gpt-image-1.5**: low $0.009 / medium $0.034 / high $0.133 (1024²); 1024×1536: $0.013 / $0.05 / $0.20; дата вывода из эксплуатации в прайс-листе — **2026-12-01** ([pricepertoken, 2026](https://pricepertoken.com/gpt-image-pricing); [LiteLLM, 2026-09-26](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json)).
3. [П] Уже есть **gpt-image-2.5** (варианты flare/sunburst) на fal: edit 1024² medium $0.013, high $0.053, «max» $0.211 — это кратно дешевле gpt-image-2 при том же уровне качества ([LiteLLM, 2026-09-26](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json)); есть системная карта «ChatGPT Images 2.5» ([OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/chatgpt-images-2-5), 2026).
4. [П] Google **Nano Banana 2** (gemini-3.1-flash-image): 0.5K $0.045, 1K $0.067, 2K $0.101, 4K $0.151; batch −50% ([apiyi, 2026](https://help.apiyi.com/en/nano-banana-2-pricing-guide-official-google-api-en.html); LiteLLM: output_cost_per_image 0.0672). **Nano Banana 2 Lite** (gemini-3.1-flash-lite-image): $0.0336 за 1K ([pricepertoken, 2026](https://pricepertoken.com/image/model/google-gemini-3-1-flash-lite-image)). **Nano Banana Pro** (gemini-3-pro-image): $0.134 за 1K/2K, $0.24 за 4K ([laozhang, 2026](https://blog.laozhang.ai/en/posts/gemini-3-pro-image-api-pricing)).
5. [П] Оригинальный **Nano Banana** (gemini-2.5-flash-image, $0.039) отключается в Gemini API **2026-10-02**, в Vertex — 2027-03-15 ([digitalapplied, 2026](https://www.digitalapplied.com/blog/gemini-2-5-flash-image-retirement-october-2-api-vertex)).
6. [П] **Seedream 4.5** — $0.04/изобр. (BytePlus, fal); **Seedream 5.0 Lite** — $0.035; 5.0 Pro — ~$0.045–0.15 ([lumenfall](https://lumenfall.ai/models/bytedance/seedream-4.5/providers); [apiyi](https://help.apiyi.com/en/seedream-5-0-lite-api-guide-cheaper-than-4-5-en.html), 2026). **FLUX.2 Pro** — $0.03/Мп (проверено BFL 2026-07-31 по [flowith](https://flowith.io/blog/flux-2-pro-pricing-2026-dev-vs-pro-vs-schnell-api/)); **FLUX Kontext Pro/Max** — $0.04/$0.08 ([LiteLLM](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json)). **Qwen-Image-Edit-2511** — открытые веса (Apache 2.0), релиз 2025-12-23; на fal $0.03/Мп ([GitHub Qwen-Image](https://github.com/QwenLM/Qwen-Image); [fal](https://fal.ai/models/fal-ai/qwen-image-edit-2511)).

**Цены: видео**
7. [П] **Veo 3.1 Lite**: 720p $0.05/с с аудио, $0.03/с без; 1080p $0.08/с с аудио, $0.05/с без → 8 с 720p = $0.40 ([aivideobootcamp, 2026](https://aivideobootcamp.com/blog/veo-3-1-lite-google-cheap-ai-video-2026/); LiteLLM `veo-3.1-lite-generate-preview`: 0.05/0.08).
8. [П] **Veo 3.1 Fast**: 720p $0.10/с (с аудио), 1080p $0.12/с, 4K $0.30/с; без аудио от $0.08/с; **Veo 3.1** стандарт $0.40/с (1080p), $0.60/с (4K) ([aifreeapi, по ставкам Google на 2026-07-23](https://www.aifreeapi.com/en/posts/veo-3-1-pricing); LiteLLM).
9. [П] Падение цены: Veo 2 на Vertex стоил $0.50/с, Veo 3 на запуске — $0.75/с; Veo 3.1 Lite 720p без аудио — $0.03/с, т.е. **−93–94% менее чем за ~15 месяцев** (LiteLLM `veo-2.0-generate-001`; [aifreeapi](https://www.aifreeapi.com/en/posts/veo-3-1-pricing); расчёт).
10. [П] **Kling 3.0 Standard image-to-video на fal**: $0.084/с без аудио, $0.126/с с аудио, $0.154/с с voice control ([fal model page](https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video), 2026). Официальный гайд Kling 3.0: 6/8 кредитов/с без аудио (720p/1080p), 9/12 — с аудио ([renderful](https://renderful.ai/blog/kling-api-pricing); [kling.ai/dev/pricing](https://kling.ai/dev/pricing), 2026). Отсюда оценка 1080p без аудио ≈ $0.112/с, с аудио ≈ $0.168/с (оценка, средняя уверенность — пропорция к цене fal 720p).
11. [П] **Sora 2 API закрыт 2026-09-24** (объявлено 2026-03-24; приложение Sora закрыто 2026-04-26); эндпоинты sora-2/sora-2-pro возвращают 410 ([OpenAI Help Center](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation); [unifically](https://unifically.com/blogs/sora-api), 2026). Цена до закрытия: $0.10/с (sora-2 720p), $0.30–0.50/с (pro).
12. [П] **Seedance 2.0** (fal): 480p $0.135/с, 720p $0.303/с, 1080p $0.682/с; **Seedance 2.0 Mini** ~$0.08/с 720p (BytePlus); **Seedance 2.5** на fal: 720p $0.473/с (LiteLLM; [nxcode](https://www.nxcode.io/resources/news/seedance-2-0-api-guide-pricing-setup-2026), 2026).
13. [П] **Hailuo 2.3** (MiniMax): 768p 6 с ≈ $0.28 pay-as-you-go, Fast — от $0.19 за генерацию ([magichour](https://magichour.ai/blog/hailuo-23-pricing); [MiniMax docs](https://platform.minimax.io/docs/guides/pricing-video), 2026). **MiniMax H3** на fal: 480p $0.05/с, 768p $0.06/с (LiteLLM, 2026-09-26).
14. [П] **Wan 2.6** i2v на fal: 720p $0.10/с, 1080p $0.15/с ([fal](https://fal.ai/models/wan/v2.6/image-to-video), 2026). Wan 2.1/2.2 — открытые веса Apache 2.0; 5B-модель Wan2.2 делает 720p@24fps на потребительской RTX 4090 ([GitHub Wan2.2](https://github.com/Wan-Video/Wan2.2), 2026-09-26).
15. [П] **Runway API**: $0.01/кредит; Gen-4 Turbo 5 кр/с ($0.05/с), Gen-4.5 12 кр/с ($0.12/с); Runway также перепродаёт Seedance 2 ($0.36/с), Hailuo 3 ($0.10/с), Veo 3.1 Fast ($0.15/с) ([Runway API pricing](https://docs.dev.runwayml.com/guides/pricing/); LiteLLM `runwayml/*`, 2026-09-26).
16. [П] **Luma**: Ray Flash 2 ≈ $0.06/с (5 с = $0.30); Ray 2 ≈ $0.08/с; Ray3.2 5 с 1080p SDR ≈ $1.20 через Agents API (с 06.2026) ([mindstudio](https://www.mindstudio.ai/blog/what-is-luma-ray-flash-2-video); [magichour](https://magichour.ai/blog/luma-dream-machine-pricing), 2026).
17. [П] **Magnific (бывш. Freepik, ребренд 2026-04-28)**: апскейлер изображений €0.10–1.20/изобр. (4× ≈ €0.20); Kling через Freepik API €0.25–0.84/клип ([vantaige](https://vantaige.io/blog/freepik-ai-is-now-magnific-pricing-changes-2026); [Freepik API](https://www.freepik.com/api/image-upscaler), 2026). Калькулятор Magnific (simulate_cost, 2026-09-26): Kling 3.0 5 с 720p = 350 кр.; Veo 3.1 Lite 8 с 720p = 320 кр.; Veo 3.1 Fast 8 с 720p = 800 кр.; Hailuo 2.3 Fast 6 с 768p = 150 кр.; Seedance 2.0 Mini 5 с = 700 кр.; Wan 2.6 5 с = 1000 кр.; **видео-апскейл Magnific 5 с ≈ 2297 кр.** (при $0.80 за Veo Fast 8 с ≈ $0.001/кредит — прокси, низкая уверенность). Вывод: видео-апскейл дороже самой генерации — генерировать сразу в целевом разрешении.

**Политики провайдеров по несовершеннолетним**
18. [П] **OpenAI**: при запуске нативной генерации изображений GPT-4o (системная карта от 2025-03-25) — «editing uploaded images of photorealistic children will not be allowed»; на каждое загруженное фото работает классификатор [child|adult] × [photorealistic|non-photorealistic], настроенный «в сторону осторожности» (пограничные случаи = ребёнок) ([System Card Addendum PDF](https://cdn.openai.com/11998be9-5319-4302-bfbf-1167e093f1fb/Native_Image_Generation_System_Card.pdf); [TechCrunch 2025-03-28](https://techcrunch.com/2025/03/28/openai-peels-back-chatgpts-safeguards-around-image-creation/)). Публичного снятия этого ограничения в найденных источниках нет; разработчики жалуются на блокировки детских фото и на over-refusals gpt-image-2 даже при `moderation: low` ([OpenAI community](https://community.openai.com/t/why-on-earth-do-we-prevent-the-use-of-child-images-in-an-unconditionally-safe-environment-and-force-unrealistic-characters/1107729); [thread 2026](https://community.openai.com/t/api-issue-moderation-over-refusals-on-gpt-image-2-with-moderation-low-where-chatgpt-always-succeeds/1388964)).
19. [П] **Google Veo**: в официальном Google Gen AI SDK (`GenerateVideosConfig.person_generation`) поддерживаемые значения для видео — только `dont_allow`, `allow_adult`; в официальном Gemini Cookbook: «Children are always blocked» ([python-genai types.py](https://raw.githubusercontent.com/googleapis/python-genai/main/google/genai/types.py); [Get_started_Veo.ipynb](https://raw.githubusercontent.com/google-gemini/cookbook/main/quickstarts/Get_started_Veo.ipynb), оба прочитаны 2026-09-26). Значение `allow_all` («adults and children») существует в enum, но на Vertex требует allowlist проекта; в регионах **EU, UK, CH, MENA** разрешено только `allow_adult` ([Vertex Veo API reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation), по результату поиска 2026-09; [forum](https://discuss.google.dev/t/request-allowlist-access-for-veo-3-1-person-generation-reference-to-video/398998)).
20. [П] **ByteDance Seedance 2.0** после перезапуска отклоняет входные изображения/видео с **реальными человеческими лицами** на уровне input-фильтра (после претензий Disney и студий) ([Phemex News](https://phemex.com/news/article/bytedance-relaunches-seedance-20-globally-with-restrictions-on-realface-uploads-68605); [MindStudio](https://www.mindstudio.ai/blog/seedance-2-0-content-restrictions-workarounds), 2026). Для фото ребёнка — непригоден; для рисунка — пригоден.
21. [П] **Adobe Firefly**: в ответах сообщества/модераторов — «You can't currently use this tool to edit images of children, under any circumstances» ([Adobe Community](https://community.adobe.com/t5/adobe-firefly-discussions/not-sure-why-my-images-quot-violate-guidelines-quot-image-depicts-children/m-p/15200515/page/2), 2025). Средняя уверенность (форум, не ToS).

**Магазины приложений**
22. [П] Apple 5.1.2(i): «You must clearly disclose where personal data will be shared with third parties, including with **third-party AI**, and obtain explicit permission before doing so». 1.2 (UGC): фильтрация, механизм жалоб, блокировка пользователей, опубликованные контакты. 5.1.1: объяснить политику хранения/удаления и как отозвать согласие ([App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), прочитано 2026-09-26).
23. [П] Apple Kids Category: возрастные группы 5 и младше / 6–8 / 9–11; запрет передачи PII/device info третьим лицам «даже в разделах для взрослых» без явного согласия родителя; сторонняя аналитика/реклама — нет (кроме узких исключений); parental gate ≠ согласие по COPPA. Новые возрастные рейтинги: 4+, 9+, **13+, 16+, 18+**; Declared Age Range API и PermissionKit/SignificantChange для законов об age assurance ([developer.apple.com/kids](https://developer.apple.com/kids/); [age assurance](https://developer.apple.com/support/age-assurance/), 2026-09-26).
24. [П] Apple Small Business Program: комиссия **15%** при выручке ≤ $1 млн/год; в US storefront разрешены внешние ссылки/кнопки на покупку на своём сайте без entitlement (3.1.1(a)) ([Apple SBP](https://developer.apple.com/app-store/small-business-program/); [Guidelines](https://developer.apple.com/app-store/review/guidelines/), 2026-09-26).
25. [БЗ] Google Play **AI-Generated Content policy**: приложения-генераторы обязаны иметь внутри приложения механизм жалобы/пометки оскорбительного AI-контента без выхода из приложения; запрет контента, эксплуатирующего детей ([Play policy](https://support.google.com/googleplay/android-developer/answer/13985936), 2024–2026). Families policy: приложения для детей — только сертифицированные рекламные SDK, запрет ряда идентификаторов ([Families](https://support.google.com/googleplay/android-developer/answer/9893335)).

**Регуляторика**
26. [БЗ] **COPPA (поправки 2025)**: финальное правило опубликовано в Federal Register 2025-04-22, вступило в силу 2025-06-23, срок соответствия — **2026-04-22**. Новое: отдельное VPC на раскрытие данных третьим лицам (реклама и т.п.), письменная политика хранения (без бессрочного хранения), письменная программа безопасности, **биометрические идентификаторы** (в т.ч. «faceprints»/шаблоны лица) включены в «personal information»; новые методы VPC — knowledge-based authentication, сверка лица с фото госдокумента, «text plus» ([FTC press release 2025-01-16](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data); [Federal Register](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule)). Фото/видео с изображением ребёнка являются «personal information» с 2013 г.
27. [БЗ] COPPA применяется к данным, собранным **от ребёнка** (<13) сервисом, направленным на детей, или при фактическом знании; данные о ребёнке, собранные **от родителя**, по FAQ FTC под COPPA не подпадают — но оценка «направленности на детей» идёт по множеству факторов (тематика, мультяшная графика, персонажи, реклама), поэтому «детская» эстетика приложения создаёт риск статуса mixed audience ([FTC COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions)).
28. [БЗ] **GDPR**: ст. 8 — согласие ребёнка на ISS с 16 лет (страны могут снизить до 13; UK GDPR — 13); ст. 4(14)/9 + Recital 51 — фото является биометрией (особая категория) **только** при обработке спец. техническими средствами для уникальной идентификации; простая генерация по фото — обычные персональные данные, но детские данные + новая технология → DPIA ([Art. 8](https://gdpr-info.eu/art-8-gdpr/); [Art. 9](https://gdpr-info.eu/art-9-gdpr/); [Recital 51](https://gdpr-info.eu/recitals/no-51/)).
29. [БЗ] **UK Age Appropriate Design Code** (15 стандартов) применяется к онлайн-сервисам, которые «likely to be accessed by children» (<18), — не только к «детским» ([ICO Children's code](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/)).
30. [БЗ] **18 U.S.C. §2258A**: провайдеры ECS/RCS обязаны сообщать о явном CSAM в CyberTipline NCMEC при фактическом знании; REPORT Act (2024) продлил обязательное хранение сообщённого материала до 1 года. **TAKE IT DOWN Act** (подписан 2025-05-19): уголовная ответственность за публикацию NCII, включая AI-дипфейки; платформы с UGC обязаны иметь процедуру удаления за 48 ч (срок внедрения — 2026-05-19) ([18 USC 2258A](https://www.law.cornell.edu/uscode/text/18/2258A); [S.146](https://www.congress.gov/bill/119th-congress/senate-bill/146)).
31. [БЗ] **EU AI Act ст. 50** (прозрачность: маркировка синтетического контента машиночитаемо, раскрытие дипфейков) применяется с **2026-08-02**; в рамках «digital omnibus» обсуждались отсрочки части требований — статус в сессии не проверен ([Art. 50](https://artificialintelligenceact.eu/article/50/)).
32. [БЗ] Инструменты против CSAM: Thorn **Safer** (хэш-матчинг + классификатор нового CSAM), Microsoft **PhotoDNA** (бесплатно для квалифицированных организаций), **Cloudflare CSAM Scanning Tool** (бесплатно для клиентов Cloudflare, фаззи-хэши NCMEC), **Hive** (модерация, в т.ч. CSAM-детекция совместно с Thorn), Google **Content Safety API** ([safer.io](https://safer.io/); [PhotoDNA](https://www.microsoft.com/en-us/photodna); [Cloudflare](https://developers.cloudflare.com/cache/reference/csam-scanning/)).

**Платежи и инфраструктура**
33. [БЗ] Stripe (US-стандарт): 2.9% + $0.30; для UK-юрлица международные карты дороже (порядка 3.25% + 20p) + ~2% за конвертацию валюты — оценка, проверить на [stripe.com/gb/pricing](https://stripe.com/gb/pricing). Paddle (Merchant of Record, берёт на себя VAT/sales tax): 5% + $0.50 ([paddle.com/pricing](https://www.paddle.com/pricing)). Google Play: 15% на первый $1 млн/год и на подписки.
34. [БЗ] Cloudflare R2: хранение ~$0.015/ГБ-мес, **без платы за исходящий трафик** ([R2 pricing](https://developers.cloudflare.com/r2/pricing/)). 10-секундный ролик 1080p ≈ 8–15 МБ → хранение/доставка < $0.001 за ролик (оценка, высокая уверенность в порядке величины).
35. [П] Альтернатива «без фото и без генеративного видео»: **Meta Animated Drawings** — открытый код (MIT) алгоритма анимации детских рисунков человеческих фигур (ACM TOG 2023) ([GitHub](https://github.com/facebookresearch/AnimatedDrawings), прочитано 2026-09-26). Себестоимость — только CPU/GPU-хостинг; нет провайдерских отказов.
36. [П] Спрос-сигнал: вирусный тренд «превратить детские каракули в реалистичные изображения через ChatGPT» ([Tom's Guide](https://www.tomsguide.com/ai/i-turned-my-kids-art-into-lifelike-images-using-chatgpt-heres-how-you-can-too), 2025) — массовый пользователь уже делает это бесплатно в ChatGPT; платить будет за видео/анимацию, физический сувенир или готовый «ритуал» (оценка).

---

## Цены моделей

Цены — за единицу через официальный API или агрегатор; «с»=секунда видео. Даты — дата проверки/публикации источника.

### Изображения (композит «ребёнок + рисунок», стилизация рисунка)

| Модель | Канал | Цена | Дата | Источник | Замечание по детям |
|---|---|---|---|---|---|
| gpt-image-2 (2026-04-21) | OpenAI / fal | low $0.006, med $0.053, high $0.211 (1024², генерация); edit med $0.061, high $0.219 | 2026-09 | [aifreeapi](https://www.aifreeapi.com/en/posts/openai-image-generation-api-pricing), [LiteLLM](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json) | Редактирование фотореалистичных детей запрещено (с 2025-03) |
| gpt-image-2.5 (flare/sunburst) | fal | edit 1024²: med $0.013, high $0.053, xhigh $0.094, max $0.211 | 2026-09-26 | LiteLLM | То же семейство; снятие ограничения не найдено |
| gpt-image-1.5 | OpenAI | $0.009 / $0.034 / $0.133 (1024²) | 2026 | [pricepertoken](https://pricepertoken.com/gpt-image-pricing) | Депрекация 2026-12-01 |
| gpt-image-1-mini | OpenAI | low $0.005, med $0.011 (1024²) | 2026-09-26 | LiteLLM | Депрекация 2026-12-01 |
| Nano Banana 2 Lite (3.1 flash-lite image) | Gemini API | $0.0336 / 1K | 2026 | [pricepertoken](https://pricepertoken.com/image/model/google-gemini-3-1-flash-lite-image) | Есть параметр person_generation (ALLOW_ALL/ADULT/NONE) в SDK; поведение на реальных детях — нет данных |
| Nano Banana 2 (3.1 flash image) | Gemini API | 0.5K $0.045, 1K $0.067, 2K $0.101, 4K $0.151; batch −50% | 2026 | [apiyi](https://help.apiyi.com/en/nano-banana-2-pricing-guide-official-google-api-en.html) | как выше |
| Nano Banana 2 | fal | 1K $0.08, 2K $0.12, 4K $0.16 | 2026-09-26 | LiteLLM | наценка агрегатора ~+20% |
| Nano Banana Pro (3 pro image) | Gemini API | 1K/2K $0.134, 4K $0.24 | 2026 | [laozhang](https://blog.laozhang.ai/en/posts/gemini-3-pro-image-api-pricing) | как выше |
| Nano Banana (2.5 flash image) | Gemini API | $0.039 | 2026 | [digitalapplied](https://www.digitalapplied.com/blog/gemini-2-5-flash-image-retirement-october-2-api-vertex) | Отключение 2026-10-02 |
| Seedream 4.5 / 5.0 Lite / 5.0 Pro | BytePlus, fal | $0.04 / $0.035 / ~$0.045–0.15 | 2026 | [lumenfall](https://lumenfall.ai/models/bytedance/seedream-4.5/providers), [apiyi](https://help.apiyi.com/en/seedream-5-0-lite-api-guide-cheaper-than-4-5-en.html) | Политика по реальным лицам для Seedream — нет данных |
| FLUX.2 Pro | BFL | $0.03/Мп | 2026-07-31 | [flowith](https://flowith.io/blog/flux-2-pro-pricing-2026-dev-vs-pro-vs-schnell-api/) | нет данных |
| FLUX.1 Kontext Pro / Max | BFL | $0.04 / $0.08 | 2026-09-26 | LiteLLM | нет данных |
| Qwen-Image-Edit-2511 | открытые веса / fal | Apache 2.0; fal $0.03/Мп | 2025-12-23 / 2026 | [GitHub](https://github.com/QwenLM/Qwen-Image), [fal](https://fal.ai/models/fal-ai/qwen-image-edit-2511) | При self-host отказов провайдера нет, но вся ответственность на вас |
| Magnific upscaler (изобр.) | Magnific API | €0.10–1.20; 4× ≈ €0.20 | 2026 | [vantaige](https://vantaige.io/blog/freepik-ai-is-now-magnific-pricing-changes-2026) | — |

### Видео (image-to-video, 5–10 с)

| Модель | Канал | 720p (за с) | 1080p (за с) | 5 с / 10 с при 720p | Источник, дата | Дети на входе |
|---|---|---|---|---|---|---|
| Veo 3.1 Lite | Gemini/Vertex | $0.05 (аудио) / $0.03 (без) | $0.08 / $0.05 | 8 с = $0.40 (с аудио), $0.24 (без) | [aivideobootcamp](https://aivideobootcamp.com/blog/veo-3-1-lite-google-cheap-ai-video-2026/), LiteLLM, 2026 | Нет: «Children are always blocked»; EU/UK/CH/MENA — только allow_adult |
| Veo 3.1 Fast | Gemini/Vertex | $0.10 (аудио), $0.08 (без) | $0.12 | 8 с = $0.80 | [aifreeapi](https://www.aifreeapi.com/en/posts/veo-3-1-pricing), 2026-07-23 | как выше |
| Veo 3.1 | Gemini/Vertex | — | $0.40 (4K $0.60) | 8 с = $3.20 | LiteLLM | как выше |
| Kling 3.0 Std | fal | $0.084 (без аудио), $0.126 (аудио) | ~$0.112 / ~$0.168 (оценка) | $0.42 / $0.84 | [fal](https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video), 2026 | Явного запрета в найденных источниках нет — нет данных, нужен тест |
| Kling 3.0 | Magnific | 350 кр. / 5 с | — | ≈$0.35 (прокси) | simulate_cost, 2026-09-26 | как выше |
| Hailuo 2.3 / 2.3 Fast | MiniMax | 768p 6 с ≈ $0.28 / от $0.19 | 1080p 6 с = 2 «video points» | — | [magichour](https://magichour.ai/blog/hailuo-23-pricing), [MiniMax](https://platform.minimax.io/docs/guides/pricing-video) | нет данных |
| MiniMax H3 | fal | 768p $0.06, 480p $0.05 | 2K $0.13 | 6 с 768p = $0.36 | LiteLLM, 2026-09-26 | нет данных |
| Seedance 2.0 | fal | $0.303 | $0.682 | $1.52 / $3.03 | LiteLLM, [nxcode](https://www.nxcode.io/resources/news/seedance-2-0-api-guide-pricing-setup-2026) | Нет: блок реальных лиц |
| Seedance 2.0 Mini | BytePlus | ~$0.08 | — | ~$0.40 / $0.80 | nxcode, 2026 | Нет (реальные лица); рисунок — да |
| Wan 2.6 | fal | $0.10 | $0.15 | $0.50 / $1.00 | [fal](https://fal.ai/models/wan/v2.6/image-to-video) | Открытые веса Wan 2.x — политика ваша |
| Runway Gen-4 Turbo / Gen-4.5 | Runway API | $0.05 / $0.12 | — | $0.25 / $0.60 (5 с) | [Runway](https://docs.dev.runwayml.com/guides/pricing/) | нет данных |
| Luma Ray Flash 2 / Ray 2 | Luma API | ~$0.06 / ~$0.08 | Ray3.2 1080p 5 с ≈ $1.20 | $0.30 (5 с Flash) | [mindstudio](https://www.mindstudio.ai/blog/what-is-luma-ray-flash-2-video), 2026 | нет данных |
| Sora 2 / 2 Pro | OpenAI | $0.10 / $0.30–0.50 | — | — | [OpenAI Help](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation) | **Закрыт 2026-09-24** |
| Видео-апскейл Magnific | Magnific | ~2297 кр. / 5 с (≈$2.3, прокси) | — | — | simulate_cost, 2026-09-26 | Экономически не нужен |

Вывод по ценам: базовый 5–8-секундный клип 720p стоит **$0.19–0.45** на дешёвых моделях (Hailuo Fast, Veo Lite, Kling Std без аудио, Runway Turbo, Luma Flash), 10 с 1080p с аудио — **$1–3.5**. Изображение-композит — **$0.01–0.22**. Главная статья затрат — видео и его перегенерации.

---

## Политики провайдеров по несовершеннолетним

Матрица: можно ли подать на вход **фото реального ребёнка**? Отдельно — рисунок ребёнка (без лица): у всех провайдеров допустим как обычный контент.

| Провайдер / модель | Фото реального ребёнка на входе | Ограничения | Хранение (retention) | Обучение на входах | Источник / уверенность |
|---|---|---|---|---|---|
| OpenAI gpt-image-1/1.5/2/2.5 (API и ChatGPT) | **Нет** (редактирование фотореалистичных детей запрещено; классификатор на каждое фото, «при сомнении — ребёнок») | Недетское/стилизованное входное изображение допустимо; `moderation: low` не снимает запрет | [БЗ] до 30 дней для abuse monitoring; ZDR — по одобрению, применимость к images — нет данных | [БЗ] API-данные не используются для обучения по умолчанию | [П] [System Card 2025-03-25](https://cdn.openai.com/11998be9-5319-4302-bfbf-1167e093f1fb/Native_Image_Generation_System_Card.pdf); высокая для 2025, средняя для 09.2026 |
| OpenAI Sora 2 API | — | Закрыт 2026-09-24 | Данные удаляются после закрытия | — | [П] [OpenAI Help](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation) |
| Google Veo 3.x (Gemini API) | **Нет** | `person_generation`: только `dont_allow`/`allow_adult` для видео; «Children are always blocked» | [БЗ] платный уровень: логи для abuse monitoring ограниченный срок; бесплатный уровень — используется для улучшения | [БЗ] платный уровень — нет | [П] SDK + Cookbook, 2026-09-26; высокая |
| Google Veo (Vertex AI) | Только с `allow_all` по **allowlist**; в EU/UK/CH/MENA — нет | Enum `ALLOW_ALL` = «adults and children» | [БЗ] без обучения; ZDR возможен по запросу | [БЗ] нет | [П] поиск по Vertex docs 2026-09; средняя |
| Google Nano Banana / 2 / Pro | **Нет данных** (в SDK есть `person_generation` ALLOW_ALL/ALLOW_ADULT/ALLOW_NONE для ImageConfig) | Дефолт и поведение на реальных детях не проверены | как Gemini API | как Gemini API | [П] SDK types.py; низкая по поведению |
| ByteDance Seedance 2.x | **Нет** (блок любых реальных лиц) | Разрешены AI-портреты/иллюстрации | нет данных | нет данных | [П] [Phemex](https://phemex.com/news/article/bytedance-relaunches-seedance-20-globally-with-restrictions-on-realface-uploads-68605); высокая |
| ByteDance Seedream | нет данных | — | нет данных | нет данных | — |
| Kuaishou Kling 2.x/3.x | **Нет данных**; явный запрет в найденных источниках не обнаружен | Общие запреты на вред детям — [БЗ] | нет данных | нет данных | Требуется тест + чтение ToS |
| MiniMax Hailuo / H3 | нет данных | Есть отдельная модель «Live Illustrations» для анимации иллюстраций (каталог Magnific) | нет данных | нет данных | [П] каталог Magnific 2026-09-26 |
| Runway | нет данных | [БЗ] модерация публичных лиц | нет данных | нет данных | — |
| Luma | нет данных | — | нет данных | нет данных | — |
| Magnific/Freepik API | нет данных (перепродаёт модели выше — наследует их фильтры) | — | нет данных | нет данных | — |
| Adobe Firefly | **Нет** (редактирование детей «under any circumstances») | — | [БЗ] Adobe не обучает на контенте пользователей | — | [П] Adobe Community; средняя |
| fal.ai / Replicate (агрегаторы) | Наследуют фильтры исходной модели; для open-weights есть `enable_safety_checker` | [БЗ] AUP запрещает CSAM | [БЗ] результаты хранятся на CDN агрегатора, срок — нет данных | [БЗ] заявляют «не обучаем» | низкая |
| Open weights (Wan 2.x, Qwen-Image-Edit, Animated Drawings) | Технически да | Ответственность за модерацию целиком на вас | Ваша политика | Нет | [П] лицензии Apache 2.0 / MIT |

**Главный вывод (оценка, высокая уверенность):** все «западные» первоклассные провайдеры (OpenAI, Google Veo, Adobe) и ByteDance Seedance **не принимают фото реальных детей**; остаются Kling/MiniMax/Runway/Luma с неизвестной политикой (может ужесточиться в любой момент после инцидента) и open weights (self-host = вы сами «провайдер» с полной ответственностью). Продукт, чья ценность держится на фото ребёнка, строится на «серой» зависимости. Продукт, где на вход идёт **рисунок** (и, опционально, стилизованный аватар), совместим со всеми провайдерами, включая самые дешёвые и качественные.

---

## Модель себестоимости ролика

Допущения: перегенерации из-за дефектов (анатомия, «уплывший» стиль, артефакты) — **оценка 30–50%**, т.к. публичных данных о доле брака нет; множители попыток 1.3 / 1.5 / 1.7. Автоматический QA-скрининг кадров дешёвой VLM ~$0.001–0.003 за проверку (оценка, средняя). Модерация входа: хэш-матчинг (бесплатно через Cloudflare/PhotoDNA) + классификатор наготы ~$0.001–0.003 (оценка). Музыка — из лицензированной библиотеки (фикс. подписка), в переменных затратах ~0. Хранение/CDN (R2) < $0.001.

| Шаг | LOW (6 с, 720–768p, без аудио) | MID (10 с, 720p, без аудио) | HIGH (2 шота × 8 с, 1080p, аудио) |
|---|---|---|---|
| 1. Композит/стилизация | Nano Banana 2 Lite $0.034 × 1.3 = **$0.044** | Nano Banana 2 1K $0.067 × 1.5 = **$0.10** | Nano Banana Pro $0.134 × 2 кадра × 1.5 = **$0.40** |
| 2. Видео | Hailuo 2.3 Fast 6 с ≈ $0.19 × 1.5 = **$0.285** (альтернатива для рисунка: Veo 3.1 Lite 6 с без аудио $0.18) | Kling 3.0 Std 10 с $0.84 × 1.5 = **$1.26** (альт.: Veo 3.1 Fast 8 с $0.80 — только рисунок) | Kling 3.0 1080p+аудио ≈$0.168/с × 16 с × 1.7 = **$4.57** (для рисунка: Veo 3.1 Fast 1080p $0.12 × 16 × 1.7 = $3.26) |
| 3. QA + модерация | $0.01 | $0.015 | $0.03 |
| 4. Апскейл | нет | нет | нет (Magnific 5 с ≈ $2.3 — невыгодно) |
| 5. Хранение, CDN, музыка | $0.005 | $0.005 | $0.01 |
| **Себестоимость доставленного ролика** | **≈ $0.34** | **≈ $1.38** | **≈ $5.0** (Kling) / **≈ $3.7** (Veo, только рисунок) |

Чувствительность (оценка): если брак 50% вместо 33% на MID, видео-строка растёт с $1.26 до $1.68 (+$0.42); переход с Kling 3.0 на Veo 3.1 Lite 1080p без аудио (рисунок) снижает MID до ≈ $0.9. Цена видео падает быстро (п. 9 фактов: −93% за ~15 мес.), поэтому к 2027 MID-качество, вероятно, будет стоить сегодняшний LOW (оценка, средняя уверенность).

---

## Маржа по моделям оплаты

Расчёт: вклад = цена − комиссия канала − себестоимость × число роликов. НДС не учтён (для US-покупателей в большинстве штатов цифровые товары облагаются иначе; в UK цена $4.99 с НДС 20% = $4.16 нетто, в DE 19% = $4.19 — минус ~17% к выручке). Комиссии: App Store 15% (Small Business) / 30%; Stripe US 2.9% + $0.30 (ориентир); Stripe UK-юрлицо + иностранная карта ≈ 5.25% + $0.27 (оценка, с конвертацией); Paddle 5% + $0.50.

| Модель оплаты | Себест. | App Store 15% | App Store 30% | Stripe US | Stripe UK intl (оценка) | Paddle |
|---|---|---|---|---|---|---|
| Разовая $4.99, LOW | $0.34 | $3.90 (78%) | $3.15 (63%) | $4.20 (84%) | $4.11 (82%) | $3.90 (78%) |
| Разовая $4.99, MID | $1.38 | $2.86 (57%) | $2.11 (42%) | $3.17 (63%) | $3.08 (62%) | $2.86 (57%) |
| Разовая $9.99, MID | $1.38 | $7.11 (71%) | $5.61 (56%) | $8.02 (80%) | $7.82 (78%) | $7.61 (76%) |
| Разовая $9.99, HIGH | $5.01 | $3.48 (35%) | $1.98 (20%) | $4.39 (44%) | $4.19 (42%) | $3.98 (40%) |
| Разовая $14.99, HIGH | $5.01 | $7.73 (52%) | $5.48 (37%) | $9.25 (62%) | $8.92 (60%) | $8.73 (58%) |
| 3-pack $12.99, MID (все 3 использованы) | $4.14 | $6.90 (53%) | $4.95 (38%) | $8.17 (63%) | $7.90 (61%) | $7.70 (59%) |
| 5-pack $19.99, MID (все 5) | $6.90 | $10.09 (50%) | $7.09 (35%) | $12.21 (61%) | $11.77 (59%) | $11.59 (58%) |
| 5-pack $19.99, MID (использовано 80%) | $5.52 | $11.47 (57%) | $8.47 (42%) | $13.59 (68%) | $13.15 (66%) | $12.97 (65%) |
| Подписка $7.99/мес, 3 MID | $4.14 | $2.65 (33%) | $1.45 (18%) | $3.32 (42%) | $3.16 (40%) | $2.95 (37%) |
| Подписка $7.99/мес, лимит 5 MID выбран | $6.90 | −$0.11 (−1%) | −$1.31 | $0.56 (7%) | $0.40 | $0.19 |
| Подписка $7.99/мес, 5 LOW | $1.72 | $5.07 (63%) | $3.87 (48%) | $5.74 (72%) | $5.58 (70%) | $5.37 (67%) |
| B2B: группа 25 детей, $149, LOW | $8.60 | — | — | $135.78 (91%) | $132.31 (89%) | $132.45 (89%) |
| B2B: группа 25 детей, $149, MID | $34.50 | — | — | $109.88 (74%) | $106.41 (71%) | $106.55 (72%) |
| B2B: группа 25 детей, $99, LOW | $8.60 | — | — | $87.23 (88%) | $84.93 (86%) | $84.95 (86%) |

Выводы:
- **Разовые покупки и паки** на LOW/MID дают 50–80% валовой маржи в любом канале. HIGH-качество окупается только от ~$14.99.
- **Подписка опасна** при «щедрых» лимитах: 5 MID-роликов в месяц за $7.99 уходят в ноль. Если подписка — то с кредитами (1 кредит = LOW, 3 кредита = MID/HIGH) и неиспользуемые кредиты сгорают.
- **B2B-пакет на группу детсада** — лучшая юнит-экономика (себестоимость 6–25% от чека) и одна транзакция на 25 роликов; но нужен канал продаж (фотографы детсадов, сети, родительские комитеты) — это и есть «моат».
- Решающая переменная — не себестоимость генерации, а **CAC** потребительского приложения; при чеке $4.99–9.99 и валовой марже $3–8 платный трафик окупается только при повторных покупках (оценка).

---

## Регуляторика и чек-лист

### Классификация продукта (оценка, средняя уверенность)
- **Приложение для родителей** (аккаунт только 18+, оплата картой/App Store, взрослый тон маркетинга): данные о ребёнке собираются **от родителя** → COPPA формально не применяется [БЗ, FTC FAQ], но действуют GDPR/UK GDPR, AADC (если сервис «вероятно используется детьми»), законы штатов о приватности/биометрии, раздел 5 FTC Act (недобросовестные практики).
- **Mixed audience** (ребёнок может сам рисовать/нажимать в приложении): нужен нейтральный age gate; для <13 — либо блок, либо VPC до сбора любых данных, включая фото/рисунки/голос (Apple прямо перечисляет «photos, videos, drawings» как данные ребёнка — [5.1.4](https://developer.apple.com/app-store/review/guidelines/)).
- **Kids Category / приложение для детей**: запрет сторонней аналитики и рекламы, запрет передачи данных третьим лицам без явного согласия родителя [П]; а генеративный провайдер — это третья сторона → практически несовместимо с облачной генерацией. **Не идти в Kids Category.**

### Методы VPC (если всё же нужен сбор от ребёнка) [БЗ]
Подписанная форма (скан), кредитная карта в связке с денежной транзакцией, звонок/видеозвонок с обученным персоналом, сверка госдокумента, knowledge-based authentication (2025), сверка лица с фото документа (2025), «text plus» (2025); «email plus» — только для внутреннего использования без раскрытия третьим лицам. Облачная генерация = раскрытие третьим лицам → «email plus» не подходит.

### GDPR / UK
- Правовое основание: договор с родителем + явное согласие родителя на обработку фото ребёнка и передачу AI-провайдеру (совпадает с требованием Apple 5.1.2(i) [П]).
- Не делать face-embedding/распознавание (InstantID, FaceID-адаптеры) — иначе обработка может стать биометрической (ст. 9, «технические средства для уникальной идентификации»), а в Иллинойсе — попасть под BIPA [БЗ].
- DPIA обязательна де-факто (дети + новые технологии + передача вне ЕЭЗ, в т.ч. потенциально в Китай при Kling/MiniMax).
- Международные передачи: SCC/DPA с каждым провайдером; для китайских провайдеров — отдельная оценка рисков передачи (оценка: главный юридический и репутационный риск для «фото ребёнка»).

### Хранение и удаление (лучшая практика)
- Исходное фото ребёнка: удалить сразу после успешной генерации (≤1 ч), максимум 24 ч; рисунок — 72 ч, если не нужен физический продукт.
- Готовое видео: ссылка живёт 72 ч – 7 дней, затем удаление; сохранение дольше — только по явному действию родителя.
- Логи — без изображений; хранить хэши и метаданные модерации.
- Исключение: материал, заблокированный как вероятный CSAM, — не удалять, а изолировать и сообщить (NCMEC/IWF/полиция), хранить по требованию закона (REPORT Act — 1 год для отчётов в NCMEC) [БЗ].
- Выбирать провайдеров с «no training» и коротким abuse-retention; подписывать DPA.

### Антиабьюз (защита от злоупотребления детскими фото)
1. **Никаких свободных текстовых промптов**: только фиксированные сценарии/шаблоны (дракон летит, рисунок оживает, танец персонажа). Это убирает 90% векторов злоупотребления (оценка).
2. Вход: хэш-матчинг (Cloudflare CSAM Scanning / PhotoDNA / Safer) + классификатор наготы; **блокировать любые фото с обнажённостью**, включая «невинные» пляжные/банные фото детей.
3. Выход: модерация провайдера + собственный кадровый скрининг.
4. Только платные пользователи, лимиты частоты, никаких публичных галерей и шеринга внутри приложения (иначе сервис становится user-to-user с обязанностями UK Online Safety Act [БЗ] и TAKE IT DOWN Act [БЗ]).
5. Кнопка «пожаловаться» в приложении (Google Play AI-Generated Content [БЗ]; Apple 1.2 [П]) и опубликованный контакт.
6. Маркировка «создано ИИ» + C2PA/метаданные (EU AI Act ст. 50 с 2026-08-02 [БЗ]); Veo уже ставит SynthID [П, Cookbook].
7. Процедура реагирования: кто и в течение скольких часов разбирает жалобу (для соло-основателя — автоматическая блокировка + ручной разбор 1 раз в день).

### Магазины: чек-лист
- Категория: Photo & Video или Entertainment, **не Kids**; возрастной рейтинг 4+/9+ по контенту, но аккаунт и оплата — для взрослых; маркетинг и скриншоты — родителям.
- Экран согласия: «фото и рисунок будут переданы [провайдер] для генерации, удаляются через N часов» + чекбокс (5.1.2(i)).
- Политика конфиденциальности с разделом о детях, сроках хранения, отзыве согласия (5.1.1(i)–(v)).
- US storefront: можно ставить ссылку на веб-оплату (Stripe/Paddle) без комиссии Apple [П, 3.1.1(a)] — важно для B2B и паков.
- Google Play: форма Data safety, декларация целевой аудитории (не дети), in-app report.

---

## Рекомендуемая архитектура с минимальным риском

**Принцип: «рисунок — главный герой, лицо ребёнка — опционально и стилизовано».**

1. **Drawing-first (по умолчанию).** Родитель фотографирует рисунок → сегментация/очистка → стилизация (Nano Banana 2 Lite / gpt-image-2.5 medium / Seedream 5 Lite, $0.01–0.07) → анимация одного из 10–30 фиксированных сценариев (Veo 3.1 Lite, Seedance 2.0 Mini, Hailuo Fast или Kling Std; $0.18–0.84) → монтаж по шаблону с музыкой и титром «Рисунок: Маша, 5 лет» (ваш After Effects-опыт → шаблоны монтажа, переходы, типографика — это и есть отличие от «сырого» клипа). Здесь нет фото ребёнка → доступны все провайдеры, включая Veo/Seedance, нет биометрии, минимальные требования.
2. **Бесплатный/дешёвый детерминированный режим**: Meta Animated Drawings (MIT) для «человечков» — себестоимость ≈ хостинг; идеально как free-tier/превью (оценка: снижает долю платных генераций, которые «не понравились»).
3. **Опциональный «камео ребёнка»** — только стилизованный (мультяшный, не фотореалистичный) аватар; провайдер — тот, чья политика это явно допускает по результатам вашего теста (кандидаты: Kling, MiniMax, self-host Qwen-Image-Edit + Wan). Выключено по умолчанию в EU/UK на старте.
4. **Аккаунт только родителя**; подтверждение 18+ и оплата картой/IAP; нет детских профилей, нет чатов, нет шеринга внутри приложения; экспорт в галерею телефона.
5. **Абстракция провайдеров** (через fal/Replicate/Magnific или собственный роутер): Sora API закрыт 2026-09-24, gpt-image-1.5 — 2026-12-01, Nano Banana 2.5 — 2026-10-02 [П] → смена модели не должна требовать релиза приложения.
6. **Авто-удаление**: фото ≤1 ч, рисунок и видео — 72 ч (или 12 мес. только для физического продукта по явному согласию и только без лица ребёнка).
7. **Регионы запуска**: US, UK, CA, AU для drawing-only; фото-камео — после DPIA и теста провайдеров; EU — drawing-only.
8. **B2B-ветка (детсады/школы)**: только рисунки, без фото; согласие собирает учреждение; результат — «фильм выставки группы» + индивидуальные ролики + открытки с QR.

---

## Физический продукт

**Статус данных: цены Printful/Prodigi/Gelato в этой сессии проверить не удалось (сайты заблокированы egress-прокси).** Ниже — ориентиры из базы знаний, помечены как «оценка, низкая уверенность»; перед запуском снять фактические цены через API/каталоги.

| Продукт | Базовая цена (оценка, низкая) | Доставка US/UK/EU (оценка, низкая) | Индонезия | Комментарий |
|---|---|---|---|---|
| Открытка 4×6"/A6 с QR (1 шт.) | ~$1–3 | $3–6 за заказ | нет данных | Gelato/Prodigi печатают локально в ряде стран — дешевле доставка |
| Набор 5–10 открыток | ~$5–12 | $4–8 | нет данных | Лучший «апселл» к 5-pack |
| Постер 8×10"–12×18" | ~$8–15 | $5–10 | нет данных | Рисунок + кадр из видео + QR |
| Фотокнига 20 стр. | ~$10–25 | $6–12 | нет данных | «Альбом года рисунков» для B2B-группы |

Экономика (оценка): набор «5 открыток + 5 роликов» за $29 с доставкой в US/UK: база+доставка ~$10–16, генерация 5 LOW ~$1.7, комиссия ~$1.4 → вклад ~$10–16 (35–55%). QR должен вести на ваш хостинг → конфликт с авто-удалением: для физического продукта хранить **только ролики без лица ребёнка** 12 мес. с опцией удаления по запросу. Для основателя в Бали физическая логистика — только через PoD с API (белая этикетка), без собственного склада; Индонезию как рынок сбыта не рассматривать на старте (нет данных о локальной печати).

---

## Сценарии: 12 / 24 / 36 месяцев (09.2026 → конец 2029)

| Сценарий | Вероятность | 12 мес. (09.2027) | 24 мес. (09.2028) | 36 мес. (конец 2029) | Сигналы (как мониторить) |
|---|---|---|---|---|---|
| **Базовый** | 55% | Видео 720p 5–8 с ≤ $0.15; первоклассные западные провайдеры продолжают блокировать реальных детей; Kling/MiniMax допускают, но ужесточают фильтры | Анимация рисунков — функция в Google Photos/ChatGPT/CapCut; платят за шаблоны, монтаж, печать, B2B-пакеты | Потребительский «сырой» генератор бесплатен; ниша живёт в ритуалах (выпускной, день рождения, выставка группы) и печати | 1) цены в LiteLLM/fal ежемесячно; 2) person_generation в Google SDK (diff types.py); 3) системные карты OpenAI; 4) анонсы Google I/O (май) и WWDC (июнь) |
| **Быстрый** | 25% | Open weights (Wan/Qwen) дают 10 с 1080p < $0.05 на своём GPU; платформы бесплатно анимируют рисунки | Потребительское приложение без канала — ноль; B2B и физический продукт — основной доход | Выигрывают владельцы каналов (фотографы, сети детсадов, школы) | 1) релизы Wan/Qwen на GitHub; 2) функции «animate drawing» в Photos/Gemini/ChatGPT; 3) цены H100/4090 в аренду |
| **Медленный / запретительный** | 20% | Скандал с AI-CSAM из детских фото → магазины требуют верификацию возраста и запрещают генерацию по фото детей; провайдеры закрывают вход реальных людей | Выживают только drawing-only продукты с жёсткой модерацией | Регуляторные требования (age assurance, маркировка) стали нормой; барьер входа защищает тех, кто уже соответствует | 1) FTC enforcement по COPPA; 2) изменения App Review Guidelines (1.2, 5.1.2, 1.3); 3) политика Kling/MiniMax; 4) отчёты NCMEC/IWF о GenAI |

---

## Ответы на ключевые вопросы (кратко, в разрезе этого потока)

- **Что станет массовым и дешёвым**: 5–10-секундная анимация картинки (уже $0.03–0.10/с), стилизация рисунка ($0.01–0.07), базовая «ожившая» открытка.
- **Что поглотят платформы**: «оживи фото/рисунок» в Google Photos, Gemini, ChatGPT, CapCut/TikTok (оценка, высокая вероятность к 2027–2028).
- **Где останутся деньги**: B2B-пакеты для учреждений и детских фотографов; физические сувениры с QR; шаблоны монтажа и арт-дирекшн (качество «как у студии»); доверие (соответствие приватности детей).
- **Доступ к инструментам**: у массового пользователя — бесплатные функции платформ; у профи — API и open weights; разница — в конвейере, модерации и шаблонах.
- **Обесценится**: умение «генерировать клип по промпту», простые обёртки над API.
- **Станет дефицитом**: соответствие требованиям по детским данным (DPIA, VPC, авто-удаление, CSAM-модерация), доступ к учреждениям, узнаваемый стиль шаблонов, умение держать брак < 20% без ручного труда.

---

## Кандидаты идей (из этого потока)

1. **«Выставка группы» для детсадов/школ (B2B, drawing-only)** — тип AB. Формат: веб-кабинет воспитателя + пакет роликов + открытки. Покупатель: детсад/родительский комитет/детский фотограф; боль — «сделать красивый подарок/отчёт без возни и без рисков с фото детей». Доказательства спроса: косвенные (вирусные тренды с детскими рисунками — [Tom's Guide](https://www.tomsguide.com/ai/i-turned-my-kids-art-into-lifelike-images-using-chatgpt-heres-how-you-can-too)); прямых данных о B2B-спросе — нет. Конкуренты: ChatGPT/Gemini (общие, $0–20/мес), Meta Animated Drawings (бесплатно, open source); цены прямых B2B-конкурентов — нет данных. Моат: канал через учреждения/фотографов + шаблоны монтажа + соответствие приватности. Риск: длинный цикл продаж, сезонность.
2. **Родительское приложение «Рисунок оживает» (drawing-first)** — тип A. Формат: iOS/Android + веб-оплата (US ссылка без комиссии Apple). Цена $4.99 за ролик / $19.99 за 5. Моат: библиотека сценариев и монтаж в стиле моушн-дизайна, скорость обновления шаблонов. Риск: поглощение платформами, CAC.
3. **Физический «оживший альбом»: открытки/постер/книга с QR** — тип A. Формат: веб-магазин + PoD (Gelato/Prodigi/Printful). Цена $19–39. Моат: бренд + упаковка + печать без склада. Риск: логистика, возвраты, цены PoD не проверены.
4. **Конвейер для детских фотографов (white-label)** — тип AB. Фотографы уже собирают согласия родителей; продукт — пакет «ожившие портреты в мультяшном стиле» с их брендингом. Моат: интеграция в их workflow, доверие. Риск: провайдерские запреты на реальных детей (нужен собственный self-host конвейер на open weights — ответственность выше).

---

## Источники

1. LiteLLM model_prices_and_context_window.json (GitHub raw) — прочитано 2026-09-26: https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
2. AI Free API — GPT Image 2 API pricing (checked 2026-09-06): https://www.aifreeapi.com/en/posts/openai-image-generation-api-pricing
3. Price Per Token — GPT Image pricing (2026): https://pricepertoken.com/gpt-image-pricing
4. WaveSpeed — GPT Image 2 pricing 2026: https://wavespeed.ai/blog/posts/gpt-image-2-pricing-2026/
5. OpenAI Deployment Safety Hub — ChatGPT Images 2.5 System Card (2026): https://deploymentsafety.openai.com/chatgpt-images-2-5
6. Apiyi — Nano Banana 2 official pricing (2026): https://help.apiyi.com/en/nano-banana-2-pricing-guide-official-google-api-en.html
7. LaoZhang — Gemini 3 Pro Image API pricing (2026): https://blog.laozhang.ai/en/posts/gemini-3-pro-image-api-pricing
8. Price Per Token — Gemini 3.1 Flash Lite Image (2026): https://pricepertoken.com/image/model/google-gemini-3-1-flash-lite-image
9. Digital Applied — Gemini 2.5 Flash Image retires Oct 2 (2026): https://www.digitalapplied.com/blog/gemini-2-5-flash-image-retirement-october-2-api-vertex
10. Lumenfall — Seedream 4.5 providers (2026): https://lumenfall.ai/models/bytedance/seedream-4.5/providers
11. Apiyi — Seedream 5.0 Lite API (2026): https://help.apiyi.com/en/seedream-5-0-lite-api-guide-cheaper-than-4-5-en.html
12. Flowith — FLUX.2 pricing 2026: https://flowith.io/blog/flux-2-pro-pricing-2026-dev-vs-pro-vs-schnell-api/
13. BFL pricing: https://bfl.ai/pricing
14. Qwen-Image GitHub README (прочитано 2026-09-26): https://github.com/QwenLM/Qwen-Image ; HF: https://huggingface.co/Qwen/Qwen-Image-Edit-2511 ; fal: https://fal.ai/models/fal-ai/qwen-image-edit-2511
15. AI Video Bootcamp — Veo 3.1 Lite (2026): https://aivideobootcamp.com/blog/veo-3-1-lite-google-cheap-ai-video-2026/
16. AI Free API — Veo 3.1 pricing guide (ставки на 2026-07-23): https://www.aifreeapi.com/en/posts/veo-3-1-pricing
17. fal — Kling Video v3 Standard image-to-video (2026): https://fal.ai/models/fal-ai/kling-video/v3/standard/image-to-video
18. Renderful — Kling API pricing 2026: https://renderful.ai/blog/kling-api-pricing ; Kling dev pricing: https://kling.ai/dev/pricing
19. OpenAI Help — What to know about the Sora discontinuation (2026): https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
20. Unifically — Sora API shutdown (2026): https://unifically.com/blogs/sora-api
21. NxCode — Seedance 2.0 API guide (2026): https://www.nxcode.io/resources/news/seedance-2-0-api-guide-pricing-setup-2026
22. Phemex News — Seedance 2.0 relaunch with real-face upload ban (2026): https://phemex.com/news/article/bytedance-relaunches-seedance-20-globally-with-restrictions-on-realface-uploads-68605
23. MindStudio — Seedance 2.0 content restrictions (2026): https://www.mindstudio.ai/blog/seedance-2-0-content-restrictions-workarounds
24. Magic Hour — Hailuo 2.3 pricing (2026): https://magichour.ai/blog/hailuo-23-pricing ; MiniMax video packages: https://platform.minimax.io/docs/guides/pricing-video
25. fal — Wan 2.6 image-to-video (2026): https://fal.ai/models/wan/v2.6/image-to-video ; Wan2.2 GitHub (прочитано 2026-09-26): https://github.com/Wan-Video/Wan2.2
26. Runway API pricing (2026): https://docs.dev.runwayml.com/guides/pricing/
27. MindStudio — Luma Ray Flash 2 (2026): https://www.mindstudio.ai/blog/what-is-luma-ray-flash-2-video ; Magic Hour — Luma pricing: https://magichour.ai/blog/luma-dream-machine-pricing
28. Vantaige — Freepik is now Magnific (2026): https://vantaige.io/blog/freepik-ai-is-now-magnific-pricing-changes-2026 ; Freepik API upscaler: https://www.freepik.com/api/image-upscaler
29. Magnific API/MCP simulate_cost и каталоги моделей — запросы 2026-09-26 (без URL, инструментальные данные)
30. OpenAI — Addendum to GPT-4o System Card: Native image generation (2025-03-25): https://cdn.openai.com/11998be9-5319-4302-bfbf-1167e093f1fb/Native_Image_Generation_System_Card.pdf
31. TechCrunch — OpenAI peels back ChatGPT's safeguards around image creation (2025-03-28): https://techcrunch.com/2025/03/28/openai-peels-back-chatgpts-safeguards-around-image-creation/
32. OpenAI Community — child images blocked thread: https://community.openai.com/t/why-on-earth-do-we-prevent-the-use-of-child-images-in-an-unconditionally-safe-environment-and-force-unrealistic-characters/1107729
33. OpenAI Community — gpt-image-2 over-refusals with moderation:low (2026): https://community.openai.com/t/api-issue-moderation-over-refusals-on-gpt-image-2-with-moderation-low-where-chatgpt-always-succeeds/1388964
34. Google python-genai types.py (прочитано 2026-09-26): https://raw.githubusercontent.com/googleapis/python-genai/main/google/genai/types.py
35. Google Gemini Cookbook — Get_started_Veo.ipynb (прочитано 2026-09-26): https://raw.githubusercontent.com/google-gemini/cookbook/main/quickstarts/Get_started_Veo.ipynb
36. Google Cloud — Veo on Vertex AI API reference (по поиску 2026-09): https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation
37. Google Developer Forums — allowlist for Veo 3.1 person generation: https://discuss.google.dev/t/request-allowlist-access-for-veo-3-1-person-generation-reference-to-video/398998 ; Gemini forum — Veo 3.1 i2v and allow_adult: https://discuss.ai.google.dev/t/veo-3-1-image-to-video-rejects-documented-persongeneration-allow-adult/181139
38. Adobe Community — Firefly and images depicting children (2025): https://community.adobe.com/t5/adobe-firefly-discussions/not-sure-why-my-images-quot-violate-guidelines-quot-image-depicts-children/m-p/15200515/page/2
39. Apple App Review Guidelines (прочитано 2026-09-26): https://developer.apple.com/app-store/review/guidelines/
40. Apple Developer — Kids (прочитано 2026-09-26): https://developer.apple.com/kids/
41. Apple — Small Business Program (прочитано 2026-09-26): https://developer.apple.com/app-store/small-business-program/
42. Apple — Age assurance Q&A (прочитано 2026-09-26): https://developer.apple.com/support/age-assurance/
43. Meta AnimatedDrawings (MIT; прочитано 2026-09-26): https://github.com/facebookresearch/AnimatedDrawings
44. Tom's Guide — kids' doodles into lifelike images with ChatGPT (2025): https://www.tomsguide.com/ai/i-turned-my-kids-art-into-lifelike-images-using-chatgpt-heres-how-you-can-too
45. [БЗ] FTC — finalizes changes to COPPA Rule (2025-01-16): https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data
46. [БЗ] Federal Register — COPPA Rule (2025-04-22): https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule
47. [БЗ] FTC — Complying with COPPA: FAQ: https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
48. [БЗ] GDPR Art. 8 / Art. 9 / Recital 51: https://gdpr-info.eu/art-8-gdpr/ ; https://gdpr-info.eu/art-9-gdpr/ ; https://gdpr-info.eu/recitals/no-51/
49. [БЗ] ICO — Children's code guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/
50. [БЗ] 18 U.S.C. §2258A: https://www.law.cornell.edu/uscode/text/18/2258A
51. [БЗ] TAKE IT DOWN Act (S.146, 119th Congress): https://www.congress.gov/bill/119th-congress/senate-bill/146
52. [БЗ] EU AI Act Art. 50: https://artificialintelligenceact.eu/article/50/
53. [БЗ] Google Play — AI-Generated Content policy: https://support.google.com/googleplay/android-developer/answer/13985936 ; Families policies: https://support.google.com/googleplay/android-developer/answer/9893335
54. [БЗ] Thorn Safer: https://safer.io/ ; Microsoft PhotoDNA: https://www.microsoft.com/en-us/photodna ; Cloudflare CSAM Scanning Tool: https://developers.cloudflare.com/cache/reference/csam-scanning/
55. [БЗ] Stripe pricing (UK): https://stripe.com/gb/pricing ; Paddle pricing: https://www.paddle.com/pricing ; Cloudflare R2 pricing: https://developers.cloudflare.com/r2/pricing/
