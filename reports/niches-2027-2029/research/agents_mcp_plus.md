# Поток 4 (дополнение). AI-агенты и MCP в креативных приложениях: проверка, исправления, новые данные (срез 26.09.2026)

> **Что это.** Дополнение к `agents_mcp.md`. Здесь нет повторов неизменённого содержания: только проверенные и исправленные утверждения, новые факты, закрытые пробелы брифа, изменения сценариев и уточнённые идеи. Использовано около 70 поисковых запросов WebSearch (лимит сессии исчерпан), 6 WebFetch-запросов к GitHub и прямые запросы к API официального MCP Registry. Факты даны с URL и датой. Оценки помечены «оценка» с уверенностью. Там, где цифры взяты из маркетинга площадки, это сказано прямо.

---

## Проверено и исправлено

### Где оригинал ошибался или устарел

1. **ИСПРАВЛЕНО: Anthropic не является «Corporate Patron» Blender за €240 000 в год.** Оригинал (факт 22) писал «не меньше €240 000 в год». Членство действительно объявили 28–29.04.2026. **Меньше чем через неделю, после протестов сообщества, Blender Foundation превратила его в разовое пожертвование.** Логотипа Anthropic больше нет в списке патронов, фонд обещал выработать общую политику по genAI ([CG Channel](https://www.cgchannel.com/2026/05/anthropics-patronage-of-blender-downgraded-to-one-off-donation/), 2026-05; [BlenderNation](https://www.blendernation.com/2026/05/01/update-anthropic-joins-the-blender-development-fund/), 2026-05-01; [Blender.org](https://www.blender.org/news/upcoming-blender-development-fund-and-ai-policies/), 2026-05). Официальный коннектор Blender Lab (blender.org/lab/mcp-server) остался ([Digital Production](https://digitalproduction.com/2026/04/30/anthropic-funds-blender-ships-claude-connector/), 2026-04-30). **Вывод для основателя:** в креативных open-source-сообществах связь с AI-вендором вызывает репутационную реакцию. Это надо учитывать в маркетинге AI-функций среди моушн- и 3D-аудитории.

2. **ИСПРАВЛЕНО: «Prism» — это, скорее всего, два разных продукта, а не одна компания.** Оригинал (факт 25) считал Prism (oneprism.io, AE-MCP) и Prism «от $39» одним игроком. Это не подтверждается.
   - **Prism от Next Horizon** (nexthorizon.art) — плагин Figma → After Effects / DaVinci Resolve. Разовая «пожизненная» оплата **от $39**, тарифы Starter (1 машина), Duo (2) и Team (3). Работает с AE CC 2019+ ([Next Horizon store](https://nexthorizon.art/store/figma-to-ae), 2026; [Figma Community](https://www.figma.com/community/plugin/1648737738684655034/prism), 2026). Сравнение «AEUX vs Overlord vs Prism», которое цитировал оригинал, — **собственный маркетинг Next Horizon**: «Prism is the tool built at Next Horizon» ([Next Horizon](https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma), 2026).
   - **OnePrism** (oneprism.io) — MCP-коннектор для AE. «Free to start», на Pro AI-действия без лимита, модель bring-your-own-AI ([OnePrism](https://oneprism.io/), 2026). В реестре значится как `io.oneprism/after-effects`, версия 1.4.0, опубликована 11.08.2026 ([Registry API](https://registry.modelcontextprotocol.io/v0/servers?search=oneprism), запрос 2026-09-26).
   - Связи между ними не нашёл. Уверенность, что это разные компании, **средняя**.

3. **ОБНОВЛЕНО: AE AI Assistant уже в публичной бете и построен на MCP.** В оригинале (факты 14–15) — закрытая бета (06.2026) и «бета, не перепроверено» (09.2026). Теперь проверено:
   - Adobe показала AI Assistant для AE **в публичной бете** на IBC2026. Он суммирует проект и реорганизует его (даже с тысячами слоёв), пишет expressions, чинит технические проблемы и работает по всему проекту, а не только в открытой композиции ([RedShark News](https://www.redsharknews.com/after-effects-ai-assistant-ibc2026), 2026-09; [Adobe Blog](https://blog.adobe.com/en/publish/2026/09/08/generate-create-directly-in-your-timeline-with-new-ai-powered-innovations-in-premiere-after-effects), 2026-09-08).
   - **В бете он бесплатен, генерации Firefly тоже.** Есть дневной лимит и отдельный недельный порог. Цену для релиза Adobe обещает объявить позже ([CG Channel](https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/), 2026-09; [Adobe Community](https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658), 2026-09).
   - На Creative COW его описывают как **«Host-Client MCP», подключённый к нескольким LLM, со своим harness от команды AE**. Ассистенты в Ps, Pr, Ai и Id устроены так же ([Creative COW](https://creativecow.net/forums/thread/adobe-adds-an-ai-assistant-mcp-to-after-effects-beta-private-beta/), 2026-08). Это форумный источник, уверенность средняя.
   - Официальная страница помощи тоже есть ([Adobe HelpX](https://helpx.adobe.com/after-effects/desktop/work-with-after-effects-ai-assistant/after-effects-ai-assistant-overview.html), 2026-09).
   - **Вывод: платформенный риск для любого «AE-агента» ещё выше, чем считал оригинал.** Adobe даёт аналог бесплатно, внутри приложения и на своём MCP-стеке.

4. **ИСПРАВЛЕНО: подключить свой MCP в ChatGPT можно не только на Business, Enterprise и Edu.** По справке OpenAI и гайдам 2026 года Developer Mode с полной поддержкой MCP (чтение и запись) доступен на **Plus и Pro**, а также Business, Enterprise и Edu. На Free его нет ([OpenAI Help](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt), 2026; [Coworker AI](https://coworker.ai/blog/chatgpt-mcp), 2026). Уверенность средняя: в 04.2026 пресса писала о пропаже функций на части Pro-аккаунтов.

5. **ИСПРАВЛЕНО: x402 не доказывает, что агенты реально платят.** Оригинал (факт 33) приводил цифры Coinbase и Chainalysis: 169 млн+ платежей, 590 тыс. покупателей. Первый независимый аудит **TRM Labs (09.09.2026)**:
   - 198,9 млн расчётов на ~$52,7 млн с мая 2025 года;
   - после очистки от самоплатежей и аномалий «вероятная коммерция» — $25,6 млн;
   - от AI-агентов из неё только **0,6–7,5%**;
   - объём, который двигают агенты, — **около $5 000–11 000 в месяц**;
   - 99,6% расчётов в USDC.
   ([TRM Labs](https://www.trmlabs.com/trm-tech-blog/whos-actually-paying-measuring-ai-agent-payments-onchain), 2026-09-09; [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/agentic-payments-are-growing-most-x402-payments-are-not-from-ai-agents), 2026-09.) Средний платёж около $0,26, дневной объём x402 около $28K, по оценкам 25–30% транзакций накручены ради лидербордов ([свод Ricosworks1 на GitHub](https://github.com/Ricosworks1/blockchain-payment-flow-analysis/releases/tag/deep-dive-ai-agent-payments-infrastructure-reality-sept-2026), 2026-09). **Реальный рынок «агент платит за вызов инструмента» в 2026 году измеряется тысячами долларов в месяц на всю экосистему.**

6. **ИСПРАВЛЕНО: трактовка «computer use пока медленный».** В оригинале (факт 38) 40 минут на задачу подавались как «медленно». Но задачи OSWorld 2.0 у **людей занимают в медиане около 1,6 часа** и требуют в среднем около 318 вызовов инструментов; при публикации лучшие агенты проходили около 31% end-to-end ([OSWorld 2.0, arXiv](https://arxiv.org/abs/2606.29537), 2026-06). **Claude Opus 5.5 (22.09.2026) набрал 81,8%** по частичному зачёту OSWorld 2.0; строгий зачёт в system card — 48,7% ([Anthropic](https://www.anthropic.com/claude-opus-5-5), 2026-09-22; [Vellum](https://www.vellum.ai/blog/claude-opus-5-5-benchmarks-explained), 2026-09). Значит, агенты с GUI уже быстрее человека на длинных задачах, но надёжно завершают меньше половины. Для AE это означает: **в 2027–2028 годах часть рутины можно будет делать вообще без коннектора**, через экран. Ценность «MCP для приложения X» падает быстрее, чем предполагал оригинал.

7. **УТОЧНЕНО: размеры каталогов (оригинал, факт 10, опирался на вторичные данные 05.2026).**

| Каталог | В оригинале | Проверено | Источник |
|---|---|---|---|
| Glama | 21K+ | **92 121** «open-source MCP servers» (по счётчику на странице) | [Glama](https://glama.ai/mcp/servers), 2026-09 |
| PulseMCP | 11,8K+ | **~21,8–22,3K** (22 311 на 16.07.2026) | [PulseMCP](https://www.pulsemcp.com/servers), 2026-09; [tooldirectory.ai](https://tooldirectory.ai/blog/state-of-mcp-servers-2026), 2026 |
| Smithery | 7K+ | «десятки тысяч записей»; **куплен Arcade.dev (сделка объявлена 05.08.2026)** | [Forbes](https://www.forbes.com/sites/janakirammsv/2026/08/10/arcade-acquires-smithery-to-own-the-agent-tool-supply-chain/), 2026-08-10 |
| Официальный Registry | 36 185 (подсчёт потока, 26.09) | 9 652 последних записи на 24.05.2026 — **согласуется** с месячным темпом оригинала (оценка, высокая) | [bex.co](https://bex.co/blog/2026/07/10/mcp-registry-discoverability-trust), 2026-07-10 |
| mcp.so | 19,7K+ | свежих данных нет | — |

   Цифры каталогов несопоставимы: Glama считает краулинговые записи, Unyly — 70K+ дедуплицированных ([Unyly](https://unyly.org/mcp-directories), 2026).

8. **УТОЧНЕНО: сколько коннекторов у Claude.** Оригинал писал: 850 коннекторов и 340 плагинов на витрине. Перепись Николя Ситтера (июль–август 2026), собранная через собственные endpoint платформ: **1 375 коннекторов Claude и 1 735 приложений ChatGPT** ([Nicolas Sitter](https://www.nicolassitter.com/research/mcp-apps-census-2026), 2026-07/08). Расхождение объясняется методикой. Anthropic в анонсе Marketplace пишет о «более 2 000» коннекторов и плагинов ([Claude Blog](https://claude.com/blog/claude-marketplace), 2026-09-23). Запуск Marketplace 23.09 и портала плагинов 25.09.2026 **подтверждены**. **Revenue share для разработчиков нет ни в одном источнике** ([Unite.AI](https://www.unite.ai/anthropic-opens-directory-submission-portal-for-claude-plugins/), 2026-09-25).

9. **УТОЧНЕНО: MCPize.** Стандартная доля автора — **80%**. 85% получают только «Founding Members», пришедшие до 10.06.2026 ([MCPize](https://mcpize.com/developers/monetize-mcp-servers), 2026). Цифры «$400–2 000+ в месяц у реальных авторов» — маркетинг площадки, уверенность низкая.

10. **УТОЧНЕНО: DaVinci Resolve 21.1 (08.09.2026) — это нативный MCP-сервер, а не только новые scripting API.**
    - В нём **88 инструментов** по всем страницам: проект, таймлайн, медиапул, цвет, Fairlight, рендер. Подключение — File > Setup AI Assistants, к Claude, Claude Code и Codex ([byteiota](https://byteiota.com/davinci-resolve-21-1-mcp-server/), 2026-09; [CineD](https://www.cined.com/davinci-resolve-21-1-released-ai-assistant-integration-via-mcp-individual-hdr-trims-and-python-scripting-moves-to-studio/), 2026-09; [Digital Production](https://digitalproduction.com/2026/09/08/resolve-21-1-adds-mcp-and-finally-gets-presets/), 2026-09-08).
    - Работает только в Studio (**$295 разово**), бесплатная версия слой скриптинга не открывает.
    - Факт «платформа берёт деньги за доступ агента» подтверждён.

11. **ПОДТВЕРЖДЕНО с деталями: Illustrator.** В Illustrator Beta встроен официальный MCP-сервер с ~40 инструментами, подключаются Cursor и Claude Code ([Adobe HelpX](https://helpx.adobe.com/in/illustrator/desktop/connect-with-other-apps-and-tools/about-using-ai-tools-with-illustrator.html), 2026). Community-сервер ie3jp теперь заявляет **63 инструмента**, а не 66 ([GitHub ie3jp](https://github.com/ie3jp/illustrator-mcp-server), 2026-09).

12. **ПОДТВЕРЖДЕНО: коннектор «Adobe for creativity» (28.04.2026).** В прессе — «50+ инструментов» по Ps, Lr, Pr, Ai, Firefly, Express, InDesign и Stock ([Adobe Blog](https://blog.adobe.com/en/publish/2026/04/28/adobe-for-creativity-connector), 2026-04-28). Оригинал называл 67 по листингу: вероятно, число инструментов выросло (оценка, средняя). **After Effects в коннекторе по-прежнему нет.** Базовая часть работает без платной подписки CC — фактически через бесплатный Express ([XDA](https://www.xda-developers.com/integrated-claude-with-adobe-without-paying-for-creative-cloud/), 2026). Коннекторы Anthropic (9 штук) доступны на всех планах Claude, включая Free ([9to5Mac](https://9to5mac.com/2026/04/28/anthropic-releases-9-new-claude-connectors-for-creative-tools-including-blender-and-adobe/), 2026-04-28).

13. **ПОДТВЕРЖДЕНО: звёзды на GitHub (WebFetch, 26.09.2026).** Dakkshin/after-effects-mcp — 657★, 127 форков, MIT, коммерческой версии нет. ahujasid/blender-mcp — **29,4K★**, 2,7K форков. Есть платный тариф: генерация 3D через Hunyuan3D, Tripo и Rodin без своих API-ключей. Есть дисклеймер «not made by Blender».

14. **ПОДТВЕРЖДЕНО с датами: переход с CEP на UXP.**
    - **Публичная бета UXP-плагинов для AE — к ноябрю 2026 года.**
    - Каждому флагману гарантировано минимум 2 года после UXP-беты.
    - В AE приём новых CEP-сабмитов прекращается, а CEP выключается по умолчанию в **декабре 2028 года**.
    - С **декабря 2029 года** CEP не входит в новые версии.
    - Photoshop перестаёт принимать новые CEP-плагины с марта 2027 года.
    - **ExtendScript переход не затрагивает** ([Adobe Developer Blog](https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications), 2026-09).
    - Для Oblique: если панель на CEP, миграцию нужно заложить на 2027–2028 годы.

15. **ПОДТВЕРЖДЕНО: skills.sh.** ~669 670 skills на июнь 2026 года; у топового (find-skills от vercel-labs) 2,0 млн установок, у frontend-design от Anthropic — 531,8K ([rajeevpentyala](https://rajeevpentyala.com/2026/06/16/discover-and-install-agent-skills-with-skills-sh/), 2026-06-16; [Ry Walker](https://rywalker.com/research/skills-sh), 2026). Порядок величины в оригинале (895K к 07.2026) правдоподобен.

16. **ПОДТВЕРЖДЕНО: ClawHub.** 824+ подтверждённых вредоносных skills из 10 700+ на 16.02.2026. По оценке Bitdefender — около 900, то есть примерно 20% ([Bitdefender Labs](https://www.bitdefender.com/en-us/blog/labs/helpful-skills-or-hidden-payloads-bitdefender-labs-dives-deep-into-the-openclaw-malicious-skill-trap), 2026-02; [particula.tech](https://particula.tech/blog/openclaw-security-crisis-malicious-ai-agents), 2026).

17. **ПОДТВЕРЖДЕНО: спецификация MCP 2026-07-28.** Stateless-ядро, фреймворк расширений (MCP Apps, Tasks — последнее внёс AWS), усиленный OAuth, формальная политика устаревания. Release candidate вышел за 10 недель до финала ([MCP Blog RC](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), 2026; [Claude Blog](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude), 2026). Цифра «~97 млн загрузок SDK в месяц» относится к марту 2026 года ([jahanzaib.ai](https://www.jahanzaib.ai/blog/mcp-97-million-installs-dev-summit-2026), 2026). **SEP-2007 (платежи) по-прежнему в статусе Draft** ([GitHub #2008](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2008), 2026-09).

18. **ПОДТВЕРЖДЕНО: GPT-6 Astra** вышел 03.09.2026: 72,6% на OSWorld 2.0 за ~40 минут на задачу ([OpenAI](https://openai.com/index/gpt-6-astra/), 2026-09-03). Но лидер теперь Opus 5.5 (см. п. 6).

---

## Новые факты

### A. Управление MCP и принятие стандарта

19. **Хронология принятия (закрывает пробел брифа):**

| Дата | Событие |
|---|---|
| 11.2024 | Anthropic выпускает MCP |
| 03.2025 | OpenAI принимает MCP (Agents SDK, затем ChatGPT desktop) |
| 04.2025 | Google DeepMind подтверждает поддержку в Gemini |
| 19.05.2025 (Build) | Windows 11 получает MCP в превью, GitHub и Microsoft входят в steering committee |
| 12.2025 | MCP передан в AAIF |

   ([The New Stack](https://thenewstack.io/why-the-model-context-protocol-won/), 2026; [Wikipedia: MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol), 2026.)
20. **AAIF: 170+ участников к апрелю 2026 года.** Среди платиновых — AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI ([IntuitionLabs](https://intuitionlabs.ai/articles/agentic-ai-foundation-open-standards), 2026-04; [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), 2025-12).
21. **Consolidation инфраструктуры. Корпорации платят за governance.**
   - Arcade.dev привлёк **$60 млн в раунде A** (06.2026, всего $72 млн) и купил Smithery (08.2026) ([Forbes](https://www.forbes.com/sites/janakirammsv/2026/08/10/arcade-acquires-smithery-to-own-the-agent-tool-supply-chain/), 2026-08-10).
   - Runlayer (MCP-шлюз и безопасность): seed $11 млн (11.2025) и **раунд A $30 млн (06.2026)**, клиенты — Gusto и Instacart. По сводке поиска раскрытое финансирование MCP-безопасности на начало 2026 года — около $40 млн ([Software Strategies Blog](https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/), 2026-03-28; [AppSentinels](https://appsentinels.ai/blog/top-10-mcp-security-companies-in-2026/), 2026). Уверенность средняя: первоисточник по Runlayer не открывал.
   - Gartner: к концу 2026 года в 40% корпоративных приложений будут агенты под конкретные задачи против <5% в 2025 году ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025), 2025-08-26).
   - **Деньги в MCP-экосистеме 2026 года — у инфраструктуры для корпораций (шлюзы, аудит, identity), а не у авторов серверов.**

### B. Креативные платформы: агент и MCP стали встроенной функцией

22. **Adobe MAX 2025 (28.10.2025).**
   - AI Assistant в Express — публичная бета.
   - AI Assistant в Photoshop (веб) — закрытая бета.
   - **Project Moonlight** — закрытая бета: агент, который координирует ассистентов разных приложений и подключается к библиотекам CC и соцсетям.
   ([Adobe Newsroom](https://news.adobe.com/news/2025/10/adobe-max-2025-creative-cloud), 2025-10-28; [Adobe Blog](https://blog.adobe.com/en/publish/2025/10/28/our-view-agentic-ai-assistants-that-work-you-in-your-favorite-apps), 2025-10-28.)
   - **10.12.2025 Photoshop, Express и Acrobat пришли в ChatGPT** — бесплатно для 800 млн пользователей ([Adobe Newsroom](https://news.adobe.com/news/2025/12/adobe-photoshop-express-acrobat-chatgpt), 2025-12-10; [TechCrunch](https://techcrunch.com/2025/12/10/adobe-brings-photoshop-express-and-acrobat-features-to-chatgpt/), 2025-12-10).
23. **Adobe «Creative Agent»: 04.2026 → 18.06.2026.** AI Assistant вышел в публичную бету в Premiere, Photoshop, Illustrator, Frame.io и InDesign; в AE тогда была закрытая бета ([Adobe Newsroom](https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion), 2026-06-18; [Adobe Newsroom](https://news.adobe.com/news/2026/04/adobe-new-creative-agent), 2026-04). В Premiere все действия ассистента попадают в стек undo и history ([Adobe Community](https://community.adobe.com/announcements-727/meet-your-new-assistant-editor-ai-assistant-in-premiere-pro-is-now-in-public-beta-1629317), 2026-06).
24. **Экономика Adobe AI (контекст для цен).** Creative Cloud Pro стоит **$69,99 в месяц и включает 4 000 генеративных кредитов**. Standard стоит $54,99 и даёт 25 кредитов. Большинство генераций Firefly — 1 кредит. Видео на партнёрских моделях — 10–450 кредитов в секунду. Докупка Firefly — $9,99–199,99 в месяц ([JustCreative](https://justcreative.com/adobe-creative-cloud-photoshop-illustrator-cost/), 2026-09). **Прогноз:** после беты AE Assistant будет тарифицироваться через эти кредиты (оценка, средняя уверенность).
25. **Figma: лимиты и экономика MCP.**
   - На Full- или Dev-seat в планах Professional и Organization — **200 вызовов MCP в день**, на Enterprise — 600. Поминутно: 10 (Professional), 15 (Organization), 20 (Enterprise). Часть инструментов (`generate_figma_design`, `whoami`, `add_code_connect_map`) не лимитируется ([Figma Developer Docs](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/), 2026).
   - **Когда Figma выступает MCP-сервером, AI-кредиты не расходуются.** Figma agent и Weave переходят из беты в GA и начнут списывать кредиты (объявлено 25.08.2026) ([Figma Help](https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ), 2026-08-25).
   - С 03.2026 на seat даётся 500–4 250 кредитов в месяц. Докупка на старте стоила ~2,4 цента за кредит по подписке и 3 цента pay-as-you-go ([UIChemy](https://uichemy.com/blog/figma-ai-credits/), 2026).
   - **Вывод: чтение Figma агентом (для переноса в AE) остаётся дешёвым и не завязано на кредиты. Генерация в Figma — платная.**
26. **Figma Motion (Config, 24.06.2026) — открытая бета на всех планах.** Таймлайн и ручные ключи доступны всем. Генерация анимации агентом, публикация анимированных компонентов и hi-res экспорт видео — только на платном Full seat. Экспорт: CSS, JSON, React, MP4, WebM, SVG, GIF ([CMSWire](https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/), 2026-06; [MakerStack](https://makerstack.co/reviews/figma-motion-review/), 2026). **Компонента-моста «Figma Motion → After Effects» среди конкурентов не нашёл (нет данных).**
27. **Canva.**
   - С 25.01.2026 Canva расширила коннектор для Claude (генерация дизайнов в стиле бренда), с 05.02.2026 — для ChatGPT. **С 03.06.2026 приложение Canva в ChatGPT работает и на бесплатном Canva** ([Canva Newsroom](https://www.canva.com/newsroom/news/deep-research-integration-mcp-server/), 2026; [Krumzi](https://www.krumzi.com/blog/design-in-chatgpt), 2026).
   - **Cavalry после покупки (24.02.2026) стал бесплатным для частных лиц, включая коммерческое использование (16.04.2026).** Раньше Pro стоил около £16 в месяц; Enterprise с SSO — по запросу ([CG Channel](https://www.cgchannel.com/2026/04/canva-makes-motion-graphics-and-animation-app-cavalry-free/), 2026-04; [CNBC](https://www.cnbc.com/2026/02/23/canva-acquires-cavalry-for-motion-graphics-and-mangoai-for-video-ads.html), 2026-02-23).
   - **Процедурная альтернатива AE теперь бесплатна.** Это давит на цены всех инструментов для моушна.
28. **Игровые движки и 3D.**
   - **Unreal Engine 5.8 (17.06.2026) поставляется с официальным плагином «Unreal MCP»**: экспериментальный, бесплатный, сервер внутри процесса редактора ([Ludus AI](https://ludusengine.com/blog/unreal-mcp-plugin-ue5-8-setup), 2026).
   - **Unity** выпустил официальный MCP-сервер в пакете AI Assistant ([Unity Blog](https://unity.com/blog/unity-ai-mcp-how-to-get-started), 2026; [StraySpark](https://www.strayspark.studio/blog/unity-mcp-server-vs-unreal-godot-blender-2026), 2026-08).
   - **Cinema 4D: официального MCP нет.** Maxon встраивает генерацию 3D Tencent HY 3D (конец 2026 года), без повышения цены ([Jon Peddie Research](https://www.jonpeddie.com/news/integrated-ai-feature-coming-to-cinema-4d/), 2026).
   - **К сентябрю 2026 года официальный MCP или агента выпустили Adobe (Ai Beta, коннектор, ассистенты), Blackmagic, Epic, Unity, Figma, Canva и Blender Lab.** Community-коннекторы к этим приложениям обесценены.
29. **LottieFiles выпустил Lottie Creator MCP (04.2026).** Claude, Codex и Gemini читают, редактируют и генерируют варианты анимаций dotLottie, заявлено 40+ агентов-клиентов ([LottieFiles](https://lottiefiles.com/tutorials/lottie-creator/lottie-creator-mcp-create-animations-with-your-favorite-ai-assistants-vs6LnaDzYAL), 2026-04).

### C. «Видео как код»: сдвиг шаблонного моушна от AE

30. **HyperFrames (HeyGen, Apache-2.0): 53,1K★, 4,8K форков, 21 agent skill.** Рендерит HTML, CSS и анимации в детерминированный MP4 через headless Chrome и FFmpeg. Нет платы за рендер и порогов для коммерческого использования ([GitHub heygen-com/hyperframes](https://github.com/heygen-com/hyperframes), WebFetch 2026-09-26).
31. **Remotion.**
   - Официальный Remotion skill стал вирусным в 01.2026: 6 млн+ просмотров демо, 25K+ установок за неделю. Сейчас **126 000+ установок, №4 на skills.sh** ([AI Vid Pipeline](https://aividpipeline.com/blog/remotion-agent-skills-guide-2026), 2026; [Remotion docs](https://www.remotion.dev/docs/ai/skills), 2026).
   - Лицензия: бесплатно для компаний меньше 3 человек. **$25 в месяц за seat** (Creators), минимум **$100 в месяц** (Automators), минимум **$500 в месяц** (Enterprise) ([Remotion pricing](https://www.remotion.dev/docs/license/pricing), 2026).
   - Выручка Remotion — **около $660K ARR** по оценке Latka, уверенность низкая ([GetLatka](https://getlatka.com/companies/remotion.dev), 2026).
   - Цитата: «Claude Code или Cursor могут писать Remotion-композицию; они не могут управлять After Effects. Это самый большой сдвиг прошлого года» ([Motionpilot](https://motionpilot.app/blog/after-effects-alternatives), 2026). После AE-ассистента Adobe и десятков AE-MCP это утверждение устарело, но позицию Remotion оно отражает.
   - **Вывод:** шаблонный и data-driven моушн уходит в код (OpenMontage 61K★, HyperFrames 53K★, Remotion). Ремесленный моушн и композитинг остаются в AE.

### D. Рынок AE-агентов: уже «красный океан» по $0–29

32. **Коммерческие и полукоммерческие AI-агенты для AE (09.2026):**

| Продукт | Модель | Цена | Источник |
|---|---|---|---|
| **Adobe AE AI Assistant** | встроен, публичная бета | бесплатно в бете (лимиты день и неделя) | [CG Channel](https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/), 2026-09 |
| **AE GPT** (aescripts, suzagear) | Agent Mode пишет и запускает ExtendScript; ChatGPT, Claude, Gemini, Ollama | **$29 разово** (pay-what-you-want), свой API-ключ | [aescripts](https://aescripts.com/ae-gpt/), 2026; [AnyPlugins](https://anyplugins.com/plugin/ae-gpt), 2026 |
| **Claude Scripter** (aescripts) | JSX из промпта, свой ключ Anthropic | цена нет данных; API ~$1–3 в месяц | [claudescripter.com](https://claudescripter.com/), 2026 |
| **Klutz GPT** (Hyper Brew) | ChatGPT в AE | бесплатно + API | [Hyper Brew](https://hyperbrew.co/tools/klutz-gpt/), 2026 |
| **MotionAmigo** (aescripts) | CEP-панель запускает Claude Code или Codex внутри AE; удалённый MCP с **300+ инструментами** | цена нет данных; v1.1.28 от 14.07.2026 | [aescripts](https://aescripts.com/motionamigo/), 2026-07 |
| **Synthetic AE MCP** (synthetic.com.ar) | платный MCP; есть и Premiere MCP | **$29 разово, $15 в месяц или $120 в год** | [Synthetic](https://synthetic.com.ar/ae-mcp), 2026 |
| **AE AI Agent** (NodeFlow Studio) | предоплаченные кредиты или BYOK | цена нет данных | [NodeFlow](https://aeai.nodeflow.studio/), 2026 |
| **OnePrism** | удалённый MCP, BYO-AI | бесплатно, Pro — нет данных | [OnePrism](https://oneprism.io/), 2026 |
| **Higgsfield for Adobe** | панель AE + Premiere; генерация, reframe, remove BG, upscale; **управляется агентом через Supercomputer или Claude (`bridge.higgsfield.ai/mcp`)** | кредиты Higgsfield | [Higgsfield Blog](https://higgsfield.ai/blog/higgsfield-after-effects), 2026-07-21; [No Film School](https://nofilmschool.com/higgsfield-adobe-ai-plugin), 2026 |
| **aftr** | ~90 команд AE через MCP, MIT | бесплатно (Show HN 12.07.2026) | [Creative AI News](https://www.creativeainews.com/articles/aftr-after-effects-claude-code-mcp-2026/), 2026-07 |
| **AI Assistant for After Effects** (Adobe Exchange) | JSX из промпта; GPT-4 Turbo или GPT-5 | нет данных | [Adobe Exchange](https://exchange.adobe.com/apps/cc/203667/ai-assistant-for-after-effects), 2026 |

   **Выручку не раскрывает ни один продукт.** Ценовой потолок категории — **$29 разово или $15 в месяц**, и это до выхода бесплатного встроенного ассистента Adobe в GA. MotionAmigo и OnePrism оба заявляют «300+ инструментов» на удалённом MCP. Возможно, это общая технологическая база, но не проверено.
33. **Figma → AE: число конкурентов Oblique продолжает расти (дополнение к потоку demand_scout):**
   - Prism (Next Horizon) — от $39 разово;
   - **UI Flow** — бесплатно 10 экспортов в день плюс пожизненная лицензия, цена нет данных ([AE Flow Tools](https://www.aeflowtools.com/uiflow), 2026);
   - **DEmotion** ([trydemotion.com](https://trydemotion.com/), 2026, цена нет данных);
   - Overlord (Battle Axe, лицензия с годом обновлений);
   - AEUX (бесплатно, Google).
   Итого минимум 6 активных инструментов без учёта MCP-агентов, которые тоже делают Figma → AE. Урок Oblique подтверждается.
34. **Бесплатные skills для моушна множатся:** LobzyJay/motion-design-with-claude — 19★, 4 skills (motion-design, aftereffects-motion, blender-motion, motion-design-critique), интеграция с Higgsfield ([GitHub](https://github.com/LobzyJay/motion-design-with-claude), WebFetch 2026-09-26).

### E. Монетизация: где реальные деньги у «инструментов для агентов»

35. **Apify — единственная площадка с проверяемыми крупными выплатами авторам.**
   - Выплаты выросли с **~$563K в месяц (09.2025) до ~$1,4–1,5 млн в месяц (08.2026)** примерно на **3 000 разработчиков** — в среднем около $470 на автора. Топ-авторы получают больше $10K MRR, «многие» — больше $1K в месяц ([Apify Partners](https://apify.com/partners/actor-developers), 2026-08; [AgentByline](https://agentbyline.com/articles/apify-actor-passive-income-what-really-earns-in-2026-67lcfr), 2026).
   - Автор получает **80%** выручки. Выплаты ежемесячно, **банковским переводом (от $100) или PayPal (от $20)** ([Apify Help](https://help.apify.com/en/articles/10057167-how-developer-payouts-work), 2026).
   - Каждый Actor автоматически доступен агентам через MCP-сервер Apify.
   - **Это рабочий аналог «калькуляторной» модели для агентов (тип B).**
36. **Stripe Machine Payments Protocol (MPP), 18.03.2026 (вместе с Tempo).**
   - Агент платит за вызов API или MCP. Поддерживаются стейблкоины и **фиат через Shared Payment Tokens (карты, BNPL)**. На Sessions (29–30.04.2026) добавлены потоковые платежи ([Stripe Blog](https://stripe.com/blog/machine-payments-protocol), 2026-03-18; [WorkOS](https://workos.com/blog/x402-vs-stripe-mpp-how-to-choose-payment-infrastructure-for-ai-agents-and-mcp-tools-in-2026), 2026).
   - Cloudflare Agents SDK даёт `paidTool` для x402 и MPP ([Cloudflare Docs](https://developers.cloudflare.com/agents/x402/charge-for-mcp-tools/), 2026).
   - **x402 Foundation** запущен под LF 14.07.2026, в нём 40 компаний; Stripe интегрировал x402 на Base в 02.2026 ([Eco](https://eco.com/support/en/articles/14845480-mcp-and-payments-a-2026-guide), 2026).
   - **Для основателя (UK Ltd, Payoneer)** фиатный путь через Stripe реалистичнее USDC. Возможность открыть Stripe на UK Ltd при резидентстве на Бали отдельно не проверял (оценка, средняя).
37. **Практика pay-per-call пока провальна:**
   - Godberry Studios запустила Content-to-Social MCP за $0,07 за операцию (12.04.2026) и **через две недели имела ноль платящих пользователей** ([Godberry](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/), 2026-04);
   - APIbase.pro — 263 инструмента от 74 провайдеров и лишь **1 700+ оплаченных через x402 вызовов**. Мейнтейнеры MCP по платёжному слою не ответили ([GitHub Discussion #2436](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/2436), 2026-03…09);
   - заявление 21st.dev про «$10K MRR за 6 недель» остаётся неверифицированным. Из проверяемого: Magic MCP запущен в 03.2025 после беты с 4K тестировщиков, **50% выручки идёт авторам компонентов** ([X @serafimcloud](https://x.com/serafimcloud/status/1897641079131746725), 2025-03).
38. **ChatGPT Apps:**
   - **2 289 приложений от 2 007 разработчиков (08.2026)**, у 95,6% сторонних разработчиков ровно одно приложение ([Node8](https://node8.ai/ai-connectors/chatgpt/), 2026-08). Были 1 624 на 02.07.2026 ([ChatGPTAppsRank](https://chatgptappsrank.com/state-of-chatgpt-apps-2026), 2026-07-16).
   - По-прежнему **запрещено продавать цифровые товары, подписки и in-app услуги**. Разрешён внешний checkout только для физических товаров; payment sheet — у избранных маркетплейсов ([OpenAI Apps SDK: Monetization](https://developers.openai.com/apps-sdk/build/monetization), 2026).
   - Приложения включает пользователь, ассистент их органически не предлагает ([Nicolas Sitter](https://www.nicolassitter.com/research/mcp-apps-census-2026), 2026). **Каталог ChatGPT — витрина без монетизации и без органического трафика.**
39. **Платные skills:** площадки заявляют 70–80% автору (Agensi — 70/30). Медианный листинг приносит **меньше $50 в месяц**, топовые — $500–3 000 ([Agensi](https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026), 2026). Это маркетинг площадки, уверенность низкая. Независимых данных о выручке от skills нет.
40. **Cursor и Cline.** Cursor v3.10 (30.06.2026) добавил Team MCP и группы в командных маркетплейсах: плагины — это бандлы из MCP, skills, субагентов и хуков, режимы Default Off, Default On и Required ([Cursor Changelog](https://cursor.com/changelog/team-marketplace-updates), 2026-06-30). В MCP Marketplace Cline 700+ серверов (03.2026) ([Cline](https://cline.bot/mcp-marketplace), 2026). **Выплат авторам нет ни там, ни там.**

### F. Безопасность: цифры

41. **Отравление инструментов (tool poisoning):**
   - в академическом исследовании (Hasan и др.) признаки отравления у **5,5% из 1 899 серверов**;
   - скан AgentSeal: находки безопасности у **66% из 1 808 серверов**;
   - бенчмарк MCPTox на 45 живых серверах: средний успех атаки **36,5%**, максимум 72,8%;
   - у YARA-сканеров ~78% ложных срабатываний.
   ([Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/), 2026; [MCPTox, arXiv](https://arxiv.org/pdf/2508.14925), 2025-08; [CSA Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-auto-execution-20260701/), 2026-07-01.) **Корпоративные покупатели выбирают вендорские или верифицированные коннекторы.** Анонимный инди-MCP в студию крупного бренда не пустят без аудита.

### G. Агентная реклама и DOOH (для идеи «DOOH Spec MCP»)

42. **AdCP (Ad Context Protocol) построен на MCP.**
   - Запущен 15.10.2025. Основатели: PubMatic, Scope3, Swivel, Triton Digital, Optable, Yahoo, плюс 23 участника запуска ([Digiday](https://digiday.com/media-buying/wtf-ad-context-protocol/), 2025-10).
   - В AgenticAdvertising.org 116+ компаний ([Star Insights](https://star.global/posts/agentic-advertising-standards-adcp-and-aamp/), 2026).
   - **Creative Protocol даёт MCP-инструменты `list_creative_formats`, `build_creative` и `preview_creative`.** Референсный creative agent поддерживает **38 форматов, включая DOOH**, издатели могут определять свои форматы ([AdCP Docs](https://docs.adcontextprotocol.org/docs/creative/formats), 2026; [GitHub adcontextprotocol/creative-agent](https://github.com/adcontextprotocol/creative-agent), WebFetch 2026-09-26: 3★, **3D и анаморфные экраны не упоминаются**).
43. **Агентный DOOH уже в работе:**
   - **Displayce** на Cannes Lions открыл набор агентов через MCP: бриф → медиаплан с подбором экранов ([ExchangeWire](https://www.exchangewire.com/blog/2026/06/29/displayce-launches-its-agentic-dooh-offering-a-suite-of-agents-available-via-mcp/), 2026-06-29);
   - **Broadsign**, Global Netherlands и Draft Digital провели полностью агентную OOH-кампанию, включая креатив и согласования ([Street Fight](https://streetfightmag.com/2026/06/25/broadsign-and-partners-execute-fully-agentic-ooh-campaign/), 2026-06-25);
   - seller-агент **VIOOH** обработал 100+ запросов на DOOH-пакеты в I полугодии 2026 года ([Star Insights](https://star.global/posts/agentic-advertising-standards-adcp-and-aamp/), 2026).
   - **Но денег через агентные протоколы идёт «очень мало»** — CTO Adform, 23.09.2026 ([PPC Land](https://ppc.land/neither-of-ad-techs-two-ai-agent-protocols-runs-at-scale-adform-cto-says/), 2026-09-23).
   - В официальном реестре DOOH-сервер по-прежнему один — Trillboards, v1.1.0 от 12.03.2026 ([Registry API](https://registry.modelcontextprotocol.io/v0/servers?search=dooh), запрос 2026-09-26).

---

## Заполненные пробелы (по пунктам брифа)

| Пункт брифа | Было в оригинале | Что добавлено |
|---|---|---|
| Принятие MCP: OpenAI, Google, Microsoft | только AAIF | Хронология 03.2025 → 04.2025 → 05.2025 → 12.2025; AAIF 170+ участников (п. 19–20) |
| Серверы в реестрах | вторичные цифры 05.2026 | Glama 92K, PulseMCP ~22K, Smithery → Arcade, официальный реестр подтверждён (п. 7) |
| Adobe: агентные анонсы MAX 2025 | не было | Express Assistant (публичная бета), Ps Assistant (закрытая), Project Moonlight; Adobe в ChatGPT 10.12.2025 (п. 22) |
| Adobe: AE | «не перепроверено» | Публичная бета на IBC 09.2026, бесплатно в бете, MCP-архитектура (п. 3) |
| Figma MCP (Dev Mode, remote) | функции | Лимиты 200/600 вызовов в день; MCP не тратит кредиты; агент уходит в GA с кредитами (п. 25) |
| Blender MCP (звёзды) | 29 360★ | 29,4K★ подтверждено; **патронаж Anthropic отменён** (п. 1, 13) |
| AE MCP: community | 72 репозитория, лидеры | Платные: Synthetic ($29, $15 в месяц), MotionAmigo, NodeFlow, Higgsfield; aftr (п. 32) |
| Premiere, Resolve, C4D, Unreal, Unity | частично | Resolve — нативный MCP с 88 инструментами (Studio $295); UE 5.8 и Unity — официальные MCP; у C4D официального нет (п. 10, 28) |
| Canva (MCP, ChatGPT) | ChatGPT-app | Canva MCP и AI Connector; Canva Free в ChatGPT с 03.06.2026; **Cavalry бесплатный** (п. 27) |
| Каталог ChatGPT и Apps SDK | вторично | 2 289 приложений, 2 007 разработчиков; цифровые товары запрещены; Developer Mode на Plus и Pro (п. 4, 38) |
| Каталог коннекторов Claude | 850 + 340 | 1 375 по переписи; «2 000+» по Anthropic; портал без revenue share (п. 8) |
| Маркетплейсы skills | skills.sh вторично | skills.sh ~670K skills; Remotion skill 126K установок; Agensi 70/30; ClawHub 824–900 вредоносных (п. 15–16, 31, 39) |
| Маркетплейсы Cursor и Cline | нет | Командные маркетплейсы Cursor (06.2026), Cline 700+; выплат нет (п. 40) |
| Платные MCP: Stripe, x402, Apify | вторично | Выплаты Apify $1,4–1,5 млн в месяц; Stripe MPP (фиат); x402 — аудит TRM: агентный объём $5–11K в месяц (п. 5, 35–37) |
| Кто платит | тезис | Корпорации за governance: Arcade $60M, Runlayer $30M A; Adobe и Blackmagic — за доступ агента через подписку (п. 10, 21, 24) |
| Безопасность | инциденты | Статистика: 5,5%, 66%, 36,5% ASR (п. 41) |
| mcp.so | 19,7K (вторично) | **свежих данных нет** |
| Реальная выручка creative-MCP или skills | нет | **Нет ни одного проверяемого числа.** Лучший прокси — выплаты Apify (п. 35), но это данные и скрейпинг, а не креатив |

---

## Обновлённые сценарии и сигналы

Новые данные меняют сценарии по двум осям. Во-первых, **встраивание агентов в приложения идёт быстрее**: Adobe AE Assistant в публичной бете, Resolve с нативным MCP, UE 5.8, Unity и Figma. Во-вторых, **платный рынок инструментов за вызов медленнее**: агентный объём x402 — $5–11K в месяц на всю экосистему, у ChatGPT и Claude нет revenue share. Поэтому пересчитываю вероятности.

| | Базовый: «агенты да, платного рынка коннекторов нет» | Быстрый: «агенты рулят приложениями + микрорынок платных инструментов» | Медленный: «ассистенты, а не агенты» |
|---|---|---|---|
| **Было** | 55% | 25% | 20% |
| **Стало** | **65%** | **20%** | **15%** |
| **Почему** | Все крупные креативные платформы выпустили своих агентов или MCP в 2026 году; деньги за вызов не текут | Встраивание агентов подтверждается, а микрорынок платежей нет (TRM, Godberry, APIbase) | Публичная бета AE Assistant и нативный MCP в Resolve снижают шанс застоя |
| **12 мес (09.2027), что добавить** | AE Assistant в GA на кредитах CC (оценка: 70%, средняя). AE UXP в публичной бете с 11.2026, первые AI-плагины на UXP. Figma agent тратит кредиты. Базовая функциональность AE-агентов ($0–29) вытеснена встроенным ассистентом | Adobe открывает AE Assistant внешним агентам (MCP-endpoint как в Ai Beta) и добавляет AE в коннектор «Adobe for creativity» | Adobe держит AE Assistant в бете и вводит жёсткие лимиты |
| **24 мес (09.2028)** | Приём CEP в AE закрыт, CEP выключен по умолчанию (12.2028): волна миграции и вымирание части старых панелей. Шаблонный моушн уходит в Remotion и HyperFrames | Выплаты Apify и похожих площадок растут; появляются креативные «actors» | — |
| **Новые сигналы** | ① цена AE Assistant в GA (HelpX, Adobe Community) ② появление AE в коннекторе Adobe ③ UXP-бета AE в срок (11.2026) | ① агентный объём x402 или MPP по отчётам TRM и Chainalysis > $1 млн в месяц ② OpenAI разрешает цифровые товары в Apps SDK ③ Anthropic вводит платные плагины | ① AE Assistant в бете дольше 12 месяцев ② новые скандалы вроде Blender и Anthropic (сообщество против AI) |

**Как мониторить (добавить к списку оригинала):**
- TRM Labs и Chainalysis — квартальные отчёты по агентным платежам (базовая точка — $5–11K в месяц, 09.2026).
- Страница выплат Apify (базовая точка — $1,4–1,5 млн в месяц, 08.2026).
- Страница [Monetization в Apps SDK](https://developers.openai.com/apps-sdk/build/monetization) — появятся ли цифровые товары.
- aescripts, категория AI: сколько новых AE-агентов в месяц (базовая точка — 10+ продуктов, п. 32).
- Форматы AdCP: появятся ли 3D и анаморфные DOOH-форматы.

---

## Идеи-кандидаты: новые и уточнённые

Общий вывод оригинала подтвердился и стал жёстче. **«MCP или агент для AE» как продукт — это красный океан:** 10+ продуктов по $0–29 и бесплатный встроенный ассистент Adobe. **Платёжные рельсы для агентов почти пусты.** Деньги достаются тому, у кого (а) узкая глубина, которую платформы не делают, (б) данные с проверяемой свежестью или (в) связь с физическим миром и сервисом.

### 1. (Уточнено) Oblique Agent Mode: Figma → AE через MCP, но как функция Oblique, а не отдельный продукт
- **Суть:** бесплатный MCP и skill поверх платной лицензии Oblique, чтобы агент (Claude Code, Codex, Figma agent) переносил фреймы Figma в AE с точностью стекла и блюров.
- **Тип:** A. **Формат:** расширение плагина; публикация в официальном Registry, в портале плагинов Claude и на aescripts.
- **Покупатель и боль:** моушн-дизайнеры, получающие макеты, которые собрал агент в Figma. Нужна точная пересборка эффектов в AE.
- **Новые доказательства:**
  - чтение Figma через MCP не тратит AI-кредиты, лимит — 200 вызовов в день на Pro seat (п. 25), то есть дешёвый вход для агента;
  - агентные AE-продукты уже продают «Figma → AE» как функцию (MotionAmigo, OnePrism, Higgsfield: «recreate a design from reference», п. 32).
- **Конкуренты и цены:**
  - Prism (Next Horizon) — от $39 разово;
  - UI Flow — free или lifetime;
  - DEmotion — нет данных;
  - Overlord — лицензия с годом обновлений;
  - AEUX — бесплатно;
  - Synthetic AE MCP — $29, $15 в месяц;
  - AE GPT — $29.
- **Гипотеза рва:** точность рендера сложных эффектов и скорость реакции на изменения Figma API. MCP — только канал.
- **Главный риск:** Adobe AE Assistant с импортом Figma (в Illustrator Beta уже есть MCP) или Figma Motion → экспорт в AE от самой Figma.
- **Готовность платить:** за Oblique — средняя, за MCP-слой — ноль. **Делать (1–2 недели), но не ждать отдельной выручки.**

### 2. (НОВАЯ) «Figma Motion → After Effects»: перенос анимации, а не только макета
- **Суть:** конвертер анимаций Figma Motion (ключи, easing, пресеты, переменные) в нативные ключи и expressions AE, чтобы UI-анимацию из Figma можно было доработать в AE (композитинг, 3D, звук, рендер под DOOH и соцсети).
- **Тип:** A. **Формат:** модуль Oblique или отдельный плагин на aescripts ($29–49, оценка) плюс бесплатный MCP-инструмент.
- **Покупатель и боль:**
  - продуктовые команды анимируют в Figma Motion (открытая бета на всех планах с 24.06.2026);
  - моушн-студии получают «почти готовую» анимацию и собирают её в AE заново.
- **Доказательства спроса (прокси):**
  - Figma Motion экспортирует JSON, CSS, React, MP4 и GIF, но **не AE** (п. 26);
  - готового моста в поиске не нашлось (нет данных);
  - спрос на Figma → AE подтверждают 6+ конкурентов Oblique (п. 33).
  Прямых данных о спросе (форумы, Reddit) нет: Reddit не индексируется.
- **Конкуренты:** прямых нет (нет данных). Косвенные: экспорт Lottie и LottieFiles Creator MCP (п. 29).
- **Гипотеза рва:** первая точная реализация, привязанная к формату Figma Motion. Скорость обновлений при изменениях Figma: формат в бете и будет меняться. Экспертиза основателя в easing и AE.
- **Главный риск:** Figma или Adobe сделают экспорт сами. Формат JSON Figma Motion может закрыться или меняться каждый месяц, и поддержка тогда не уложится в 2–4 часа в неделю.
- **Платформенный риск:** высокий. **Проверка:** за 1 неделю выяснить, стабилен ли JSON-экспорт Figma Motion и насколько полно он описывает кривые.

### 3. (Уточнено) Спецификации 3D и анаморфных DOOH-экранов как «кастомные форматы AdCP» + preflight + лиды для студии
- **Суть:** закрыть то, чего нет в стандарте: 3D и анаморфные экраны (геометрия, точка обзора, разрешение, fps, кодеки, лимиты). Данные публикуются как:
  - кастомные форматы AdCP через `list_creative_formats`;
  - бесплатный MCP;
  - SEO-страницы;
  - платный preflight-отчёт.
  Главная цель — лиды для студии анаморфных билбордов.
- **Тип:** AB. **Формат:** база данных (B) + студия и 3D-команда (A).
- **Покупатель и боль:** агентства и медиабайеры, чьи агенты (Displayce, Broadsign, VIOOH) уже планируют DOOH. Для 3D и анаморфа в AdCP спецификаций нет.
- **Новые доказательства:**
  - AdCP creative agent: 38 форматов с DOOH, но без 3D и анаморфа (п. 42);
  - агентный DOOH запущен у Displayce, Broadsign и VIOOH (п. 43).
- **Контр-доказательство:** «очень мало денег» проходит через агентные протоколы (Adform, 23.09.2026). Поэтому монетизировать надо через студию, а не через MCP.
- **Конкуренты и цены:** AdCP reference creative agent — бесплатно, open source; Trillboards — free tier; Displayce — корпоративный, цена нет данных; BDOOH и DOOH Marketing — бесплатные гайды.
- **Гипотеза рва:** физический мир (реальные кампании студии и связи с операторами), 3D-экспертиза, свежесть данных, ранний вход в стандарт.
- **Главный риск:** операторы сами опубликуют форматы в AdCP; рынок 3D DOOH мал.
- **Готовность платить:** за данные — низкая; за preflight перед дорогим размещением и за продакшн — средняя или высокая. **Рекомендация:** MVP за 2 недели как лидогенератор студии.

### 4. (НОВАЯ) Портфель Apify Actors для креативных и рекламных данных
- **Суть:** 5–10 «actors» (скрейперы и нормализаторы) с оплатой за результат на Apify Store. Кандидаты:
  - публичные библиотеки рекламы и креативные спецификации площадок;
  - каталоги DOOH-экранов;
  - цены и обновления плагинов и шаблонов (aescripts, Motion Array — проверить ToS);
  - трендовые форматы и музыка.
  Каждый actor автоматически доступен агентам через MCP Apify.
- **Тип:** B, с элементом A в выборе ниш.
- **Формат:** Actors на Apify. Сборка через Claude Code — 1–2 недели на пачку.
- **Покупатель и боль:** агентства, маркетологи и разработчики агентов, которым нужны свежие структурированные данные без собственной инфраструктуры.
- **Доказательства спроса:**
  - выплаты Apify **$1,4–1,5 млн в месяц на ~3 000 авторов (08.2026)**, рост около ×2,6 за 11 месяцев с $563K;
  - топ-авторы получают больше $10K MRR, 80% выручки идёт автору (п. 35);
  - выплаты банком или PayPal. Совместимость с Payoneer — оценка, средняя: вероятно, через банковские реквизиты Payoneer.
- **Конкуренты и цены:** тысячи actors в Store, по нишам основателя нет данных. Прокси: даже для каталога Smithery уже есть платный scraper-actor ([Apify](https://apify.com/maximedupre/smithery-mcp), 2026).
- **Гипотеза рва:** скорость починки при изменении сайтов, выбор узких ниш, где основатель понимает ценность данных, накопленные отзывы и рейтинг в Store.
- **Главный риск:**
  - скрейперы ломаются, и поддержка может превысить 4 часа в неделю;
  - юридические риски ToS;
  - медиана заработка скромная (около $470 в среднем, распределение перекошено).
- **Платформенный риск:** средний. Apify может поменять комиссию.

### 5. (НОВАЯ) CEP → UXP: skill-пак и сервис миграции для разработчиков AE-плагинов
- **Суть:** набор Claude Code skills и чек-листов «мигрировать CEP-панель AE на UXP» плюс платная миграция под ключ через агента. Окно — с ноября 2026 года (UXP-бета AE) до декабря 2028 года (CEP выключен по умолчанию в AE).
- **Тип:** A (экосистема Adobe и опыт выпуска Oblique). Код пишет Claude Code, основатель проверяет результат в AE.
- **Формат:**
  - бесплатный skill-пак на GitHub и skills.sh как воронка;
  - платная миграция $500–3 000 за плагин (оценка, низкая уверенность);
  - сначала на собственном Oblique как кейс.
- **Покупатель и боль:** небольшие авторы плагинов на aescripts и Adobe Exchange. Для них миграция — нежеланная работа, а CEP исчезнет из новых версий с 12.2029 (п. 14). Для Photoshop приём новых CEP закрывается уже в 03.2027.
- **Доказательства спроса:**
  - жёсткий таймлайн Adobe (п. 14);
  - на форуме Adobe есть ветка «Should developers stop building CEP plugins?» ([Adobe Community](https://community.adobe.com/questions-606/cep-uxp-roadmap-should-developers-stop-building-cep-plugins-and-what-happens-to-existing-ones-1614807), 2026).
  - Число CEP-плагинов для AE — нет данных. Прокси: в агрегаторе AnyPlugins ~1 363 инструмента для AE (не только CEP) ([AnyPlugins](https://anyplugins.com/after-effects), 2026).
- **Конкуренты и цены:**
  - официальные гайды Adobe «UXP for CEP developers» — бесплатно;
  - Hyper Brew (фреймворки и инструменты для Adobe, в том числе Klutz GPT) — цены консалтинга нет данных. Наличие у них UXP-фреймворка «Bolt UXP» — по памяти, не проверено.
- **Гипотеза рва:** ранний вход, кейсы, репутация в сообществе aescripts, накопленные skills по граблям UXP в AE.
- **Главный риск:** Adobe выпустит автоконвертер; рынок маленький (оценка: сотни, а не тысячи клиентов); это сервис, а не пассивный продукт.
- **Вердикт:** держать как временную возможность на 2027–2028 годы. Не приоритет, но skill-пак дешёвый.

### 6. (Уточнено) Delivery QC Agent: проверка экспорта с оплатой за отчёт
- **Что изменилось:**
  - в Resolve 21.1 88 MCP-инструментов для рендера и экспорта, но QC нет (п. 10);
  - в AE Assistant QC тоже не заявлен (п. 3);
  - платить за отчёт теперь можно через Stripe MPP в фиате (п. 36).
- **Тип:** AB. **Формат:** CLI и MCP на ffprobe + веб-отчёт; $15–29 в месяц или $1–3 за отчёт (оценка, низкая).
- **Конкуренты:** MediaInfo и ffprobe (бесплатно), Telestream Vidchecker и Interra Baton (enterprise, цены нет данных).
- **Главный риск:** не изменился — низкая готовность платить у фрилансеров, Frame.io или Media Encoder добавят проверки. **Сначала опрос 10 студий.**

### 7. (Уточнено) Brand Motion Skills: только как B2B-сервис, не как продукт в маркетплейсе skills
- **Что изменилось:**
  - платные skills в маркетплейсах в медиане приносят меньше $50 в месяц (маркетинг Agensi, п. 39);
  - бесплатные мотион-skills растут: Remotion — 126K установок, HyperFrames — 21 skill, LobzyJay — 4 skills;
  - теперь есть куда встраивать бренд-skills: AE Assistant, Figma skills, Remotion и HyperFrames.
- **Тип:** A. **Формат:** настройка моушн-системы бренда под агентные стеки (Figma, Remotion или HyperFrames, AE Assistant) по фиксированной цене. Оценка: $2–10K, уверенность низкая.
- **Вердикт:** это продолжение студийного сервиса. В «портфель самоокупаемых продуктов» не подходит.

### Изменения приоритета относительно оригинала
1. **№1 (Oblique Agent Mode)** — делать, как функцию.
2. **№2 (Figma Motion → AE)** — новая проверка на 1 неделю: самый сильный кандидат типа A в этом потоке, если формат стабилен.
3. **№3 (3D/анаморф DOOH + AdCP)** — делать как лидогенератор студии.
4. **№4 (Apify Actors)** — лучший кандидат типа B с доказанными выплатами.
5. №5 и №6 — проверить спрос. №7 — только сервис.
6. **Отдельный платный AE-агент или MCP — не делать** (подтверждено: 10+ конкурентов по $0–29 и бесплатный Adobe).

---

## Источники

1. CG Channel — AE 26.5 и AI Assistant beta, https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/ (2026-09)
2. RedShark News — AE AI Assistant enters public beta (IBC2026), https://www.redsharknews.com/after-effects-ai-assistant-ibc2026 (2026-09)
3. Creative COW — Adobe adds an AI Assistant (MCP) to AE Beta, https://creativecow.net/forums/thread/adobe-adds-an-ai-assistant-mcp-to-after-effects-beta-private-beta/ (2026-08)
4. Adobe Community — New in AE Beta: AI Assistant, https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658 (2026-09)
5. Adobe HelpX — AE AI Assistant overview, https://helpx.adobe.com/after-effects/desktop/work-with-after-effects-ai-assistant/after-effects-ai-assistant-overview.html (2026-09)
6. Adobe Blog — Premiere & AE IBC innovations, https://blog.adobe.com/en/publish/2026/09/08/generate-create-directly-in-your-timeline-with-new-ai-powered-innovations-in-premiere-after-effects (2026-09-08)
7. Adobe Newsroom — Creative Agent expansion, https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion (2026-06-18)
8. Adobe Newsroom — New Creative Agent, https://news.adobe.com/news/2026/04/adobe-new-creative-agent (2026-04)
9. Adobe Newsroom — MAX 2025 Creative Cloud, https://news.adobe.com/news/2025/10/adobe-max-2025-creative-cloud (2025-10-28)
10. Adobe Blog — Our view on agentic AI, https://blog.adobe.com/en/publish/2025/10/28/our-view-agentic-ai-assistants-that-work-you-in-your-favorite-apps (2025-10-28)
11. Adobe Newsroom — Photoshop, Express, Acrobat in ChatGPT, https://news.adobe.com/news/2025/12/adobe-photoshop-express-acrobat-chatgpt (2025-12-10)
12. TechCrunch — Adobe brings Photoshop, Express, Acrobat to ChatGPT, https://techcrunch.com/2025/12/10/adobe-brings-photoshop-express-and-acrobat-features-to-chatgpt/ (2025-12-10)
13. Adobe Blog — Adobe for creativity connector, https://blog.adobe.com/en/publish/2026/04/28/adobe-for-creativity-connector (2026-04-28)
14. 9to5Mac — 9 Claude connectors for creative tools, https://9to5mac.com/2026/04/28/anthropic-releases-9-new-claude-connectors-for-creative-tools-including-blender-and-adobe/ (2026-04-28)
15. XDA — Claude + Adobe without paying for CC, https://www.xda-developers.com/integrated-claude-with-adobe-without-paying-for-creative-cloud/ (2026)
16. Adobe HelpX — MCP server in Illustrator, https://helpx.adobe.com/in/illustrator/desktop/connect-with-other-apps-and-tools/about-using-ai-tools-with-illustrator.html (2026)
17. GitHub — ie3jp/illustrator-mcp-server, https://github.com/ie3jp/illustrator-mcp-server (2026-09)
18. Adobe Community — Premiere AI Assistant public beta, https://community.adobe.com/announcements-727/meet-your-new-assistant-editor-ai-assistant-in-premiere-pro-is-now-in-public-beta-1629317 (2026-06)
19. JustCreative — Adobe CC pricing guide (credits), https://justcreative.com/adobe-creative-cloud-photoshop-illustrator-cost/ (2026-09)
20. Adobe Developer Blog — UXP comes to flagship applications, https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications (2026-09)
21. Adobe Community — CEP/UXP roadmap thread, https://community.adobe.com/questions-606/cep-uxp-roadmap-should-developers-stop-building-cep-plugins-and-what-happens-to-existing-ones-1614807 (2026)
22. Figma Developer Docs — MCP rate limits & access, https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/ (2026)
23. Figma Help — AI credit updates FAQ, https://help.figma.com/hc/en-us/articles/42614902212887-AI-credit-updates-FAQ (2026-08-25)
24. UIChemy — Figma AI credits explained, https://uichemy.com/blog/figma-ai-credits/ (2026)
25. CMSWire — Figma launches Code Layers & Motion, https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/ (2026-06)
26. MakerStack — Figma Motion review, https://makerstack.co/reviews/figma-motion-review/ (2026)
27. Canva Newsroom — Canva in ChatGPT & MCP server, https://www.canva.com/newsroom/news/deep-research-integration-mcp-server/ (2026)
28. Krumzi — Design in ChatGPT 2026, https://www.krumzi.com/blog/design-in-chatgpt (2026)
29. CG Channel — Canva makes Cavalry free, https://www.cgchannel.com/2026/04/canva-makes-motion-graphics-and-animation-app-cavalry-free/ (2026-04)
30. CNBC — Canva acquires Cavalry and MangoAI, https://www.cnbc.com/2026/02/23/canva-acquires-cavalry-for-motion-graphics-and-mangoai-for-video-ads.html (2026-02-23)
31. CG Channel — Anthropic patronage downgraded, https://www.cgchannel.com/2026/05/anthropics-patronage-of-blender-downgraded-to-one-off-donation/ (2026-05)
32. BlenderNation — Update: Anthropic and Blender Development Fund, https://www.blendernation.com/2026/05/01/update-anthropic-joins-the-blender-development-fund/ (2026-05-01)
33. Blender.org — Development Fund and AI policies, https://www.blender.org/news/upcoming-blender-development-fund-and-ai-policies/ (2026-05)
34. Digital Production — Anthropic funds Blender, ships connector, https://digitalproduction.com/2026/04/30/anthropic-funds-blender-ships-claude-connector/ (2026-04-30)
35. GitHub — ahujasid/blender-mcp (29,4K★), https://github.com/ahujasid/blender-mcp (WebFetch 2026-09-26)
36. GitHub — Dakkshin/after-effects-mcp (657★), https://github.com/Dakkshin/after-effects-mcp (WebFetch 2026-09-26)
37. CineD — DaVinci Resolve 21.1 MCP, https://www.cined.com/davinci-resolve-21-1-released-ai-assistant-integration-via-mcp-individual-hdr-trims-and-python-scripting-moves-to-studio/ (2026-09)
38. Digital Production — Resolve 21.1 adds MCP, https://digitalproduction.com/2026/09/08/resolve-21-1-adds-mcp-and-finally-gets-presets/ (2026-09-08)
39. byteiota — Resolve 21.1 native MCP server (88 tools), https://byteiota.com/davinci-resolve-21-1-mcp-server/ (2026-09)
40. Unity Blog — Unity MCP server, https://unity.com/blog/unity-ai-mcp-how-to-get-started (2026)
41. Ludus AI — Unreal MCP plugin UE 5.8, https://ludusengine.com/blog/unreal-mcp-plugin-ue5-8-setup (2026)
42. StraySpark — Unity vs Unreal vs Godot vs Blender MCP, https://www.strayspark.studio/blog/unity-mcp-server-vs-unreal-godot-blender-2026 (2026-08)
43. Jon Peddie Research — Integrated AI in Cinema 4D, https://www.jonpeddie.com/news/integrated-ai-feature-coming-to-cinema-4d/ (2026)
44. LottieFiles — Lottie Creator MCP, https://lottiefiles.com/tutorials/lottie-creator/lottie-creator-mcp-create-animations-with-your-favorite-ai-assistants-vs6LnaDzYAL (2026-04)
45. GitHub — heygen-com/hyperframes (53,1K★), https://github.com/heygen-com/hyperframes (WebFetch 2026-09-26)
46. Remotion Docs — Agent Skills, https://www.remotion.dev/docs/ai/skills (2026)
47. AI Vid Pipeline — Remotion Agent Skills guide 2026, https://aividpipeline.com/blog/remotion-agent-skills-guide-2026 (2026)
48. Remotion — License & Pricing, https://www.remotion.dev/docs/license/pricing (2026)
49. GetLatka — Remotion revenue (оценка), https://getlatka.com/companies/remotion.dev (2026)
50. Motionpilot — After Effects alternatives 2026, https://motionpilot.app/blog/after-effects-alternatives (2026)
51. aescripts — AE GPT, https://aescripts.com/ae-gpt/ (2026)
52. AnyPlugins — AE GPT ($29 lifetime), https://anyplugins.com/plugin/ae-gpt (2026)
53. Claude Scripter, https://claudescripter.com/ (2026)
54. Hyper Brew — Klutz GPT, https://hyperbrew.co/tools/klutz-gpt/ (2026)
55. aescripts — MotionAmigo, https://aescripts.com/motionamigo/ (2026-07-14)
56. Synthetic — After Effects MCP ($29, $15 в месяц, $120 в год), https://synthetic.com.ar/ae-mcp (2026)
57. NodeFlow — AE AI Agent, https://aeai.nodeflow.studio/ (2026)
58. OnePrism — After Effects MCP Server, https://oneprism.io/ (2026)
59. Official MCP Registry — io.oneprism/after-effects v1.4.0, https://registry.modelcontextprotocol.io/v0/servers?search=oneprism (запрос 2026-09-26)
60. Higgsfield Blog — Higgsfield inside After Effects, https://higgsfield.ai/blog/higgsfield-after-effects (2026-07-21)
61. No Film School — Higgsfield plugins for Premiere & AE, https://nofilmschool.com/higgsfield-adobe-ai-plugin (2026)
62. Creative AI News — aftr (Show HN), https://www.creativeainews.com/articles/aftr-after-effects-claude-code-mcp-2026/ (2026-07)
63. Adobe Exchange — AI Assistant for After Effects (3rd party), https://exchange.adobe.com/apps/cc/203667/ai-assistant-for-after-effects (2026)
64. Next Horizon — Prism store (from $39), https://nexthorizon.art/store/figma-to-ae (2026)
65. Next Horizon — AEUX vs Overlord vs Prism (самореклама), https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma (2026)
66. Figma Community — Prism plugin, https://www.figma.com/community/plugin/1648737738684655034/prism (2026)
67. AE Flow Tools — UI Flow, https://www.aeflowtools.com/uiflow (2026)
68. DEmotion, https://trydemotion.com/ (2026)
69. GitHub — LobzyJay/motion-design-with-claude, https://github.com/LobzyJay/motion-design-with-claude (WebFetch 2026-09-26)
70. The New Stack — Why MCP won, https://thenewstack.io/why-the-model-context-protocol-won/ (2026)
71. Wikipedia — Model Context Protocol, https://en.wikipedia.org/wiki/Model_Context_Protocol (2026-09)
72. IntuitionLabs — Agentic AI Foundation guide (170+ members), https://intuitionlabs.ai/articles/agentic-ai-foundation-open-standards (2026-04)
73. Linux Foundation — AAIF formation, https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation (2025-12)
74. MCP Blog — 2026-07-28 Release Candidate, https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ (2026)
75. Claude Blog — MCP 2026-07-28 coming to Claude, https://claude.com/blog/bringing-mcp-2026-07-28-to-claude (2026)
76. jahanzaib.ai — MCP 97M installs (Dev Summit), https://www.jahanzaib.ai/blog/mcp-97-million-installs-dev-summit-2026 (2026)
77. GitHub — SEP-2007 issue #2008, https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2008 (2026-09)
78. Glama — MCP servers (92 121), https://glama.ai/mcp/servers (2026-09)
79. PulseMCP — Server directory (~21,8–22,3K), https://www.pulsemcp.com/servers (2026-09)
80. tooldirectory.ai — State of MCP servers 2026, https://tooldirectory.ai/blog/state-of-mcp-servers-2026 (2026)
81. Unyly — MCP directories compared, https://unyly.org/mcp-directories (2026)
82. Forbes — Arcade acquires Smithery, https://www.forbes.com/sites/janakirammsv/2026/08/10/arcade-acquires-smithery-to-own-the-agent-tool-supply-chain/ (2026-08-10)
83. bex.co — MCP registry discoverability (9 652 записи на 24.05), https://bex.co/blog/2026/07/10/mcp-registry-discoverability-trust (2026-07-10)
84. Nicolas Sitter — MCP apps census 2026, https://www.nicolassitter.com/research/mcp-apps-census-2026 (2026-07/08)
85. Node8 — ChatGPT Apps Directory (2 289 apps), https://node8.ai/ai-connectors/chatgpt/ (2026-08)
86. ChatGPTAppsRank — State of ChatGPT Apps 2026, https://chatgptappsrank.com/state-of-chatgpt-apps-2026 (2026-07-16)
87. OpenAI — Apps SDK Monetization, https://developers.openai.com/apps-sdk/build/monetization (2026)
88. OpenAI Help — Developer mode and MCP apps, https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt (2026)
89. Coworker AI — ChatGPT MCP plans 2026, https://coworker.ai/blog/chatgpt-mcp (2026)
90. Claude Blog — Claude Marketplace, https://claude.com/blog/claude-marketplace (2026-09-23)
91. Unite.AI — Claude plugin directory submission portal, https://www.unite.ai/anthropic-opens-directory-submission-portal-for-claude-plugins/ (2026-09-25)
92. SiliconANGLE — Agent Skills open standard, https://siliconangle.com/2025/12/18/anthropic-makes-agent-skills-open-standard/ (2025-12-18)
93. Rajeev Pentyala — skills.sh, https://rajeevpentyala.com/2026/06/16/discover-and-install-agent-skills-with-skills-sh/ (2026-06-16)
94. Ry Walker — skills.sh research, https://rywalker.com/research/skills-sh (2026)
95. Agensi — AI agent skills marketplaces 2026, https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026 (2026)
96. Cursor Changelog — Team marketplaces & Team MCP, https://cursor.com/changelog/team-marketplace-updates (2026-06-30)
97. Cline — MCP Marketplace, https://cline.bot/mcp-marketplace (2026)
98. Apify — Actor developers partner page, https://apify.com/partners/actor-developers (2026-08)
99. Apify Help — Developer payouts, https://help.apify.com/en/articles/10057167-how-developer-payouts-work (2026)
100. AgentByline — Apify Actor passive income 2026, https://agentbyline.com/articles/apify-actor-passive-income-what-really-earns-in-2026-67lcfr (2026)
101. Apify Store — Smithery scraper actor (прокси), https://apify.com/maximedupre/smithery-mcp (2026)
102. MCPize — Monetize MCP servers (80%, founding 85%), https://mcpize.com/developers/monetize-mcp-servers (2026)
103. Godberry Studios — How to monetize MCP servers (ноль платящих), https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/ (2026-04)
104. X @serafimcloud — Magic MCP launch, https://x.com/serafimcloud/status/1897641079131746725 (2025-03)
105. GitHub Discussion #2436 — MCP payment layer, https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/2436 (2026-03…09)
106. TRM Labs — Who's actually paying?, https://www.trmlabs.com/trm-tech-blog/whos-actually-paying-measuring-ai-agent-payments-onchain (2026-09-09)
107. PYMNTS — Most x402 payments aren't from AI agents, https://www.pymnts.com/news/artificial-intelligence/2026/agentic-payments-are-growing-most-x402-payments-are-not-from-ai-agents (2026-09)
108. GitHub Ricosworks1 — AI agent payments deep dive, https://github.com/Ricosworks1/blockchain-payment-flow-analysis/releases/tag/deep-dive-ai-agent-payments-infrastructure-reality-sept-2026 (2026-09)
109. Stripe — Introducing the Machine Payments Protocol, https://stripe.com/blog/machine-payments-protocol (2026-03-18)
110. WorkOS — x402 vs Stripe MPP, https://workos.com/blog/x402-vs-stripe-mpp-how-to-choose-payment-infrastructure-for-ai-agents-and-mcp-tools-in-2026 (2026)
111. Cloudflare Docs — Charge for MCP tools, https://developers.cloudflare.com/agents/x402/charge-for-mcp-tools/ (2026)
112. Eco — MCP and payments 2026 guide (x402 Foundation), https://eco.com/support/en/articles/14845480-mcp-and-payments-a-2026-guide (2026)
113. Software Strategies Blog — Agentic AI security funding (Runlayer), https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/ (2026-03-28)
114. AppSentinels — Top MCP security companies 2026, https://appsentinels.ai/blog/top-10-mcp-security-companies-in-2026/ (2026)
115. Gartner — 40% of enterprise apps with AI agents by 2026, https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 (2025-08-26)
116. Practical DevSecOps — MCP security statistics 2026, https://www.practical-devsecops.com/mcp-security-statistics-2026-report/ (2026)
117. arXiv — MCPTox benchmark, https://arxiv.org/pdf/2508.14925 (2025-08)
118. CSA Lab Space — MCP tool poisoning & auto-execution, https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-auto-execution-20260701/ (2026-07-01)
119. Bitdefender Labs — OpenClaw malicious skills, https://www.bitdefender.com/en-us/blog/labs/helpful-skills-or-hidden-payloads-bitdefender-labs-dives-deep-into-the-openclaw-malicious-skill-trap (2026-02)
120. Particula — OpenClaw 20% skills malicious, https://particula.tech/blog/openclaw-security-crisis-malicious-ai-agents (2026)
121. OpenAI — GPT-6 Astra, https://openai.com/index/gpt-6-astra/ (2026-09-03)
122. Anthropic — Introducing Claude Opus 5.5, https://www.anthropic.com/claude-opus-5-5 (2026-09-22)
123. Vellum — Claude Opus 5.5 benchmarks explained, https://www.vellum.ai/blog/claude-opus-5-5-benchmarks-explained (2026-09)
124. arXiv — OSWorld 2.0, https://arxiv.org/abs/2606.29537 (2026-06)
125. Digiday — WTF is AdCP, https://digiday.com/media-buying/wtf-ad-context-protocol/ (2025-10)
126. AdCP Docs — Creative formats, https://docs.adcontextprotocol.org/docs/creative/formats (2026)
127. GitHub — adcontextprotocol/creative-agent, https://github.com/adcontextprotocol/creative-agent (WebFetch 2026-09-26)
128. Star Insights — AdCP and AAMP (VIOOH), https://star.global/posts/agentic-advertising-standards-adcp-and-aamp/ (2026)
129. ExchangeWire — Displayce agentic DOOH via MCP, https://www.exchangewire.com/blog/2026/06/29/displayce-launches-its-agentic-dooh-offering-a-suite-of-agents-available-via-mcp/ (2026-06-29)
130. Street Fight — Broadsign fully agentic OOH campaign, https://streetfightmag.com/2026/06/25/broadsign-and-partners-execute-fully-agentic-ooh-campaign/ (2026-06-25)
131. PPC Land — Adform CTO: neither protocol runs at scale, https://ppc.land/neither-of-ad-techs-two-ai-agent-protocols-runs-at-scale-adform-cto-says/ (2026-09-23)
132. Official MCP Registry — поиск «dooh» (Trillboards v1.1.0), https://registry.modelcontextprotocol.io/v0/servers?search=dooh (запрос 2026-09-26)
133. AnyPlugins — After Effects plugins (~1 363 инструмента, прокси), https://anyplugins.com/after-effects (2026)
