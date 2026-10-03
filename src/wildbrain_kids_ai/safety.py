from dataclasses import dataclass, field


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


__all__ = ["SafetyPolicy"]
