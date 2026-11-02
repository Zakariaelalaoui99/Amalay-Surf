# Amalay Surf — website

Static HTML + Tailwind CSS (compiled, no CDN/JIT script tag).

## Structure

- `index.html` — the whole one-page site
- `src/input.css` — Tailwind entry + custom reveal-on-scroll CSS
- `dist/output.css` — compiled, minified CSS (generated, don't hand-edit)
- `tailwind.config.js` — palette (`cream`, `ink`, `pine`, `sand`, `stone`) and fonts (Fraunces / Manrope)
- `images/` — real photos are wired in (hero, intro/coastline, all 3 lesson cards,
  instructor, 10-photo gallery). Each was resized/compressed for web (~2MB total, down
  from ~35MB of DSLR originals). Also `logo-mark.png` (icon only, used in the nav +
  favicon) and `logo-full.png` (full lockup, used in the footer) — both derived from the
  supplied logo artwork, inverted to white for use on dark backgrounds.
- `originals/` — full-resolution source photos and the original logo file, kept for
  reference. Not used by the site and not meant to be deployed — safe to exclude from
  hosting/upload.
- `scripts/gen_placeholders.py` — regenerates a labeled placeholder SVG if you ever need
  a stand-in for a photo you haven't shot yet.

## Before this goes live

1. **One placeholder left:** `images/contact-visual.svg` (the small image next to the
   contact form). Send a photo for it — a map screenshot or a closing lifestyle shot both
   work — and I'll wire it in the same way as the rest.
2. **Contact details** — done. Email (`zakariaelalaoui99@gmail.com`) and phone
   (`+212 648-014379`) are wired into the mailto form, CTA band, contact section, and
   footer. The WhatsApp link (`wa.me/212648014379`) assumes the same number takes
   WhatsApp — flag it if that's not the case.
3. The inquiry form uses a `mailto:` form action (opens the visitor's email client with the
   message pre-filled) per your choice — no backend required, but it only works reliably on
   desktop mail clients and requires the visitor to actually hit "send" in their own email
   app. If you later want guaranteed delivery, swap the form's `action`/`method`/`enctype`
   for a service like Formspree.

## Build / preview

```bash
npm install          # once
npm run build        # compiles src/input.css -> dist/output.css
npm run watch        # rebuild on change while editing
```

To preview locally:

```bash
python3 -m http.server 8080
# open http://localhost:8080/index.html
```
