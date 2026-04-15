from src.capture.keystroke_capture import KeystrokeCapture
from src.features.feature_extraction import FeatureExtractor
from src.auth.authenticator import Authenticator
from src.models.ml_model import MLAuthenticator
import numpy as np

user_id = "user1"

auth = Authenticator(threshold=0.3)
ml_auth = MLAuthenticator(contamination=0.2)

NUM_SAMPLES = 5
all_features = []

# ----------- REGISTER PHASE -----------
print(f"\n--- REGISTER ({NUM_SAMPLES} samples) ---")

for i in range(NUM_SAMPLES):
    print(f"\nSample {i+1}: Type normally")
    
    kc = KeystrokeCapture()
    data = kc.capture()

    fe = FeatureExtractor(data)
    features = fe.extract_features()

    print(f"Time: {features['total_time']:.2f}s | Speed: {features['typing_speed']:.2f}")

    all_features.append(features)

# ----------- AVERAGE PROFILE (Threshold Method) -----------
avg_profile = {}

for key in all_features[0].keys():
    avg_profile[key] = np.mean([f[key] for f in all_features])

auth.save_profile(user_id, avg_profile)

# ----------- TRAIN ML MODEL -----------
ml_auth.train(all_features)

print("\n✅ Profile created + ML model trained!")

# ----------- LOGIN PHASE -----------
print("\n--- LOGIN (type again) ---")

kc = KeystrokeCapture()
data = kc.capture()

fe = FeatureExtractor(data)
new_features = fe.extract_features()

# ----------- RESULTS -----------

print("\n📊 Login Stats:")
print(f"Time Taken: {new_features['total_time']:.2f} sec")
print(f"Typing Speed: {new_features['typing_speed']:.2f} keys/sec")

# Threshold result
result_threshold = auth.authenticate(user_id, new_features)

# ML result
result_ml = ml_auth.predict(new_features)

print("\n🔐 Threshold Result:")
print(result_threshold)

print("\n🤖 ML Result:")
print(result_ml)