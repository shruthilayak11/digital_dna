import json
import os


class Authenticator:
    def __init__(self, threshold=0.3):
        self.threshold = threshold

    def load_profile(self, user_id):
        path = f"data/profiles/{user_id}.json"

        if not os.path.exists(path):
            return None

        with open(path, "r") as f:
            return json.load(f)

    def save_profile(self, user_id, features):
        path = f"data/profiles/{user_id}.json"

        with open(path, "w") as f:
            json.dump(features, f, indent=4)

    def compare(self, new_features, stored_features):
        score = 0
        total = len(stored_features)

        for key in stored_features:
            diff = abs(new_features[key] - stored_features[key])

            # Normalize difference (avoid scale issues)
            if stored_features[key] != 0:
                diff_ratio = diff / stored_features[key]
            else:
                diff_ratio = diff

            if diff_ratio < self.threshold:
                score += 1

        confidence = score / total
        return confidence

    def authenticate(self, user_id, new_features):
        stored_features = self.load_profile(user_id)

        if stored_features is None:
            return "No profile found. Please register first."

        confidence = self.compare(new_features, stored_features)

        if confidence >= 0.5:
            return f"Genuine User ✅ (confidence: {confidence:.2f})"
        else:
            return f"Imposter ❌ (confidence: {confidence:.2f})"