#!/usr/bin/env python3
"""
Generate the secondary navigation pages referenced by the main portal nav.

These are intentionally light, on-brand placeholder pages so the deployed
site has no broken links. Replace the <main> content with real content when
ready — they already share css/styles.css, so the look stays consistent.
"""
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")

# nav order: (href, label)
NAV = [
    ("community.html",     "Inner Circle"),
    ("news-offers.html",   "News &amp; Offers"),
    ("recent-shoots.html", "Client Spotlight"),
    ("connect.html",       "Connect"),
]


def nav_html(active_href):
    links = []
    for href, label in NAV:
        is_active = href == active_href
        color = "white" if is_active else "rgba(255,255,255,0.55)"
        links.append(
            f'    <a href="{href}" style="font-family:\'Montserrat\',sans-serif;'
            f'font-size:9px;font-weight:500;letter-spacing:0.22em;text-transform:uppercase;'
            f'color:{color};padding:20px 22px;border-left:1px solid var(--border-dark);'
            f'transition:color 0.2s;text-decoration:none;" '
            f'onmouseover="this.style.color=\'white\'" '
            f'onmouseout="this.style.color=\'{color}\'">{label}</a>'
        )
    links_str = "\n".join(links)
    return f'''<nav style="background:var(--black);padding:0 40px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border-dark);">
  <a href="index.html" style="display:flex;align-items:center;padding:13px 0;"><img src="assets/logos/logo-light.png" alt="Verve Intimate Society" style="height:34px;width:auto;display:block;" /></a>
  <div style="display:flex;align-items:stretch;gap:0;">
{links_str}
  </div>
</nav>'''


def page(active_href, eyebrow, title_html, body_html):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Verve Intimate Society — {eyebrow}</title>
  <link rel="icon" type="image/png" href="assets/favicon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,600&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

{nav_html(active_href)}

<section class="hero">
  <div class="hero-bg-img"></div>
  <p class="hero-eyebrow">{eyebrow}</p>
  <h1>{title_html}</h1>
  <p class="hero-society">Society</p>
{body_html}
</section>

<section class="footer-cta">
  <h2>The Verve Intimate <em>Society</em></h2>
  <p>Earn credits every time you visit or share your love for the brand.</p>
  <a href="index.html" class="btn btn-accent">Back to VIP Rewards</a>
</section>

</body>
</html>
'''


def coming_soon(tagline):
    return f'''  <p class="hero-tagline" style="margin-top:28px;">{tagline}</p>
  <p class="hero-desc">This page is coming soon. In the meantime, explore your VIP Rewards dashboard.</p>
  <div class="hero-btns">
    <a href="index.html" class="btn btn-accent" style="background:#4e1610;">Go to VIP Rewards</a>
  </div>'''


PAGES = {
    "community.html": dict(
        eyebrow="Inner Circle",
        title='The Inner <em>Circle</em>',
        body=coming_soon("A private space for our most cherished members."),
    ),
    "news-offers.html": dict(
        eyebrow="News &amp; Offers",
        title='News &amp; <em>Offers</em>',
        body=coming_soon("Launches, seasonal offers and Society-only invitations."),
    ),
    "recent-shoots.html": dict(
        eyebrow="Client Spotlight",
        title='Client <em>Spotlight</em>',
        body=coming_soon("Celebrating the women who stepped into their power with us."),
    ),
    "connect.html": dict(
        eyebrow="Connect",
        title='Let\'s <em>Connect</em>',
        body='''  <p class="hero-tagline" style="margin-top:28px;">We would love to hear from you.</p>
  <p class="hero-desc">
    Email <a href="mailto:info@verveintimate.com.au" style="color:var(--accent-pale);border-bottom:1px solid var(--accent-pale);">info@verveintimate.com.au</a><br>
    Instagram <a href="https://www.instagram.com/verve_intimate" target="_blank" style="color:var(--accent-pale);border-bottom:1px solid var(--accent-pale);">@verve_intimate</a><br>
    TikTok <a href="https://www.tiktok.com/@verveintimate" target="_blank" style="color:var(--accent-pale);border-bottom:1px solid var(--accent-pale);">@verveintimate</a>
  </p>
  <div class="hero-btns">
    <a href="https://www.verveintimate.com.au" target="_blank" class="btn btn-accent" style="background:#4e1610;">Visit verveintimate.com.au</a>
    <a href="index.html" class="btn btn-outline">VIP Rewards</a>
  </div>''',
    ),
}

for href, cfg in PAGES.items():
    html = page(href, cfg["eyebrow"], cfg["title"], cfg["body"])
    with open(os.path.join(ROOT, href), "w") as f:
        f.write(html)
    print(f"  wrote {href}")
print("Done.")
