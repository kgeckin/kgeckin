# Profile visual language

## Direction

The GitHub README and [portfolio website](https://kgeckin.github.io/) share an editorial infrastructure identity. The profile is a compact entry point that directs readers to the standalone website and to a small number of actual public repositories.

## Priority

1. Identify Kardelen Geçkin and her current infrastructure engineering role.
2. Feature StorageOps Lab as a working observability project, accurately distinguishing simulation and voluntary host monitoring.
3. Show public LinguaX, Inventory Portal and Falcon 9 analysis without unverified production claims.
4. Offer an expandable systems engineering perspective and scientific background.
5. Direct visitors to the larger portfolio for additional experiments.

## Visual system

| Element | Treatment |
| --- | --- |
| Background | Deep charcoal and low saturation blue black |
| Accent | Restrained champagne gold with teal infrastructure signals |
| Typography | Large editorial headings and clear secondary captions |
| Images | Lightweight, self contained SVG artwork maintained in the repository |
| Layout | One full width hero and a curated sequence of clickable project covers |
| Motion | Static by default, no external widget counters or activity farming |

The profile and portfolio use original graphics, with consistent visual language but different layouts optimized for their platforms.

## Assets

* `assets/hero.svg`: name, current identity and infrastructure visualization.
* `assets/work-storageops.svg`: featured observability project.
* `assets/work-linguax.svg`: language application prototype.
* `assets/work-inventory.svg`: asset administration prototype.
* `assets/work-falcon.svg`: data science capstone.
* `assets/system-thinking.svg`: infrastructure delivery lifecycle.
* `assets/signature.svg`: close and link to the portfolio.

## Privacy and provenance

* Only link to confirmed public projects.
* No corporate server hostnames, customer names, topology identifiers, credentials, licenses or internal costs.
* No credential capture tools or private security-awareness repositories in the public project gallery.
* A project can be showcased without releasing proprietary materials, using a separately designed fictional demonstration with a clean Git history and approved ownership.
* Do not treat the StorageOps simulator's measurements as production device telemetry.
* Never use fictional screenshot data as an actual monitoring observation.

## Validation

Run `python scripts/validate_profile.py` before merging and inspect the actual GitHub-rendered profile README. GitHub markdown permits links and native expandable details but does not support arbitrary running front-end JavaScript. All dynamic interactions belong on the GitHub Pages site.
