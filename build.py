#!/usr/bin/env python3
"""Assemble data/*.txt + template.html -> index.html (fichier unique, sans dépendance)."""
import json, pathlib, sys

root = pathlib.Path(__file__).parent
fiches, n = [], 0
for lv in ["A1", "A2", "B1", "B2", "C1"]:
    lines = [l for l in (root / "data" / f"{lv.lower()}.txt").read_text("utf-8").splitlines() if l.strip()]
    print(lv, len(lines))
    for ln in lines:
        p = ln.split("|")
        assert len(p) == 7, f"{lv}: {len(p)} champs -> {ln[:60]}"
        emo, cat, en, fr, items, ex, tip = p
        assert cat in ("V", "G", "C", "E", "PV", "P"), ln[:60]
        its = []
        for it in items.split(";"):
            assert it.count("=") == 1, f"{lv}: item -> {it}"
            left, right = it.split("=")
            e = ""
            head, _, rest = left.partition(" ")
            if rest and any(ord(c) > 0x2000 for c in head):
                e, left = head, rest
            its.append([e, left.strip(), right.strip()])
        assert len(its) == 5, f"{lv}: {len(its)} items -> {en}"
        assert ex.count("=") == 1, f"{lv}: exemple -> {ex}"
        n += 1
        fiches.append({"id": n, "lv": lv, "cat": cat, "emo": emo, "en": en, "fr": fr,
                       "items": its, "ex": ex.split("="), "tip": tip})
print("total", n)
titles = [f["en"] for f in fiches]
dups = {t for t in titles if titles.count(t) > 1}
if dups: print("doublons:", dups)
html = (root / "template.html").read_text("utf-8").replace(
    "/*DATA*/[]", json.dumps(fiches, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
(root / "index.html").write_text(html, "utf-8")
print("index.html", len(html) // 1024, "Ko")
sys.exit(0 if n == 300 else 1)
