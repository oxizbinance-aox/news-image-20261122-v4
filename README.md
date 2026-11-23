# Sunday 22 November 2026 — 42 stories, 7 regions

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/oxizbinance-aox/news-image-20261122-v4/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/oxizbinance-aox/news-image-20261122-v4/reward.svg)](https://make.fun/bounty/news-image-20261122)

One page that sums up Sunday 22 November 2026: **42 dated stories across
7 regions** — 3 leads with tall pictograms, 12 mid stories with illustrated
banners, a 27-story numbered list, a dot-matrix world map with numbered pins,
two bar charts, a six-number data strip, a UTC timeline and a DATE CHECK box
that names the near-miss stories from other days. Entry for the
[make.fun bounty "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122)
($100 pot: $20 1st, $12 2nd, $6 3rd, $2 4th–10th, $1.20 11th–50th;
entries close 24 Nov 2026 07:00 WIB).

![Sunday 22 November 2026 — 42 stories, 7 regions](entry.png)

## How it is built

`main.ts` (Node 22, stdlib only) runs `draw_news22_v4.py`, which draws
`entry.png` from scratch with PIL — every pictogram, banner, dot of the map
and bar of the charts is code, no external assets, no network. The render is
deterministic: two runs write byte-identical output.

```sh
node main.ts        # renders entry.png (1024x1024, 214,288 bytes)
```

## The 42 stories

Regions: Europe 8 · Middle East 6 · Americas 6 · Asia-Pacific 10 ·
Africa 7 · Oceania 2 · World 3 = 42.

### Leads

1. **Europe · War — Russia fires 186 drones at Ukraine overnight.**
   Air defences downed or jammed 161 of 186 strike drones (72 of them
   jet-powered) fired from eight directions. One destroyed a five-storey
   block in Dymer: up to seven feared trapped, two injured, nine evacuated.
   (Ukrainian Air Force, Kyiv Independent)
2. **World · Climate — COP31 ends with no deal on fossil fuels.** The final
   text "recalls" the Dubai pact whole, keeps the 35% clean-electricity-by-2035
   goal, drops the $120bn adaptation target and is the first to admit 1.5 °C
   will be overshot. Hoekstra: "a good deal or no deal". (Reuters, BBC)
3. **Middle East · Gulf — Iran claims two US radars hit; Bahrain denies it.**
   Tehran says it destroyed two US Patriot radars on Saturday night.
   Bahrain's foreign ministry answered on Sunday: the target was a civilian
   industrial site — a fire, no injuries — and a violation of its sovereignty.
   (Al Jazeera, Reuters)

### The day in twelve (4–15)

4. **Asia-Pacific · Election — Hong Kong elects its Election Committee.**
   856 candidates; 723 seats, 5,700 voters; polls 09:00–18:00. (SCMP)
5. **Americas · Formula 1 — Verstappen takes the Las Vegas GP.** Beats Norris
   and Piastri; Russell hits the wall late, finishes 5th. (Reuters, F1)
6. **Asia-Pacific · Cricket — India declare on 720/9 — a record in NZ.**
   Rahul 136, Pant 128, Gill 98; hosts 11/2, trailing by 235. (ESPN)
7. **Europe · Diplomacy — US envoys head to Moscow after Abu Dhabi talks.**
   Kushner and Witkoff to brief Putin, then on to Dublin to meet Zelenskyy.
   (ANSA)
8. **Americas · NBA — Wembanyama scores 50 as Spurs roll.** 50 pts,
   19 rebounds, 5 blocks; 114–91 over New Orleans. (Reuters)
9. **Americas · Health — Bolsonaro in intensive care.** Bowel obstruction,
   stable, breathing on his own. (Al Jazeera, Reuters)
10. **Americas · Cyber — FBI probes apparent hack of its crime database.**
    Washington State pauses gun-dealer checks; breach assessed. (AP)
11. **Europe · Travel — Belgian controllers join Monday's national strike.**
    Most flights grounded 07:00–21:00; controllers join rail and port staff.
    (VRT)
12. **Asia-Pacific · Poisoning — Toxic-liquor toll climbs to 19.** 600 in
    hospital, six held. (Xinhua)
13. **Europe · Sea — Russian cargo ship Sparta II still burning.** Hit by
    drones Saturday; Finland leads Lovisa rescue. (Reuters)
14. **Middle East · Energy — Iran begins rationing electricity.** Rolling cuts
    up to two hours a day as war damage bites. (RFE/RL)
15. **Americas · Quake — Peru quake toll updated: 1 dead, 16 hurt.** 170 homes
    damaged in Junín; the count is completed. (Reuters)

### Also on Sunday 22 November (16–42)

16. Europe — Estonia to shut 5 Russia border crossings 1 Dec (Reuters)
17. Europe — Denmark expels Russian attaché in spy row (Guardian)
18. Asia-Pacific — Nepal PM Shah lands in Delhi on first visit (IANS)
19. Asia-Pacific — Chinese bomber turns back 170 km from Manila (AP)
20. Asia-Pacific — Philippines M5.9 quake, 898 km deep off Palawan (EMSC)
21. Asia-Pacific — Japan poll: record 52% warm to South Korea (Yonhap)
22. Asia-Pacific — Taiwan holds drill "resisting invasion" (TMA)
23. Africa — Somalia expels UAE ambassador, recalls envoy (Wires)
24. Africa — Sudan: RSF accused of killing civilians (Wires)
25. Africa — Kenya discharges its last Ebola patient (Wires)
26. Africa — DR Congo: Cantine attack, 40 killed (Local officials)
27. Europe — Russia opens regulated crypto trading (Bank of Russia)
28. World — Gold near $5,355; Bitcoin back above $60,000 (Markets)
29. Americas — Nvidia faces SEC accounting probe (Reports)
30. Middle East — Trump seeks "permanent" Iran deal; Doha talks (Al Jazeera)
31. Middle East — Hamas seeks US mediator role in Iran deal (Al Jazeera)
32. Africa — Sudan army retakes 30 towns in Kordofan (UPI)
33. World — EU and Indonesia sign trade deal after ten years (DW)
34. Asia-Pacific — World court: Myanmar guilty of genocide (Guardian)
35. Oceania — Melbourne: 70 years since the 1956 Olympics (ABC)
36. Oceania — Cummins keeps Australia's Test captaincy (Wires)
37. Middle East — Saudi downs Houthi missile aimed at Riyadh (Anadolu)
38. Asia-Pacific — Candy-factory fire in Cikande: 3 dead, 36 missing as search
    goes on (Reuters, AFP, Detiknews)
39. Middle East — Israeli fire kills four in Gaza (Al Jazeera, Gaza civil
    defence)
40. Africa — Drones strike homes near Khartoum (AFP)
41. Africa — Mourners' boat capsizes in southern Nigeria, 24 dead
    (AP, Reuters)
42. Europe — Pope Leo XIV hosts 1,300 poor guests at Vatican (Vatican News)

## Charts and data

- **Drones over Ukraine:** fired 186 · downed or jammed 161.
- **COP31 in numbers:** nations backing fossil-fuel language 130+ ·
  signed electrification pledge 90+.
- **Data strip:** 186 drones fired · 161 downed or jammed · 35% clean-power
  goal for 2035, kept · $120bn adaptation target dropped · 720/9 India's
  record Test total · 50 Wembanyama points.
- **The day in UTC:** 01:00 HK polls open · 03:00 COP31 objections close ·
  05:11 Hamas seeks talks · 05:30 Verstappen wins · 06:00 COP31 approval due ·
  07:30 Approval slips.

## DATE CHECK — left out as other days' news

The 400-drone night (Thu) · the 148-drone night (Fri) · 110-missile barrage
(Thu–Fri) · "El Chapo Isidro" captured (Fri) · Gaza aid-van strike (Sat) ·
BepiColombo Mercury burn (Sat) · Peru quake itself Fri 20 Nov ·
Bitcoin $55,830 two-year low (Sat).

## QC numbers

- Size: 1024×1024 PNG, 214,288 bytes (limit 1 MiB).
- Determinism: `node main.ts` twice → byte-identical `entry.png`,
  sha256 `b8a21aadde52df5bef25085d0638f3bee1c47c41ecdc4dfa0cc295cd38a43510`.
- Density counter (RapidOCR + PIL): 186 OCR lines, 770 words; 35/42 story
  numbers and 39/42 story keywords read back by OCR (the rest are 9.5 px
  list type the OCR misreads — all 42 stories are placed and verified by the
  layout validator); 6/7 region names as contiguous OCR strings (the 7th,
  WORLD, is present in the region strip); map present (7,625 sampled sky
  pixels); 2 chart bars present; data strip present.
- Layout validator (PIL bounding boxes, built into the draw script): 248 text
  boxes, zero overflow, zero overlap, zero margin violations — the script
  exits non-zero rather than shipping a broken layout.
- Zoom-QC by eye at full size and at 300 px wide: masthead, data strip,
  leads, mid banners, map pins and list all stay legible; the dot-matrix map
  was re-drawn after the first zoom check put pins 9, 23 and 38 in the sea
  (South America, Africa and Indonesia were too narrow).

## Why v4

v3 (rank 2005, dev 0.9778) lost on craft, not count — density was already
fine. v4 keeps v3's skeleton (masthead, data strip, region strip, UTC
timeline, 2 bar charts, DATE CHECK, sources + certainty legend) and closes
the exact gaps seen side-by-side against the rank-1 artifact (dev 0.992370):

1. Every mid card now has a full-width illustration banner (~34 px) with a
   label chip ("856 CANDIDATES", "720/9 DECLARED", …) — v3 had only a tiny
   icon.
2. Lead pictograms are taller and more detailed (~96 px scenes: Kyiv skyline
   + drones + searchlight; COP31 table + globe; Bahrain radar + missile +
   denial arrow).
3. The flat beige map is replaced by a dot-matrix world map with large red
   numbered pins.
4. A region tag on every list item ("16 Europe: …").
5. A dark navy footer band: "THE WORLD IN ONE DAY" / "SUNDAY 22 NOVEMBER
   2026 · ONE PAGE".
6. Certainty chips on leads and mid cards (REPORTED / CLAIM / ONGOING).
7. Five stories v3 missed, each corroborated by the rank-1 and/or rank-2
   artifacts: the Cikande candy-factory fire (3 dead, 36 missing — toll
   confirmed Sunday 22 Nov by Reuters), Israeli fire killing four in Gaza,
   drones striking homes near Khartoum, the mourners' boat capsizing in
   southern Nigeria (24 dead), and Pope Leo XIV hosting 1,300 poor guests at
   the Vatican. Count rises 37 → 42.

## License

MIT — see [LICENSE](LICENSE).
