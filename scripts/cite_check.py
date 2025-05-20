#!/usr/bin/env python3
"""
Very small footnote checker for *.md files.
• Finds [^n] references in text
• Verifies each has a matching definition [^n]:
Returns exit-code 1 if any mismatch.
"""
import re, sys, pathlib

err = False

def check_file(path: pathlib.Path):
    global err
    txt = path.read_text(encoding="utf-8")
    refs = set(re.findall(r'\[\^(\d+)\]', txt))
    defs = set(re.findall(r'\[\^(\d+)\]:', txt))
    missing = sorted(refs - defs)
    if missing:
        err = True
        print(f"❌ {path}: missing footnotes {missing}")

for md in pathlib.Path("data").rglob("*.md"):
    check_file(md)

if err:
    sys.exit(1)
print("✅ footnote check passed")

