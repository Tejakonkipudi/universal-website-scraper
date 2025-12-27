import json
import pandas as pd

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_csv(data, path):
    df = pd.DataFrame([data])
    df.to_csv(path, index=False)
