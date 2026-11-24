"""Builds the Bilingua Tutor info site (static HTML for GitHub Pages).

    python build.py                 # pre-release: closed-test sign-up call to action
    python build.py --live          # after the Play listing is live: Google Play badge
    python build.py --privacy path\\to\\policy.md   # use another policy source

Edit copy here, then rebuild. Output is written next to this file.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = "--live" in sys.argv
PRIVACY_MD = os.path.join(HERE, "privacy-policy.md")
if "--privacy" in sys.argv:
    PRIVACY_MD = sys.argv[sys.argv.index("--privacy") + 1]

SITE = "https://tutor.kalmarium.com"
NAME = "Bilingua Tutor"
EMAIL = "kalmariumservices@gmail.com"
PKG = "com.bilingua.tutor"
PLAY = "https://play.google.com/store/apps/details?id=%s&referrer=utm_source%%3Dwebsite%%26utm_medium%%3Dhero" % PKG
TODAY = "2026-11-24"
DESC = ("An AI language tutor that explains why. A hand-written grammar map for Dutch, German, Finnish, "
        "Hungarian and English, plus Lucy, a tutor who corrects one thing at a time. Runs on your phone or with "
        "your own AI provider. No account, no ads.")

MAILTO_TEST = ("mailto:%s?subject=%s&body=%s" % (
    EMAIL,
    "Bilingua%20Tutor%20closed%20test%20sign-up",
    "Hi%2C%20I%20would%20like%20to%20test%20Bilingua%20Tutor.%0D%0A%0D%0A"
    "Google%20account%20email%20I%20use%20in%20the%20Play%20Store%20on%20my%20phone%3A%20%0D%0A"
    "Phone%20model%20and%20Android%20version%3A%20%0D%0A"
    "Language%20I%20am%20learning%3A%20%0D%0A%0D%0A"
    "I%20will%20keep%20the%20app%20installed%20for%20at%20least%2014%20days.%0D%0A"))

BADGE = """<a class="badge" href="%s" aria-label="Get it on Google Play" rel="noopener">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 56" aria-hidden="true" focusable="false">
    <rect x="1" y="1" width="198" height="54" rx="9" fill="#000" stroke="#a6a6a6" stroke-width="1.5"/>
    <g transform="translate(14 6)">
      <polygon points="2,2 24,22 2,42" fill="#00c4f5"/>
      <polygon points="2,2 32,18.7 24,22" fill="#00e676"/>
      <polygon points="24,22 32,18.7 38,22 32,25.3" fill="#ffd400"/>
      <polygon points="2,42 24,22 32,25.3" fill="#ff3d4a"/>
    </g>
    <text x="62" y="21" fill="#fff" font-family="system-ui, Arial, sans-serif" font-size="11" textLength="62" lengthAdjust="spacingAndGlyphs">GET IT ON</text>
    <text x="62" y="43" fill="#fff" font-family="system-ui, Arial, sans-serif" font-size="24" font-weight="600" textLength="128" lengthAdjust="spacingAndGlyphs">Google Play</text>
  </svg>
