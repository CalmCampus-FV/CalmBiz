# CalmBiz

CalmBiz holds the CalmCampus demos and prototypes for companies (staff wellbeing, aimed at employers). It is new: there are no company demos yet. University demos live in [CalmCampus-FV/CalmUni](https://github.com/CalmCampus-FV/CalmUni), the website (including [cc.braunf.com/companies/](https://cc.braunf.com/companies/)) in [CalmCampus-FV/CalmWeb](https://github.com/CalmCampus-FV/CalmWeb), the iOS app in [CalmCampus-FV/CalmApp](https://github.com/CalmCampus-FV/CalmApp), and the research and design archive in [CalmCampus-FV/CalmCampus](https://github.com/CalmCampus-FV/CalmCampus).

## Layout

- `demos/<id>/` - one folder per company demo, with an `index.html`, self-contained (relative paths, no files from outside the folder). Empty for now; see `demos/README.md`.
- `scripts/check-demos.py` - the check CI runs: every demo has an index.html, links resolve, nothing loads from other hosts, the disclaimer is present and the banned wording is absent.

## Rules for demos

- Plain HTML/CSS/JS, no build step unless a demo really needs one. No backend, no accounts, no analytics, no third-party scripts, fonts or embeds.
- Answers stay on the device (local storage); nothing is sent anywhere.
- Never invent content: no fake company names, logos, testimonials, quotes, numbers or results. Labelled example data is allowed only when it is clearly marked Example.
- If a demo is ever published under cc.braunf.com, it goes the same way as the university demos: the source stays here and CalmWeb serves a copy in `docs/<path>/` (see CalmUni's AGENTS.md). Once a link is sent, never move or rename it.

## Wording rules (all CalmCampus copy)

- Never claim pilots, results, partnerships or detection. No "early signs", no "stop burnout", no claim that CalmCampus finds burnout or gets people to seek help. Wellness wording only ("supports").
- Every user-facing surface carries the full disclaimer: we are students, not medical professionals; CalmCampus does not diagnose or treat; we strongly suggest a doctor, occupational health or support service.
- The check-in takes less than a minute. Data stays on the phone.
- No em dashes. Names: Florian Braùn (with the ù) and Hélène David.

## Commands

```bash
python3 scripts/check-demos.py
python3 -m http.server 8080 --directory demos   # view the demos locally
```

CI (`.github/workflows/ci.yml`) runs the check on every push and PR. `.github/workflows/claude.yml` is the Claude Code action (write access, triggered by `@claude`); it needs the `CLAUDE_CODE_OAUTH_TOKEN` repository secret.
