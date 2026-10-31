# Profile design system

## Direction

Premium Minimal is a calm, editorial expression of an infrastructure engineering portfolio and a developing architectural perspective.
The design is intentionally restrained: typography, generous spacing, hairline
rules and a single warm accent take priority over glow effects or visual noise.

## Palette

| Token | Value | Usage |
| --- | --- | --- |
| Background | `#0B0D12` | Main hero canvas |
| Surface | `#10141A` | Supporting strip |
| Text | `#F5F3EE` | Main typography |
| Secondary | `#A8ACB5` | Small labels |
| Accent | `#D6BA86` | Minimal champagne highlighting |
| Border | `#AFA38E` | Low-opacity separators |

## Assets

- `assets/hero.svg` is the first impression and should remain legible at narrower widths.
- `assets/telemetry.svg` summarizes four areas without making unverified claims.
- `assets/signature.svg` provides a distinct visual ending.
- `assets/system-thinking.svg` illustrates the integrated infrastructure lifecycle without depicting any confidential architecture.
- SVGs are self-contained and avoid external font or image dependencies.
- Subtle animation is decorative only, with reduced-motion support.

## Content rules

1. Center the narrative on real infrastructure delivery and system integration. Treat storage, virtualization, networking, Linux, cloud and security as connected parts of infrastructure, not separate competing identities.
2. Make a clear distinction between current role, prior work, and developing architecture interests.
3. Link only to public projects that actually exist.
4. Do not publish enterprise data, confidential technical details, credentials or proprietary source.
5. Keep descriptions focused on capabilities and the concrete artifact, rather than buzzwords.
6. Avoid external statistics panels in the main composition because they can fail or distract.

## Validation

Run `python scripts/validate_profile.py` before proposing a change.
Automated CI can be enabled after GitHub Actions runners are available for the repository.
The validator checks SVG XML integrity, accessibility labels and local image references.

## GitHub rendering

GitHub sanitizes README HTML and does not permit custom page-level CSS or JavaScript.
The layout therefore uses compatible Markdown/HTML tables and linked static SVG assets.
