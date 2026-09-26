# Поток 4. AI-агенты и MCP в креативных приложениях (срез на 26.09.2026)

> **Методология и ограничения.** Лимит WebSearch в этой сессии был исчерпан до старта потока, а прокси блокировал большинство сайтов (adobe.com, figma.com, openai.com, smithery.ai, mcp.so, glama.ai, pulsemcp.com, aescripts.com, reddit.com, techcrunch.com). Поэтому опора такая:
> (1) **первичные данные**, собранные самостоятельно: полная выгрузка официального MCP Registry через API (119 601 запись, 36 185 уникальных серверов, 26.09.2026), GitHub API (звёзды и даты репозиториев), README на GitHub, блог MCP, страницы claude.com;
> (2) **полные тексты статей** из локального архива техно-новостей (≈64 тыс. материалов с 09.2025 по 09.2026: TechCrunch, The Verge, Ars Technica, Computerworld, Figma и Anthropic и др.);
> (3) **вторичные исследовательские заметки** разработчиков на GitHub (помечены «вторично»);
> (4) данные параллельных потоков этой же сессии (помечены «поток X»).
> Каталоги Smithery, Glama, PulseMCP и mcp.so напрямую проверить не удалось: их цифры вторичные. Оценки помечены «оценка» с уверенностью.

---

## Ключевые факты

### A. MCP как стандарт: управление, версии, масштаб

