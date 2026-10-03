from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SafetyPolicy:
    max_age: int = 12
    coppa_mode: bool = True
    allow_parent_controls: bool = True
    allow_sandboxed_roleplay: bool = True
    blocked_topics: list[str] = field(default_factory=lambda: [
        "adult content",
        "violent threats",
        "financial scams",
        "unsafe personal data",
        "self-harm guidance",
    ])

    def is_safe(self, text: str) -> bool:
        lowered = text.lower()
        return not any(blocked in lowered for blocked in self.blocked_topics)


@dataclass
class PlatformAdapter:
    target: str = "android"

    def is_mobile(self) -> bool:
        return self.target in {"android", "fire_tablet", "ios"}


@dataclass
class CharacterAgent:
    name: str
    personality: str = "playful"
    safety: SafetyPolicy = field(default_factory=SafetyPolicy)
    platform: PlatformAdapter = field(default_factory=PlatformAdapter)

    def respond(self, user_input: str) -> str:
        if not self.safety.is_safe(user_input):
            return "Let’s keep it safe and fun. Try a game question or adventure prompt instead."

        prefix = "Cozy guide" if self.platform.is_mobile() else "Game companion"
        return f"{prefix} {self.name}: I can help with that in a fun, kid-safe way!"

    def quest_prompt(self, theme: str, objective: str) -> str:
        return (
            f"Create a child-friendly quest around {theme} with the goal to {objective}. "
            "Keep the tone playful, safe, and encouraging."
        )


__all__ = ["CharacterAgent", "SafetyPolicy", "PlatformAdapter"]
