import random
import time
print("\n" * 30)
running_sum = 0
count = 0
while True:
    outcome = random.random() < 0.5
    count += 1
    if outcome:
        running_sum += 10
    if count < 1000:
        continue
    print()
    print("  Trial #:", count)
    print("  Outcome:", "HEADS" if outcome else "TAILS")
    print("  Reward:", "$10" if outcome else "$0")
    print(f"  Average Reward: ${running_sum / count: 0.2f}" )
    time.sleep(0.05)