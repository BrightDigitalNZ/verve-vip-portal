/* ════════════════════════════════════════════════════════════════════════
   VERVE INTIMATE SOCIETY — VIP REWARDS
   Front-end behaviour (extracted from the design source of truth).

   Includes:
   • URL-parameter profile personalisation (name / spend / credits / tier / gallery)
   • Tier auto-calculation + progress bar
   • Tab switching
   • FAQ accordion
   • Image-permission consent flow (+$50 credit)
   • Shoot discount-code reveal & copy
   • Ambassador code copy
   • Refer-a-friend form logic
   ════════════════════════════════════════════════════════════════════════ */

/* ── Personalisation from URL params ─────────────────────────
   Send clients a link like:
   index.html?name=Sophie&spend=2995
   Or with manual credits: ?name=Sophie&credits=500&tier=Fierce
   ────────────────────────────────────────────────────────── */
(function () {
  var params = new URLSearchParams(window.location.search);
  var name    = params.get('name')    || 'Holly';
  var spend   = parseFloat(params.get('spend')) || 3000;
  var tier    = params.get('tier');
  var gallery = params.get('gallery');

  // Auto-calculate credits from spend ($1 per $10)
  var credits = params.get('credits')
    ? parseInt(params.get('credits'))
    : Math.floor(spend / 10);

  // Auto-assign tier from spend if not provided
  if (!tier) {
    if      (spend >= 4501) tier = 'Icon';
    else if (spend >= 3000) tier = 'Fierce';
    else if (spend >= 1500) tier = 'Bold';
    else                    tier = 'Bare';
  }

  // Hero greeting
  if (name) {
    document.getElementById('heroEyebrow').textContent = 'Welcome back, ' + name;
    document.getElementById('memberName').textContent  = name;
  }

  // Credits
  if (credits) {
    document.getElementById('memberCredits').textContent = '$' + credits.toLocaleString();
  }

  // Tier label + progress bar
  var tiers = {
    'Bare':   { label: 'Bare Member',   lower: 'Bare',   upper: 'Bold — A$1,500+',    pct: 15 },
    'Bold':   { label: 'Bold Member',   lower: 'Bold',   upper: 'Fierce — A$3,000+',  pct: 42 },
    'Fierce': { label: 'Fierce Member', lower: 'Fierce', upper: 'Icon — A$4,501+',    pct: 72 },
    'Icon':   { label: 'Icon Member',   lower: 'Fierce', upper: 'Icon ✦',              pct: 100 }
  };
  var t = tiers[tier] || tiers['Bare'];
  document.getElementById('memberTier').textContent   = t.label;
  document.getElementById('tierProgress').style.width = t.pct + '%';
  document.getElementById('tierLower').textContent    = t.lower;
  document.getElementById('tierUpper').textContent    = t.upper;
  if (tier === 'Icon') {
    document.getElementById('tierNote').textContent = 'You have reached our highest tier. Thank you for being an extraordinary part of the Society.';
  } else if (spend > 0) {
    var next = tier === 'Bold' ? 3000 : tier === 'Bare' ? 1500 : 4501;
    var diff = next - spend;
    document.getElementById('tierNote').textContent = 'Spend A$' + diff.toLocaleString() + ' more to reach your next tier.';
  }

  // Pictime gallery link
  var galleryBtn = document.getElementById('galleryRedeemBtn');
  if (galleryBtn) {
    if (gallery) {
      galleryBtn.href = decodeURIComponent(gallery);
      galleryBtn.target = '_blank';
      galleryBtn.textContent = 'View My Gallery →';
      galleryBtn.style.background = 'var(--accent)';
    } else {
      galleryBtn.href = 'mailto:info@verveintimate.com.au?subject=Gallery Access Request';
      galleryBtn.textContent = 'Request Gallery Link';
    }
  }
})();

/* Shoot code reveal */
function revealCode() {
  document.getElementById('shootRedeem').style.display = 'none';
  document.getElementById('shootCode').style.display = 'block';
}