</a>""" % html.escape(PLAY)

if LIVE:
    CTA_PRIMARY = BADGE + '\n        <p class="price-note"><strong>Free to try for 14 days</strong>, then a one-time unlock. No subscription, no ads.</p>'
else:
    CTA_PRIMARY = ('<a class="btn" href="/testing.html">Join the closed test</a>\n'
                   '        <p class="price-note"><strong>Coming to Google Play.</strong> Help test the first release and keep the unlock free.</p>')

FAQ = [
    ("Is Bilingua Tutor free?",
     "It is free to download. The grammar map and your reviews stay free with no time limit. The AI features (Lucy, the Sentence Lab, the Reader's AI help and voice mode) are free for 14 days from first launch, then you unlock them once with a single payment through Google Play. There is no subscription. The price is shown in Google Play for your country. If you connect a cloud AI provider with your own key, that provider bills you for what you use; the on-device model costs nothing to run."),
    ("Do I need an account?",
     "No. There is nothing to sign up for, and the developer runs no server that receives your words, chats, voice, progress or API keys."),
    ("Where does my text and voice go?",
     "With the on-device model, nowhere: it stays on your phone. If you choose a cloud provider (OpenAI, Anthropic, Google Gemini, OpenRouter, Azure or your own Ollama or LM Studio server), what you write goes straight from your phone to that provider, using your own key, under that provider's terms. Voice mode can use your phone's speech recognition, or a realtime voice provider you configure; in that case microphone audio goes to that provider, and the app asks you to confirm before it is used the first time. Android's own backup can include app data if you have it switched on."),
    ("Which languages does it cover?",
     "The grammar map has 343 hand-written rules for Dutch, German, Finnish, Hungarian and English. Lucy and the Sentence Lab work in 18 languages, rules are explained in 13 languages, and the app itself comes in 14 languages."),
    ("Is Lucy a real teacher?",
     "No. Lucy is an AI model and can be wrong. Her answers are labelled as AI-generated, every correction points at a rule you can read yourself, and you can report an answer from inside the app."),
    ("What do I need for the on-device model?",
     "A recent arm64 phone with about 6 GB of RAM and Wi-Fi for a one-time download of about 2.6 GB. It is slower and less accurate than the large cloud models. The grammar map and reviews work without it."),
    ("Does it show ads or track me?",
     "No ads and no account. The developer adds no analytics or tracking software. Libraries from Google that handle purchases can send Google their own technical diagnostics; the privacy policy names them. This website counts page views with a cookie-free script."),
    ("Is there an iPhone version?", "Not yet. Bilingua Tutor is an Android app."),
    ("How is it different from Bilingua Reader?",
     "Bilingua Reader is a separate app from the same developer for reading EPUB and PDF books with a translation under each sentence. Bilingua Tutor is for studying grammar and practising with an AI tutor."),
]

FEATURES = [
    ("A grammar map that explains itself",
     "343 hand-written rules for Dutch, German, Finnish, Hungarian and English, from A1 to C1. Each rule comes with the reason it exists, example sentences colour-coded by word role and read aloud on tap, and its exceptions. It works offline and needs no AI."),
    ("Sentence Lab",
     "Write or say a sentence and get a verdict, the corrected version, every word coloured by its role, and the rules you applied or broke. Tap a rule for the full explanation or a drill."),
    ("Lucy, a tutor who talks back",
     "Chat in the language you are learning, at your level, with a translation under every line. Lucy corrects one mistake per turn, with the rule and the reason, and offers sixteen one-tap actions such as simpler, harder, conjugate, roleplay and fill the gaps. She is an AI and can be wrong."),
    ("Reviews that build themselves",
     "Saved words, sentences and Lucy's corrections become flashcards on their own, scheduled with spaced repetition and a daily reminder. Prefer AnkiDroid? Send the cards there instead."),
    ("Read what you want to read",
     "Share an article from your browser or paste text, then read it sentence by sentence with translations and word roles, and send any sentence to the Lab or to Lucy."),
    ("Your AI, your choice",
     "Run Gemma on your phone, or connect OpenAI, Anthropic, Google Gemini, OpenRouter, Azure or your own Ollama or LM Studio server with your own key. Keys are encrypted with the Android Keystore."),
]

SHOTS = [
    ("shot-map.jpg", "The grammar map with Dutch rules grouped by topic and level", "The grammar map"),
    ("shot-rule.jpg", "A rule page with the reason the rule exists and colour-coded examples", "Why the rule exists"),
    ("shot-lucy.jpg", "Lucy correcting a Dutch sentence and linking the grammar rule", "One correction at a time"),
    ("shot-review.jpg", "A flashcard created from a correction", "Reviews that build themselves"),
    ("shot-ai.jpg", "The AI provider screen with the on-device model selected", "Your AI, your choice"),
    ("shot-light.jpg", "The same app in the light Daylight theme", "Light and dark themes"),
]

MORE = [
    ("https://bilingua.kalmarium.com", "Bilingua Reader - bilingual EPUB and PDF reader"),
    ("https://knowdrop.kalmarium.com", "Knowdrop - daily trivia quiz"),
    ("https://lingua.kalmarium.com", "Lingua Pairs - translation memory game"),
    ("https://netcheck.kalmarium.com", "Ultimate Network Troubleshooter - Wi-Fi and network analyzer"),
    ("https://prep4cert.kalmarium.com", "Prep 4 Cert - certification exam practice"),
    ("https://tankageddon.kalmarium.com", "Tankageddon - tank battle game"),
    ("https://crackafold.kalmarium.com", "Crack A Fold - foldable phone crack prank"),
]


def e(s):
    return html.escape(s, quote=True)


def head(title, desc, path, extra=""):
    url = SITE + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0a1419">
<link rel="icon" type="image/png" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta property="og:site_name" content="{NAME}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Bilingua Tutor: grammar map and AI tutor on a phone">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/img/og-image.jpg">
<link rel="stylesheet" href="/style.css">
{extra}<script defer src="https://overwatch.kalmarium.com/h.js" data-app="bilingua-tutor"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <div class="wrap">
    <a class="brand" href="/"><img src="/img/icon-192.png" width="40" height="40" alt="{NAME} app icon">{NAME}</a>
    <nav aria-label="Main">
      <a href="/#features">Features</a>
      <a href="/#screens">Screenshots</a>
      <a href="/#faq">FAQ</a>
      <a href="/testing.html">Join the test</a>
      <a href="/privacy-policy.html">Privacy</a>
    </nav>
  </div>
</header>
"""


