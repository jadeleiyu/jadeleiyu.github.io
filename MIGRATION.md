# Migration notes

## What this version contains

- Profile, photo, contact links, CV, research description, employment and education copied from the existing public repository.
- All 23 entries from the existing `publications.bib`, converted into one editable `PUBLICATIONS.md`.
- Original titles, authors and venue information retained. Paper links are included only when an explicit URL, DOI, or complete arXiv ID is available.
- A plain white layout, responsive portrait and typography, heading-based navigation, and keyboard focus styles.
- A single GitHub Pages publishing workflow; no automatic content-writing workflows.

No example posts, demo projects, teaching content, theme modules or theme-update jobs are carried into this replacement template.
The existing GitHub repository and public website have not been changed by preparing this template.

## Bibliography items to review

Two source records have no explicit `year` field and appear under **Undated**:

- `jiralerspong2024geometric`: Geometric Signatures of Compositionality in Language Models. Its venue includes “NeurIPS 2024”, but its year field is empty.
- `hongreasoning`: The Reasoning-Memorization Interplay in Language Models Is Mediated by a Single Direction.

The bibliography contains several related titles that may be different versions of the same work (including the critic-reward and hallucination papers). All were retained. Remove or combine them in `PUBLICATIONS.md` if desired.
Missing links remain plain titles. No absent metadata was invented or independently updated.

## One-time installation on the existing GitHub repository

This ZIP is a complete replacement website source, not a patch to mix into the old Hugo Blox theme.

1. Keep the current repository history and create a migration branch. Keep a backup of any uncommitted local changes before replacing files.
2. On that branch, replace the old website source with the files in this ZIP, including `.github/workflows/publish.yaml` and `.gitignore`. Preserve the repository's `.git` directory and any existing `CNAME` domain file. Do not carry over the old `config/`, `content/`, `go.mod`, `go.sum`, `hugoblox.yaml`, old theme layouts, or old import/update workflows: those belong to the old theme.
3. Confirm that the branch includes `HOME.md`, `PUBLICATIONS.md`, `hugo.toml`, `layouts/`, `static/`, and the new publishing workflow. Review the diff and use the supplied preview to check the proposed design before merging into `main`.
4. In GitHub **Settings → Pages → Build and deployment**, select **GitHub Actions** if it is not already selected.
5. Merge the migration branch into `main`. Check **Actions → Publish website** for a successful run. The normal address remains `https://jadeleiyu.github.io/`.

The public GitHub Pages deployment requires repository write access. This preparation does not claim to have performed that migration or verified a run on GitHub.
Existing deep links such as old publication detail pages, post pages and `experience/` are not recreated by this compact single-page template. Add redirects before migration if you need to retain those links. The CV path `uploads/resume.pdf` is preserved.

## Validation

The supplied source is built with Hugo 0.136.5. Build output is checked for the expected profile, all 23 paper entries, navigation targets, and local assets.
The optional converter is independent of the normal website build. Browser-based visual verification was unavailable in the preparation environment; the private preview is provided for review on desktop and mobile.