/* Copy the shoot discount code shown inside an element (click-to-copy) */
function copyDiscountCode(el) {
  navigator.clipboard.writeText(el.textContent.trim()).then(function () {
    var orig = el.textContent;
    el.textContent = 'Copied!';
    setTimeout(function () { el.textContent = orig; }, 1800);
  });
}

/* Image consent */
function submitConsent() {
  var checked = document.getElementById('consentCheck').checked;
  var name    = document.getElementById('consentName').value.trim();
  if (!checked) { alert('Please tick the checkbox to give permission.'); return; }
  if (!name)    { alert('Please type your full name as your signature.'); return; }

  // Add $50 to displayed credit balance
  var creditsEl = document.getElementById('memberCredits');
  var current   = parseInt(creditsEl.textContent.replace(/[^0-9]/g, '')) || 0;
  var updated   = current + 50;
  creditsEl.textContent = '$' + updated.toLocaleString();

  // Animate the credit card briefly
  creditsEl.style.transition = 'color 0.4s';
  creditsEl.style.color = 'var(--accent)';
  setTimeout(function () { creditsEl.style.color = ''; }, 1800);

  document.getElementById('confirmedName').textContent = name;
  document.getElementById('consentForm').style.display = 'none';
  document.getElementById('consentConfirmed').style.display = 'block';
}

/* FAQ accordion */
function toggleFaq(el) {
  el.parentElement.classList.toggle('open');
}

/* Tab switching — works for any .tab-nav on page */
document.querySelectorAll('.tab-nav, .tab-nav-sm').forEach(function (nav) {
  nav.querySelectorAll('.tab-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      nav.querySelectorAll('.tab-btn').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
    });
  });
});

/* Copy ambassador code */
function copyCode() {
  navigator.clipboard.writeText('HOLLY20').then(function () {
    var btn = document.getElementById('copyBtn');
    btn.textContent = 'Copied!';
    btn.style.borderColor = 'var(--gold)';
    btn.style.color = 'var(--gold-light)';
    setTimeout(function () {
      btn.textContent = 'Copy Code';
      btn.style.borderColor = '';
      btn.style.color = '';
    }, 2500);
  });
}

/* Send referral */
function sendReferral() {
  var inputs = document.querySelectorAll('#refer input, #refer textarea');
  var name  = inputs[0].value.trim();
  var email = inputs[1].value.trim();
  if (!name || !email) {
    alert("Please enter your friend's name and email address.");
    return;
  }
  var btn = document.querySelector('#refer .btn-gold');
  btn.textContent = '✓ Referral Sent!';
  btn.style.background = '#2a7a4a';
  inputs.forEach(function (i) { i.value = ''; i.disabled = true; });
  setTimeout(function () {
    btn.textContent = 'Send Referral Invite';
    btn.style.background = '';
    inputs.forEach(function (i) { i.disabled = false; });
  }, 4000);
}

/* Add another referral row */
function addAnotherReferral() {
  var form = document.querySelector('#refer [style*="grid-template-columns:1fr 1fr"]').parentElement;
  var newRow = document.createElement('div');
  newRow.style.cssText = 'border-top:1px solid rgba(255,255,255,0.08);margin-top:20px;padding-top:20px;';
  newRow.innerHTML = `
    <p style="font-size:9px;letter-spacing:0.18em;text-transform:uppercase;color:var(--gold-light);font-weight:600;margin-bottom:14px;">+ Another Friend</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
      <input type="text" placeholder="Friend's Name" style="width:100%;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);color:white;padding:14px 16px;font-family:'Montserrat',sans-serif;font-size:12px;outline:none;" />
      <input type="email" placeholder="Their Email" style="width:100%;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);color:white;padding:14px 16px;font-family:'Montserrat',sans-serif;font-size:12px;outline:none;" />
    </div>
    <input type="tel" placeholder="Mobile Number (optional)" style="width:100%;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);color:white;padding:14px 16px;font-family:'Montserrat',sans-serif;font-size:12px;outline:none;" />
  `;
  form.insertBefore(newRow, form.querySelector('button[onclick="sendReferral()"]'));
}