def foot():
    more = "\n".join(f'      <li><a href="{u}">{e(t)}</a></li>' for u, t in MORE)
    return f"""<footer class="site">
  <div class="wrap">
    <h2>More from Kalmarium Services</h2>
    <ul class="more">
{more}
    </ul>
    <p class="legal"><a href="/privacy-policy.html">Privacy policy</a> <a href="/testing.html">Join the closed test</a> <a href="mailto:{EMAIL}">{EMAIL}</a> <a href="https://kalmarium.com">kalmarium.com</a></p>
    <p>{NAME} is made by Kalmarium Services. Gemma is a trademark of Google LLC. Google Play is a trademark of Google LLC. Not affiliated with any exam body.</p>
  </div>
</footer>
</body>
</html>
"""


def jsonld_app():
    install = f'  "installUrl": "{PLAY}",\n' if LIVE else ""
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "MobileApplication",
  "name": "{NAME}",
  "operatingSystem": "Android",
  "applicationCategory": "EducationalApplication",
  "description": "{e(DESC)}",
  "url": "{SITE}/",
{install}  "image": "{SITE}/img/og-image.jpg",
  "inLanguage": "en",
  "offers": {{"@type": "Offer", "price": "0", "priceCurrency": "EUR", "availability": "https://schema.org/InStock"}},
  "publisher": {{"@type": "Organization", "name": "Kalmarium Services", "url": "https://kalmarium.com"}}
}}
</script>
"""


def jsonld_faq():
    import json
    data = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2, ensure_ascii=False) + "\n</script>\n"


def index():
    feats = "\n".join(f'      <article class="card"><h3>{e(t)}</h3><p>{e(p)}</p></article>' for t, p in FEATURES)
    shots = "\n".join(
        f'      <figure><img src="/img/{f}" width="540" height="960" loading="lazy" alt="{e(alt)}"><figcaption>{e(cap)}</figcaption></figure>'
        for f, alt, cap in SHOTS)
    faq = "\n".join(f"      <details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    title = "Bilingua Tutor: AI Language Tutor with a Grammar Map"
    body = f"""<main id="main">
  <div class="wrap hero">
    <div>
      <h1>An AI language tutor that explains <em>why</em>, not just what</h1>
      <p class="lead">Bilingua Tutor pairs a hand-written grammar map with Lucy, an AI tutor who corrects one thing at a time. It runs on your phone or with the AI provider you choose. No account, no ads.</p>
      <div class="cta">
        {CTA_PRIMARY}
      </div>
      <ul class="pills">
        <li>343 grammar rules</li>
        <li>Dutch, German, Finnish, Hungarian, English</li>
        <li>On-device AI</li>
        <li>No account</li>
      </ul>
    </div>
    <div class="hero-shot">
      <div class="phone"><img src="/img/shot-rule.jpg" width="540" height="960" alt="A grammar rule page: why Dutch has de and het, with colour-coded examples"></div>
    </div>
  </div>

  <section id="features">
    <div class="wrap">
      <h2>What it does</h2>
      <p class="sub">A tutor for people who want to understand the language, not just tap through it.</p>
      <div class="features">
{feats}
      </div>
    </div>
  </section>

  <section id="screens" class="band">
    <div class="wrap">
      <h2>See it in use</h2>
      <p class="sub">Screenshots from the app on an Android phone.</p>
      <div class="shots">
{shots}
      </div>
    </div>
  </section>

  <section id="good-to-know">
    <div class="wrap">
      <h2>Good to know</h2>
      <div class="two">
        <article class="card">
          <h3>Private by design, with honest limits</h3>
          <p>No account and no server run by the developer. With the on-device model your text stays on your phone. If you pick a cloud provider, your text or voice goes to that provider with your own key, and the app tells you so first. Details are in the <a href="/privacy-policy.html">privacy policy</a>.</p>
        </article>
        <article class="card">
          <h3>Fair pricing</h3>
          <p>The grammar map and your reviews are free for good. The AI features are free for 14 days, then a single one-time unlock. No subscription. Cloud AI providers you connect bill you directly for usage.</p>
        </article>
      </div>
    </div>
  </section>

  <section id="faq" class="band">
    <div class="wrap">
      <h2>Questions and answers</h2>
      <p class="sub">Short answers about price, privacy and what the app can do.</p>
{faq}
    </div>
  </section>

  <section id="get">
    <div class="wrap">
      <h2>Help test the first release</h2>
      <p class="sub">Bilingua Tutor is heading to Google Play. Google asks new apps to run a closed test first, so testers are very welcome.</p>
      <div class="cta">
        <a class="btn" href="/testing.html">Join the closed test</a>
        <p class="price-note">Questions or feedback? <a href="mailto:{EMAIL}">{EMAIL}</a> - read the <a href="/privacy-policy.html">privacy policy</a>.</p>
      </div>
    </div>
  </section>
