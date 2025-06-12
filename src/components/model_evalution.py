import os 
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import csv
from src.entity import ModelEvalutionConfig

class ModelEvalution:
    def __init__(self, config=ModelEvalutionConfig):
        self.config = config
        self.model_path = self.config.model_path
        self.tokenizer_path = self.config.tokenizer_path

        self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_path, local_files_only=True)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path, local_files_only=True)

        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        if not os.path.exists(self.config.prediction_results):
            with open(self.config.prediction_results, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["text", "label", "confidence"])

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = F.softmax(outputs.logits, dim=-1)
            prediction = torch.argmax(probs, dim=-1).item()
            confidence = probs[0][prediction].item()

        label = "Real News" if prediction == 1 else "Fake News"
        print(f"📰 Text: {text}")
        print(f"📢 Prediction: {label} ({confidence:.4f} confidence)")

        with open(self.config.prediction_results, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([text, label, confidence])
        return {"prediction": label, "confidence": round(confidence, 4)}
