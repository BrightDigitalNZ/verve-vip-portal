# Verve Intimate Society — VIP Rewards

The front-end for the **Verve Intimate Society** VIP rewards platform
(for `verveintimate.com.au`). A single-page, static, dependency-free site:
members land on a personalised dashboard, see their credit balance and tier,
learn how to earn and redeem credits, refer friends, become an ambassador, and
give image permission — all from one elegant page.

> **Status:** Production-ready structure with **labelled placeholder imagery**.
> Drop in the final brand assets (see [Swapping in real assets](#swapping-in-real-assets))
> and deploy. No build step, no framework, no server required.

---

## Project structure

```
verve-vip-portal/
├── index.html              ← the VIP Rewards platform (main page)
├── community.html          ← "Inner Circle"     (nav stub — coming soon)
├── news-offers.html        ← "News & Offers"    (nav stub — coming soon)
├── recent-shoots.html      ← "Client Spotlight" (nav stub — coming soon)
├── connect.html            ← "Connect"          (contact details)
│
├── css/
│   └── styles.css          ← all styles (colours, fonts, layout, responsive)
│
├── js/
│   └── main.js             ← all behaviour (personalisation, tabs, FAQ,
│                              consent, code reveal, referral form, modal)
│
├── assets/
│   ├── favicon.png         ← brand "V" favicon (placeholder)
│   ├── images/             ← all photography (placeholders — swap these)
│   │   ├── img-hero.jpg
│   │   ├── img-studio.jpg
│   │   ├── img-banner.jpg
│   │   ├── gallery-1.jpg … gallery-4.jpg
│   │   ├── ambassador.jpg
│   │   ├── footer.jpg
│   │   ├── simpson.jpg
│   │   ├── nannini.png
│   │   └── robe-vi.png
│   └── logos/              ← brand logo placeholders
│       ├── logo-light.png  ← for dark backgrounds (the nav)
│       └── logo-dark.png   ← for light backgrounds
│
├── scripts/                ← helper scripts (NOT served to visitors)
│   ├── generate_placeholders.py   ← regenerates placeholder imagery
│   └── generate_stub_pages.py     ← regenerates the nav stub pages
│
├── .nojekyll               ← tells GitHub Pages to serve files as-is
├── .gitignore
└── README.md
```

The design is preserved exactly from the original source of truth — the same
colour variables, fonts, breakpoints and JavaScript. The only structural change
is separating the inline `<style>` and `<script>` into `css/styles.css` and
`js/main.js`, and moving imagery into `assets/`.

---

## Local preview

It's a static site — just open `index.html` in a browser. To preview exactly
as it will deploy (so relative paths and the personalisation params behave),
run a tiny local server from the project root:

```bash
# Python 3 (already on most machines)
python3 -m http.server 8000
# → visit http://localhost:8000

# …or Node
npx serve .
```

### Personalisation links

The dashboard personalises from URL parameters, so you can send each client a
tailored link:

| Parameter | Example | Effect |
|-----------|---------|--------|
| `name`    | `?name=Sophie` | Greeting + profile name |
| `spend`   | `?spend=2995`  | Auto-calculates credits ($1 per $10) **and** tier |
| `credits` | `?credits=500` | Sets credit balance manually (overrides the spend calc) |
| `tier`    | `?tier=Fierce` | Forces tier label (`Bare` / `Bold` / `Fierce` / `Icon`) |
| `gallery` | `?gallery=<url-encoded-pictime-link>` | Wires the gallery button to the client's private gallery |

**Example:**
`index.html?name=Sophie&spend=2995&gallery=https%3A%2F%2Fgallery.pictime.com%2Fsophie`

If no params are given it defaults to a demo state (`name=Holly`, `spend=3000`
→ Fierce, 300 credits).

---

## Deploying to GitHub Pages (zero config)

This repo is ready to serve as-is. The `.nojekyll` file ensures GitHub Pages
serves every file unprocessed.

1. Push this repo to GitHub.
2. **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Pick your branch (e.g. `main`) and folder **`/ (root)`**, then **Save**.
5. Wait ~1 minute. Your site is live at
   `https://<your-org>.github.io/<repo-name>/`.

### Custom domain (`verveintimate.com.au`)

> ⚠️ `verveintimate.com.au` already hosts the live WooCommerce store, so this
> rewards portal will almost certainly live on a **subdomain** (e.g.
> `society.verveintimate.com.au` or `rewards.verveintimate.com.au`) rather than
> the apex domain. Confirm the intended domain (see the checklist below).

To attach a subdomain once confirmed:

1. Create a file named **`CNAME`** in the repo root containing the single line,
   e.g. `society.verveintimate.com.au`.
2. At your DNS provider, add a **CNAME** record:
   `society` → `<your-org>.github.io`.
3. In **Settings → Pages → Custom domain**, enter the same hostname and enable
   **Enforce HTTPS**.

(No `CNAME` file is committed yet — it's intentionally left out so it can't
mis-route the live domain before you've decided.)

---

## Swapping in real assets

Replace the placeholder files in `assets/images/` (and `assets/logos/`) with the
final assets, **keeping the same filenames** — no code changes needed.

| Use in design | Filename (drop in `assets/images/`) | Suggested spec | Original photographer file |
|---|---|---|---|
| Hero background (studio interior, sofa + framed print) | `img-hero.jpg` | ~1920×1080, landscape | _(new)_ |
| Full-width studio band (white bed studio set) | `img-studio.jpg` | ~1920×860, landscape | _(new)_ |
| Manifesto band ("I am enough" mirror shot) | `img-banner.jpg` | ~1920×1080, landscape | _(new)_ |
| Gallery panel 1 (lingerie portrait, cropped) | `gallery-1.jpg` | ~700×1000, portrait | `1079082955-Holland_BLAKE028.jpg` |
| Gallery panel 2 (face portrait, white sheets) | `gallery-2.jpg` | ~700×1000, portrait | `1099084488 - Gray - HET-18.jpg` |
| Gallery panel 3 (auburn half-face crop) | `gallery-3.jpg` | ~700×1000, portrait | `1069090112-Tallon-CC-124.jpg` |
| Gallery panel 4 | `gallery-4.jpg` | ~700×1000, portrait | `1079085815-LOWE-MTR037.jpg` |
| Ambassador portrait (B&W, seated) | `ambassador.jpg` | ~960×1180, portrait | `1029094589-Pearce-JCN438.jpg` |
| Footer CTA background | `footer.jpg` | ~1920×900, landscape | `KEZ_MJA-45.jpg` |
| Return CTA banner background | `simpson.jpg` | ~1920×900, landscape | `simpson.jpg` |
| Feature panel in "Earn" section | `nannini.png` | ~1080×360, wide | `nannini.png` |
| Referral gift robe (product shot) | `robe-vi.png` | ~720×900, portrait, ideally transparent PNG | `ROBE VI.png` |

> **Filename note:** the photographer's coded filenames (and `ROBE VI.png`, which
> contained a space) were renamed to clean, web-safe names. The mapping above is
> the source of truth. If you'd prefer to keep the original names instead, tell me
> and I'll repoint the references.

### Regenerating placeholders
If you ever need the labelled placeholders back (e.g. after experimenting),
re-run:

```bash
python3 scripts/generate_placeholders.py   # needs Pillow: pip install Pillow
```

---

## Credit logic & tiers (preserved exactly)

**Earning**

| Action | Credit |
|---|---|
| Investment / spend | $1 per $10 spent |
| Follow on Instagram | $20 |
| Follow on TikTok | $20 |
| Refer a friend (on their booking) | $150 |
| Share your images (permission to use online) | $60 |
| Review or post (per platform) | $25 each |
| Add photos/video to a review | +$25 bonus |
| Film testimonial | $100 |
| Image permission (in-page consent) | +$50 |
| Ambassador booking (per booking, via code) | $150 |

**Tiers** (annual spend)

| Tier | Spend range |
|---|---|
| Bare   | A$0 – $1,500 |
| Bold   | A$1,500 – $3,000 |
| Fierce | A$3,000 – $4,500 |
| Icon   | A$4,501+ |

**Redemption codes** (as designed): shoot discount `SOCIETY300`, demo ambassador
code `HOLLY20`. The "New Shoot Credit" redeems for $295; the "Mini Shoot" for
$1,495.

> These values live in `js/main.js` (tier thresholds / progress) and as literal
> copy in `index.html` (earn cards, tiers table, redeem cards). Search for the
> number you want to change.

---

## How the forms currently behave

The interactive pieces are **front-end only** right now (matching the design):

- **Refer a Friend** — validates name + email, shows a "Referral Sent!"
  confirmation, but does **not** yet transmit anywhere.
- **Image Permission** — validates the checkbox + signature, shows a thank-you
  state and visually adds +$50, client-side only.
- **Submit Your Reward / claim flows** — link out to an existing Google Form
  (`forms.gle/u5tqBeihEhK7mCmV8`).
- **Review modal** — links out to Google/Instagram/TikTok.

To make the referral and consent forms actually deliver, they need a backend or
form service wired in (see the checklist). This is a deliberate, clearly-marked
seam — not a missing piece of the design.

---

## What I need from you to finalise

See [`HANDOFF.md`](HANDOFF.md) for the full checklist (assets, copy, form
handling, and domain/deploy decisions).
