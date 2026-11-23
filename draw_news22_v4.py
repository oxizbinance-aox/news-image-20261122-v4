#!/usr/bin/env python3
"""Draw entry.png for news-image-20261122 v4 — 'Sunday 22 November 2026'.

A light broadsheet: 3 leads with tall pictograms, 12 mid cards with
full-width illustration banners, a dot-matrix world map with numbered pins,
a 27-item numbered list, two bar charts, a six-number data strip, a UTC
timeline, a DATE CHECK box and a dark navy footer. 1024x1024, deterministic.

Everything is drawn from scratch with PIL; no external assets, no network.
All text is wrapped to fit its box — any overflow raises, so the script
fails loudly instead of shipping a broken layout.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# ---------------------------------------------------------------- palette
PAPER = (250, 246, 238)
INK = (26, 26, 26)
NAVY = (13, 27, 62)
NAVY2 = (18, 38, 84)
RED = (178, 34, 34)
RED_DK = (139, 0, 0)
GOLD = (201, 162, 39)
TEAL = (0, 128, 128)
GREEN = (34, 139, 34)
GREY = (110, 110, 105)
LINE = (200, 192, 178)
CARD = (255, 255, 255)
SKY = (214, 231, 240)
CHIP_TXT = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    path = os.path.join(FONT_DIR, name)
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF_I = lambda s: font("DejaVuSerif-Italic.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_O = lambda s: font("DejaVuSans-Oblique.ttf", s)

# ---------------------------------------------------------------- data
LEADS = [
    {
        "n": 1, "place": "KYIV REGION, UKRAINE", "beat": "WAR",
        "chip": "REPORTED", "chip_bg": TEAL,
        "head": "Russia fires 186 drones at Ukraine overnight",
        "body": ("Air defences downed or jammed 161 of 186 strike drones "
                 "fired from eight directions. One destroyed "
                 "a five-storey block in Dymer: up to seven feared trapped, "
                 "two injured, nine evacuated. (Ukrainian Air Force)"),
        "scene": "kyiv",
    },
    {
        "n": 2, "place": "ANTALYA, TÜRKIYE", "beat": "CLIMATE",
        "chip": "ONGOING", "chip_bg": NAVY2,
        "head": "COP31 ends with no deal on fossil fuels",
        "body": ("The final text \u2018recalls\u2019 the Dubai pact whole, keeps the 35% "
                 "clean-electricity goal for 2035, drops the $120bn adaptation "
                 "target and admits 1.5\u00b0C will be overshot. (Reuters, BBC)"),
        "scene": "cop31",
    },
    {
        "n": 3, "place": "MANAMA, BAHRAIN", "beat": "GULF",
        "chip": "CLAIM", "chip_bg": RED,
        "head": "Iran claims two US radars hit; Bahrain denies it",
        "body": ("Tehran says it destroyed two US Patriot radars on Saturday "
                 "night. Bahrain answered Sunday: the target was a civilian "
                 "site \u2014 a fire, no injuries \u2014 a violation of its "
                 "sovereignty. (Al Jazeera, Reuters)"),
        "scene": "bahrain",
    },
]

MIDS = [
    {"n": 4, "place": "HONG KONG", "beat": "ELECTION", "chip": "REPORTED",
     "banner": "856 CANDIDATES", "bg": (196, 52, 52),
     "head": "Hong Kong elects its Election Committee",
     "body": "856 candidates, 723 seats; polls 09:00\u201318:00. (SCMP)",
     "scene": "ballot"},
    {"n": 5, "place": "LAS VEGAS", "beat": "FORMULA 1", "chip": "REPORTED",
     "banner": "POLE TO FLAG", "bg": (24, 24, 40),
     "head": "Verstappen takes the Las Vegas GP",
     "body": "Beats Norris and Piastri; Russell 5th. (Reuters, F1)",
     "scene": "f1"},
    {"n": 6, "place": "WELLINGTON", "beat": "CRICKET", "chip": "REPORTED",
     "banner": "720/9 DECLARED", "bg": (46, 125, 50),
     "head": "India declare 720/9 \u2014 a record in NZ",
     "body": "Rahul 136, Pant 128, Gill 98; hosts 11/2. (ESPN)",
     "scene": "cricket"},
    {"n": 7, "place": "MOSCOW", "beat": "DIPLOMACY", "chip": "REPORTED",
     "banner": "ABU DHABI \u2192 MOSCOW", "bg": (90, 60, 140),
     "head": "US envoys to Moscow after Abu Dhabi talks",
     "body": "Kushner and Witkoff brief Putin, then Dublin. (ANSA)",
     "scene": "plane"},
    {"n": 8, "place": "SAN ANTONIO", "beat": "NBA", "chip": "REPORTED",
     "banner": "50 POINTS", "bg": (196, 94, 22),
     "head": "Wembanyama scores 50 as Spurs roll",
     "body": "50 pts, 19 rebounds, 5 blocks; 114\u201391. (Reuters)",
     "scene": "nba"},
    {"n": 9, "place": "BRAS\u00cdLIA", "beat": "HEALTH", "chip": "REPORTED",
     "banner": "IN INTENSIVE CARE", "bg": (0, 120, 140),
     "head": "Bolsonaro in intensive care",
     "body": "Bowel obstruction; stable, breathing on his own. (Reuters)",
     "scene": "health"},
    {"n": 10, "place": "WASHINGTON", "beat": "CYBER", "chip": "REPORTED",
     "banner": "FBI PROBE", "bg": (40, 60, 90),
     "head": "FBI probes hack of its crime database",
     "body": "State pauses gun-dealer checks; breach assessed. (AP)",
     "scene": "cyber"},
    {"n": 11, "place": "BRUSSELS", "beat": "TRAVEL", "chip": "REPORTED",
     "banner": "FLIGHTS GROUNDED", "bg": (120, 40, 90),
     "head": "Belgian controllers join Monday strike",
     "body": "Most flights grounded 07:00\u201321:00. (VRT)",
     "scene": "strike"},
    {"n": 12, "place": "MANIPUR, INDIA", "beat": "POISONING", "chip": "REPORTED",
     "banner": "TOLL AT 19", "bg": (140, 110, 20),
     "head": "Toxic-liquor toll climbs to 19",
     "body": "600 in hospital, six held. (Xinhua)",
     "scene": "bottle"},
    {"n": 13, "place": "GULF OF FINLAND", "beat": "SEA", "chip": "REPORTED",
     "banner": "SHIP ABLAZE", "bg": (60, 60, 60),
     "head": "Russian cargo ship Sparta II still burning",
     "body": "Hit by drones Saturday; Finland leads rescue. (Reuters)",
     "scene": "ship"},
    {"n": 14, "place": "TEHRAN, IRAN", "beat": "ENERGY", "chip": "REPORTED",
     "banner": "POWER CUTS", "bg": (180, 130, 20),
     "head": "Iran begins rationing electricity",
     "body": "Rolling cuts up to two hours a day. (RFE/RL)",
     "scene": "power"},
    {"n": 15, "place": "JUN\u00cdN, PERU", "beat": "QUAKE", "chip": "REPORTED",
     "banner": "1 DEAD, 16 HURT", "bg": (120, 70, 30),
     "head": "Peru quake toll: 1 dead, 16 hurt",
     "body": "170 homes damaged in Jun\u00edn; count completed. (Reuters)",
     "scene": "quake"},
]

# (number, region, text) — every line trimmed to fit one line at 9.5px.
LIST = [
    (16, "Europe", "Estonia to shut 5 Russia crossings 1 Dec (Reuters)"),
    (17, "Europe", "Denmark expels Russian attach\u00e9 in spy row (Guardian)"),
    (18, "Asia-Pacific", "Nepal PM Shah lands in Delhi (IANS)"),
    (19, "Asia-Pacific", "Chinese bomber turns back off Manila (AP)"),
    (20, "Asia-Pacific", "M5.9 quake 898 km deep off Palawan (EMSC)"),
    (21, "Asia-Pacific", "Japan poll: record 52% warm to South Korea (Yonhap)"),
    (22, "Asia-Pacific", "Taiwan holds drill \u2018resisting invasion\u2019 (TMA)"),
    (23, "Africa", "Somalia expels UAE ambassador, recalls envoy (Wires)"),
    (24, "Africa", "Sudan: RSF accused of killing civilians (Wires)"),
    (25, "Africa", "Kenya discharges its last Ebola patient (Wires)"),
    (26, "Africa", "DR Congo: Cantine attack, 40 killed (Local officials)"),
    (27, "Europe", "Russia opens crypto trading (Bank of Russia)"),
    (28, "World", "Gold near $5,355; Bitcoin above $60,000 (Markets)"),
    (29, "Americas", "Nvidia faces SEC accounting probe (Reports)"),
    (30, "Middle East", "Trump seeks \u2018permanent\u2019 Iran deal (Al Jazeera)"),
    (31, "Middle East", "Hamas seeks US role as Iran mediator (Al Jazeera)"),
    (32, "Africa", "Sudan army retakes 30 towns in Kordofan (UPI)"),
    (33, "World", "EU\u2013Indonesia sign trade deal after ten years (DW)"),
    (34, "Asia-Pacific", "World court: Myanmar guilty of genocide (Guardian)"),
    (35, "Oceania", "Melbourne: 70 years since the 1956 Olympics (ABC)"),
    (36, "Oceania", "Cummins keeps Australia\u2019s Test captaincy (Wires)"),
    (37, "Middle East", "Saudi downs Houthi missile over Riyadh (Anadolu)"),
    (38, "Asia-Pacific", "Cikande factory fire: 3 dead, 36 missing (Reuters)"),
    (39, "Middle East", "Israeli fire kills four in Gaza (Al Jazeera)"),
    (40, "Africa", "Drones strike homes near Khartoum (AFP)"),
    (41, "Africa", "Mourners\u2019 boat capsizes in Nigeria, 24 dead (AP)"),
    (42, "Europe", "Pope hosts 1,300 poor guests at Vatican (Vatican News)"),
]

REGIONS = [("EUROPE", 8, (178, 34, 34)), ("MIDDLE EAST", 6, (140, 40, 90)),
           ("AMERICAS", 6, (24, 90, 160)), ("ASIA-PACIFIC", 10, (196, 120, 20)),
           ("AFRICA", 7, (34, 139, 34)), ("OCEANIA", 2, (0, 120, 140)),
           ("WORLD", 3, (90, 90, 90))]

DATA_STRIP = [
    ("186", "drones fired overnight"),
    ("161", "downed or jammed"),
    ("35%", "clean-power goal for 2035, kept"),
    ("$120bn", "adaptation target dropped"),
    ("720/9", "India\u2019s record Test total"),
    ("50", "Wembanyama points"),
]

UTC_ITEMS = [
    ("01:00", "HK polls open"), ("03:00", "COP31 objections close"),
    ("05:11", "Hamas seeks talks"), ("05:30", "Verstappen wins"),
    ("06:00", "COP31 approval due"), ("07:30", "Approval slips"),
]

DATE_CHECK = ("Left out as other days\u2019 news: the 400-drone night (Thu) \u00b7 "
              "the 148-drone night (Fri) \u00b7 110-missile barrage (Thu\u2013Fri) \u00b7 "
              "\u2018El Chapo Isidro\u2019 captured (Fri) \u00b7 Gaza aid-van strike (Sat) \u00b7 "
              "BepiColombo Mercury burn (Sat) \u00b7 Peru quake itself Fri 20 Nov \u00b7 "
              "Bitcoin $55,830 two-year low (Sat)")

SOURCES = ("Sources: Reuters, BBC, Al Jazeera, The Guardian, AP, SCMP, ESPN, Xinhua, "
           "RFE/RL, UPI, DW, AFP, Detiknews, Anadolu, Vatican News, EMSC, Yonhap, "
           "IANS, ABC, TMA, VRT, ANSA, F1, Wires. Pictures and map: original, drawn in code.")

LEGEND = ("CERTAINTY: REPORTED = carried by the day\u2019s wires \u00b7 CLAIM = one side\u2019s "
          "account, labelled as such \u00b7 ONGOING = still to happen when drawn")

# Dot-matrix world map: 64 cols x 32 rows. Col 0 = -180 lon, row 0 = ~84N.
# Land is listed as (row, first_col, last_col) runs, built from a coarse
# equirectangular outline; the renderer turns each land cell into a dot.
LAND_RUNS = [
    (1, 8, 14), (1, 21, 22),
    (2, 5, 16), (2, 20, 23),
    (3, 3, 18), (3, 20, 23), (3, 33, 36), (3, 38, 58),
    (4, 4, 18), (4, 21, 22), (4, 32, 36), (4, 38, 59),
    (5, 5, 18), (5, 29, 30), (5, 31, 36), (5, 38, 59),
    (6, 6, 17), (6, 29, 30), (6, 31, 35), (6, 40, 50), (6, 56, 57),
    (7, 7, 16), (7, 30, 35), (7, 40, 48), (7, 47, 54), (7, 56, 57),
    (8, 8, 15), (8, 29, 31), (8, 37, 41), (8, 44, 46), (8, 47, 54), (8, 56, 57),
    (9, 8, 13), (9, 30, 32), (9, 37, 40), (9, 44, 48), (9, 47, 53),
    (10, 9, 13), (10, 30, 37), (10, 38, 40), (10, 44, 48), (10, 49, 53),
    (11, 10, 13), (11, 30, 38), (11, 44, 49), (11, 50, 53),
    (12, 12, 14), (12, 13, 17), (12, 30, 41), (12, 44, 46), (12, 48, 53),
    (13, 13, 17), (13, 31, 41), (13, 49, 56),
    (14, 13, 21), (14, 31, 40), (14, 49, 56),
    (15, 14, 23), (15, 32, 40), (15, 50, 55),
    (16, 14, 24), (16, 32, 39), (16, 51, 55),
    (17, 15, 23), (17, 32, 38), (17, 51, 53),
    (18, 15, 23), (18, 33, 37),
    (19, 16, 22), (19, 33, 36),
    (20, 16, 20), (20, 33, 35), (20, 52, 59),
    (21, 16, 19), (21, 33, 35), (21, 52, 59),
    (22, 17, 18), (22, 53, 58), (22, 63, 63),
    (23, 17, 18), (23, 62, 63),
    (24, 17, 17), (24, 62, 62),
]


def build_world_map():
    grid = [[" "] * 64 for _ in range(32)]
    for r, c0, c1 in LAND_RUNS:
        for c in range(c0, c1 + 1):
            grid[r][c] = "#"
    return ["".join(row) for row in grid]


WORLD_MAP = build_world_map()

# (story number, lon, lat) for map pins. Display coords for 1 and 2 are
# nudged ~2 deg so their pins do not touch at this scale.
PINS = [
    (1, 28.0, 52.0), (2, 33.0, 35.0), (3, 50.6, 26.2), (4, 114.2, 22.3),
    (5, -115.1, 36.2), (6, 174.8, -41.3), (8, -98.5, 29.4),
    (9, -47.9, -15.8), (10, -77.0, 38.9), (11, 4.4, 50.8), (12, 93.9, 24.8),
    (15, -75.2, -11.0), (18, 77.2, 28.6), (23, 45.3, 2.0), (24, 30.2, 15.5),
    (26, 25.2, -1.7), (35, 145.0, -37.8), (38, 106.2, -6.1), (41, 6.5, 5.5),
]

# ---------------------------------------------------------------- helpers
TEXT_BOXES = []  # (x0, y0, x1, y1, label) — every text bbox, for validation.


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split(" ")
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def draw_text(draw, xy, text, fnt, fill, anchor="la", tag=""):
    x, y = xy
    draw.text((x, y), text, font=fnt, fill=fill, anchor=anchor)
    bb = draw.textbbox((x, y), text, font=fnt, anchor=anchor)
    TEXT_BOXES.append((bb[0], bb[1], bb[2], bb[3], tag or text[:24]))
    return bb


def text_h(draw, text, fnt):
    bb = draw.textbbox((0, 0), text, font=fnt)
    return bb[3] - bb[1]


def chip(draw, x, y, text, fnt, bg, fg=CHIP_TXT, pad_x=5, pad_y=2):
    """Small filled label chip; returns (w, h)."""
    tw = draw.textlength(text, font=fnt)
    w_, h_ = int(tw) + 2 * pad_x, text_h(draw, text, fnt) + 2 * pad_y + 2
    draw.rounded_rectangle([x, y, x + w_, y + h_], radius=2, fill=bg)
    draw.text((x + pad_x, y + pad_y), text, font=fnt, fill=fg)
    TEXT_BOXES.append((x, y, x + w_, y + h_, "chip:" + text))
    return w_, h_


def num_circle(draw, cx, cy, n, r=9):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED, outline=(255, 255, 255), width=1)
    fnt = SANS_B(8 if r <= 6 else 10)
    draw.text((cx, cy), str(n), font=fnt, fill=(255, 255, 255), anchor="mm")
    TEXT_BOXES.append((cx - r, cy - r, cx + r, cy + r, "pin:%d" % n))

# ---------------------------------------------------------------- scenes
def _stars(draw, x0, y0, w, h, pts):
    for px, py, r in pts:
        draw.ellipse([x0 + px - r, y0 + py - r, x0 + px + r, y0 + py + r],
                     fill=(255, 255, 220))


def scene_kyiv(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(10, 16, 46))
    _stars(draw, x, y, w, h, [(20, 12, 1), (60, 8, 1), (110, 18, 2),
                              (170, 10, 1), (230, 16, 1), (290, 8, 2),
                              (250, 30, 1), (90, 28, 1), (150, 6, 1)])
    # moon
    draw.ellipse([x + w - 52, y + 8, x + w - 28, y + 32], fill=(240, 230, 180))
    # skyline: dark blocks with lit windows
    base = y + h
    for bx, bw, bh in [(0, 46, 52), (48, 38, 66), (88, 52, 44), (142, 40, 60),
                       (184, 46, 48), (232, 42, 70), (276, 49, 54)]:
        draw.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(16, 22, 52))
        for wx in range(bx + 6, bx + bw - 6, 12):
            for wy in range(base - bh + 8, base - 8, 14):
                if (wx * 7 + wy * 3) % 5 < 2:
                    draw.rectangle([x + wx, wy, x + wx + 5, wy + 7],
                                   fill=(255, 204, 80))
    # searchlight beam from lower right
    draw.polygon([(x + w - 30, base), (x + w - 90, y + 6),
                  (x + w - 60, y + 6), (x + w - 8, base)], fill=(255, 240, 170))
    # drones: small crosses with orange trails
    for dx, dy in [(70, 22), (150, 14), (210, 26)]:
        draw.line([x + dx - 18, y + dy + 4, x + dx, y + dy], fill=(255, 150, 60), width=2)
        draw.line([x + dx - 5, y + dy - 5, x + dx + 5, y + dy + 5], fill=(255, 255, 255), width=2)
        draw.line([x + dx - 5, y + dy + 5, x + dx + 5, y + dy - 5], fill=(255, 255, 255), width=2)


def scene_cop31(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(14, 64, 64))
    # globe, left
    cx, cy, r = x + 52, y + 44, 34
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(38, 140, 120))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(180, 230, 210), width=2)
    draw.arc([cx - 22, cy - 26, cx + 22, cy + 26], 200, 340, fill=(180, 230, 210), width=2)
    draw.arc([cx - 26, cy - 10, cx + 26, cy + 10], 90, 270, fill=(180, 230, 210), width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=(180, 230, 210), width=2)
    # sun
    draw.ellipse([x + w - 46, y + 10, x + w - 22, y + 34], fill=(255, 205, 90))
    # conference table with delegates
    ty = y + h - 26
    draw.rectangle([x + 110, ty, x + w - 8, ty + 12], fill=(120, 72, 32))
    draw.rectangle([x + 110, ty + 12, x + w - 8, ty + 16], fill=(90, 52, 22))
    for i, dx in enumerate(range(122, w - 20, 26)):
        draw.ellipse([x + dx, ty - 16, x + dx + 12, ty - 4], fill=(232, 190, 150))
        draw.rectangle([x + dx - 2, ty - 4, x + dx + 14, ty + 2],
                       fill=[(180, 40, 40), (40, 90, 180), (40, 140, 60),
                             (220, 160, 40)][i % 4])
    # document on the table
    draw.rectangle([x + w - 96, ty - 6, x + w - 52, ty + 2], fill=(255, 255, 255))


def scene_bahrain(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(24, 18, 54))
    _stars(draw, x, y, w, h, [(30, 10, 1), (90, 16, 1), (160, 8, 2), (220, 14, 1)])
    # ground
    draw.rectangle([x, y + h - 22, x + w, y + h], fill=(52, 44, 66))
    # radar dishes
    for dx in (36, 130):
        draw.polygon([(x + dx, y + h - 22), (x + dx + 8, y + h - 44),
                      (x + dx + 26, y + h - 44), (x + dx + 34, y + h - 22)],
                     fill=(120, 120, 140))
        draw.arc([x + dx - 2, y + h - 62, x + dx + 36, y + h - 28], 180, 360,
                 fill=(200, 200, 220), width=3)
    # missile arc with flame, right side
    draw.arc([x + 190, y - 6, x + 300, y + 70], 200, 320, fill=(255, 255, 255), width=3)
    draw.ellipse([x + 252, y + 8, x + 264, y + 20], fill=(255, 150, 40))
    draw.ellipse([x + 256, y + 12, x + 262, y + 18], fill=(255, 220, 120))
    # denial arrow: white curved arrow looping back
    draw.arc([x + 200, y + 34, x + 280, y + 88], 300, 90, fill=(255, 255, 255), width=3)
    draw.polygon([(x + 204, y + 52), (x + 196, y + 62), (x + 210, y + 64)],
                 fill=(255, 255, 255))
    # small fire at a dish
    draw.polygon([(x + 44, y + h - 44), (x + 52, y + h - 60), (x + 60, y + h - 44)],
                 fill=(255, 140, 40))


def _darken(c):
    return tuple(max(0, v * 2 // 3) for v in c)


def banner_chip(draw, x, y, text, bg):
    fnt = SANS_B(8)
    tw = draw.textlength(text, font=fnt)
    bw, bh = int(tw) + 10, 13
    draw.rectangle([x, y, x + bw, y + bh], fill=_darken(bg))
    draw.text((x + 5, y + 2), text, font=fnt, fill=(255, 255, 255))
    TEXT_BOXES.append((x, y, x + bw, y + bh, "banner:" + text))


def scene_ballot(draw, x, y, w, h):
    draw.rectangle([x + 96, y + 12, x + 140, y + 30], fill=(255, 255, 255))
    draw.rectangle([x + 100, y + 6, x + 136, y + 12], fill=(220, 220, 220))
    draw.line([x + 104, y + 16, x + 114, y + 26], fill=RED, width=3)
    draw.line([x + 114, y + 26, x + 134, y + 8], fill=RED, width=3)
    draw.rectangle([x + 20, y + 22, x + 60, y + 28], fill=(255, 255, 255))


def scene_f1(draw, x, y, w, h):
    for i in range(8):
        for j in range(2):
            if (i + j) % 2 == 0:
                draw.rectangle([x + 96 + i * 7, y + 6 + j * 7,
                                x + 103 + i * 7, y + 13 + j * 7], fill=(255, 255, 255))
    draw.rectangle([x + 16, y + 20, x + 76, y + 27], fill=(255, 60, 60))
    draw.rectangle([x + 56, y + 14, x + 76, y + 20], fill=(200, 200, 220))
    draw.line([x + 8, y + 24, x + 14, y + 24], fill=(255, 255, 255), width=2)


def scene_cricket(draw, x, y, w, h):
    draw.rectangle([x, y + 24, x + w, y + h], fill=(30, 100, 40))
    draw.line([x + 100, y + 6, x + 128, y + 30], fill=(230, 200, 140), width=5)
    draw.ellipse([x + 138, y + 18, x + 148, y + 28], fill=(200, 40, 40))
    draw.rectangle([x + 20, y + 10, x + 60, y + 16], fill=(255, 255, 255))


def scene_plane(draw, x, y, w, h):
    draw.polygon([(x + 96, y + 16), (x + 140, y + 16), (x + 152, y + 20),
                  (x + 140, y + 23), (x + 96, y + 23)], fill=(255, 255, 255))
    draw.polygon([(x + 118, y + 16), (x + 126, y + 8), (x + 132, y + 16)],
                 fill=(255, 255, 255))
    draw.ellipse([x + 20, y + 14, x + 34, y + 28], fill=(255, 200, 60))
    draw.rectangle([x + 20, y + 28, x + 34, y + 32], fill=(200, 60, 60))


def scene_nba(draw, x, y, w, h):
    draw.ellipse([x + 104, y + 4, x + 132, y + 32], fill=(230, 110, 30))
    draw.arc([x + 104, y + 4, x + 132, y + 32], 90, 270, fill=(120, 50, 10), width=2)
    draw.line([x + 104, y + 18, x + 132, y + 18], fill=(120, 50, 10), width=2)
    draw.rectangle([x + 24, y + 8, x + 52, y + 12], fill=(255, 255, 255))
    draw.line([x + 28, y + 12, x + 28, y + 22], fill=(255, 255, 255), width=2)
    draw.line([x + 48, y + 12, x + 48, y + 22], fill=(255, 255, 255), width=2)


def scene_health(draw, x, y, w, h):
    draw.rectangle([x + 104, y + 8, x + 116, y + 28], fill=(255, 255, 255))
    draw.rectangle([x + 98, y + 14, x + 122, y + 22], fill=(255, 255, 255))
    pts = [(20, 22), (36, 22), (44, 10), (52, 28), (60, 16), (68, 22), (84, 22)]
    draw.line([(x + px, y + py) for px, py in pts], fill=(255, 255, 255), width=2)


def scene_cyber(draw, x, y, w, h):
    draw.ellipse([x + 100, y + 6, x + 126, y + 32], outline=(255, 255, 255), width=3)
    draw.line([x + 122, y + 28, x + 134, y + 34], fill=(255, 255, 255), width=3)
    draw.text((x + 104, y + 12), "01", font=SANS_B(10), fill=(255, 255, 255))
    for px, py in [(24, 12), (40, 12), (56, 12), (24, 24), (40, 24), (56, 24)]:
        draw.ellipse([x + px, y + py, x + px + 5, y + py + 5], fill=(140, 200, 255))


def scene_strike(draw, x, y, w, h):
    draw.polygon([(x + 96, y + 16), (x + 136, y + 16), (x + 146, y + 20),
                  (x + 136, y + 23), (x + 96, y + 23)], fill=(255, 255, 255))
    draw.ellipse([x + 22, y + 6, x + 48, y + 32], outline=(255, 60, 60), width=3)
    draw.line([x + 26, y + 28, x + 44, y + 10], fill=(255, 60, 60), width=3)


def scene_bottle(draw, x, y, w, h):
    draw.rectangle([x + 108, y + 6, x + 118, y + 12], fill=(255, 255, 255))
    draw.rectangle([x + 100, y + 12, x + 126, y + 32], fill=(230, 230, 230))
    draw.polygon([(x + 30, y + 28), (x + 42, y + 8), (x + 54, y + 28)],
                 outline=(255, 220, 60), width=2)
    draw.text((x + 38, y + 16), "!", font=SANS_B(11), fill=(255, 220, 60))


def scene_ship(draw, x, y, w, h):
    draw.polygon([(x + 96, y + 24), (x + 150, y + 24), (x + 142, y + 32),
                  (x + 104, y + 32)], fill=(200, 200, 210))
    draw.rectangle([x + 110, y + 14, x + 130, y + 24], fill=(160, 160, 170))
    for fx in (108, 120, 132):
        draw.polygon([(x + fx, y + 14), (x + fx + 4, y + 4),
                      (x + fx + 8, y + 14)], fill=(255, 140, 40))
    draw.rectangle([x + 16, y + 26, x + 80, y + 30], fill=(120, 180, 220))


def scene_power(draw, x, y, w, h):
    draw.polygon([(x + 112, y + 4), (x + 102, y + 20), (x + 110, y + 20),
                  (x + 104, y + 32), (x + 120, y + 14), (x + 112, y + 14)],
                 fill=(255, 220, 60))
    draw.line([x + 24, y + 6, x + 24, y + 32], fill=(255, 255, 255), width=2)
    draw.line([x + 24, y + 10, x + 14, y + 18], fill=(255, 255, 255), width=2)
    draw.line([x + 24, y + 10, x + 34, y + 18], fill=(255, 255, 255), width=2)


def scene_quake(draw, x, y, w, h):
    pts = [(96, 20), (108, 12), (118, 24), (130, 10), (142, 22), (152, 14)]
    draw.line([(x + px, y + py) for px, py in pts], fill=(255, 220, 60), width=2)
    draw.line([(x + 16, y + 28), (x + 34, y + 22), (x + 44, y + 28),
               (x + 62, y + 20), (x + 80, y + 28)], fill=(255, 255, 255), width=2)
    draw.rectangle([x + 30, y + 12, x + 44, y + 22], fill=(200, 200, 200))


LEAD_SCENES = {"kyiv": scene_kyiv, "cop31": scene_cop31, "bahrain": scene_bahrain}
MID_SCENES = {"ballot": scene_ballot, "f1": scene_f1, "cricket": scene_cricket,
              "plane": scene_plane, "nba": scene_nba, "health": scene_health,
              "cyber": scene_cyber, "strike": scene_strike, "bottle": scene_bottle,
              "ship": scene_ship, "power": scene_power, "quake": scene_quake}

# ---------------------------------------------------------------- layout
MARGIN = 16
CW = W - 2 * MARGIN  # 992


def hbar(draw, x, y, label, value, frac, color, max_w=190, label_w=168):
    """One horizontal bar row: label, bar, value."""
    f_lab, f_val = SANS(10), SANS_B(11)
    draw_text(draw, (x, y), label, f_lab, INK, tag="bar:" + label)
    bx = x + label_w
    draw.rectangle([bx, y + 1, bx + max_w, y + 12], fill=(232, 228, 220))
    draw.rectangle([bx, y + 1, bx + int(max_w * frac), y + 12], fill=color)
    draw_text(draw, (bx + max_w + 6, y), value, f_val, INK, tag="barval:" + value)


def render():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    del TEXT_BOXES[:]

    # ---- top navy band
    draw.rectangle([0, 0, W, 24], fill=NAVY)
    draw_text(draw, (MARGIN, 5), "THE WORLD IN ONE DAY", SANS_B(11), (255, 255, 255),
              tag="topband")
    r_txt = "42 STORIES \u00b7 7 REGIONS \u00b7 EVERY ONE DATED SUNDAY 22 NOVEMBER 2026"
    draw_text(draw, (W - MARGIN, 5), r_txt, SANS_B(11), GOLD, anchor="ra", tag="topband-r")

    # ---- masthead
    title = "Sunday 22 November 2026"
    tf = SERIF_B(58)
    draw_text(draw, (W // 2, 28), title, tf, INK, anchor="ma", tag="masthead")
    sub = ("186 drones over Ukraine in the night \u00b7 COP31 ends with no fossil-fuel "
           "deal \u00b7 Iran\u2019s radar claim meets Bahrain\u2019s denial")
    draw_text(draw, (W // 2, 98), sub, SERIF_I(17), RED_DK, anchor="ma", tag="subhead")

    # ---- data strip
    y0, y1 = 114, 168
    draw.line([MARGIN, y0, W - MARGIN, y0], fill=INK, width=2)
    draw.line([MARGIN, y1, W - MARGIN, y1], fill=INK, width=2)
    cell_w = CW / 6
    for i, (num, cap) in enumerate(DATA_STRIP):
        cx = MARGIN + i * cell_w
        if i:
            draw.line([cx, y0 + 6, cx, y1 - 6], fill=LINE, width=1)
        draw_text(draw, (cx + cell_w / 2, y0 + 4), num, SERIF_B(26), RED_DK,
                  anchor="ma", tag="data:" + num)
        draw_text(draw, (cx + cell_w / 2, y0 + 34), cap, SANS(9.5), GREY,
                  anchor="ma", tag="datacap:" + cap)

    # ---- region strip
    y0 = 171
    x = MARGIN
    draw_text(draw, (x, y0 + 4), "REGIONS:", SANS_B(10), INK, tag="regions-label")
    x += draw.textlength("REGIONS: ", font=SANS_B(10)) + 4
    for name, count, color in REGIONS:
        w_, h_ = chip(draw, int(x), y0, "%s %d" % (name, count), SANS_B(10), color)
        x += w_ + 6

    # ---- UTC timeline
    y0 = 195
    draw.rectangle([MARGIN, y0, W - MARGIN, y0 + 20], fill=NAVY)
    draw_text(draw, (MARGIN + 8, y0 + 4), "THE DAY IN UTC", SANS_B(10), GOLD,
              tag="utc-label")
    tx = MARGIN + 8 + draw.textlength("THE DAY IN UTC  ", font=SANS_B(9.5))
    for k, (t, what) in enumerate(UTC_ITEMS):
        draw_text(draw, (tx, y0 + 4), t, SANS_B(9.5), (255, 255, 255), tag="utc:" + t)
        tx += draw.textlength(t + " ", font=SANS_B(9.5))
        draw_text(draw, (tx, y0 + 4), what, SANS(9.5), (220, 225, 240), tag="utcw:" + what)
        tx += draw.textlength(what, font=SANS(9.5))
        if k < len(UTC_ITEMS) - 1:
            draw_text(draw, (tx, y0 + 4), "  \u00b7  ", SANS(9.5), GOLD, tag="utc-sep")
            tx += draw.textlength("  \u00b7  ", font=SANS(9.5))

    # ---- three leads
    y0, lead_h, pic_h = 219, 232, 96
    lead_w, lead_gap = 325, 8
    for i, lead in enumerate(LEADS):
        lx = MARGIN + i * (lead_w + lead_gap)
        draw.rectangle([lx, y0, lx + lead_w, y0 + lead_h], fill=CARD,
                       outline=LINE, width=1)
        LEAD_SCENES[lead["scene"]](draw, lx + 1, y0 + 1, lead_w - 2, pic_h)
        # number badge on the pictogram
        num_circle(draw, lx + 16, y0 + pic_h - 14, lead["n"], r=10)
        # kicker + certainty chip (right-aligned)
        ky = y0 + pic_h + 7
        kick = "%d %s \u00b7 %s" % (lead["n"], lead["place"], lead["beat"])
        draw_text(draw, (lx + 8, ky), kick, SANS_B(10), RED_DK, tag="kick:%d" % lead["n"])
        fnt = SANS_B(9)
        tw = draw.textlength(lead["chip"], font=fnt)
        cw = int(tw) + 10
        chh = text_h(draw, lead["chip"], fnt) + 4
        draw.rounded_rectangle([lx + lead_w - 8 - cw, ky, lx + lead_w - 8, ky + chh],
                               radius=2, fill=lead["chip_bg"])
        draw.text((lx + lead_w - 8 - cw + 5, ky + 2), lead["chip"], font=fnt,
                  fill=CHIP_TXT)
        TEXT_BOXES.append((lx + lead_w - 8 - cw, ky, lx + lead_w - 8, ky + chh,
                           "chip:" + lead["chip"]))
        # headline
        hy = ky + 15
        lines = wrap(draw, lead["head"], SERIF_B(19), lead_w - 16)
        assert len(lines) <= 2, "lead %d headline wraps to %d lines" % (lead["n"], len(lines))
        for li, ln in enumerate(lines):
            draw_text(draw, (lx + 8, hy + li * 23), ln, SERIF_B(19), INK,
                      tag="leadhead:%d" % lead["n"])
        # body
        by = hy + len(lines) * 23 + 4
        blines = wrap(draw, lead["body"], SANS(11), lead_w - 16)
        assert len(blines) <= 4, "lead %d body wraps to %d lines" % (lead["n"], len(blines))
        for li, ln in enumerate(blines):
            draw_text(draw, (lx + 8, by + li * 14), ln, SANS(11), (40, 40, 40),
                      tag="leadbody:%d" % lead["n"])

    # ---- charts row
    y0 = 455
    draw.rectangle([MARGIN, y0, MARGIN + 490, y0 + 62], fill=CARD, outline=LINE, width=1)
    draw.rectangle([W - MARGIN - 490, y0, W - MARGIN, y0 + 62], fill=CARD,
                   outline=LINE, width=1)
    draw_text(draw, (MARGIN + 8, y0 + 4), "THE NIGHT OVER UKRAINE \u2014 DRONES",
              SANS_B(11), INK, tag="chart1-title")
    hbar(draw, MARGIN + 8, y0 + 24, "Fired", "186", 186 / 186, RED)
    hbar(draw, MARGIN + 8, y0 + 42, "Downed or jammed", "161", 161 / 186, NAVY2)
    draw_text(draw, (W - MARGIN - 482, y0 + 4), "COP31 IN NUMBERS \u2014 NATIONS",
              SANS_B(11), INK, tag="chart2-title")
    hbar(draw, W - MARGIN - 482, y0 + 24, "Backed fossil-fuel language", "130+",
         130 / 130, TEAL)
    hbar(draw, W - MARGIN - 482, y0 + 42, "Signed electrification pledge", "90+",
         90 / 130, GOLD)

    # ---- mid label
    draw_text(draw, (MARGIN, 522), "THE DAY IN TWELVE", SANS_B(11), INK,
              tag="mid-label")
    draw_text(draw, (W - MARGIN, 522), "THE STORIES THAT MOVED THE WORLD TODAY",
              SANS(10), GREY, anchor="ra", tag="mid-label-r")

    # ---- mid grid: 6 cols x 2 rows
    gy0, card_w, card_h, gap = 536, 160, 105, 6
    for idx, mid in enumerate(MIDS):
        r, c = divmod(idx, 6)
        cx = MARGIN + c * (card_w + gap)
        cy = gy0 + r * (card_h + 4)
        draw.rectangle([cx, cy, cx + card_w, cy + card_h], fill=CARD,
                       outline=LINE, width=1)
        draw.rectangle([cx + 1, cy + 1, cx + card_w - 1, cy + 34], fill=mid["bg"])
        MID_SCENES[mid["scene"]](draw, cx + 1, cy + 1, card_w - 2, 33)
        banner_chip(draw, cx + 4, cy + 4, mid["banner"], mid["bg"])
        # certainty chip, bottom-right of the banner
        fnt = SANS_B(7.5)
        tw = draw.textlength(mid["chip"], font=fnt)
        chw = int(tw) + 8
        draw.rectangle([cx + card_w - 4 - chw, cy + 34 - 12,
                        cx + card_w - 4, cy + 34 - 1], fill=TEAL)
        draw.text((cx + card_w - 4 - chw + 4, cy + 34 - 11), mid["chip"],
                  font=fnt, fill=(255, 255, 255))
        TEXT_BOXES.append((cx + card_w - 4 - chw, cy + 22,
                           cx + card_w - 4, cy + 33, "midchip:" + mid["chip"]))
        kick = "%d %s \u00b7 %s" % (mid["n"], mid["place"].split(",")[0], mid["beat"])
        draw_text(draw, (cx + 5, cy + 38), kick, SANS_B(9), RED_DK,
                  tag="midkick:%d" % mid["n"])
        hlines = wrap(draw, mid["head"], SANS_B(12), card_w - 10)
        assert len(hlines) <= 2, "mid %d headline wraps to %d" % (mid["n"], len(hlines))
        for li, ln in enumerate(hlines):
            draw_text(draw, (cx + 5, cy + 50 + li * 15), ln, SANS_B(12), INK,
                      tag="midhead:%d" % mid["n"])
        blines = wrap(draw, mid["body"], SANS(9.5), card_w - 10)
        assert len(blines) <= 2, "mid %d body wraps to %d" % (mid["n"], len(blines))
        for li, ln in enumerate(blines):
            draw_text(draw, (cx + 5, cy + 81 + li * 12), ln, SANS(9.5),
                      (40, 40, 40), tag="midbody:%d" % mid["n"])

    # ---- bottom: dot map (left) + numbered list (right)
    by0, bh = 754, 170
    map_w = 300
    draw.rectangle([MARGIN, by0, MARGIN + map_w, by0 + bh], fill=CARD,
                   outline=LINE, width=1)
    draw_text(draw, (MARGIN + 8, by0 + 5), "WHERE IT HAPPENED", SANS_B(11), INK,
              tag="map-title")
    draw_text(draw, (MARGIN + map_w - 8, by0 + 6), "pins match story numbers",
              SANS(9), GREY, anchor="ra", tag="map-sub")
    mx0, my0, mw, mh = MARGIN + 8, by0 + 24, map_w - 16, bh - 32
    draw.rectangle([mx0, my0, mx0 + mw, my0 + mh], fill=SKY)
    dot_dx, dot_dy = mw / 64.0, mh / 32.0
    for ri, row in enumerate(WORLD_MAP):
        for ci, ch in enumerate(row):
            if ch == "#":
                dx = mx0 + (ci + 0.5) * dot_dx
                dy = my0 + (ri + 0.5) * dot_dy
                draw.ellipse([dx - 1.6, dy - 1.6, dx + 1.6, dy + 1.6],
                             fill=(122, 110, 88))
    for n, lon, lat in PINS:
        px = mx0 + (lon + 180.0) / 360.0 * mw
        py = my0 + (90.0 - lat) / 180.0 * mh
        num_circle(draw, px, py, n, r=6)
    # list
    lx0 = MARGIN + map_w + 8
    lw = W - MARGIN - lx0
    draw_text(draw, (lx0, by0 + 5), "ALSO ON SUNDAY 22 NOVEMBER \u2014 27 MORE STORIES",
              SANS_B(11), INK, tag="list-title")
    col_w = (lw - 12) / 2
    row_h = (bh - 26) / 14.0
    for i, (n, region, text) in enumerate(LIST):
        col, row = divmod(i, 14)
        x = lx0 + col * (col_w + 12)
        y = by0 + 24 + row * row_h
        head = "%d %s: " % (n, region)
        draw_text(draw, (x, y), head, SANS_B(9.5), RED_DK, tag="listhead:%d" % n)
        hx = x + draw.textlength(head, font=SANS_B(9.5)) + 2
        bb = draw_text(draw, (hx, y), text, SANS(9.5), INK, tag="list:%d" % n)
        assert bb[2] <= lx0 + (col + 1) * (col_w + 12) - 4, \
            "list %d overflows its column" % n

    # ---- DATE CHECK
    y0 = 928
    draw.rectangle([MARGIN, y0, W - MARGIN, y0 + 34], outline=RED, width=2)
    cw, ch = chip(draw, MARGIN + 6, y0 + 5, "DATE CHECK", SANS_B(10), RED)
    dlines = wrap(draw, DATE_CHECK, SANS(10), CW - cw - 24)
    assert len(dlines) <= 2, "DATE CHECK wraps to %d lines" % len(dlines)
    for li, ln in enumerate(dlines):
        draw_text(draw, (MARGIN + 6 + cw + 10, y0 + 4 + li * 14), ln, SANS(10),
                  INK, tag="datecheck")

    # ---- sources + legend
    draw_text(draw, (MARGIN, 966), SOURCES, SANS(8), GREY, tag="sources")
    draw_text(draw, (MARGIN, 978), LEGEND, SANS(8), GREY, tag="legend")

    # ---- footer navy band
    draw.rectangle([0, 1002, W, H], fill=NAVY)
    draw_text(draw, (MARGIN, 1008), "THE WORLD IN ONE DAY", SANS_B(10),
              (255, 255, 255), tag="footer")
    draw_text(draw, (W - MARGIN, 1008), "SUNDAY 22 NOVEMBER 2026 \u00b7 ONE PAGE",
              SANS_B(10), GOLD, anchor="ra", tag="footer-r")

    return img


def validate(img):
    """Layout validator: every recorded text box must sit inside the page
    (allowing the full-bleed top/footer bands) and no two text boxes from
    different elements may overlap."""
    errors = []
    for (x0, y0, x1, y1, tag) in TEXT_BOXES:
        if x0 < 0 or y0 < 0 or x1 > W or y1 > H:
            errors.append("out of page: %s %s" % (tag, (x0, y0, x1, y1)))
        if x0 < 8 and "topband" not in tag and "footer" not in tag:
            errors.append("left margin: %s %s" % (tag, (x0, y0, x1, y1)))
        if x1 > W - 8 and "topband" not in tag and "footer" not in tag:
            errors.append("right margin: %s %s" % (tag, (x0, y0, x1, y1)))
    # pairwise text overlap (chips sit on artwork, so only compare boxes
    # whose tags are plain text, not chips/pins/banners)
    plain = [b for b in TEXT_BOXES
             if not b[4].startswith(("chip:", "pin:", "banner:", "midchip:"))]
    for i in range(len(plain)):
        for j in range(i + 1, len(plain)):
            a, b = plain[i], plain[j]
            ox = min(a[2], b[2]) - max(a[0], b[0])
            oy = min(a[3], b[3]) - max(a[1], b[1])
            if ox > 1 and oy > 1:
                errors.append("text overlap: %s vs %s" % (a[4], b[4]))
    return errors


def main():
    img = render()
    errors = validate(img)
    if errors:
        print("LAYOUT FAIL (%d):" % len(errors))
        for e in errors[:30]:
            print("  - " + e)
        sys.exit(1)
    img.save(OUT, format="PNG", optimize=True)
    size = os.path.getsize(OUT)
    print("wrote %s (%d bytes, %dx%d)" % (OUT, size, W, H))
    print("text boxes recorded: %d" % len(TEXT_BOXES))
    if size > 1048576:
        print("SIZE FAIL: over 1 MiB")
        sys.exit(1)


if __name__ == "__main__":
    main()
