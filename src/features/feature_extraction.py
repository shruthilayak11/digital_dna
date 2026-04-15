import numpy as np


class FeatureExtractor:
    def __init__(self, keystrokes):
        self.keystrokes = keystrokes

    def extract_features(self):
        hold_times = []
        flight_times = []

        for i in range(len(self.keystrokes)):
            key_data = self.keystrokes[i]

            # Hold time = release - press
            hold = key_data["release_time"] - key_data["press_time"]
            hold_times.append(hold)

            # Flight time = current press - previous release
            if i > 0:
                prev_key = self.keystrokes[i - 1]
                flight = key_data["press_time"] - prev_key["release_time"]
                flight_times.append(flight)

        features = {
            "avg_hold_time": np.mean(hold_times) if hold_times else 0,
            "std_hold_time": np.std(hold_times) if hold_times else 0,
            "avg_flight_time": np.mean(flight_times) if flight_times else 0,
            "std_flight_time": np.std(flight_times) if flight_times else 0,
            "typing_speed": self._typing_speed(),
            "total_time": self._total_time()   # ✅ NEW FEATURE
        }

        return features

    def _typing_speed(self):
        if len(self.keystrokes) < 2:
            return 0

        total_time = self.keystrokes[-1]["release_time"] - self.keystrokes[0]["press_time"]
        return len(self.keystrokes) / total_time if total_time > 0 else 0

    def _total_time(self):   # ✅ NEW FUNCTION
        if len(self.keystrokes) < 2:
            return 0

        return self.keystrokes[-1]["release_time"] - self.keystrokes[0]["press_time"]