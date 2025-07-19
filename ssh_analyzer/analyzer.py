from datetime import timedelta
from collections import defaultdict

class Analyzer:
    def __init__(self, entries, threshold=5, window=timedelta(seconds=60)):
        self.entries = entries
        self.threshold = threshold
        self.window = window
        self.alerts = []  # tuples: (ip, window_start, window_end, count)

    def run(self):
        # collect failure timestamps per IP
        fails = defaultdict(list)
        for e in self.entries:
            if e.status.lower() != 'accepted':
                fails[e.ip].append(e.timestamp)

        # detect any window with >= threshold failures
        for ip, times in fails.items():
            times.sort()
            start = 0
            for i, t in enumerate(times):
                # slide window start until within window size
                while times[i] - times[start] > self.window:
                    start += 1
                count = i - start + 1
                if count >= self.threshold:
                    self.alerts.append((ip, times[start], times[i], count))
                    break
