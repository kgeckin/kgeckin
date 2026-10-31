# Profile visual language

## Direction

An interactive editorial portfolio, not a technical résumé.

The first view needs only three things:
1. A clear personal identity and current work.
2. Three actual, clickable public projects.
3. An invitation to explore optional context.

Architecture interests and technical background stay in short, expandable sections.
No giant skills inventory, product matrix, experience chronology, or public counter.

## Visual system

| Element | Treatment |
| --- | --- |
| Canvas | Charcoal and near black |
| Accent | A single warm champagne highlight |
| Type | Oversized names and project titles |
| Illustration | Abstract nodes, architecture diagrams, waveforms and data trajectories |
| Spacing | Calm, generous and editorial |
| Animation | Subtle decoration only, with reduced-motion support |

## Assets

- assets/hero.svg introduces the identity.
- assets/work-inventory.svg links to the public inventory application.
- assets/work-linguax.svg links to the language application prototype.
- assets/work-falcon.svg links to the analytics capstone.
- assets/system-thinking.svg lives inside a collapsed section.
- assets/signature.svg provides a visual ending.

Cards are distinct visuals that link to their actual repository pages.
All visual assets are maintained locally in this repository.

## Interaction

GitHub README supports real clickable links and HTML details / summary disclosure
controls. It does not support arbitrary page-level JavaScript or custom
application-style interactions in README content. Keep interactions native.

## Content principles

- Show working projects before listing technologies.
- Describe current infrastructure delivery accurately and succinctly.
- Treat architecture as an ongoing development direction.
- Keep vendor product names, abbreviations and implementation details out of the first view.
- Never share customer-specific topology, credentials or proprietary work.
- Only showcase links that exist.
- Do not present ideas or prototypes as production deployments.

## Validation

Run python scripts/validate_profile.py in a repository checkout before merging.
The validator checks local image references, alt text and SVG XML structure.
