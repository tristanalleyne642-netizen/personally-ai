from dataclasses import dataclass


@dataclass
class PlatformAdapter:
    target: str = "android"

    def is_mobile(self) -> bool:
        return self.target in {"android", "fire_tablet", "ios"}


__all__ = ["PlatformAdapter"]
