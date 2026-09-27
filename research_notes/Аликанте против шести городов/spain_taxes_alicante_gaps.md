# Spain 2026: autónomo taxes (IRPF + RETA) for an Alicante family, plus the remaining Alicante school gaps

The family: two parents aged 24, married, and one child aged 4–5. All are Russian citizens coming on the Digital Nomad Visa. The father is a freelance motion designer earning $5k/$6k/$8k a month, all from clients outside Spain. The wife has no income.

Research date: 27 Sep 2026. **Method caveat:** the network egress proxy blocked every page fetch (BOE, DOGV, seg-social.es, AEAT sede, hisenda.gva.es, eursc.eu, escuelaeuropea.org, kingscollegeschools.org, ibo.org, garrigues, guiafiscal and others all returned "CONNECT 403"). So every finding below comes from **search-result extracts** of the cited URLs, not from reading the full pages. 35 web searches were used. The "accessed" date is 27 Sep 2026 for all URLs.

---

## Q1. RETA 2026: contribution table, norm, MEI, and the exact monthly cuota at ~€3,200 / ~€3,700 / ~€4,800 net per month

### Takeaway
The 2026 RETA table is **frozen at the 2025 bases**. Real Decreto-ley 3/2026 of 3 Feb 2026 extends the transitional table in RDL 13/2022, and the contribution order is Orden PJC/297/2026 of 30 March. The only change is the MEI, which rose from 0.8% to **0.9%**, so the total rate went from 31.4% to **31.5%**. The monthly cuota at the minimum base is **€478.68** for €3,190–3,620 net per month, **€504.41** for €3,620–4,050, and **€545.59** for €4,050–6,000.

