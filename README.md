# Prism

One idea, refracted into many looks.

Prism is a small, versioned library of the building blocks for turning dense, technical content (quant finance, systems design, whatever) into infographic posters that are actually readable. It started life as a pile of one-off image prompts and got out of hand - so now it lives here: structured, named, and machine-readable, so an agent or an API can compose from it instead of copy-pasting prompts forever.

## The idea: four independent axes

A poster is four separate choices. Keep each one small and finite, then compose them into effectively infinite outputs. (That is the Grammar of Graphics philosophy, lifted from charts up to whole posters.)

- **Archetype** - the *skeleton*. What relationship the content expresses (flow, comparison, timeline, part-to-whole, ...). Finite by design, because it is classified by function, not appearance. See `archetypes/`.
- **Layout** - the *arrangement*. Where blocks sit: grid, radial, network, layered, freeform - plus nesting and an edge layer for organic, non-linear compositions. See `layouts/`.
- **Zoom** - the *depth*. A numeric level-of-detail, not a fixed tier. Past the legibility ceiling, spill into a multi-image series. See `zoom/`.
- **Style** - the *skin*. Palette, type, masthead, borders. Most of the library lives here today. See `styles/`.

Archetype x Layout x Zoom x Style. Pick one from each.

## Repo layout

```
prism/
  schema/        # JSON Schema every style obeys
  styles/        # the skins (A = journal, C = editorial)
  archetypes/    # the finite functional families (FT spine)
  layouts/       # topologies, operators, edges, constraints
  zoom/          # the level-of-detail parameter + spill rule
  registry/      # index.json - build artifact an API can serve
  scripts/       # build_index.py
```

## How styles are stored

Each style is a folder under `styles/` with a `style.yaml` (the source of truth) and an optional `README.md` with example renders. `style.yaml` holds metadata (what it is good for, how dense it goes) plus a `prompt_scaffold` - the reusable art-direction prompt with a `{{CONTENT_BLOCK}}` slot you drop actual content into.

`registry/index.json` is a build artifact (run `scripts/build_index.py`) that flattens every style into one file an API can serve directly.

## Status legend

- `approved` - battle-tested, use freely
- `candidate` - generated and liked, not yet locked in
- `draft` - experimental
- `deprecated` - superseded

## Using it from an agent

See `AGENTS.md`.

## License

MIT. The prompt text is yours to remix.