1. **MCP передан в Agentic AI Foundation (AAIF), фонд под Linux Foundation.** Сооснователи — Anthropic, Block и OpenAI; поддержка Google, Microsoft, AWS, Cloudflare, Bloomberg. Стартовые проекты фонда: MCP, goose, AGENTS.md. На момент передачи было «97 млн+ загрузок SDK в месяц» и «~10 000 активных серверов». Первоклассные клиенты: ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot, VS Code ([MCP Blog](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/), 2025-12-09).
2. **Версии спецификации:** 2025-11-25 (Tasks, упрощённая авторизация через URL-регистрацию клиента, extensions framework, sampling с инструментами) ([MCP Blog](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/), 2025-11-25) и **2026-07-28**. Вторая сделала протокол **stateless**: убраны handshake `initialize` и session ID, добавлены Multi Round-Trip Requests и маршрутизация по заголовкам. **MCP Apps, Tasks и Enterprise-Managed Authorization** стали официальными расширениями. Roots, Sampling и Logging объявлены устаревшими ([MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/), 2026-07-28).
3. **Масштаб в июле 2026:** «около полумиллиарда загрузок в месяц» по Tier-1 SDK, у TypeScript- и Python-SDK больше 1 млрд загрузок за всё время. У Honeycomb почти 20% интерактивных запросов в месяц делают агенты ([MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/), 2026-07-28). Рост с 97 млн в месяц (12.2025) до ~500 млн в месяц (07.2026) — примерно ×5 за 7 месяцев.
4. **Новая дорожная карта (22.08.2026)** — пять приоритетов: агентные примитивы, HTTP-транспорт, идентичность агентов и корпоративная безопасность (Workload Identity, DPoP), улучшенные примитивы, DX SDK. **Платежи и монетизация в дорожной карте не упоминаются** ([MCP Blog](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/), 2026-08-22).
5. **MCP Apps** (26.01.2026) — официальное расширение для интерактивного UI внутри чата (iframe-песочница, двусторонний JSON-RPC). Построено на основе OpenAI Apps SDK и MCP-UI. Поддержка: Claude (web и desktop), Goose, VS Code Insiders, ChatGPT ([MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/), 2026-01-26). Для креатива это значит, что превью рендера, таймлайн и слайдеры можно показать прямо в чате.
6. **MCP стал базовым интерфейсом для всех.** В 2026 году свои MCP выпустили X (06.2026), Meta Ads (07.2026), Apple Safari Technology Preview (07.2026) и Google Home (09.2026) ([TechCrunch](https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/), 2026-06-30; [WebKit](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/), 2026-07; [9to5Google](https://9to5google.com/2026/09/16/google-home-mcp), 2026-09-16).

### B. Реестры и каталоги: предложение взрывается

7. **Официальный MCP Registry (первичный подсчёт через API, 26.09.2026): 36 185 уникальных серверов** (119 601 запись с учётом версий), активны 35 796, помечены устаревшими 389. **61,2% имеют удалённый (hosted) endpoint.** Среди пакетов: npm 10 221, PyPI 3 966, `.mcpb` 1 333, OCI 1 000 ([registry.modelcontextprotocol.io/v0/servers](https://registry.modelcontextprotocol.io/v0/servers), выгрузка 2026-09-26). Реестр запущен в preview 08.09.2025 ([MCP Blog](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/), 2025-09-08).
8. **Темп: новые серверы в реестре по месяцу первой публикации:** 01.2026 — 391, 02 — 1 160, 03 — 1 952, 04 — 2 556, 05 — 3 041, 06 — 3 899, 07 — 5 105, 08 — 6 654, **09 (1–26) — 10 220**. Предложение удваивается примерно каждые 2 месяца. Подсчёт мой, по сохранившимся записям; удалённые не учтены.
9. **Креатив — крошечная доля реестра:** Figma упоминается в 46 серверах (0,13%), семейство Adobe — в 22 (0,06%), Blender — в 9, DaVinci — в 5, After Effects — примерно в 5, Remotion — в 3, Lottie/Rive — в 4, DOOH/signage — в 9. Для сравнения: **x402 упоминают 1 221 сервер (3,4%)**, это самая монетизированная прослойка ([Registry API](https://registry.modelcontextprotocol.io/v0/servers), подсчёт 2026-09-26). Большинство креативных MCP живут на GitHub и в реестр не попадают.
10. **Независимые каталоги (вторично, низкая–средняя уверенность):** Glama 21K+, mcp.so 19,7K+, PulseMCP 11,8K+, Smithery 7K+ серверов с сильным пересечением ([заметка clankwright](https://github.com/clankwright/science/blob/main/comsci/ai-empowerment/raw/mcp-ecosystem/ecosystem-state-may-2026.md), 2026-05). По независимому аудиту около **52% публичных MCP-серверов фактически мертвы**. У skills.sh (Vercel) около 895 тыс. проиндексированных skills, у топового — 2,5 млн установок ([заметка alp82](https://github.com/alp82/aistack/blob/main/docs/research/competitor-landscape-2026-07.md), 2026-07). Первоисточники этих цифр проверить не удалось.
11. **Claude Marketplace (26.09.2026): 850 коннекторов и 340 плагинов**, 16 категорий. Из креатива на витрине Adobe, Canva, Figma ([claude.com/connectors](https://claude.com/connectors), 2026-09-26). Сам маркетплейс запущен 23.09.2026. Там заявлено «более 2 000» коннекторов и плагинов. **Покупки идут через перераспределение «committed Anthropic spend»**, то есть это канал для корпоративных партнёров (CrowdStrike, Harvey, Legora, Lovable), а не для инди ([Claude Blog](https://claude.com/blog/claude-marketplace), 2026-09-23).
12. **Портал публикации плагинов для Claude (25.09.2026):** MCP-коннектор или бандл MCP + skills, автопроверка и safety-скан. Портал доступен разработчикам на платных планах Claude, в метриках есть установки и просмотры листинга. **Механики оплаты или revenue share нет** ([Claude Blog](https://claude.com/blog/build-plugins-for-claude), 2026-09-25).

### C. Платформы креативного софта: агент встраивается внутрь

13. **Adobe Firefly AI Assistant** («Project Moonlight» с MAX 2025) показан 15.04.2026. Это чат-агент, который «оркестрирует рабочие процессы между приложениями CC», со **skills** (есть библиотека, можно собирать свои) и памятью о предпочтениях ([Ars Technica](https://arstechnica.com/ai/2026/04/adobe-takes-creative-cloud-into-claude-code-esque-territory/), 2026-04-15).
14. **С 18.06.2026 ассистент в публичной бете внутри Photoshop, Premiere, Illustrator, InDesign и Frame.io, а в After Effects — в закрытой бете.** Premiere: раскладывает футаж по бинам, переименовывает клипы пачкой, ставит маркеры. Illustrator: 50 версий из таблицы, preflight шрифтов. Это «не computer-use агент» ([TNW](https://thenextweb.com/news/adobe-ai-week-firefly-agent-disney-semrush-genstudio-linkedin), 2026-06-24; [TechCrunch](https://techcrunch.com/2026/06/18/adobe-adds-its-ai-assistant-to-premiere-illustrator-and-indesign/), 2026-06-18). Firefly работает из ChatGPT, Claude и Copilot, обещаны Gemini и Slack. Express, Premiere и Acrobat пришли в Slack 02.09.2026 ([TechCrunch](https://techcrunch.com/2026/09/02/adobe-is-making-its-tools-available-in-slack/), 2026-09-02).
15. **AE 26.5 (09.2026): в бете появился агентный AI Assistant.** Он генерирует исполняемый JSX, пишет и отлаживает expressions, чинит риги, реорганизует проект (поток adobe_platforms: [CG Channel](https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/), 2026-09; [Adobe Community](https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658), 2026-09). Мной не перепроверено: сайты заблокированы.
16. **Adobe уже встраивает собственный MCP-сервер в настольные приложения.** В **Illustrator Beta 30.4+ есть встроенный официальный MCP** (~40 инструментов: анализ и пакетная обработка документов, пока без создания объектов). Статус «beta-only» на август 2026. Community-проект с 66 инструментами позиционирует себя как «всё, что умеет официальный MCP, и больше» ([ie3jp/illustrator-mcp-server](https://github.com/ie3jp/illustrator-mcp-server), 2026-08/09). Это прямой прецедент для After Effects.
17. **Коннектор «Adobe for creativity» для Claude (28.04.2026): 67 инструментов**, 9 продуктов (Acrobat, Photoshop, Lightroom, Illustrator, Firefly, Premiere, Express, InDesign, Stock), endpoint `adobe-creativity.adobe.io/mcp`. **After Effects в нём нет** ([Claude Marketplace](https://claude.com/marketplace/connectors/adobe-creativity), 2026-09-26; [Anthropic](https://www.anthropic.com/news/claude-for-creative-work), 2026-04-28).
18. **Корпоративный слой Adobe.** Firefly Graph (06.2026): 300+ типов нод, модели Adobe, Google и OpenAI. Для Creative Cloud for Enterprise, по кредитам ([Computerworld](https://www.computerworld.com/article/4186410/adobe-new-firefly-graph-can-turn-creative-workflows-into-reusable-assets.html), 2026-06). **Workfront MCP и AI Collaborators в GA (08.2026)** подключают внешних агентов (Copilot Studio, Claude, Writer) с правами доступа, аудитом и одобрением человеком ([The Letter Two](https://thelettertwo.com/2026/08/13/adobe-launches-ai-collaborators-workfront-general-availability/), 2026-08-13). CX Enterprise с «agent skills» показан на Summit 2026 ([SiliconANGLE](https://siliconangle.com/2026/04/20/adobe-deploys-agents-across-customer-experience-tools/), 2026-04-20). CEO Шантану Нараен уходит, и главная задача преемника — «age of agents» ([Computerworld](https://www.computerworld.com/article/4146823/adobe-summit-2026-how-adobe-hopes-to-redesign-marketing-and-creativity-with-ai.html), 2026-04-13).
19. **Figma открыла холст агентам (24.03.2026).** Инструмент `use_figma` через MCP даёт Claude Code, Codex и другим клиентам **писать** в файлы, используя компоненты и переменные. Skills — markdown-инструкции, часть из них написало сообщество. Цитата: «This will eventually be a usage-based paid feature», сейчас бесплатно в бете ([Figma Blog](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/), 2026-03-24). «Code to Canvas» с Anthropic (17.02.2026) сделал поток двусторонним ([SiliconANGLE](https://siliconangle.com/2026/02/26/figmas-orchestration-bet-mcp-network-effects-redefine-software-defensibility/), 2026-02-26).
20. **Figma Config 2026 (24.06.2026): Figma Motion** — таймлайн, ключи, пресеты, анимация через агента, экспорт MP4/WebM/анимированного SVG/GIF и кода (CSS/JSON/React). «Motion is also MCP-compatible». Там же шейдеры и Weave tools ([Figma Blog](https://www.figma.com/blog/config-2026-recap/), 2026-06). **С 11.08.2026 Weave-инструменты запускаются из ChatGPT, Claude и Cursor через Figma MCP.** С 13.08.2026 в Figma Community работает библиотека **50+ agent skills** с публикацией. С 05.08.2026 админы ставят лимиты AI-кредитов ([Figma Release Notes](https://www.figma.com/release-notes/?title=figma-mcp-run-weave-tools-right-from-your-favorite-agent), 2026-08).
21. **Canva монетизирует чат-каналы как воронку.** К октябрю 2025 было 26 млн+ разговоров с Canva-app в ChatGPT. Canva входит в топ-10 доменов по рефералам из ChatGPT, LLM-рефералы дают двузначный % трафика. ARR $4 млрд, 265 млн MAU ([TechCrunch](https://techcrunch.com/2026/02/18/canva-gets-to-4b-in-revenue-as-llm-referral-traffic-rises/), 2026-02-18). Через ChatGPT, Claude и Copilot сделано **12 млн+ дизайнов** ([Digital Trends](https://www.digitaltrends.com/computing/canva-now-lets-chatgpt-create-designs-that-match-your-brand-logo-font-and-colors/), 2026-02-14). Canva владеет Affinity (коннектор в Claude) и купила Cavalry (поток adobe_platforms: [TechCrunch](https://techcrunch.com/2026/02/23/canva-acquires-startups-working-on-animation-and-marketing/), 2026-02-23).
22. **Blender: официальный коннектор от Blender Lab** («verified by Anthropic», апрель 2026). Anthropic стал Corporate Patron Blender Development Fund: **не меньше €240 000 в год** ([claude.com/connectors/blender](https://claude.com/connectors/blender), 2026-09; [The Verge](https://www.theverge.com/ai-artificial-intelligence/919648/anthropic-claude-creative-connectors-adobe-blender), 2026-04-28). Самый популярный community-MCP после этого переименован в «MCP for Blender» с дисклеймером «not made by Blender». Монетизация: GitHub Sponsors, Buy me a coffee и «premium» (генерация 3D без своих API-ключей) ([ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender), 2026-09).
23. **DaVinci Resolve 21.1 (08.09.2026)** интегрировал Claude, Claude Code и ChatGPT Codex через 20 новых scripting API. **Продвинутый скриптинг перенесли в платную Studio.** Пользователи отмечают, что API не умеет базовых операций монтажа (сдвинуть клип) ([конспект ahastudio](https://github.com/ahastudio/til/blob/main/video/davinci-resolve-21-1.md), 2026-09; [Blackmagic PR](https://www.blackmagicdesign.com/media/release/20260908-03), 2026-09-08). Платформа берёт деньги за доступ агента.

### D. Community-MCP для креативных приложений (GitHub, 26.09.2026)

24. **Таблица лидеров** (поиск GitHub «<app> mcp»; число репозиториев — верхняя граница с шумом):

| Приложение | Репозиториев | Лидер | ★ | Создан |
|---|---|---|---|---|
| After Effects | 72 | [Dakkshin/after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp) | 657 | 2025-04-12 |
| Premiere Pro | 49 | [hetpatel-11/Adobe_Premiere_Pro_MCP](https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP) | 609 | 2025-07-07 |
| Photoshop | 86 | [alisaitteke/photoshop-mcp](https://github.com/alisaitteke/photoshop-mcp) | 520 | 2026-01-26 |
| DaVinci Resolve | 73 | [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) | 3 148 | 2025-03-18 |
| Blender | 906 | [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 29 360 | 2025-03-07 |
| Cinema 4D | 9 | [ttiimmaacc/cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp) | 127 | 2025-03-13 |
| Houdini | 65 | [capoomgit/houdini-mcp](https://github.com/capoomgit/houdini-mcp) | 298 | 2025-03-17 |
| TouchDesigner | 51 | [8beeeaaat/touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp) | 549 | 2025-04-13 |
| Unreal | 504 | [chongdashu/unreal-mcp](https://github.com/chongdashu/unreal-mcp) | 2 086 | 2025-03-28 |
| Unity | 883 | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | 14 491 | 2025-03-18 |
| Figma | 2 105 | [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | 15 915 | 2025-02-13 |

25. **After Effects: 72 репозитория, ускорение в 2026 году.** 8 в 2025 году, 30 в I полугодии 2026 года, 34 в июле — сентябре 2026 года (поток adobe_platforms, поиск GitHub, 2026-09-26). Свежие: JUNKDOGE-JOE (73★, 04.2026), kumoproductions (69★, 08.2026, у них есть и C4D-MCP), Engine-Room-Games, aftr «Puppeteer for AE» (07.2026), ishu86 (70+ инструментов, шаблоны lower thirds и титров) ([поиск GitHub](https://github.com/search?q=after+effects+mcp&type=repositories), 2026-09-26). **Коммерческий игрок: Prism (oneprism.io), «After Effects MCP», 300+ инструментов**, удалённый endpoint, «free plan, no card» (в реестре с 02.08.2026) ([Registry](https://registry.modelcontextprotocol.io/v0/servers?search=oneprism), 2026-08-02). В сравнениях Figma → AE Prism встречается «от $39» (поток demand_scout: [Next Horizon](https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma), 2026). Вероятно, это та же компания: оценка, уверенность средняя. **Прямой конкурент Oblique идёт через MCP-канал.**
26. **Как на практике монетизируют популярные creative-MCP: open source как воронка платного агента.** Unity-MCP (14,5K★) «спонсируется и поддерживается Aura — AI-ассистентом для Unreal и Unity». **Aura купила Flopperam (Unreal MCP, 1,1K★)** ([CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp), 2026-06; [flopperam/unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp), 2026-09). Plainly (облачный рендер AE-шаблонов) держит официальный MCP (6★) как канал к своему SaaS ([plainly-videos/mcp-server](https://github.com/plainly-videos/mcp-server), 2026-09).
27. **Skills для моушна массовые и бесплатные.** OpenMontage — 61,3K★, 700+ файлов skills и знаний по производству видео (03.2026). video-talkcraft — 1,2K★ меньше чем за месяц (08.2026, 109 «motion recipe cards», Remotion). motion-design-skills (iart-ai) — 33★ ([GitHub](https://github.com/calesthio/OpenMontage), [GitHub](https://github.com/Vincentwei1021/video-talkcraft), [GitHub](https://github.com/iart-ai/motion-design-skills), 2026-09-26). У эталонного репозитория anthropics/skills 178K★ ([GitHub](https://github.com/anthropics/skills), 2026-09-26). Стандарт Agent Skills открыт 18.12.2025 ([Claude Blog](https://claude.com/blog/organization-skills-and-directory), 2025-12-18).

### E. Монетизация: есть ли реальные деньги

28. **Нативных платежей в MCP нет.** SEP-2007 «Payment Support for MCP Servers» (x402 v2, код ошибки `-32402`) в статусе **Draft** с 23.12.2025. В спецификацию 2026-07-28 он не вошёл ([GitHub issue #2008](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2008), 2025-12-23; [MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/), 2026-07-28).
29. **OpenAI.** Приём приложений в каталог ChatGPT открыт 17.12.2025 ([OpenAI](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/), 2025-12-17). По вторичному разбору документации Apps SDK (07.2026): монетизация только через **внешний checkout**, «payment sheet» в закрытой бете, **цифровые товары и подписки не одобрены**, revenue share не раскрыт ([заметка pavel-rp](https://github.com/pavel-rp/second-memory-mcp/blob/master/docs/research/results/04-monetization-market-research.md), 2026-07-07). Instant Checkout не взлетел: «около дюжины» мерчантов Shopify. Покупки переведены в приложения партнёров ([The Decoder](https://the-decoder.com/chatgpt-users-research-products-but-wont-buy-there-forcing-openai-to-rethink-its-commerce-strategy/), 2026-03-07). По данным Growth Memo, Instant Checkout к середине 2026 года закрыт ([Growth Memo](https://www.growth-memo.com/p/ai-halftime-report-h1-2026), 2026-07-29).
30. **Anthropic.** Revenue share для разработчиков коннекторов нет (вторично, [pavel-rp](https://github.com/pavel-rp/second-memory-mcp/blob/master/docs/research/results/04-monetization-market-research.md), 2026-07). Новый Marketplace продаёт партнёрские продукты за committed spend корпоративных клиентов (факт 11).
31. **Реальные платные MCP — это доступ к платным данным или вычислениям.** Вторично, цены проверены автором заметки 07.07.2026: Ref.tools — $9/мес за 1 000 кредитов («сотни подписчиков», по словам самой компании); 21st.dev Magic MCP — $20–40/мес (заявление основателя «$10K MRR за 6 недель» **не верифицировано**); Bright Data MCP — $499–1 999/мес; Tavily — $0,008 за кредит; Zapier MCP — 1 вызов = 2 задачи ([pavel-rp](https://github.com/pavel-rp/second-memory-mcp/blob/master/docs/research/results/04-monetization-market-research.md), 2026-07-07). **Агрегированной выручки рынка платных MCP нет ни в одном источнике.**
32. **Площадки с выплатами.** **Apify**: 80% revenue share авторам Actors (вторично), официальный MCP-сервер принимает оплату за вызов через **x402 (USDC на Base) и Skyfire** ([apify/apify-mcp-server](https://github.com/apify/apify-mcp-server), 2026-09). **MCPize**: заявлены 85% автору, выплаты через Stripe Connect, порог $100 ([mcpize/mcpize-skills](https://github.com/mcpize/mcpize-skills), 2026). Цифры вроде «топ-авторы зарабатывают $3–10K в месяц» — маркетинг площадки. Уверенность низкая.
33. **x402:** Coinbase и Chainalysis сами сообщают о **169 млн+ платежей, 590 тыс. покупателей и 100 тыс. продавцов за первый год**. Протоколом управляет x402 Foundation под LF, AWS CloudFront/WAF поддерживает его с ~06.2026 (вторично, **без независимого аудита** — [pavel-rp](https://github.com/pavel-rp/second-memory-mcp/blob/master/docs/research/results/04-monetization-market-research.md), 2026-07). Visa, Mastercard и Ripple присоединились к стандарту ([CoinDesk](https://www.coindesk.com/tech/2026/07/15/visa-mastercard-and-ripple-join-the-standard-letting-ai-agents-pay-in-stablecoins), 2026-07-15). Для основателя это USDC, а не фиатные выплаты на Payoneer.
34. **Инфраструктура «платного MCP» почти никому не нужна.** Шаблоны вроде paid-mcp-starter, toolbooth, paid-skills (метеринг Claude Skills + Stripe) и x402-mcp-server собрали **0–2 звезды** ([поиск GitHub «mcp monetization paid»](https://github.com/search?q=mcp+monetization+paid&type=repositories), 2026-09-26). Спроса со стороны разработчиков на монетизацию коннекторов не видно.

### F. Безопасность: она определяет, кто покупает

35. **Маркетплейс skills как вектор атаки.** Bitdefender нашёл **~900 вредоносных пакетов в ClawHub (реестр skills OpenClaw) — около 20% всех опубликованных skills**. CVE-2026-25253 даёт RCE в один клик; 15 200 инстансов уязвимы ([InfoQ](https://www.infoq.com/news/2026/03/aws-lightsail-openclaw-security/), 2026-03-17; [Unit 42](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/), 2026-06).
36. **Другие инциденты:** «RCE by design» в архитектуре MCP ([CSO Online](https://www.csoonline.com/article/4159889/rce-by-design-mcp-architectural-choice-haunts-ai-agent-ecosystem.html), 2026-04-20); кража OAuth-токенов Claude Code через MCP-hijacking ([SecurityWeek](https://www.securityweek.com/claude-code-oauth-tokens-can-be-stolen-through-stealthy-mcp-hijacking/), 2026-05); вредоносные skills для Claude Code ([Reversec](https://labs.reversec.com/posts/2026/05/skill-issues-compromising-claude-code-with-malicious-skills-agents-part-1), 2026-05); ANSI-инъекции в MCP ([BrightSec](https://brightsec.com/research/detecting-ansi-escape-sequence-injection-in-mcp-servers-with-dast/), 2026-07); критическая уязвимость в Microsoft UFO MCP ([GBHackers](https://gbhackers.com/critical-microsoft-ufo-mcp-flaw/), 2026-09-02). Ответ рынка: бейджи «verified by Anthropic», safety-скан в портале плагинов, Enterprise-Managed Authorization в спецификации. **Студии и корпорации покупают доверие**: официальные коннекторы вендоров, а не анонимные репозитории.

### G. Сигналы против MCP как продукта

37. **CLI и skills вытесняют «обёрточные» MCP.** «Мы удаляем большинство наших MCP-серверов… агенты с терминалом заменяют большинство MCP» ([Maharship](https://maharship.com/blog/why-mcp-was-always-a-bad-idea/), 2026-09-14). Проблему «MCP съедает контекст» Claude Code частично закрыл отложенной загрузкой инструментов: минус 85%+ контекста ([Quandri](https://www.quandri.io/engineering-blog/mcp-is-dead), 2026-05-29).
38. **Computer use пока медленный.** GPT-6 Astra — «лучшая модель для computer use»: **72,6% на OSWorld 2.0 при ~40 минутах на задачу** против 65,7% за ~75 минут у GPT-5.6 Sol ([OpenAI](https://openai.com/index/gpt-6-astra/), 2026-09-03). GUI-агенты пока не заменяют API и MCP для производственной работы в AE. Когда время упадёт до минут, ценность коннекторов снова снизится.

---

## Сценарии: 12 / 24 / 36 месяцев (сентябрь 2026 → конец 2029)

Три вопроса потока: (1) будут ли агенты управлять AE, Premiere, Figma и Blender в реальном производстве; (2) появится ли платный рынок MCP, skills и коннекторов; (3) кто заберёт ценность.

| | **Базовый: «агенты да, платный рынок коннекторов нет» — 55%** | **Быстрый: «агенты рулят приложениями, появляется микрорынок платных инструментов» — 25%** | **Медленный: «ассистенты, а не агенты» — 20%** |
|---|---|---|---|
| **12 мес (09.2027)** | AE AI Assistant в GA или поздней бете на кредитах. Firefly AI Assistant есть во всех флагманах. Запись в Figma через агентов стала платной (usage-based). Агенты рутинно выполняют уборку проекта, переименование, версии и ресайзы, expressions и preflight. Hero-анимацию делают руками. В реестре 70–100K серверов (оценка, средняя), AE-MCP на GitHub больше 150. SEP-2007 остаётся черновиком. Маркетплейсы Claude и ChatGPT без revenue share для инди | Adobe добавляет встроенный MCP в AE Beta (по образцу Illustrator 30.4) и расширяет свой коннектор на AE. SEP-2007 принят как расширение, Claude и ChatGPT показывают цену инструмента и платят через x402 или MPP. Computer use укладывается меньше чем в 10 минут на задачу | AE Assistant надолго застревает в бете. Кредиты дорогие, студии запрещают агентов из-за IP и безопасности. После новых инцидентов (как с ClawHub) корпорации ограничивают сторонние MCP |
| **24 мес (09.2028)** | Оркестрация между приложениями (Firefly Assistant + Graph, Figma Motion ↔ код) стала стандартом корпоративных content supply chains. Платформы берут деньги за агентный доступ (кредиты, Studio-тарифы). CEP в AE выключен по умолчанию (12.2028): часть старых плагинов умирает. Инди-MCP — бесплатные воронки | Агенты собирают шаблонные ролики end-to-end в AE, Premiere и Resolve. Рынок платных утилит для AE сокращается вдвое (оценка, низкая). Появляется микрорынок платных инструментов за вызов, но в креативе он маленький: деньги у данных и рендера | Агенты полезны для скриптов и expressions. Платные плагины и шаблоны живут как в 2024–2025. Реестры забиты мёртвыми серверами, платёжные расширения не взлетают |
| **36 мес (конец 2029)** | 50–70% версий и адаптаций в крупных студиях делают агенты (оценка, низкая). Ценность у Adobe, Figma, Canva, Anthropic и OpenAI, а также у владельцев данных, контента, доверия и сервиса. «MCP для приложения X» как товар не существует | Большая часть рутинного моушна идёт через агентов. Платформы плюс владельцы уникальных ассетов (пресеты, риги, спецификации), которые агенты «потребляют», плюс сервис | Рынок остаётся «плагины + шаблоны + сервис», агенты — функция внутри приложений |
| **Опережающие сигналы** | ① GA и цена AE Assistant ② коннектор Adobe пополняется AE ③ Figma объявляет цены на агентную запись | ① встроенный MCP в AE Beta ② SEP-2007 или PR #2007 принят ③ revenue share в портале плагинов Claude или Apps SDK ④ OSWorld: меньше 10 минут на задачу | ① AE Assistant в бете дольше 12 месяцев ② новые громкие CVE и отзывы коннекторов ③ посты «удаляем MCP» становятся мейнстримом |

**Как мониторить (раз в месяц, ~30 минут):**
1. **Adobe:** заметки о релизах AE Beta и страница helpx «about using AI tools with After Effects» по аналогии с [Illustrator](https://helpx.adobe.com/illustrator/desktop/connect-with-other-apps-and-tools/about-using-ai-tools-with-illustrator.html); листинг [Adobe connector](https://claude.com/marketplace/connectors/adobe-creativity) — появился ли AE, выросло ли число инструментов (сейчас 67).
2. **Платежи в MCP:** статус [issue #2008 / PR #2007](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2008) и посты [блога MCP](https://blog.modelcontextprotocol.io/posts/).
3. **Маркетплейсы:** [блог Claude](https://claude.com/blog) (платные плагины, revenue share) и страница монетизации Apps SDK у OpenAI.
4. **Клоны:** число AE-MCP в [поиске GitHub](https://github.com/search?q=after+effects+mcp&type=repositories) (базовая точка 72), версии и описание Prism в [реестре](https://registry.modelcontextprotocol.io/v0/servers?search=oneprism). Если Prism вводит платный тариф и растёт, это сигнал, что платёжеспособный спрос есть.
5. **Computer use:** время на задачу в OSWorld в анонсах моделей (базовая точка ~40 минут).

---

## Ответы на ключевые вопросы

**Что станет массовым и дешёвым**
- **Коннекторы к любому приложению.** Для AE 72 репозитория, у многих 30–300 инструментов, пишутся агентом за дни. «MCP для X» — это commodity, как и skills: бесплатные, их сотни тысяч в индексах (факты 10, 24–27).
- **Рутинные операции внутри приложений:** переименование, бины, маркеры, пакетный экспорт, версии из таблиц, expressions и JSX, preflight шрифтов. Adobe уже встроила это в ассистента (факты 14–15).
- **Figma → код → холст и базовый UI-моушн:** Figma Motion экспортирует в видео и код, MCP-совместим (факт 20).

**Что поглотят платформы**
- Агента внутри приложения (Adobe Firefly AI Assistant, Figma agent, Resolve 21.1).
- Официальные MCP-endpoint (Illustrator Beta, Adobe for creativity, Figma, Canva, Blender Lab).
- Библиотеки skills (Figma Community, skills в Firefly), нодовые пайплайны (Firefly Graph, Figma Weave).
- Витрину и дистрибуцию (Claude Marketplace, каталог ChatGPT, официальный реестр).
- Платформы продают агентный доступ через свои тарифы и кредиты: Resolve Studio, AI-кредиты Figma, кредиты Firefly (факты 19, 20, 23).

**Где останутся деньги**
1. **Данные и спецификации, которых нет у платформ**, особенно связанные с физическим миром: экраны DOOH, их технические требования и сроки согласований (поток dooh_3d: у Vistar лимит 10 МБ на статику и 50 МБ на видео; согласование от 1 до 5 рабочих дней; стандарта для 3D/анаморфных экранов нет ([BDOOH](https://bdooh.com/research/dooh-creative-spec-reference/), 2026; [DOOH Marketing](https://doohmarketing.com/dooh-creative-specs-guide), 2026)).
2. **Результат, а не инструмент.** Конвейеры версий продаются по рендер-минутам: Plainly $69–649 в месяц, Nexrender от €99 в месяц, Templater от $67,50 (поток demand_scout: [Capterra](https://www.capterra.com/p/10026817/Plainly/), [Nexrender](https://www.nexrender.com/pricing), 2026).
3. **Доверие и управление в корпорациях.** Верифицированные коннекторы, аудит, права (Workfront AI Collaborators, EMA).
4. **Платные данные и вычисления с MCP как каналом** (Ref, Bright Data, Apify).
5. **Узкая глубина, которая платформе безразлична.** Точность переноса стекла и блюров Figma → AE — ниша Oblique.
6. **Контент, который агенты «потребляют»:** пресеты, риги, 3D-сцены, библиотеки движения. Агенту нужны ассеты. Прокси: Blender-MCP встроил Poly Haven и Sketchfab, Instavar раздаёт шаблоны Remotion через MCP (факты 22, реестр).

**У кого будет доступ к инструментам**
- **Массовый пользователь** получает агентов бесплатно или дёшево через Claude, ChatGPT и Firefly: у Canva 12 млн+ дизайнов через чат-ботов (факт 21).
- **Профи** получают глубину: community-MCP в AE, UXP-плагины, скрипты. Но и в Premiere, и в AE у них теперь встроенный ассистент.
- **Корпорации** получают оркестрацию и governance: Firefly Graph для Enterprise, Workfront MCP, CX Enterprise, закупку через Claude Marketplace.
- По вторичным данным, свой MCP в ChatGPT (Developer Mode) можно подключить только на планах Business, Enterprise и Edu ([pavel-rp](https://github.com/pavel-rp/second-memory-mcp/blob/master/docs/research/results/04-monetization-market-research.md), 2026-07).

**Какие навыки обесценятся**
- Написание expressions и скриптов, знание меню и UI приложений, рутинные операции с ассетами.
- Ресайзы и версии, базовый UI-моушн.
- **Само умение делать плагин или коннектор.** Любой собирает MCP через Claude Code; урок Oblique распространяется на всю категорию.

**Какие станут дефицитом**
- **Вкус и арт-дирекция.**
- **Умение формализовать «что такое хорошо» в skills.** Figma прямо пишет, что эта экспертиза «ценнее, чем когда-либо» (факт 19).
- Проектирование пайплайнов и QA результатов агентов.
- Проверка безопасности и доверие.
- Курирование данных.
- Физическое производство (DOOH, анаморф, съёмка).
- Отношения с клиентами и студиями.

---

## Возможности для основателя

Общий вывод до списка. **Продавать коннектор (MCP для AE) как самостоятельный продукт нельзя.** Бесплатных аналогов 72, у Prism бесплатный план, у Adobe есть прецедент встроенного MCP (Illustrator) и собственный ассистент в AE. MCP и skills стоит использовать как **канал дистрибуции и формат упаковки** для активов, которые трудно скопировать: точности Oblique, данных DOOH, стандартов QC и знаний студии.

### 1. «Oblique Agent Mode»: MCP + skill поверх Oblique
- **Суть:** агент (Claude Code, Codex, Figma agent) по команде переносит фреймы Figma в AE с точностью Oblique для стекла и блюров. MCP и skill бесплатны, лицензия Oblique платная.
- **Тип:** A.
- **Формат:** расширение существующего плагина — локальный stdio-MCP плюс SKILL.md. Публикация в официальном реестре, портале плагинов Claude и Figma Community skills. Сборка через Claude Code 1–2 недели.
- **Покупатель и боль:** моушн-дизайнеры и студии, у которых дизайн уже делает агент в Figma (`use_figma`, Figma Motion). Им нужен «последний километр» в AE без ручной пересборки эффектов.
- **Доказательства спроса:**
  - запись в Figma агентами открыта 24.03.2026, Figma Motion MCP-совместим (факты 19–20);
  - в karly-herrera/after-effects-mcp (05.2026) есть «Figma → AE pipelines»;
  - Prism совмещает Figma → AE и AE-MCP (300+ инструментов, 08.2026) (факт 25).
  Прямых данных о платёжеспособности нет.
- **Конкуренты и цены:** Prism — от $39 (поток demand_scout), MCP бесплатно; Overlord — ранее $45; UXLink — $99,99; LazyLord и FAE — бесплатно (поток adobe_platforms).
- **Гипотеза рва:** точность рендера стекла и блюров, скорость обновлений, дистрибуция через aescripts. MCP здесь только канал.
- **Главный риск:** Adobe добавляет импорт Figma или экспорт Figma Motion в AE. Бесплатные клоны догоняют по эффектам.
- **Готовность платить:** средняя — за Oblique; за MCP-слой нулевая.
- **Платформенный риск:** высокий.

### 2. Самостоятельный «AE Agent Connector» (для полноты — не рекомендую)
- **Суть:** платный MCP и панель для управления AE агентом.
- **Тип:** A.
- **Формат:** CEP/UXP-панель плюс MCP, подписка.
- **Покупатель и боль:** моушн-дизайнеры, которые хотят «Claude Code для AE».
- **Доказательства:** спрос на игрушку есть — 657★ у лидера и 72 репозитория. Доказательств оплаты нет: у Prism бесплатный план, у самого популярного creative-MCP (Blender, 29K★) доход только от донатов и премиум-кредитов (факт 22).
- **Конкуренты и цены:** Prism (бесплатно или от $39); десятки бесплатных MIT-репозиториев; Adobe AE AI Assistant (входит в CC, кредиты — нет данных).
- **Гипотеза рва:** нет. Максимум — если завязать на собственную библиотеку пресетов и ригов.
- **Главный риск:** встроенный MCP или ассистент Adobe в AE. Вероятность встроенного MCP в AE Beta до конца 2027 года — 50–60% (оценка, средняя; прецедент — Illustrator 30.4).
- **Готовность платить:** низкая.
- **Платформенный риск:** очень высокий.
- **Вердикт:** не делать. Модель Aura (open-source MCP как воронка платного агента, покупка конкурентов) требует венчурного бюджета и фултайм-команды.

### 3. «DOOH & Anamorphic Spec MCP»: база спецификаций экранов + preflight
- **Суть:** выверенная база экранов DOOH и 3D-анаморфных экранов. Поля: разрешение, шаг пикселя, форматы, fps, кодеки, лимиты файлов, длина лупа, сроки согласования, геометрия угла и точка обзора для анаморфа.
- **Тип:** AB. База — тип B, связка со студией и 3D-экспертиза — тип A.
- **Формат:**
  - SEO-страницы «спеки и стоимость экрана X» по модели калькуляторов;
  - бесплатный MCP для агентов медиапланирования;
  - платный preflight API или кредиты для агентств: проверка файла по спеке экрана и отчёт;
  - лидогенерация для студии анаморфных билбордов.
- **Покупатель и боль:** агентства и продакшны, которые делают DOOH и 3D-кампании. Спецификации разбросаны по PDF, отказы при модерации стоят дней.
- **Доказательства спроса:**
  - Vistar: 10 МБ на статику, 50 МБ на видео; согласование от 1 до 5 рабочих дней; стандарта для 3D нет (поток dooh_3d);
  - Trillboards опубликовал DOOH-MCP («5 000+ экранов», 03.2026) и пример агента с 38 инструментами ([Registry](https://registry.modelcontextprotocol.io/v0/servers?search=trillboards), [GitHub](https://github.com/trillboards/dooh-agent-example), 2026-03);
  - DOOH Marketing предлагает MCP для агентов (поток dooh_3d, [doohmarketing.com](https://doohmarketing.com/), 2026);
  - у FOOH.com 64 экрана и 40+ 3D-кампаний ([FOOH](https://fooh.com/blog/dooh-library-and-screens-on-fooh-com/), 2025–2026).
  Объём поиска — нет данных.
- **Конкуренты и цены:** OAAA Mockup Generator, AdQuick Visualize и OUTFRONT Preview — бесплатны; Trillboards — free tier; DOOH Marketing — цены нет данных; открытая [Vistar dynamic-creative-spec](https://github.com/vistarmedia/dynamic-creative-spec).
- **Гипотеза рва:**
  - курирование данных плюс свежесть: скорость обновлений;
  - связь с физическим миром — операторы и собственные кампании студии;
  - анаморфная геометрия, которую знает 3D-команда.
- **Главный риск:** узкий рынок; операторы и SSP публикуют собственные MCP; поддержка базы может занять больше 4 часов в неделю.
- **Готовность платить:** низкая за данные, средняя за preflight перед дорогим размещением.
- **Платформенный риск:** средний. Adobe этим не займётся, SSP могут.

### 4. «Delivery QC Agent»: проверка экспорта перед сдачей клиенту
- **Суть:** агент или CLI проверяет отрендеренные файлы по правилам площадок (соцсети, DOOH, громкость) и выдаёт отчёт для клиента. Работает из AE, Premiere и Resolve, а также как MCP-инструмент для агентных пайплайнов.
- **Тип:** AB. База правил — тип B, её надо обновлять; знание продакшна — тип A.
- **Формат:** десктопный CLI на ffprobe плюс MCP плюс веб-отчёт. $15–29 в месяц или кредиты за отчёт (оценка).
- **Покупатель и боль:** небольшие студии и фрилансеры с десятками версий на кампанию. Отказы площадок и правки клиента из-за неверного кодека, битрейта, safe zones или лупа.
- **Доказательства спроса:**
  - Resolve 21.1 даёт агенту пакетный рендер, но не QC (факт 23);
  - простого QC «под соцсети и DOOH» с отчётом для клиента в выборке не нашлось (поток motion_industry);
  - конвейеры версий продаются по $69–649 в месяц (поток demand_scout).
  Прямых жалоб (Reddit) нет данных.
- **Конкуренты и цены:** MediaInfo и ffprobe — бесплатно, без правил; Telestream Vidchecker и Interra Baton — корпоративные, цены нет данных; Frame.io — ревью, не QC.
- **Гипотеза рва:** ежемесячно обновляемая база правил площадок — «калькуляторная» дисциплина — плюс шаблон отчёта, которому доверяют клиенты.
- **Главный риск:** Adobe Media Encoder или Frame.io добавят проверки, у фрилансеров низкая готовность платить.
- **Платформенный риск:** средний.

### 5. «Brand Motion Skills»: моушн-система бренда как agent skills
- **Суть:** упаковать моушн-систему бренда (тайминги, easing, типографику в движении, правила переходов, запреты) в skills для Figma agent, Firefly AI Assistant, Claude и Remotion. Продаётся брендам и агентствам как настройка «под ключ». Бесплатные публичные skills служат лид-магнитом.
- **Тип:** A.
- **Формат:** сервис плюс пакет. $2–10K за настройку (оценка, низкая уверенность). Публичные skills в Figma Community и на GitHub.
- **Покупатель и боль:** in-house команды брендов, у которых агенты генерируют «generic» моушн. Figma прямо продаёт skills как способ «научить агента, как выглядит хорошо».
- **Доказательства:**
  - в Figma Community 50+ skills с публикацией (13.08.2026), у Firefly AI Assistant есть библиотека skills (04.2026) (факты 13, 20);
  - спрос на моушн-skills большой, но бесплатный: OpenMontage 61K★, video-talkcraft 1,2K★ за месяц (факт 27);
  - Adobe продаёт брендовую консистентность корпорациям (Firefly Foundry, GenStudio) (факт 18).
- **Конкуренты и цены:** бесплатные skills на GitHub; агентства брендинга (цены нет данных); Adobe GenStudio (enterprise).
- **Гипотеза рва:** вкус, портфолио, отношения с клиентами, кейсы студии. Текст skill копируется, результат и доверие — нет.
- **Главный риск:** это сервис, а не продукт без обслуживания. Не укладывается в 2–4 часа в неделю без шаблонизации.
- **Готовность платить:** B2B есть (за результат), B2C — ноль.
- **Платформенный риск:** низкий–средний.

### 6. «Creative MCP Index»: каталог и тесты совместимости креативных MCP и skills
- **Суть:** нишевый каталог MCP и skills для AE, Premiere, Resolve, Blender, C4D, Houdini, TouchDesigner и Figma. Автотесты «работает ли на версии X», скан безопасности, число инструментов, дата обновления, ежемесячный дайджест.
- **Тип:** B.
- **Формат:** SEO-сайт плюс рассылка. Спонсорство, аффилиатные ссылки на платные инструменты (Prism и подобные), платные обзоры.
- **Покупатель и боль:** моушн-дизайнеры и технические директора студий, которые тонут в 72 AE-MCP и боятся вредоносных пакетов (ClawHub — 20% вредоносных).
- **Доказательства:**
  - в реестре 36 185 серверов, 10 220 новых за сентябрь 2026 (факты 7–8);
  - «~52% мертвы» (вторично) (факт 10);
  - креативные MCP разбросаны по GitHub (факт 24);
  - общие каталоги (Glama, PulseMCP, mcp.so, Smithery) не тестируют совместимость с приложениями.
- **Конкуренты и цены:** общие каталоги бесплатны; обзоры chatforest.com (нет данных по трафику).
- **Гипотеза рва:** авторитет в нише плюс тестовый стенд плюс регулярность — накопленный контент.
- **Главный риск:** слабая монетизация. Витрины Claude и ChatGPT забирают дистрибуцию, трафик на запросы вида «after effects mcp» маленький (нет данных).
- **Платформенный риск:** средний.

### 7. «Agent-ready Motion Assets»: пресеты и риги с машиночитаемыми метаданными
- **Суть:** библиотека пресетов, ригов и сцен (включая шаблоны 3D-билбордов) с описаниями и параметрами, которые агент может найти и применить через MCP. Продажа паками или подпиской.
- **Тип:** A.
- **Формат:** ассеты на aescripts, Gumroad и Polar плюс бесплатный MCP-поиск по своей библиотеке.
- **Покупатель и боль:** агенты генерируют «с нуля» и выдают generic. Качественные ассеты превращают агентный результат в продакшн.
- **Доказательства (прокси, уверенность низкая):**
  - Blender-MCP интегрирует Poly Haven, Sketchfab и 3D-генерацию как ключевые функции (факт 22);
  - Instavar отдаёт шаблоны Remotion через MCP (реестр, 2026-09-20);
  - у Adobe в Firefly появились Elements, переиспользуемые ассеты (факт 14).
- **Конкуренты и цены:** Envato и Motion Array (подписка, цены нет данных в этом потоке); бесплатные библиотеки.
- **Гипотеза рва:** накопленный контент плюс вкус. Агенты сами по себе не делают хороших ригов и пресетов.
- **Главный риск:** генеративные модели обесценивают стоковые ассеты. Пиратство.
- **Платформенный риск:** средний.

**Приоритет для основателя:**
1. **№1 сразу** — дёшево, усиливает уже существующий актив.
2. **№3 как проверка** — 2 недели на прототип базы по 30–50 экранам и сбор обратной связи от 5 агентств. Синергия со студией.
3. **№4 — проверить спрос** опросом студий до разработки.
4. **№2 не делать.**

---

## Источники

1. MCP Blog — список постов, https://blog.modelcontextprotocol.io/posts/ (2026-09)
2. MCP joins the Agentic AI Foundation, https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ (2025-12-09)
3. Anthropic — Donating MCP / AAIF, https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation (2025-12-09)
4. One Year of MCP: November 2025 Spec Release, https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/ (2025-11-25)
5. Introducing the MCP Registry, https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/ (2025-09-08)
6. MCP Apps, https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/ (2026-01-26)
7. The 2026-07-28 Specification, https://blog.modelcontextprotocol.io/posts/2026-07-28/ (2026-07-28)
8. The New MCP Roadmap, https://blog.modelcontextprotocol.io/posts/mcp-roadmap/ (2026-08-22)
9. Official MCP Registry API (полная выгрузка), https://registry.modelcontextprotocol.io/v0/servers (2026-09-26)
10. SEP-2007 Payment Support for MCP Servers, https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2008 (2025-12-23)
11. Anthropic — Claude for Creative Work, https://www.anthropic.com/news/claude-for-creative-work (2026-04-28)
12. The Verge — Claude creative connectors, https://www.theverge.com/ai-artificial-intelligence/919648/anthropic-claude-creative-connectors-adobe-blender (2026-04-28)
13. Claude — Connectors directory, https://claude.com/connectors (2026-09-26)
14. Claude Marketplace — Adobe for creativity, https://claude.com/marketplace/connectors/adobe-creativity (2026-09-26)
15. Claude — Blender connector, https://claude.com/connectors/blender (2026-09-26)
16. Claude — Figma connector, https://claude.com/connectors/figma (2026-09-26)
17. Claude Blog — Claude Marketplace, https://claude.com/blog/claude-marketplace (2026-09-23)
18. Claude Blog — Build plugins for Claude, https://claude.com/blog/build-plugins-for-claude (2026-09-25)
19. Claude Blog — Agent Skills open standard, https://claude.com/blog/organization-skills-and-directory (2025-12-18)
20. Anthropic — Claude Skills, https://www.anthropic.com/news/skills (2025-10-16)
21. Ars Technica — Firefly AI Assistant, https://arstechnica.com/ai/2026/04/adobe-takes-creative-cloud-into-claude-code-esque-territory/ (2026-04-15)
22. TechCrunch — Adobe AI assistant in Premiere/Illustrator/InDesign, https://techcrunch.com/2026/06/18/adobe-adds-its-ai-assistant-to-premiere-illustrator-and-indesign/ (2026-06-18)
23. TNW — Adobe AI week, https://thenextweb.com/news/adobe-ai-week-firefly-agent-disney-semrush-genstudio-linkedin (2026-06-24)
24. TechCrunch — Adobe tools in Slack, https://techcrunch.com/2026/09/02/adobe-is-making-its-tools-available-in-slack/ (2026-09-02)
25. Computerworld — Firefly Graph, https://www.computerworld.com/article/4186410/adobe-new-firefly-graph-can-turn-creative-workflows-into-reusable-assets.html (2026-06)
26. The Letter Two — Adobe AI Collaborators / Workfront MCP, https://thelettertwo.com/2026/08/13/adobe-launches-ai-collaborators-workfront-general-availability/ (2026-08-13)
27. SiliconANGLE — Adobe CX Enterprise, https://siliconangle.com/2026/04/20/adobe-deploys-agents-across-customer-experience-tools/ (2026-04-20)
28. Computerworld — Adobe Summit 2026 / смена CEO, https://www.computerworld.com/article/4146823/adobe-summit-2026-how-adobe-hopes-to-redesign-marketing-and-creativity-with-ai.html (2026-04-13)
29. ie3jp/illustrator-mcp-server (сравнение с официальным Illustrator MCP), https://github.com/ie3jp/illustrator-mcp-server (2026-08/09)
30. Adobe Help — AI tools with Illustrator, https://helpx.adobe.com/illustrator/desktop/connect-with-other-apps-and-tools/about-using-ai-tools-with-illustrator.html (2026; не открылся, ссылка из README)
31. CG Channel — AE 26.5 + AI Assistant beta (поток adobe_platforms), https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/ (2026-09)
32. Adobe Community — AE AI Assistant beta (поток adobe_platforms), https://community.adobe.com/announcements-532/new-in-after-effects-beta-after-effects-ai-assistant-1635658 (2026-09)
33. Adobe Developer Blog — UXP во флагманах (поток adobe_platforms), https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications (2026-09)
34. Figma Blog — Agents, meet the Figma canvas, https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/ (2026-03-24)
35. Figma Blog — Config 2026 recap, https://www.figma.com/blog/config-2026-recap/ (2026-06)
36. Figma Release Notes — Weave via MCP, skills в Community, лимиты AI-кредитов, https://www.figma.com/release-notes/?title=figma-mcp-run-weave-tools-right-from-your-favorite-agent (2026-08)
37. SiliconANGLE — Figma orchestration bet / Code to Canvas, https://siliconangle.com/2026/02/26/figmas-orchestration-bet-mcp-network-effects-redefine-software-defensibility/ (2026-02-26)
38. TechCrunch — Canva $4B ARR, LLM-рефералы, https://techcrunch.com/2026/02/18/canva-gets-to-4b-in-revenue-as-llm-referral-traffic-rises/ (2026-02-18)
39. Digital Trends — Canva brand kit в ChatGPT, 12M designs, https://www.digitaltrends.com/computing/canva-now-lets-chatgpt-create-designs-that-match-your-brand-logo-font-and-colors/ (2026-02-14)
40. TechCrunch — Canva acquires animation startups (поток adobe_platforms), https://techcrunch.com/2026/02/23/canva-acquires-startups-working-on-animation-and-marketing/ (2026-02-23)
41. DaVinci Resolve 21.1 — конспект, https://github.com/ahastudio/til/blob/main/video/davinci-resolve-21-1.md (2026-09)
42. Blackmagic Design PR — Resolve 21.1, https://www.blackmagicdesign.com/media/release/20260908-03 (2026-09-08)
43. OpenAI — Developers can now submit apps to ChatGPT, https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/ (2025-12-17)
44. OpenAI — Apps SDK, https://developers.openai.com/apps-sdk/ (2025-10-06)
45. The Decoder — ChatGPT commerce retreat, https://the-decoder.com/chatgpt-users-research-products-but-wont-buy-there-forcing-openai-to-rethink-its-commerce-strategy/ (2026-03-07)
46. Growth Memo — AI Halftime Report H1 2026, https://www.growth-memo.com/p/ai-halftime-report-h1-2026 (2026-07-29)
47. OpenAI — GPT-6 Astra (computer use, OSWorld 2.0), https://openai.com/index/gpt-6-astra/ (2026-09-03)
48. Вторично: pavel-rp — Monetization market research (MCP, Apps SDK, x402, цены платных MCP), https://github.com/pavel-rp/second-memory-mcp/blob/master/docs/research/results/04-monetization-market-research.md (2026-07-07)
49. Вторично: clankwright — MCP ecosystem state (каталоги), https://github.com/clankwright/science/blob/main/comsci/ai-empowerment/raw/mcp-ecosystem/ecosystem-state-may-2026.md (2026-05)
50. Вторично: alp82 — competitor landscape (skills.sh, мёртвые серверы), https://github.com/alp82/aistack/blob/main/docs/research/competitor-landscape-2026-07.md (2026-07)
51. apify/apify-mcp-server (x402, Skyfire), https://github.com/apify/apify-mcp-server (2026-09)
52. mcpize/mcpize-skills (85% revenue share), https://github.com/mcpize/mcpize-skills (2026)
53. CoinDesk — Visa, Mastercard, Ripple join x402, https://www.coindesk.com/tech/2026/07/15/visa-mastercard-and-ripple-join-the-standard-letting-ai-agents-pay-in-stablecoins (2026-07-15)
54. GitHub search — «mcp monetization paid», https://github.com/search?q=mcp+monetization+paid&type=repositories (2026-09-26)
55. InfoQ — OpenClaw/ClawHub (900 вредоносных skills), https://www.infoq.com/news/2026/03/aws-lightsail-openclaw-security/ (2026-03-17)
56. Unit 42 — OpenClaw skill marketplace supply-chain, https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/ (2026-06)
57. CSO Online — RCE by design в MCP, https://www.csoonline.com/article/4159889/rce-by-design-mcp-architectural-choice-haunts-ai-agent-ecosystem.html (2026-04-20)
58. SecurityWeek — MCP hijacking и OAuth Claude Code, https://www.securityweek.com/claude-code-oauth-tokens-can-be-stolen-through-stealthy-mcp-hijacking/ (2026-05)
59. Reversec — Skill Issues, https://labs.reversec.com/posts/2026/05/skill-issues-compromising-claude-code-with-malicious-skills-agents-part-1 (2026-05)
60. BrightSec — ANSI escape injection в MCP, https://brightsec.com/research/detecting-ansi-escape-sequence-injection-in-mcp-servers-with-dast/ (2026-07)
61. GBHackers — Microsoft UFO MCP flaw, https://gbhackers.com/critical-microsoft-ufo-mcp-flaw/ (2026-09-02)
62. Quandri — MCP is dead?, https://www.quandri.io/engineering-blog/mcp-is-dead (2026-05-29)
63. Maharship — Why MCP was always a bad idea, https://maharship.com/blog/why-mcp-was-always-a-bad-idea/ (2026-09-14)
64. TechCrunch — X MCP server, https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/ (2026-06-30)
65. WebKit — Safari MCP server, https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/ (2026-07)
66. 9to5Google — Google Home MCP, https://9to5google.com/2026/09/16/google-home-mcp (2026-09-16)
67. GitHub — Dakkshin/after-effects-mcp, https://github.com/Dakkshin/after-effects-mcp (2026-09-26)
68. GitHub search — after effects mcp (72 репозитория), https://github.com/search?q=after+effects+mcp&type=repositories (2026-09-26)
69. Registry — Prism / oneprism After Effects MCP, https://registry.modelcontextprotocol.io/v0/servers?search=oneprism (2026-08-02)
70. GitHub — ahujasid/mcp-for-blender, https://github.com/ahujasid/mcp-for-blender (2026-09-26)
71. GitHub — samuelgursky/davinci-resolve-mcp, https://github.com/samuelgursky/davinci-resolve-mcp (2026-09-26)
72. GitHub — hetpatel-11/Adobe_Premiere_Pro_MCP, https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP (2026-09-26)
73. GitHub — alisaitteke/photoshop-mcp, https://github.com/alisaitteke/photoshop-mcp (2026-09-26)
74. GitHub — ttiimmaacc/cinema4d-mcp, https://github.com/ttiimmaacc/cinema4d-mcp (2026-09-26)
75. GitHub — capoomgit/houdini-mcp, https://github.com/capoomgit/houdini-mcp (2026-09-26)
76. GitHub — 8beeeaaat/touchdesigner-mcp, https://github.com/8beeeaaat/touchdesigner-mcp (2026-09-26)
77. GitHub — chongdashu/unreal-mcp, https://github.com/chongdashu/unreal-mcp (2026-09-26)
78. GitHub — CoplayDev/unity-mcp (Aura), https://github.com/CoplayDev/unity-mcp (2026-09-26)
79. GitHub — flopperam/unreal-engine-mcp (куплен Aura), https://github.com/flopperam/unreal-engine-mcp (2026-09-26)
80. GitHub — GLips/Figma-Context-MCP, https://github.com/GLips/Figma-Context-MCP (2026-09-26)
81. GitHub — figma/mcp-server-guide, https://github.com/figma/mcp-server-guide (2026-09-26)
82. GitHub — plainly-videos/mcp-server, https://github.com/plainly-videos/mcp-server (2026-09)
83. GitHub — anthropics/skills, https://github.com/anthropics/skills (2026-09-26)
84. GitHub — calesthio/OpenMontage, https://github.com/calesthio/OpenMontage (2026-09-26)
85. GitHub — Vincentwei1021/video-talkcraft, https://github.com/Vincentwei1021/video-talkcraft (2026-09-26)
86. GitHub — iart-ai/motion-design-skills, https://github.com/iart-ai/motion-design-skills (2026-09-26)
87. Registry / GitHub — Trillboards DOOH MCP, https://github.com/trillboards/dooh-agent-example (2026-03)
88. Поток dooh_3d — BDOOH creative spec reference, https://bdooh.com/research/dooh-creative-spec-reference/ (2026)
89. Поток dooh_3d — DOOH Marketing specs guide / MCP, https://doohmarketing.com/dooh-creative-specs-guide (2026)
90. Поток dooh_3d — FOOH.com screens library, https://fooh.com/blog/dooh-library-and-screens-on-fooh-com/ (2025–2026)
91. Vistar dynamic creative spec, https://github.com/vistarmedia/dynamic-creative-spec (2025-10)
92. Поток demand_scout — Next Horizon: AEUX vs Overlord vs Convertify vs Prism, https://nexthorizon.art/blog/aeux-vs-overlord-vs-convertify-vs-prism-best-way-to-transfer-and-animate-figma (2026)
93. Поток demand_scout — Plainly pricing (Capterra), https://www.capterra.com/p/10026817/Plainly/ (2026)
94. Поток demand_scout — Nexrender pricing, https://www.nexrender.com/pricing (2026)
