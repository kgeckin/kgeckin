# KG Repository System

A consistent visual and documentation standard for software, infrastructure, security, AI and academic repositories.

## The principle

Every repository should feel like part of the same portfolio, while explaining its actual contents accurately. The first screen should answer **what it is**, **what it does**, and **where to start**. Technical documentation stays below the introduction.

The GitHub profile is the portfolio entrance. Each repository is an individual case study.

## Visual identity

| Token | Value |
| --- | --- |
| Background | `#0C1015` |
| Surface | `#151B22` |
| Main text | `#F4F1E9` |
| Secondary | `#A7A9AD` |
| Accent | `#D6BB8B` |
| Separator | `#3B4047` |

Use the same self-contained SVG header in each repository, with a project-specific title and subtitle. No rainbow badges, readme-stat cards or unrelated animated images. Use actual screenshots and architecture diagrams when they clarify a working project.

The header lives at `docs/assets/cover.svg` for ordinary repositories and `Capstone/assets/cover.svg` for LinguaX. Prefer relative paths so branches render correctly.

## Shared README order

1. **Cover and one-sentence summary.** One short explanation and up to three useful links.
2. **Overview.** The problem and the artifact, not a personal biography.
3. **What it includes.** Three to five concrete features or repository contents.
4. **Getting started.** Real, verified prerequisites and commands. For a non-runnable archive, use *Explore the materials* instead.
5. **Repository structure.** A short and accurate directory map.
6. **Validation.** Tests and their exact commands, or honestly state that they are unavailable.
7. **Architecture & decisions.** A short high-level explanation with a link to deeper documentation if appropriate.
8. **Security & limitations.** What is safe to run or share, data handling and known constraints.
9. **License.** Reference the actual license file and intellectual-property boundaries.

## Variants

| Repository type | README differences |
| --- | --- |
| Runnable application | Include setup, configuration, execution, tests and screenshots if available |
| Infrastructure or security lab | Include scope, synthetic environment, threat model, diagrams, safety and validation |
| Data science project | Include dataset provenance, method, reproducibility, evaluation and limitations |
| Coursework / archive | Use a shorter contents index, environment notes and learning outcomes |
| Portfolio/profile | Use a distinct visual-first landing page, with very little technical detail |
| Confidential/private client work | Keep proprietary data and brand identities out of publicly released derivatives |

Do not add setup commands unless code actually supports them. Do not invent metrics, test success, production deployments, certifications or integrations.

## Engineering repository conventions

```text
repo/
├── README.md
├── LICENSE                  # only if licensing rights are clear
├── .gitignore
├── .editorconfig            # when useful
├── docs/
│   ├── assets/
│   │   └── cover.svg
│   └── ARCHITECTURE.md      # substantive projects only
├── src/                     # application source when appropriate
├── tests/                   # executable, isolated tests
└── requirements.txt         # or ecosystem equivalent
```

Existing repositories may retain historically meaningful course folders. Refactoring folder names is not a prerequisite for uniform documentation.

## Definition of done

Before a README is considered standardized:

* Project name, links and status are correct.
* It shares the same cover aesthetics and section hierarchy.
* It provides a valid entrypoint or an honest explanation that the repository is an archive.
* It has no dead images, invented features, secret values, or claims of unrun tests.
* Paths and commands correspond to actual files.
* Private or corporate materials are not copied into public repos.
* Changes are reviewed in a branch and Pull Request before merging.

The source template is [TEMPLATE.md](TEMPLATE.md). This guide is the single reference for future repository documentation updates.
