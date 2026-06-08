# Handoff checklist — what I need from you to finalise

Everything below is the only thing standing between this repo and a finished,
live site. Grouped so you can hand pieces to whoever owns them.

---

## 1. Logos & brand assets

- [ ] **Primary logo** — vector if possible (`.svg`), plus a transparent `.png`
      fallback. Two versions:
  - light (for the dark nav / dark sections) → replaces `assets/logos/logo-light.png`
  - dark (for cream sections) → replaces `assets/logos/logo-dark.png`
  - Suggested PNG size: ~900×300 (or 3× the display height for retina).
- [ ] Should the **nav** show the logo image instead of the current text
      wordmark ("VERVE INTIMATE")? If yes, send the lockup you want there and the
      target height (~20–28px).
- [ ] **Favicon** — currently a placeholder "V". Send a square mark (512×512 PNG)
      if you want a branded one → replaces `assets/favicon.png`.

## 2. Photography / image assets

Drop final files into `assets/images/` using **exactly** these filenames
(full spec table is in `README.md`):

- [ ] `img-hero.jpg` — studio interior (sofa + framed print), landscape
- [ ] `img-studio.jpg` — white bed studio set, wide landscape
- [ ] `img-banner.jpg` — "I am enough" mirror shot (manifesto band)
- [ ] `gallery-1.jpg` — lingerie portrait, cropped body shot
- [ ] `gallery-2.jpg` — face portrait, woman on white sheets
- [ ] `gallery-3.jpg` — auburn half-face close crop
- [ ] `gallery-4.jpg` — fourth gallery portrait
- [ ] `ambassador.jpg` — B&W artistic seated portrait
- [ ] `footer.jpg` — footer CTA background
- [ ] `simpson.jpg` — return CTA banner background
- [ ] `nannini.png` — feature panel in the "Earn" section
- [ ] `robe-vi.png` — the referral-gift robe (transparent PNG looks best)

Notes:
- [ ] Confirm you're happy with the **renamed filenames** (originals had coded
      names + a space in `ROBE VI.png`). Say the word if you'd rather keep the
      originals and I'll repoint everything.
- [ ] Any **image rights / model release** constraints I should know about before
      these go on a public page?

## 3. Copy, member data & links

- [ ] Confirm the **earning amounts** are final. ⚠️ One inconsistency to settle:
      the earn card says **Refer a Friend = $150**, but the FAQ says
      **"referring friends ($200 each)"** and the ambassador stats show
      **"200 points per booking"**. Which is correct — **$150 or $200**? I'll make
      it consistent everywhere.
- [ ] Same check for **"Share your images $60"** (earn card) vs the in-page
      **Image Permission +$50** consent reward — intentional, or should they match?
- [ ] Final **redemption codes** — keep `SOCIETY300` (shoot) and the ambassador
      code format (`HOLLY20` is a demo; codes are per-member)?
- [ ] The **shop / book links** all point to one WooCommerce checkout URL
      (`...add-to-cart=30707...`). Confirm that's the right product, or send the
      correct URL(s).
- [ ] Confirm the **studio locations** in the review modal (Surry Hills, South
      Melbourne, Brisbane) and their Google review links are current.
- [ ] Are the **secondary nav pages** (Inner Circle, News & Offers, Client
      Spotlight, Connect) in scope for me to build out, or do they already exist
      elsewhere on the main site (so the nav should link there instead)? Right now
      they're elegant "coming soon" stubs.

## 4. Form submission & integrations

The **Refer a Friend** and **Image Permission** forms are front-end only today
(by design). To make them live, pick an approach:

- [ ] **Referral form** — where should submissions go?
  - Keep using the existing **Google Form** (`forms.gle/u5tqBeihEhK7mCmV8`)?
  - A no-backend form service (**Formspree**, **Getform**, **Basin**) → I just
    need the endpoint/email.
  - Send the referral **email/SMS** automatically (needs an email service —
    e.g. **EmailJS** client-side, or a small backend/serverless function +
    **SendGrid/Postmark** and an **SMS** provider like Twilio). Tell me which.
- [ ] **Image Permission consent** — should the signed consent be **recorded**
      anywhere (it currently only updates the UI)? If yes, same options as above,
      plus: do you need a stored/audit copy (name, timestamp, consent text) for
      compliance?
- [ ] **Credit balances** — is there a system of record (loyalty platform, CRM,
      spreadsheet)? Today balances come purely from the URL `?credits=` / `?spend=`
      params. If you want real-time balances, I need to know the source/API.
- [ ] Provide any **API keys / service accounts** for whichever services we pick
      (share securely — not in the repo).

## 5. Domain & deployment

- [ ] **Which domain** should this live on? `verveintimate.com.au` is the live
      WooCommerce store, so I'm assuming a **subdomain** — please confirm the exact
      one (e.g. `society.verveintimate.com.au` or `rewards.verveintimate.com.au`).
- [ ] **Hosting** — GitHub Pages (set up here, zero-config), or do you prefer it
      served from the existing site/host (e.g. as a WordPress page/subdirectory)?
- [ ] Who manages **DNS**? Once the subdomain is decided I'll give exact CNAME
      records (and add the `CNAME` file to the repo).
- [ ] Any **analytics / tracking** to include (Google Analytics, Meta Pixel,
      cookie-consent banner)?
- [ ] Confirm the **GitHub repo + branch** that should be the deploy source.

---

### Fastest path to launch
If you just want it live to review: send the **12 images + logo**, confirm the
**$150 vs $200** referral amount, and tell me the **subdomain** — that alone gets
a polished, working site published. Forms/integrations can follow.
