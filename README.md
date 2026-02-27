# Yang's Blog

A personal blog built with [Hugo](https://gohugo.io/) and the [Blowfish](https://blowfish.page/) theme. Hosted on GitHub Pages at [zexergy.com](https://zexergy.com).

## Content Sections

- **Blog** — Technical articles on Python, Linux, Docker, and data science
- **Battery** — Daily battery running status summaries
- **Market** — Energy market analysis and insights

## Local Development

```bash
# Install Hugo (Windows)
winget install Hugo.Hugo.Extended

# Start dev server
hugo server -D

# Build for production
hugo --gc --minify
```

## Creating New Posts

```bash
# New blog post
hugo new content blog/my-new-post/index.md

# New battery report (automated)
python scripts/generate_battery_report.py

# New market analysis
hugo new content market/my-analysis/index.md
```

## Deployment

Automated via GitHub Actions on push to `main`. See `.github/workflows/hugo.yml`.