### Cited Findings
- RDL 3/2026, of 3 Feb 2026, "para la revalorización de las pensiones públicas y otras medidas urgentes en materia de Seguridad Social", is BOE-A-2026-2548 — [BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548). Secondary sources say that during 2026 the general and reduced tables are those in DT1 of RDL 13/2022, i.e. the 2025 amounts carried over — [elderecho.com](https://elderecho.com/el-gobierno-prorroga-las-cuotas-de-autonomos-en-2026-sin-subidas); [supercontable](https://www.supercontable.com/boletin/H/articulos/suben_en_2026_las_cuotas_autonomos_societarios_y_autonomos_colaboradores.html)
- The contribution order for 2026 is Orden PJC/297/2026, of 30 March (BOE-A-2026-7296) — [BOE](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7296)
- "Las cuotas de autónomos 2026 se han congelado respecto a 2025… 15 tramos… de 200 € a 590 €/mes… El único cambio real es la subida del MEI al 0,9%… tipo 31,5% (CC 28,3 + CP 1,3 + CA 0,9 + FP 0,1 + MEI 0,9)" — [Infoautónomos](https://www.infoautonomos.com/seguridad-social/cuota-de-autonomos-cuanto-se-paga/); [Wolters Kluwer](https://www.wolterskluwer.com/es-es/expert-insights/cuotas-autonomos-2026)
- The minimum cuota is €205.88 and the maximum is €1,606.88 per month. The maximum base in 2026 is €5,101.20 (0.315 × 5,101.20 = 1,606.88) — [contasimple / alegra extracts](https://www.contasimple.com/blog/cuotas-autonomos-2026/)
- Tramo 9 (net €3,190.01–3,620/month) has a base of €1,519.61–3,620 and a cuota of **€478.68**–1,140.30. Tramo 11 (net €4,050.01–6,000) has a base of €1,732.03–5,101.20 and a cuota of **€545.59**–1,606.88 — [search extract, Infoautónomos / Wolters Kluwer / ayudatpymes result set](https://ayudatpymes.com/gestron/cuota-autonomos/)
- Exception, not relevant to this family: for *autónomos societarios* and family collaborators, the minimum base rose 42% to €1,424.40 per month in 2026 — [supercontable](https://www.supercontable.com/boletin/H/articulos/suben_en_2026_las_cuotas_autonomos_societarios_y_autonomos_colaboradores.html)

### Inferences
- Tramo 10 (net €3,620–4,050) has a base of 1,601.31 × 0.315 = **€504.41**. This comes from the 2025 DT1 table times the 31.5% rate. It is not directly quoted in any extract, but it is consistent with tramos 9 and 11.
- Answers for the three incomes asked about, using the minimum base of each tramo:
  - ~€3,200 net → €478.68
  - ~€3,700 net → €504.41
  - ~€4,800 net → €545.59
- The previous 2025 figures (≈€460/490/530) were slightly low mainly because of the MEI. They were also placed in the wrong tramo.
- Placing the family in a tramo: the Seguridad Social "rendimiento neto" equals the IRPF net (after expenses, the RETA cuota and the difícil-justificación allowance) minus a 7% generic deduction, divided by 12. My Python model gives:
  - With 10% expenses: $60k → €3,105 per month (tramo 8, **€452.94**); $72k → €3,794 (tramo 10, **€504.41**); $96k → €5,228 (tramo 11, **€545.59**).
  - With 5% expenses: $60k → €3,286 (tramo 9, €478.68); $72k → €4,039 (tramo 10); $96k → €5,556 (tramo 11).
- The cuota is provisional. Seguridad Social regularises it against the AEAT figures after the year ends.

### Gaps
- I could not open the BOE text of RDL 3/2026 or Orden PJC/297/2026 (fetch blocked). The per-tramo base figures come from secondary extracts plus the known 2025 DT1 table.
- Tramo 8 (€2,760–3,190: base 1,437.91 → €452.94) is also my own calculation, not quoted.

---

## Q2. Tarifa plana (€80) in 2026: norm and duration

### Takeaway
In practice the tarifa plana is **applied at €80 per month for the first 12 months**. It can be extended for another 12 months only if net income in year 1 is below the SMI (€17,094 per year in 2026), which this family will not meet. **Legal nuance:** no norm published for 2026 expressly sets the amount. It rests on art. 38 ter LETA (introduced by RDL 13/2022) and on budget extension. The Seguridad Social is still applying €80, and the MEI is charged on top, so the real payment is about €85–88 per month.

### Cited Findings
- "With budgets extended, no published norm has yet set the amount for 2026: it does not appear in either… Order PJC/297/2026 or in Royal Decree-Law 3/2026… In practice, the 80 € fee continues to be applied… advisable to check the amount in Import@ss… MEI of 0.9%… total ≈85–88 €/month" — [Radar Fiscal](https://radarfiscal.es/en/guias/tarifa-plana-autonomos/)
- The tarifa plana is €80 per month for the first 12 months and can be extended for 12 more months if first-year net income is below the SMI. The SMI for 2026 is €17,094 per year (Real Decreto 126/2026) — [palenciaasesores](https://palenciaasesores.es/tarifa-plana-autonomos-2026/); [conversoriaecnae](https://conversoriaecnae.substack.com/p/tarifa-plana-autonomos-2026-renovacion)
- The flat rate can only be extended once, and the extension must be requested before the 12 months end — [declarando.es](https://declarando.es/prorroga-tarifa-plana-autonomos)

### Inferences
- The model uses €80 + 0.9% MEI on the minimum base (≈€88.56 per month, ≈€1,063 per year) for year 1.
- Year 2 is at the full cuota: net income is about €30–60k per year, far above the SMI, so there is no extension.
- Eligibility requires no RETA registration in the previous 2 years (3 if the person previously had the tarifa plana). This is the standard rule, but it was not re-verified here. The family has never been in RETA, so it should be eligible.
- If registration happens mid-year, the 12 tarifa-plana months straddle two calendar years. The model assumes a 1 January start, so the "year 1" figures are an idealisation.

### Gaps
- There is no official 2026 text confirming the €80 amount. Confirm in Import@ss at registration.

---

## Q3. Comunitat Valenciana: IRPF scale, minimums and deductions for 2026 income

### Takeaway
**New for 2026:** Ley 5/2026 of 31 July (DOGV 10 Aug 2026; BOE-A-2026-19331), in its art. 18, amended art. 2 of Ley 13/1997. It **cut the Valencian scale retroactively from 1 Jan 2026**. The rates now run from **8.8% to 29.35%** (previously 9% to 29.5%), with the same 11 brackets. The personal and family minimums stay at **€6,105 per taxpayer and €2,640 for the first child**, 10% above the state amounts.

The only Valencian deduction that really matters for this family is the **habitual-residence rent deduction**. It is 25% of rent, capped at €950, because the tenant is 35 or younger. It only applies if the base liquidable is **≤ €47,000 in joint filing** (≤ €30,000 individual). That limit is met in years 1–2 at all three incomes except $96k, and in year 3+ only at $60k (and partly at $72k).

### Cited Findings
- Ley 5/2026, de 31 de julio, de medidas fiscales, de gestión administrativa y financiera, y de organización de la Generalitat, is BOE-A-2026-19331 — [BOE ELI](https://www.boe.es/eli/es-vc/l/2026/07/31/5); [noticias.juridicas](https://noticias.juridicas.com/base_datos/CCAA/1009432-l-presidencia-5-2026-de-31-jul-ca-valencia-medidas-fiscales-de-gestion.html)
- "Marginal rates of the autonomous IRPF scale were reduced for 2026, now ranging between 8.8% and 29.35% (previously 9%–29.50%)… eleven types with retroactive effects from 1 Jan 2026… measures in force from 11 Aug 2026 except IRPF, which applies to all 2026" — [Garrigues](https://www.garrigues.com/es_ES/noticia/comunidad-valenciana-repasamos-principales-novedades-tributos-autonomicos-2026-2027) (extract); [Cuatrecasas](https://www.cuatrecasas.com/es/spain/fiscalidad/art/comunidad-valenciana-novedades-tributarias-2026)
- "With a general taxable base of 22,000 €, the autonomous quota drops 54 € (from 2,280 to 2,226); with 72,000 € the reduction rises to 324 €… decrease of 0.15–0.6 pp per bracket; first bracket 0–12,000 at 8.8% = 1,056 €; 29.35% from 200,000 €" — [guiafiscal.es](https://guiafiscal.es/irpf/valencia/) (secondary); the reduction is "más de un 2%" and covers the brackets up to €100,000 — [Valencia Plaza](https://valenciaplaza.com/valenciaplaza/comunitat-valenciana1/el-gobierno-valenciano-rebaja-la-tarifa-autonomica-del-irpf-mas-de-un-2-para-2026); [valencianews](https://valencianews.es/economia/rebaja-irpf-comunitat-valenciana-2026-ley-medidas-fiscales-vivienda-protegida/)
- Valencian autonomous minimums: taxpayer €6,105; descendants €2,640 / 2,970 / 4,400 / 4,950, plus €3,080 for a child under 3 — [AEAT Manual Renta 2025 – CV importes mínimo](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c14-adecuacion-impuesto-circunstancias-personales/minimo-autonomico-personal-familiar/comunitat-valenciana-importes-minimo-personal-familiar.html). None of the extracts reports a change to the minimums in Ley 5/2026.
- Rent deduction (arrendamiento de vivienda habitual), CV, 2025 rules:
  - 20% of rent, capped at €800; **25% capped at €950 if the tenant is ≤35**, a victim of gender violence or disabled; 30% capped at €1,100 if two or more of these apply.
  - Requires base liquidable general + ahorro ≤ €30,000 (individual) or **≤ €47,000 (joint)**.
  - No family member may own another dwelling within 50 km for half the year or more.
  - Source: [AEAT Manual Renta 2025 – CV arrendamiento](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025-deducciones-autonomicas/comunitat-valenciana/arrendamiento-pago-cesion-uso-vivienda-habitual.html); [elEconomista](https://www.eleconomista.es/declaracion-renta/noticias/13845969/03/26/requisitos-para-la-deduccion-por-alquiler-de-la-renta-20252026-en-la-comunidad-valenciana-asi-te-lo-puedes-desgravar.html)
- Birth or adoption deduction: €600 for the first child, for the year of birth and the following two years only, with a base limit of €30k/€47k. **This child (4–5) is not eligible** — [tramitarbien/taxfix extracts](https://taxfix.com/es-es/renta/deducciones/deducciones-autonomicas-en-la-comunidad-valenciana/)
- A secondary site also lists: dental/mental/optical health up to €150; sport 30% up to €150; and "hijos menores de 5 años (660–1.100 €)" — [LaborIA](https://laboria.app/tabla-irpf-2026/valencia/). **This last item is unverified and may be a misreading.** It is not in the AEAT or elEconomista extracts.
- The official list is the GVA "Beneficios fiscales 2025" PDF — [hisenda.gva.es](https://hisenda.gva.es/documents/168162620/0/Beneficios+fiscales+2025+ampliado+con+requisitos.pdf/6f47593e-f72f-06c4-5d0e-33185d694428) (could not be opened).

### Inferences
- **Reconstructed 2026 Valencian scale used in the model**, marked as assumed except where anchored:
  - 0–12k: 8.8% (anchored)
  - 12–22k: 11.7% (derived from the €2,226 at €22k)
  - 22–32k: 14.6%
  - 32–42k: 17.0%
  - 42–52k: 19.4%
  - 52–62k: 21.9%
  - 62–72k: 24.4%
  - 72–100k: 26.0%
  - 100–150k: 27.0%
  - 150–200k: 28.05%
  - >200k: 29.35% (anchored)
- Brackets 3–7 are calibrated so that the total cut at €72k equals the reported €324. The split between them is an assumption. The possible error is a few tens of euros at these incomes.
- Sensitivity check (year 3+, joint, 10% expenses): the 2026 scale saves only €100 / €148 / €259 per year compared with the 2025 scale.
- The rent-deduction taper (linear between €44k and €47k joint) is **my assumption and needs verification**. Some Valencian deductions phase out; others are a hard cliff.
- If the deduction is a hard cliff instead, $72k year 3+ joint (BL ≈ €45.6k) would get the full €950.
- The rent deduction requires the fianza to be deposited with the Generalitat, and the family must be CV-resident for the year.

### Gaps
- I could not read the official article 18 text, so the full bracket-by-bracket 2026 Valencian rates are not verified (BOE/DOGV fetch blocked).
- Not verified whether Ley 5/2026 or Ley 5/2025 changed the rent-deduction limits or amounts for 2026.
- The "menores de 5 años" deduction is unverified.

---

## Q4. Joint-taxation reduction (€3,400), the 7%/€2,000 rule, and the 20% start-up reduction in 2026

### Takeaway
- The **€3,400 joint reduction is unchanged**. It has not been updated since 2007.
- **Correction to the previous calculation:** gastos de difícil justificación are **5%, not 7%**, with the €2,000 cap. The AEAT Manual Renta 2025 says 5% applies for 2025. RDL 16/2025, which contained year-end tax measures, was **not validated** (derogated; Congress vote 27 Jan 2026, 171 in favour, 178 against). For these incomes the cap binds either way, so the effect is **€0**.
- The **20% start-up reduction** (art. 32.3 LIRPF) applies to the first year with positive net income and the following year, on up to €100k of net income. There is a real risk that the father's earlier freelancing from Bali counts as "prior activity".

### Cited Findings
- Joint reduction: €3,400 for married couples, €2,150 for single-parent units; not updated since 2007 — [AEAT Manual 2025 – reducción por tributación conjunta](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c13-determinacion-renta-contribuyente-sujeta-gravamen/reducciones-base-imponible-general/reduccion-tributacion-conjunta.html); [merca2, May 2026](https://www.merca2.es/2026/05/09/declaracion-conjunta-irpf-congelacion-hacienda-2378209/)
- AEAT: "En el período impositivo 2025 se mantiene la aplicación del porcentaje del 5 por 100 … sin que la cuantía resultante pueda superar 2.000 euros anuales" — [AEAT novedades Renta 2025](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/rendimiento-actividades-economicas.html)
- RDL 16/2025 of 23 Dec 2025 (BOE-A-2025-26458) was not validated. The repeal was published in the BOE on 28 Jan 2026 — [BOE](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-26458); [fiscal-impuestos](https://www.fiscal-impuestos.com/derogacion-medidas-tributaria-IRPF-IS-IVA-IVTNU-RDLey-16-2025-no-convalidado); [noticias.juridicas](https://noticias.juridicas.com/actualidad/noticias/20823-iquest;que-implica-el-portazo-al-real-decreto-ley-16-2025-en-el-congreso-a-nivel-fiscal/)
- *Conflict:* some adviser blogs claim "7% in 2026" ([getquipu](https://getquipu.com/blog/gastos-de-dificil-justificacion/)), while others say 5% ([conversoriaecnae](https://www.conversoriaecnae.es/gastos-deducibles/gastos-dificil-justificacion)). The AEAT statement for 2025, plus the derogation of RDL 16/2025, points to **5% for 2026** unless a later norm (not found) restored 7%.
- 20% start-up reduction rules (art. 32.3 LIRPF):
  - estimación directa;
  - activity started after 1 Jan 2013;
  - first period with positive net income and the following one;
  - on up to €100,000 of net income;
  - no other economic activity in the year before the start date;
  - not available if more than 50% of income comes from a former employer of the previous year.
  - Sources: [AEAT Manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2024/c07-rendimientos-actividades-economicas-estimacion-directa/fase-3-determinacion-rendimiento-neto-total/reduccion-rendimiento-neto-inicio-actividad-economica.html); [Infoautónomos](https://www.infoautonomos.com/blog/fiscalidad/acogerte-reduccion-20-irpf-por-inicio-de-actividad/); DGT V0452-25 (no 20% if the first year was in módulos) — [Iberley](https://www.iberley.es/noticias/segun-dgt-reduccion-inicio-actividad-no-puede-aplicarse-si-primer-ejercicio-se-aplica-modulos-luego-se-pasa-estimacion-directa-35130)

### Inferences
- **Risk flag for the 20% reduction:** the father freelanced as a motion designer while living in Bali. The "no activity in the prior year" test may be read as covering any activity, including abroad. If so, the 20% reduction would not apply. I found no DGT ruling that settles this for a newly arrived non-resident; get an adviser's opinion.
- Without the 20% reduction, year 1 IRPF rises by about €1.3–2.9k.
- **Joint filing is always better** for this family, by about €1.5–2.4k per year. Joint filing gives the €3,400 reduction plus the full child minimum. Individual filing gets no reduction, and the child minimum is split 50/50 between parents (art. 61 LIRPF), so the father gets €1,200 state / €1,320 CV. This prorating rule comes from my knowledge and was not re-verified. Even if the father got the full child minimum, individual filing is still worse: 27.0 / 28.7 / 31.4% vs 22.9–29.5% joint.
- Joint filing also makes the rent deduction reachable (€47k vs €30k limit).
- Beckham regime (art. 93 LIRPF): not modelled. Self-employed freelancers generally qualify only as "entrepreneurs" certified by ENISA under the Startups Law. That is not the typical DNV freelancer case, and was not verified here.

### Gaps
- No official 2026 confirmation of the 5% rate. It is inferred from the default rule plus the RDL 16/2025 derogation.
- The DGT position on prior foreign activity and the 20% reduction is not found.

---

## Q5. Recomputed total burden (IRPF state + CV + RETA), EUR/USD 1.1367

### Takeaway
The previous figures are **broadly confirmed**. Without the rent deduction, the new model gives:
- steady state (joint, 10% expenses): **24.7% / 26.7% / 29.5%** (previously 25.0 / 26.7 / 29.7);
- year 1: **13.6% / 15.4% / 18.4%** (previously 13.6 / 15.5 / 18.5).

**New:** if the family rents and qualifies for the CV rent deduction (≤35, BL ≤ €47k joint), the $60k and $72k cases drop further, to **11.8% / 13.9%** in year 1 and **22.9% / 25.9%** steady state. With 5% expenses instead of 10%, the burden is 1.5–2.3 points higher.

**Model assumptions:**
- estimación directa simplificada;
- difícil justificación at 5%, capped at €2,000 (the cap binds);
- RETA: tarifa plana in year 1, full tramo from year 2;
- the 20% start-up reduction applies in years 1–2 (see the Q4 risk);
- full calendar-year residence;
- the state scale is unchanged at 9.5/12/15/18.5/22.5/24.5 (not re-verified for 2026; no change reported);
- state minimums €5,550 + €2,400; CV minimums €6,105 + €2,640;
- joint reduction €3,400;
- rent deduction €950 with an assumed taper between €44k and €47k;
- 2026 CV scale reconstructed (Q3);
- "expenses" are real business expenses as a % of gross; net = gross − expenses − IRPF − RETA.

### Cited Findings
- Parameters as cited in Q1–Q4. The EUR/USD rate of 1.1367 (ECB, 24 Sep 2026) was provided by the brief, not verified.

### Inferences

**Results, 10% expenses** (EUR unless marked; "Net" = after tax, RETA and expenses)

| $/yr | Yr | Mode | Gross € | RETA € | IRPF state € | IRPF CV € (after rent ded.) | Rent ded. | Total € | Total $ | % gross | Net € | Net $ | Net $/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 60k | 1 | joint | 52,784 | 1,063 | 3,151 | 1,993 | 950 | 6,206 | 7,054 | 11.8% | 41,300 | 46,946 | 3,912 |
| 60k | 1 | indiv | 52,784 | 1,063 | 3,787 | 3,637 | 0 | 8,487 | 9,647 | 16.1% | 39,019 | 44,353 | 3,696 |
| 60k | 2 | joint | 52,784 | 5,435 | 2,626 | 1,478 | 950 | 9,540 | 10,844 | 18.1% | 37,966 | 43,156 | 3,596 |
| 60k | 2 | indiv | 52,784 | 5,435 | 3,250 | 3,042 | 0 | 11,727 | 13,331 | 22.2% | 35,778 | 40,669 | 3,389 |
| 60k | 3+ | joint | 52,784 | 5,435 | 3,880 | 2,760 | 950 | 12,075 | 13,726 | 22.9% | 35,431 | 40,274 | 3,356 |
| 60k | 3+ | indiv | 52,784 | 5,435 | 4,623 | 4,405 | 0 | 14,462 | 16,439 | 27.4% | 33,043 | 37,561 | 3,130 |
| 72k | 1 | joint | 63,341 | 1,063 | 4,450 | 3,285 | 950 | 8,798 | 10,001 | 13.9% | 48,209 | 54,799 | 4,567 |
| 72k | 1 | indiv | 63,341 | 1,063 | 5,193 | 4,957 | 0 | 11,213 | 12,746 | 17.7% | 45,794 | 52,054 | 4,338 |
| 72k | 2 | joint | 63,341 | 6,053 | 3,712 | 2,606 | 950 | 12,371 | 14,062 | 19.5% | 44,636 | 50,738 | 4,228 |
| 72k | 2 | indiv | 63,341 | 6,053 | 4,455 | 4,250 | 0 | 14,758 | 16,775 | 23.3% | 42,249 | 48,025 | 4,002 |
| 72k | 3+ | joint | 63,341 | 6,053 | 5,523 | 4,848 | 458* | 16,424 | 18,669 | 25.9% | 40,583 | 46,131 | 3,844 |
| 72k | 3+ | indiv | 63,341 | 6,053 | 6,266 | 6,082 | 0 | 18,401 | 20,916 | 29.1% | 38,606 | 43,884 | 3,657 |
| 96k | 1 | joint | 84,455 | 1,063 | 7,263 | 7,204 | 0 | 15,529 | 17,652 | 18.4% | 60,480 | 68,748 | 5,729 |
| 96k | 1 | indiv | 84,455 | 1,063 | 8,006 | 8,065 | 0 | 17,133 | 19,475 | 20.3% | 58,876 | 66,925 | 5,577 |
| 96k | 2 | joint | 84,455 | 6,547 | 6,451 | 6,279 | 0 | 19,277 | 21,912 | 22.8% | 56,732 | 64,488 | 5,374 |
| 96k | 2 | indiv | 84,455 | 6,547 | 7,194 | 7,104 | 0 | 20,845 | 23,695 | 24.7% | 55,164 | 62,705 | 5,225 |
| 96k | 3+ | joint | 84,455 | 6,547 | 9,110 | 9,250 | 0 | 24,906 | 28,311 | 29.5% | 51,103 | 58,089 | 4,841 |
| 96k | 3+ | indiv | 84,455 | 6,547 | 9,989 | 10,195 | 0 | 26,731 | 30,385 | 31.7% | 49,278 | 56,015 | 4,668 |

\*Partial, because of the assumed taper (BL €45,554). With a hard cliff it would be the full €950.

RETA per month: year 1 ≈ €88.6. Years 2+: $60k → €452.94 (tramo 8); $72k → €504.41 (tramo 10); $96k → €545.59 (tramo 11).

**Results, 5% expenses** (joint rows; individual is about 2–5 points worse)

| $/yr | Yr | RETA € | IRPF st € | IRPF CV € | Rent ded. | Total € | Total $ | % gross | Net € | Net $/mo |
|---|---|---|---|---|---|---|---|---|---|---|
| 60k | 1 | 1,063 | 3,467 | 2,352 | 950 | 6,882 | 7,822 | 13.0% | 43,263 | 4,098 |
| 60k | 2 | 5,744 | 2,906 | 1,750 | 950 | 10,400 | 11,822 | 19.7% | 39,745 | 3,765 |
| 60k | 3+ | 5,744 | 4,311 | 3,157 | 950 | 13,211 | 15,017 | 25.0% | 36,934 | 3,499 |
| 72k | 1 | 1,063 | 4,919 | 3,723 | 950 | 9,704 | 11,031 | 15.3% | 50,470 | 4,781 |
| 72k | 2 | 6,053 | 4,180 | 3,037 | 950 | 13,270 | 15,084 | 21.0% | 46,904 | 4,443 |
| 72k | 3+ | 6,053 | 6,109 | 5,920 | 0 | 18,082 | 20,554 | 28.5% | 42,092 | 3,987 |
| 96k | 1 | 1,063 | 7,888 | 7,944 | 0 | 16,894 | 19,204 | 20.0% | 63,338 | 6,000 |
| 96k | 2 | 6,547 | 7,076 | 6,983 | 0 | 20,606 | 23,423 | 24.4% | 59,626 | 5,648 |
| 96k | 3+ | 6,547 | 10,060 | 10,280 | 0 | 26,887 | 30,562 | 31.8% | 53,345 | 5,053 |

Individual filing with 5% expenses, % of gross (years 1 / 2 / 3+):
- $60k: 17.5 / 23.9 / 29.6
- $72k: 19.2 / 24.7 / 30.9
- $96k: 22.0 / 26.3 / 34.0

**Joint filing without the rent deduction** (for families that do not qualify), % of gross (years 1 / 2 / 3+):

| $/yr | 10% expenses | 5% expenses |
|---|---|---|
| 60k | 13.6 / 19.9 / 24.7 | 14.8 / 21.5 / 26.8 |
| 72k | 15.4 / 21.0 / 26.7 | 16.8 / 22.5 / 28.5 |
| 96k | 18.4 / 22.8 / 29.5 | 20.0 / 24.4 / 31.8 |

Base liquidable, joint, 10% expenses (years 1 / 2 / 3+), relevant to the €47k rent limit:
- $60k: 32.2k / 28.7k / 36.7k
- $72k: 39.8k / 35.8k / 45.6k
- $96k: 55.0k / 50.6k / 64.1k

Note that year 2 has a *lower* base than year 1, because full RETA is deductible from year 2 onward.

**Other notes:**
- IRPF is paid in advance through modelo 130 (20% quarterly on year-to-date net income) and settled in the annual Renta. This affects cash flow, not the total.
- Invoices to foreign clients: B2B EU clients use reverse charge (inversión del sujeto pasivo), and services to non-EU clients are not subject to Spanish VAT. VAT was not in scope.
- **Year 1 in practice:** if the family arrives mid-2026, they are probably not Spanish tax residents for 2026 (fewer than 183 days). "Year 1" for IRPF would then be 2027, while the 12 tarifa-plana months start at RETA registration. These may not coincide.

**Python code used** (run 27 Sep 2026):

```python
# Spain 2026 IRPF (state + Comunitat Valenciana) + RETA for a freelance autonomo in Alicante
FX = 1.1367  # USD per EUR, ECB 24 Sep 2026 (given)

STATE = [(12450,.095),(20200,.12),(35200,.15),(60000,.185),(300000,.225),(float('inf'),.245)]
# Valencia 2026 (Ley 5/2026) - RECONSTRUCTED: anchors 8.8% first bracket, cuota at 22k = 2,226,
# cuota reduction at 72k = 324 vs 2025 scale, top 29.35%. Brackets 3-7 split is an assumption.
VAL26 = [(12000,.088),(22000,.117),(32000,.146),(42000,.170),(52000,.194),(62000,.219),
         (72000,.244),(100000,.260),(150000,.270),(200000,.2805),(float('inf'),.2935)]
VAL25 = [(12000,.09),(22000,.12),(32000,.15),(42000,.175),(52000,.20),(62000,.225),
         (72000,.25),(100000,.265),(150000,.275),(200000,.285),(float('inf'),.295)]

def scale(base, sc):
    t, lo = 0.0, 0.0
    for hi, r in sc:
        if base > lo: t += (min(base, hi) - lo) * r
        lo = hi
    return t

# RETA 2026 = 2025 general table (RDL 13/2022 DT1, extended by RDL 3/2026); rate 31.5% (incl. MEI 0.9%)
RETA = [(670,653.59),(900,718.95),(1166.70,849.67),(1300,950.98),(1500,960.78),(1700,960.78),
        (1850,1143.79),(2030,1209.15),(2330,1274.51),(2760,1356.21),(3190,1437.91),(3620,1519.61),
        (4050,1601.31),(6000,1732.03),(float('inf'),1928.10)]
RATE = 0.315
def reta_monthly(net_month):
    for hi, b in RETA:
        if net_month <= hi: return round(b*RATE, 2)

def reta_full(gross, exp):
    q = 500.0
    for _ in range(50):
        rn = gross - exp - 12*q                      # IRPF net before generic expenses
        rn -= min(0.05*rn, 2000)                     # gastos dificil justificacion (EDS)
        ss_net = rn*0.93/12                          # 7% generic deduction for SS
        q = reta_monthly(ss_net)
    return 12*q, ss_net

TARIFA_PLANA = 80.0 + 0.009*950.98   # 80 EUR + MEI on min base (~88.56) - conservative
def compute(usd, exp_pct, year, joint=True, val=VAL26, rent_ded=True, child_full=False):
    g = usd/FX; exp = g*exp_pct
    if year == 1: reta = 12*TARIFA_PLANA; ss_net = None
    else: reta, ss_net = reta_full(g, exp)
    rn = g - exp - reta
    gdj = min(0.05*rn, 2000); rn -= gdj
    red20 = 0.2*min(rn, 100000) if year in (1, 2) else 0
    bi = rn - red20
    bl = max(bi - (3400 if joint else 0), 0)
    child_s, child_v = (2400, 2640) if (joint or child_full) else (1200, 1320)
    min_s, min_v = 5550+child_s, 6105+child_v
    cs = max(scale(bl, STATE) - scale(min_s, STATE), 0)
    cv = max(scale(bl, val) - scale(min_v, val), 0)
    # Valencian rent deduction: 25% (tenant <=35) cap 950; limit BL 47k joint / 30k indiv,
    # linear taper assumed over last 3k (44-47k / 27-30k) - FLAGGED
    ded = 0
    if rent_ded:
        lim = 47000 if joint else 30000
        if bl <= lim - 3000: ded = 950
        elif bl <= lim: ded = 950*(lim - bl)/3000
    cv = max(cv - ded, 0)
    irpf = cs + cv
    total = irpf + reta
    net = g - exp - total
    return dict(g=g, exp=exp, reta=reta, ss_net=ss_net, bl=bl, cs=cs, cv=cv, ded=ded,
                irpf=irpf, total=total, pct=100*total/g, net=net)

# driver: loops over usd in (60000,72000,96000), exp in (.10,.05), year in (1,2,3), joint/indiv
```

### Gaps
- State scale 2026 unchanged: this is an assumption. No change was reported, and it was not re-verified on the BOE.
- 2026 CV brackets 3–7: reconstructed (Q3).
- Rent-deduction taper: assumed.
- 20% start-up reduction eligibility with prior foreign activity: uncertain (Q4).
- Tarifa plana €80: in practice yes, but no 2026 norm expressly sets it (Q2).
- Not modelled: pension plans, private health insurance for the self-employed (deductible up to €500 per person per year; not re-verified), and home-office utility share (30% of the proportional part).

---

## Q6. Alicante school gaps

### Takeaway
The official school pages could not be fetched, and the search extracts **did not reveal the 2026/27 Category III fee amounts at the European School of Alicante** or the **Mutxamel fees**. What was found:
- **King's College Alicante:** Reception tuition 2025/26 was €9,100 per year, with a non-refundable **enrolment fee of €1,550**. The school day and extended hours were not found.
- **El Valle Alicante:** listed on ibo.org. Its description says it offers **all three IB programmes (PYP, MYP, DP)**. It is **private** (Micole/Todoeduca describe it as a "Colegio Privado"; one Micole page says "Concertado" — conflicting). The price range is €300–700 per month.

### Cited Findings
- **European School of Alicante (ESA):**
  - Category III pupils pay the *minerval* set annually by the Board of Governors. Paying it is mandatory to confirm admission.
  - The school lists "Category III – School year 2025-2026" and a "School fees" page; the amounts were not visible in the extracts.
  - Billing contact: ALI-BILLING@eursc.eu.
  - Sources: [ESA Category III 2025-26](https://www.escuelaeuropea.org/en/escuela-europea-de-alicante/category-iii-school-year-2025-2026); [ESA School fees](https://www.escuelaeuropea.org/en/escuela-europea-de-alicante/school-fees); [ESA Enrolments](https://www.escuelaeuropea.org/en/escuela-europea-de-alicante/enrolments); enrolment policy PDFs [2025/26](https://www.escuelaeuropea.org/sites/default/files/2025-02/ESA_Enrolment%20policy%202025_2026.pdf)
  - For comparison only (Brussels European Schools, 2025/26, Category III): about €4,370 for nursery and €6,009 for primary per year — [internationalschools.brussels](https://internationalschools.brussels/en/tuition-fees-in-european-schools-in-brussels/). *Alicante's schedule may differ; do not substitute it.*
- **King's College, The British School of Alicante:**
  - Reception (ages 4–5), 2025/26: Term 1 €3,640 + Term 2 €2,730 + Term 3 €2,730 = **€9,100 per year**; lunch is compulsory and included.
  - "Pupils joining the school are charged a non-refundable **enrolment fee of €1,550** per pupil payable on acceptance"; an annual re-enrolment fee is added to the third-term bill.
  - Sources: [doris.school fees](https://www.doris.school/schools/spain/kings-college-the-british-school-of-alicante/fees); [ISD fees 2025/26](https://www.international-schools-database.com/in/alicante-costa-blanca/king's-college-the-british-school-of-alicante/fees); official FY26 fee PDF [kalicante_rebranded_fy26.pdf](https://www.alicante.kingscollegeschools.org/sites/school21/files/2025-03/kalicante_rebranded_fy26.pdf) and bus PDF [K_Alicante_Rebranded_FY26-SP-bus.pdf](https://www.alicante.kingscollegeschools.org/sites/school21/files/2025-09/K_Alicante_Rebranded_FY26-SP-bus.pdf) (could not be opened)
- **Colegio El Valle Alicante** (Avda. de la Condomina 65, 03540 Sant Joan d'Alacant / Alicante):
  - Appears in the IBO "find an IB school" directory — [ibo.org](https://ibo.org/programmes/find-an-ib-school/ibaem/c/colegio-el-valle-alicante/).
  - Described as "el primer y único colegio en la Comunidad Valenciana que imparte los tres programas del IB… desde Infantil hasta Bachillerato" — [school site / Micole extract](https://colegioelvallealicante.com/en/)
  - "Colegio Privado de Educación Infantil, Primaria, Secundaria y Bachillerato… entre 300 y 700 € mensuales" — [Micole](https://www.micole.net/alicante/sant-joan-dalacant/colegio-el-valle-alicante); another Micole/aggregator extract calls it "Concertado" — [micole (older page)](https://www.micole.net/alicante/sant-joan-dalacant/colegio-el-valle)
  - Contact: 965 15 56 19, secre.ali@colegioelvalle.com
- **The English School of Mutxamel:**
  - "Does not make its tuition fees public online", including for 2026/27.
  - Private, British Council certified, ages 3–17 (Nursery/Reception to Sixth Form), Pearson Edexcel IGCSE.
  - About €300 for materials on enrolment (one-off).
  - Contact: +34 965 951 017, info@theenglishschool.es, C/ Pintor Gisbert 3, Mutxamel.
  - Sources: [international-schools-database](https://www.international-schools-database.com/in/alicante-costa-blanca/the-english-school-alicante-costa-blanca); [doris.school](https://www.doris.school/schools/spain/the-english-school-of-mutxamel/overview-key-info); [MumAbroad](https://mumabroad.com/the-english-school-of-mutxamel/)

### Inferences
- **El Valle, private vs concertado:** the El Valle network (Madrid and Alicante) is generally private. A €300–700 monthly fee does not fit a concertado school, where Infantil/Primaria tuition is free. So "privado" is more likely. Confirm with the school.
- **El Valle IB:** the ibo.org listing confirms at least one authorised programme. The claim of all three programmes comes from the school itself and could not be confirmed programme-by-programme on ibo.org (fetch blocked).
- **ESA English section for a Russian-speaking child:** under standard European Schools rules, a pupil without an official-EU-language mother tongue (SWALS) is usually placed in the English section. Category III admission depends on available places, and ESA sections are often full at lower levels. This comes from general knowledge of eursc.eu rules and is **not verified** for ESA 2026/27. Check the enrolment policy PDF.
- For King's Reception, the fee PDF typically lists "extended day"/"early morning" services, but this was not visible.

### Gaps
- ESA 2026/27 Category III fee amounts (Nursery and Primary): not found. Next step: the escuelaeuropea.org fee page or email ALI-BILLING@eursc.eu.
- ESA English-section placement for a Russian-speaking child: not verified.
- King's Alicante 2026/27 Reception fee (only 2025/26 found), school-day timetable, and early/late care hours: not found.
- El Valle 2026/27 exact Infantil 4–5 fees; private vs concertado (conflicting sources); programme-level IB authorisation dates on ibo.org: not verified.
- English School of Mutxamel fees: not published; must request directly.
