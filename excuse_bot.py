@@ -1 +1,56 @@
# MAJOR-PROJECT-
import random

# Categories of excuses
categories = {
    "late": [
        "I got stuck in traffic due to a huge accident.",
        "My alarm didn't go off this morning.",
        "There was an unexpected power outage in my area.",
        "My pet was sick and I had to take care of it."
    ],
    "missed_work": [
        "I had a medical emergency and had to rush to the hospital.",
        "I wasn't feeling well and decided to take rest to avoid spreading illness.",
        "There was a family emergency that needed my immediate attention.",
        "I had an appointment that I couldn't reschedule."
    ],
    "missed_deadline": [
        "My computer crashed and I lost all my work.",
        "I misunderstood the deadline date.",
        "I was helping a friend with a crisis and lost track of time.",
        "There was a technical issue with the submission portal."
    ],
    "default": [
        "Something unexpected came up.",
        "I had a personal issue that couldn't be delayed.",
        "I was overwhelmed with other responsibilities.",
        "I tried, but things just didn’t go as planned."
    ]
}

def generate_excuse(category="default"):
    excuse_list = categories.get(category, categories["default"])
    return random.choice(excuse_list)

# User interaction
if __name__ == "__main__":
    print("Excuse Generator AI\n")
    print("Choose a situation:")
    print("1. Late")
    print("2. Missed Work")
    print("3. Missed Deadline")
    print("4. Random\n")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        cat = "late"
    elif choice == '2':
        cat = "missed_work"
    elif choice == '3':
        cat = "missed_deadline"
    else:
        cat = "default"

    excuse = generate_excuse(cat)
    print(f"\nYour AI-generated excuse:\n🗣️  {excuse}")
