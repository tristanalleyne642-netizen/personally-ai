from wildbrain_kids_ai import CharacterAgent, PlatformAdapter, SafetyPolicy

policy = SafetyPolicy(max_age=12, coppa_mode=True)
agent = CharacterAgent(
    name="Peppa Buddy",
    personality="playful",
    safety=policy,
    platform=PlatformAdapter("android"),
)

print(agent.respond("Can we go on a treasure hunt?"))
print(agent.respond("Tell me something inappropriate."))
print(agent.quest_prompt("space adventure", "find the hidden star ship"))