</main>
"""
    return head(title, DESC, "/", jsonld_app() + jsonld_faq()) + body + foot()


def testing():
    title = "Join the Bilingua Tutor closed test"
    desc = "Help test Bilingua Tutor before its Google Play release. Email us the Google account you use on your phone and keep the app installed for 14 days."
    body = f"""<main id="main" class="wrap doc">
<h1>Join the Bilingua Tutor closed test</h1>
<p><em class="updated">Last updated: {TODAY}</em></p>
<p>Bilingua Tutor is an AI language tutor with a hand-written grammar map for Dutch, German, Finnish, Hungarian and English. Before it goes live on Google Play, Google requires a closed test with real people on real phones. You would be one of them.</p>
<p><a class="btn" href="{e(MAILTO_TEST)}">Email us to sign up</a></p>
<p class="note">The button opens your email app with a short message to fill in. We reply with the invite and the opt-in link. Spaces are limited and invites go out in the order we get them.</p>

<h2>What we ask of you</h2>
<ol class="steps">
<li><strong>Email us</strong> the Google account (Gmail address) you use in the Play Store on your Android phone, your phone model and Android version, and the language you are learning.</li>
<li><strong>Join the test group</strong> from the invite we send you, using that same Google account.</li>
<li><strong>Open the opt-in link</strong> from the invite and tap "Become a tester".</li>
<li><strong>Install the app from Google Play</strong> using the link on that page.</li>
<li><strong>Keep it installed and stay opted in for at least 14 days</strong>, and open it a few times. Google counts this, so please do not uninstall early.</li>
<li><strong>Tell us what you find</strong>: through the feedback option on the Play test page, or by email to <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ol>

