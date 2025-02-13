import random

def ai_decision_maker():
    actions = ["Move Forward", "Turn Left", "Turn Right", "Stop"]
    return random.choice(actions)

# Example execution
for _ in range(5):
    print(f"AI Decision: {ai_decision_maker()}")
