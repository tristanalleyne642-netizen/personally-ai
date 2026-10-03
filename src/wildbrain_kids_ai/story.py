from dataclasses import dataclass


@dataclass
class Quest:
    title: str
    objective: str
    difficulty: str = "easy"
    tone: str = "playful"

    def summary(self) -> str:
        return f"{self.title}: {self.objective}"


__all__ = ["Quest"]
