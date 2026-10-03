# COPPA and safe AI design

This project is intended for kid-safe game experiences and follows a conservative "less data, more safety" philosophy.

## Guidance

- Default to age-gated prompts and content controls.
- Keep all roleplay inside playful, age-appropriate scenarios.
- Do not collect unnecessary personal details.
- Do not allow unrestricted browsing or unfiltered adult content.
- Give parents or guardians visible controls.
- Use minimal-memory patterns for gameplay state.

## Recommended defaults

- `max_age = 12`
- `coppa_mode = True`
- `allow_parent_controls = True`
- `allow_sandboxed_roleplay = True`
