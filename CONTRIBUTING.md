# Contributing Guide
> **Welcome!** This repo uses the classic Git command-line (CLI) workflow:  
> **Fork → Clone → Branch → Commit → Push → Pull-Request**.  
> Below is a quick, copy-paste-friendly guide. Please keep each PR focused on one topic.
---
## 1 · Quick Start ( CLI )
```bash
# 1-a. Fork the repo on GitHub (button top-right), then:
git clone https://github.com/<your-username>/quran-tafsir-ai.git
cd quran-tafsir-ai
# 1-b. Create a feature branch
git checkout -b feature/<short-topic>
# 1-c. Hack away …
#       ├── data/
#       └── docs/
# 1-d. Stage & commit
git add .
git commit -m "feat: add tafsir for 1:8"
# 1-e. Push to your fork
git push -u origin feature/<short-topic>
# 1-f. Open the Pull Request
#      (GitHub prints a link or visit your fork ▶︎ Compare & pull request)
```

main is a protected branch → direct pushes are blocked; every change must come via PR and one maintainer approval.

## 2 · Writing & File Layout

| Topic | Rule |
|------|------|
| File location | New ayah → data/###_surah-name/###.md |
| Heading depth | Use ### max (#, ## acceptable); avoid ####+. |
| Footnotes | Cite in text [^1], list bottom: [^1]: Source, vol, p. |
| Tables | Align pipes \| |
| Arabic | Prefer U+06xx glyphs; transliteration in *italics*. |

## 3 · Review & Merge
- Maintainer reviews your PR; they may request tweaks.
- At least 1 approving review is required (branch-protection rule).
- Maintainers may squash / re-title commits for a clean history.

## 4 · Local Lint (optional)
```bash
# Markdown lint (optional)
npm i -g markdownlint-cli
markdownlint .
# Citation checker (optional)
python scripts/cite_check.py
```

## 5 · Etiquette
- Be respectful; explain why the change helps.
- Small, atomic PRs merge faster than giant ones.
- If unsure, open a Draft PR early and ask for feedback.

JazakumAllahu khayran — may your contribution be accepted and beneficial!
