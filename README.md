# Personally AI

**Official WildBrain-supported open-source SDK for child-safe AI character experiences.**

Personally AI is powered by **Claude** and designed for interactive entertainment, learning, and family-safe game environments.

This project is a free developer foundation for:
- AI companions in kids games powered by Claude
- character-driven storytelling and quests with child-safe Claude integration
- safe toy and learning experiences 
- Android, Fire Tablet, and desktop game integrations
- custom engine and cloud integration workflows

## Claude Integration

Personally AI uses **Claude** (by Anthropic) as the backbone for conversational character logic:
- Safe, thoughtful responses optimized for child-appropriate interactions
- Fine-tuning support for custom character personalities
- Integration with AWS infrastructure for scalable deployment
- COPPA-compliant safety filtering layered on top of Claude's base model

## Related references

- WildBrain acquires Personality AI: https://www.wildbrain.com/trade-news/wildbrain-acquires-personality-ai-a-trusted-partner-for-bringing-beloved-characters-to-life
- WildBrain / Personality AI coverage: https://finance.yahoo.com/technology/ai/articles/wildbrain-acquires-personality-ai-trusted-115500730.html
- Licensing Magazine coverage: https://www.licensingmagazine.com/2026/09/01/wildbrain-acquires-personality-ai-to-expand-interactive-ip-portfolio/
- Claude API Docs: https://docs.anthropic.com/claude/

## Goals

- Keep AI child-safe and age-appropriate using Claude's thoughtful design
- Support branded character experiences without unsafe adult content
- Allow integration with Godot, Unreal, Android, Fire Tablet, and custom game engines
- Make it easy to build a conversational game NPC or character assistant powered by Claude
- Provide a free/open-source SDK foundation for experimentation and learning

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-claude-api-key"
python examples/peppa_demo.py
```

## Package layout

```text
personally-ai/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── docs/
│   ├── coppa.md
│   ├── claude-integration.md
│   ├── android-fire-tablet.md
│   └── engine-integration.md
├── examples/
│   └── peppa_demo.py
├── src/
│   ├── personally_ai/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── safety.py
│   │   ├── platforms.py
│   │   ├── claude_client.py
│   │   └── story.py
├── tests/
│   └── test_sdk.py
└── .github/
```

## Example

```python
from personally_ai import CharacterAgent, SafetyPolicy, PlatformAdapter, ClaudeClient

policy = SafetyPolicy(max_age=12, coppa_mode=True)
claude_client = ClaudeClient(api_key="your-api-key")

agent = CharacterAgent(
    name="Peppa Buddy",
    personality="playful",
    safety=policy,
    platform=PlatformAdapter("android"),
    model_client=claude_client,
)

print(agent.respond("Can we go on a treasure hunt?"))
print(agent.respond("Tell me something inappropriate."))
```

## Safety design

This SDK includes built-in child-safe patterns layered on top of Claude:
- age-based conversation rules
- blocked topic filtering
- parent controls support
- safe roleplay boundaries
- no unrestricted adult content
- anonymized / minimal data handling defaults
- Claude content policy compliance for minors

## Supported integrations

- Godot
- Unreal Engine
- Custom Python game loops
- Android packaging
- Fire Tablet support
- AWS-hosted model backends with Claude
- Claude API (direct and through AWS Bedrock)

## License

MIT

## Contributing

Contributions are welcome. Please keep changes child-safe, documentation-friendly, and Claude-compatible.