<h2>Good to know before you join</h2>
<ul>
<li>You need an Android phone (Android 8 or newer) and a Google account. There is no iPhone version.</li>
<li>The grammar map and reviews work straight away. The AI tutor can run on your phone with a one-time download of about 2.6 GB over Wi-Fi, which needs a recent arm64 phone with about 6 GB of RAM. Or you can connect an AI provider with your own key.</li>
<li>Lucy is an AI and can be wrong. Her answers are labelled, and you can report an answer inside the app.</li>
<li>Testers get the AI unlock for free. During the test you will not be charged.</li>
<li>If you use a cloud AI provider with your own key, that provider bills you for usage. The on-device model costs nothing.</li>
</ul>

<h2>What happens to your email</h2>
<p>We use the address you send only to add you to the test and to write to you about it. It is not shared with anyone else, and we delete it after the test ends. Google receives your Google account address as part of running the closed test, under Google's own privacy policy. See our <a href="/privacy-policy.html">privacy policy</a> for how the app itself handles data.</p>
<p>Questions? <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</main>
"""
    return head(title, desc, "/testing.html") + body + foot()


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])_([^_]+)_(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: '<a href="%s">%s</a>' % (m.group(2).replace('"', "%22"), m.group(1)), s)
    s = re.sub(r"(?<![\"'>=/])(https?://[^\s<)]+[^\s<).,;])", r'<a href="\1">\1</a>', s)
    s = re.sub(r"(?<![\w>\"=:/])([\w.+-]+@[\w-]+\.[\w.-]+)", r'<a href="mailto:\1">\1</a>', s)
    return s


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", s).lower()).strip("-")


def md_to_html(md):
    lines = md.splitlines()
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)", ln)
        if m:
            lvl = len(m.group(1))
            txt = inline(m.group(2))
            out.append("<h%d id=\"%s\">%s</h%d>" % (lvl, slug(txt), txt, lvl))
            i += 1
            continue
        if ln.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i])
                i += 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            cells = [r for r in cells if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
            t = ["<div class=\"table-wrap\"><table>"]
            for n, r in enumerate(cells):
                tag = "th" if n == 0 else "td"
                t.append("<tr>" + "".join("<%s>%s</%s>" % (tag, inline(c), tag) for c in r) + "</tr>")
            t.append("</table></div>")
            out.append("\n".join(t))
            continue
        if re.match(r"^\s*[-*]\s+", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            out.append("<ul>\n" + "\n".join("<li>%s</li>" % inline(x) for x in items) + "\n</ul>")
            continue
        if re.match(r"^\s*\d+[.)]\s+", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+[.)]\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+[.)]\s+", "", lines[i]))
                i += 1
            out.append("<ol>\n" + "\n".join("<li>%s</li>" % inline(x) for x in items) + "\n</ol>")
            continue
        para = [ln.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,3}\s|\s*[-*]\s|\s*\d+[.)]\s|\s*\|)", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))
    return "\n".join(out)


def privacy():
    if not os.path.exists(PRIVACY_MD):
        return None
    md = open(PRIVACY_MD, encoding="utf-8").read()
    body = md_to_html(md)
    title = "Privacy Policy - Bilingua Tutor"
    desc = ("Privacy policy for Bilingua Tutor: no account, no ads, no developer server, AI on your phone by default, "
            "and exactly which optional services receive text or voice.")
    return head(title, desc, "/privacy-policy.html") + '<main id="main" class="wrap doc">\n' + body + "\n</main>\n" + foot()


def write(name, content):
    if content is None:
        print("skipped", name)
        return
    with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", name, len(content))


if __name__ == "__main__":
    write("index.html", index())
    write("testing.html", testing())
    write("privacy-policy.html", privacy())
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    urls = ["/", "/testing.html", "/privacy-policy.html"]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join("  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n  </url>\n" % (SITE, u, TODAY) for u in urls)
          + "</urlset>\n")
    write("CNAME", "tutor.kalmarium.com\n")
    write(".nojekyll", "")
