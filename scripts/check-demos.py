#!/usr/bin/env python3
"""Checks for the company demos, run by CI and by hand:  python3 scripts/check-demos.py

For every demos/<id>/ folder:
1. There is an index.html.
2. Every relative href/src in its pages points at a file that exists.
3. No page or stylesheet loads anything from another host (plain <a href> links are fine).
4. Every index.html carries the CalmCampus disclaimer and none of the banned wording.
"""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
demos_dir = root / "demos"
bad = []
BANNED = [r"early signs?", r"stop burnout", r"detects?\b", r"diagnos(?:e|is)\b(?! or treat)", "\u2014", r"\bpilot\b"]
DISCLAIMER = "not medical professionals"

demos = sorted(p for p in demos_dir.iterdir() if p.is_dir())
for demo in demos:
    index = demo / "index.html"
    if not index.exists():
        bad.append(f"{demo.relative_to(root)}: missing index.html")
    for page in sorted(demo.rglob("*.html")):
        text = page.read_text()
        for ref in re.findall(r'(?:href|src)="([^"]+)"', text):
            if re.match(r"(https?:|mailto:|tel:|data:|blob:|#)", ref) or "{" in ref:
                continue
            target = ref.split("#")[0].split("?")[0]
            base = demo if target.startswith("/") else page.parent
            if target and not (base / target.lstrip("/")).exists():
                bad.append(f"{page.relative_to(root)}: missing {ref}")
        for tag in re.findall(r"<(?:script|link|img|iframe|source|video|audio|embed|object)\b[^>]*>", text):
            if re.search(r'rel="(?:canonical|alternate)"', tag):
                continue
            for url in re.findall(r'(?:src|href|srcset|data)="(https?://[^"]+)"', tag):
                bad.append(f"{page.relative_to(root)}: external resource {url}")
        visible = re.sub(r"<[^>]+>", " ", text)
        for pat in BANNED:
            if re.search(pat, visible, re.I):
                bad.append(f"{page.relative_to(root)}: banned wording /{pat}/")
        if page == index and DISCLAIMER not in visible:
            bad.append(f"{page.relative_to(root)}: missing the disclaimer")
    for css in demo.rglob("*.css"):
        for url in re.findall(r"url\(\s*['\"]?(https?:[^)'\"]+)", css.read_text()):
            bad.append(f"{css.relative_to(root)}: external url() {url}")

print("\n".join(bad) or f"ok ({len(demos)} demos)")
sys.exit(1 if bad else 0)
