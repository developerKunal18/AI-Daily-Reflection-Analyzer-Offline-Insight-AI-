print("🧠 AI Daily Reflection Analyzer \n")

achievements = input("What did you achieve today? ").lower()
challenges = input("What challenges did you face? ").lower()
learning = input("What did you learn today? ").lower()
energy = int(input("Energy level today (1–5): "))

print("\n📊 REFLECTION ANALYSIS")

# Productivity
if len(achievements.split()) > 3:
    print("✅ Productivity: Good")
else:
    print("⚠️ Productivity: Low")

# Growth
if learning.strip():
    print("🌱 Growth Mindset: Active")
else:
    print("⚠️ Growth Mindset: Missing")

# Energy
if energy >= 4:
    print("⚡ Energy Level: High")
elif energy >= 2:
    print("🔋 Energy Level: Moderate")
else:
    print("🚨 Energy Level: Low")

print("\n🧭 AI Reflection Feedback")

if energy <= 2:
    print("• You need better rest and recovery")
if not learning.strip():
    print("• Try to learn at least one thing daily")
if "stress" in challenges or "tired" in challenges:
    print("• Consider reducing workload or taking breaks")
if energy >= 4 and learning.strip():
    print("• Great day! Maintain this balance")
