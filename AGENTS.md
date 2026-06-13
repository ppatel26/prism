# Using Prism from an agent

Prism is a style + structure registry. An agent reads it to decide how to render a piece of content as an infographic poster, composing art direction from the four axes instead of inventing it from scratch.

## Selection algorithm

1. Read the content. Decide its dominant **relationship** -> pick an archetype (`archetypes/README.md`, FT nine families).
2. Estimate information density (count the blocks) -> set a **zoom** level (`zoom/README.md`). If it exceeds the legibility ceiling, plan a multi-image series.
3. Choose a **layout topology** that fits the archetype and block count (`layouts/README.md`).
4. Choose a **style** (`styles/`) by matching `density_rating` to your zoom and `best_for` to the use case. Prefer `status: approved`.
5. Compose the final prompt: take the style's `prompt_scaffold` and replace `{{CONTENT_BLOCK}}` (and any `{{TITLE}}` / `{{SUBTITLE}}` slots) with the archetype/layout-structured content.

## Machine-readable entry points

- `registry/index.json` - flattened list of all styles (id, family, status, density_rating, best_for, depth_mechanism, default_aspect_ratio). Filter on these.
- `schema/style.schema.json` - the contract every style file obeys.

## Conventions

- Style ids are kebab-case and stable. Never renumber - deprecate instead.
- Default to a style's `default_aspect_ratio` unless the caller overrides.
- When unsure on density, pick the approved style with the highest `density_rating` (currently `a1-nature-journal`).
