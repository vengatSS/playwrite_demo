import subprocess
import threading

# List of individual feature files to run in parallel
features = [
    "features/login.feature"
]*10

def run_feature(feature_path):
    print(f"Running: {feature_path}")
    subprocess.run(f"python test_runner/run_tests.py --feature={feature_path}", shell=True)

threads = []
for feature in features:
    t = threading.Thread(target=run_feature, args=(feature,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
