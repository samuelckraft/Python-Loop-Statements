#Task 1
import random

moods = ['happy', 'sad', 'energetic', 'calm', 'mad']

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for x in days:
    mood_day = random.choice(moods)
    print(f"On {x} you were feeling {mood_day}")
