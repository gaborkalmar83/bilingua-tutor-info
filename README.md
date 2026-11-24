# Bilingua Tutor - info site

Static site for https://tutor.kalmarium.com (GitHub Pages, custom domain). Home page with screenshots, closed-test sign-up page, privacy policy. Kept separate from the private app repo on purpose, like the other `*-info` repos.

## Files

- `build.py` - generates `index.html`, `testing.html`, `privacy-policy.html`, `sitemap.xml`, `robots.txt`, `CNAME`, `.nojekyll`. Copy lives in the script.
- `privacy-policy.md` - the policy text (same text as `store/privacy-policy.md` in the app repo). Edit it, then rebuild.
- `make_images.py` - builds `img/` (icons, 540x960 screenshots, Open Graph image) from `raw/` (gitignored 1080x1920 PNGs).
- `style.css` - Canal palette (Daylight and Midnight Canal), no purple.

## Publish

1. Push this repo to GitHub as `gaborkalmar83/bilingua-tutor-info`, enable Pages from the `main` branch root.
2. Set the custom domain `tutor.kalmarium.com` (the `CNAME` file does this) and add a CNAME record `tutor` -> `gaborkalmar83.github.io` in Wix DNS.
3. Check https://tutor.kalmarium.com/privacy-policy.html loads over HTTPS. The app and the Play listing point at it.

## When the app is live on Google Play

```
python build.py --live
```

swaps the closed-test button for the Google Play badge (referrer-tagged link). Commit and push.

## Rules for the copy

Say only what the code does. No "nothing leaves your phone" without "with the on-device model". Lucy is always called an AI. No exam claims. Plain hyphens, no purple.
