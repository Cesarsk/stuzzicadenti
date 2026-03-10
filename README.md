# Stuzzicadenti

The World of Toothpicks — explore types, history, and cultural traditions.

## Overview

Stuzzicadenti is an interactive showcase website exploring the fascinating world of toothpicks — from ancient Roman gold picks to modern cocktail culture. Features a gallery of 6 toothpick types with flip-card animations, an illustrated timeline spanning 1.8 million years, and fun facts.

## Features

- **Gallery** — 6 toothpick types (Classic, Flat Paddle, Cocktail, Tsumayoji, Flavored, Luxury Metal) with flip-card reveal
- **Timeline** — Historical journey from prehistoric origins to modern revival
- **Fun Facts** — Key statistics ($1B+ market, 20B consumed/year in US)
- **Animations** — CSS flip cards, scroll-reveal, hover effects (respects `prefers-reduced-motion`)
- **SEO** — Open Graph, Twitter Cards, JSON-LD, canonical, robots.txt

## Tech Stack

- HTML5 + CSS3 (vanilla, no frameworks)
- BEM methodology for CSS architecture
- IntersectionObserver for scroll animations
- GitHub Pages (static hosting)
- GitHub Actions CI/CD

## Architecture

```
stuzzicadenti/
├── src/
│   ├── index.html          # Main page
│   ├── css/
│   │   └── style.css       # Styles (BEM)
│   ├── js/
│   │   └── main.js         # Extracted scripts (CSP compliant)
│   ├── robots.txt          # Search engine directives
│   └── sitemap.xml         # Sitemap for SEO
├── .github/
│   └── workflows/
│       ├── deploy.yml       # GitHub Pages deployment
│       └── lint.yml         # HTML validation + secret detection
├── .kiki/
│   └── auto-jira.yaml      # Kiki automation config
├── .gitignore
└── README.md
```

## Deployment

| Branch | Environment | URL |
|--------|------------|-----|
| `dev` | Preview | Auto-deployed on push |
| `main` | Production | [stuzzicadenti-ag.github.io/stuzzicadenti](https://stuzzicadenti-ag.github.io/stuzzicadenti/) |

## Development

```bash
git clone https://github.com/stuzzicadenti-ag/stuzzicadenti.git
cd stuzzicadenti
open src/index.html
```

## Security & Accessibility

- **CSP meta tag**: Content Security Policy to restrict script/style sources
- **Inline JS extracted**: Moved inline scripts to `src/js/main.js` (CSP compliant)
- **Noscript fallback**: Graceful degradation message when JavaScript is disabled
- **og:image meta tag**: Open Graph image for social media previews
- **sitemap.xml**: Added for search engine discoverability
- **Lint workflow fixed**: Updated GitHub Actions lint CI
- **Mobile tap handler**: Touch support for flip-card interactions on mobile
- **Hero button contrast**: Improved color contrast on hero CTA button
- **Dead CSS removed**: Cleaned up unused CSS rules
- **Label eligibility fix**: Corrected bug in toothpick label display logic

## License

All rights reserved. Copyright 2026 Stuzzicadenti AG.
