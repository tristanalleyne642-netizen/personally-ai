# Engine integration guide

## Godot

- Expose a lightweight JSON API for character prompts.
- Keep all prompts asynchronous and scene-based.
- Cache safe dialogue templates locally.

## Unreal Engine

- Use a runtime bridge with character state and scene context.
- Keep prompts short and session-scoped.
- Handle generated dialogue as a gameplay event, not as a raw free-form web search.

## Custom engines

- Keep the character layer separate from rendering logic.
- Expose a character interface that can be connected to any UI stack.
