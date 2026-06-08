# Editing the Verve VIP Rewards site with Claude Code

A plain-English guide to changing this website yourself — **no terminal, no
coding, no installing anything.** You do it all in your web browser (or even on
your phone) by chatting with Claude in normal English.

> **Two short parts:**
> **Part A** is a one-time setup for *Tineke* (your developer).
> **Part B onward** is for *you* (the owner) — that's the part to follow day-to-day.

---

## A few words first (what these terms mean)

You'll see a handful of words. Here's all you need to know:

- **Repository (or "repo")** — just the folder that holds all the website's files. Ours is called **`verve-vip-portal`**.
- **Branch** — a safe working copy. Changes on a branch do **not** affect the live website until they're approved.
- **Pull Request (PR)** — a tidy "please save these changes into the real website" request. You click a button; Claude writes it for you.
- **Merge** — clicking **approve** on that request. *This* is the moment your change becomes part of the website.

**The golden rule: nothing you do touches the live website until you click _Merge_.** So you genuinely cannot break anything by experimenting. 🙂

---

## Part A — One-time setup (Tineke does this once, ~10 minutes)

**1. Invite the owner to the GitHub repository**
   - Go to `https://github.com/BrightDigitalNZ/verve-vip-portal`
   - Click **Settings** (top menu) → **Collaborators** (left menu) → **Add people**
   - Type the owner's **GitHub username or email** → send the invite.
   - *(If she doesn't have a GitHub account yet, she creates a free one at [github.com/signup](https://github.com/signup) first, then you invite that username.)*

**2. Turn on the live preview site (so she can see her changes)**
   - In the repo: **Settings → Pages → Build and deployment → Source → "Deploy from a branch"**
   - Branch: `claude/cool-hopper-pjYYA`, folder **`/ (root)`** → **Save**
   - After ~1 minute the site is live at: **https://brightdigitalnz.github.io/verve-vip-portal/**

**3. Send the owner these four things:**
   - The repo name: **`verve-vip-portal`**
   - The branch to work from (for now: **`claude/cool-hopper-pjYYA`**)
   - The live site link: **https://brightdigitalnz.github.io/verve-vip-portal/**
   - A link to this guide.

> 💡 *Optional tidy-up:* the working branch has a long auto-generated name. If you
> rename the default branch to `main` (Settings → Branches), the instructions
> below get even simpler. Ask Claude to help if you'd like.

---

## Part B — One-time setup (the owner does this once, ~10 minutes, all in the browser)

**1. Get a Claude plan that includes Claude Code.**
   - Go to [claude.ai](https://claude.ai) and sign up / sign in.
   - You'll need a **paid plan — Pro, Max, or Team** (Claude Code on the web isn't on the free plan). Pro is the usual starting point.

**2. Accept the GitHub invitation.**
   - Check your email for an invite from GitHub to `BrightDigitalNZ/verve-vip-portal` and click **Accept**. (Or accept it at [github.com/notifications](https://github.com/notifications).)

**3. Open Claude Code on the web.**
   - Go to **[claude.ai/code](https://claude.ai/code)** and sign in with the same Claude account.

**4. Connect GitHub (a button will prompt you).**
   - Claude will ask to connect GitHub. Click through to **install the Claude GitHub App** and **allow access** to your repositories. Choose to give it access to the Verve repo (or "all repositories" — either is fine).

**5. Create your environment.**
   - You'll be asked to create a "cloud environment." **Just leave everything on the defaults and click `Create environment`.** You never have to touch this again.

✅ That's the setup done. From now on it's just steps in Part C.

---

## Part C — How to make a change (your everyday routine)

Everything here is clicking and typing plain English. No code.

**1. Go to [claude.ai/code](https://claude.ai/code).**

**2. Choose the website to work on.**
   - Just below the message box there's a **repository selector** — click it and pick **`verve-vip-portal`**.
   - Next to it is a **branch** selector. Make sure it shows **`claude/cool-hopper-pjYYA`** (or `main` if Tineke renamed it).

**3. (Optional) Pick how hands-on you want to be.**
   - The mode dropdown defaults to **Auto accept edits** — Claude makes the change and shows you the result. This is safe (remember: nothing is live until you merge).
   - Prefer to approve the plan *before* Claude edits anything? Switch it to **Plan mode** and Claude will describe what it intends to do first.

**4. Type what you want, in normal English, then press Enter.**
   Be specific — say *what* and *where*. Some real examples for this site:
   - `On the homepage, change the hero line "Earn credits every time you visit us..." to "Earn rewards every time you visit or share."`
   - `In the "How to earn credits" section, change the Instagram reward from $20 to $25.`
   - `Update the FAQ answer about referrals so it says $150, not $200.`
   - `Swap the booking button link to https://www.verveintimate.com.au/new-booking-page`
   - `Add a new FAQ: "Can I gift my credits to a friend?" with the answer "Credits are linked to your account and can't be transferred, but you can refer a friend for $150."`

   👉 *Tip: the more specific you are (the exact words, the exact section), the better the result.* You can also paste a screenshot.

**5. Let Claude work.**
   - It thinks and edits for a minute or two. You can **close the tab or switch to your phone** — it keeps going and saves your place.

**6. Look at what changed.**
   - You'll see a little **`+12 −3`** indicator (lines added/removed). Click it to see the changes laid out. Don't worry about reading code — focus on whether the wording/values look right.

**7. Want a tweak? Just say so.**
   - Type another message like `Actually, make that wording warmer` or `Change $25 back to $20`, and press Enter. Repeat as much as you like.

**8. Save it into the website.**
   - When you're happy, click **`Create PR`** at the top of the changes view (choose the normal/full PR option).
   - That opens the request on GitHub. Click the green **`Merge pull request`** button, then **`Confirm merge`**.

**9. See it live.**
   - Wait about a minute, then open **https://brightdigitalnz.github.io/verve-vip-portal/** and refresh. Your change is there. 🎉

---

## A few reassurances & tips

- **You can't break the live site by experimenting.** Changes only go live at the **Merge** step. If you never merge, nothing happens.
- **Not sure how to phrase something?** Ask Claude directly in the chat: `How do I change the colours?` or `Where is the referral reward set?` — it knows this project.
- **Made a mistake after merging?** Just start a new task and say `Undo the last change` or `Put the Instagram reward back to $20`. Tineke can also revert anything instantly.
- **On the go?** Install the **Claude** app (iPhone or Android), open the **Code** tab, and do all of the above from your phone.
- **Replacing photos** (the logo or images): that's the one thing best handed to Tineke, since it means uploading image files. You can still *ask* for it in a task and Claude will tell you exactly what file it needs.

---

## (Optional, advanced) Doing this on your own computer

There's also a version of Claude Code that runs on your own computer using the
"terminal" (a typing-based program). **You do not need this** — the web version
above does everything. Only explore it if you become curious; ask Tineke, or see
Anthropic's guide at [code.claude.com/docs](https://code.claude.com/docs/en/quickstart).

---

*Questions about the site itself (rewards, tiers, forms) are covered in
`README.md` and `HANDOFF.md` in this same repository.*
