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
│   └── robots.txt          # Search engine directives
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

## License

All rights reserved. Copyright 2026 Stuzzicadenti AG.
