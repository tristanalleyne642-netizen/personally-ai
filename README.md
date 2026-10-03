# WildBrain Kids AI SDK

Open-source starter SDK for building kid-safe character AI experiences inspired by children’s entertainment IP workflows and safe conversational systems.

This repository is a clean starting point for developers who want to build:
- AI companions for kids games
- character-driven educational experiences
- safe storytelling agents
- Android / Fire Tablet / desktop game integrations
- Steam, Godot, Unreal, or custom engine plug-ins
- model-backed conversations with strong safety layers

Important: this project is an independent open-source starter and is not affiliated with or endorsed by WildBrain, Personality AI, Peppa Pig, Teletubbies, or any brand owner.

## Related industry references

- WildBrain acquires Personality AI: https://www.wildbrain.com/trade-news/wildbrain-acquires-personality-ai-a-trusted-partner-for-bringing-beloved-characters-to-life
- WildBrain / Personality AI coverage: https://finance.yahoo.com/technology/ai/articles/wildbrain-acquires-personality-ai-trusted-115500730.html
- Licensing Magazine coverage: https://www.licensingmagazine.com/2026/09/01/wildbrain-acquires-personality-ai-to-expand-interactive-ip-portfolio/

## Goals

- Keep the AI child-safe and age-appropriate
- Support branded character experiences without unsafe adult content
- Allow integration with Godot, Unreal, Android, and custom game engines
- Make it easy to build a conversational game NPC or character assistant
- Provide a free/open-source SDK foundation for experimentation and learning

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/peppa_demo.py
```

## Package layout

```text
wildbrain-kids-ai/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── docs/
│   ├── coppa.md
│   ├── android-fire-tablet.md
│   └── engine-integration.md
├── examples/
│   └── peppa_demo.py
├── src/
│   └── wildbrain_kids_ai/
│       ├── __init__.py
│       ├── agent.py
│       ├── safety.py
│       ├── platforms.py
│       └── story.py
└── tests/
    └── test_sdk.py
```

## Example

```python
from wildbrain_kids_ai import CharacterAgent, SafetyPolicy, PlatformAdapter

policy = SafetyPolicy(max_age=12, coppa_mode=True)
agent = CharacterAgent(
    name="Peppa Buddy",
    personality="playful",
    safety=policy,
    platform=PlatformAdapter("android"),
)

print(agent.respond("Can we go on a treasure hunt?"))
print(agent.respond("Tell me something inappropriate."))
```

## Safety design

This SDK includes built-in child-safe patterns:
- age-based conversation rules
- blocked topic filtering
- parent controls support
- safe roleplay boundaries
- no unrestricted adult content
- anonymized / minimal data handling defaults

## Supported integrations

- Godot
- Unreal Engine
- Custom Python game loops
- Android packaging
- Fire Tablet support
- AWS-hosted model backends
- Claude-style model integration wrappers

## License

MIT

## Contributing

Contributions are welcome. Please keep changes child-safe, documentation-friendly, and model-agnostic.
