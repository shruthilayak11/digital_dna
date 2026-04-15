from sklearn.ensemble import IsolationForest
import numpy as np


class MLAuthenticator:
    def __init__(self, contamination=0.3):
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.trained = False
        self.keys = None

    def train(self, feature_list):
        self.keys = list(feature_list[0].keys())
        X = np.array([[f[k] for k in self.keys] for f in feature_list])

        self.model.fit(X)
        self.trained = True

    def predict(self, features):
        if not self.trained:
            return "Model not trained ❌"

        X = np.array([[features[k] for k in self.keys]])
        prediction = self.model.predict(X)

        if prediction[0] == 1:
            return "Genuine User ✅ (ML)"
        else:
            return "Imposter ❌ (ML)"