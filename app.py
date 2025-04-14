# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch

# app = FastAPI()

# # تحميل النموذج والمجزئ
# model_name = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

# # تعريف نموذج البيانات
# class Complaint(BaseModel):
#     description: str

# @app.post("/analyze")
# def analyze_complaint(complaint: Complaint):
#     inputs = tokenizer(complaint.description, return_tensors="pt", truncation=True, padding=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#         logits = outputs.logits
#         predicted_class = torch.argmax(logits, dim=1).item()

#     # تحديد التصنيف بناءً على الفئة المتوقعة
#     if predicted_class == 2:
#         return {"status": "accepted", "category": "شكوى واضحة"}
#     elif predicted_class == 1:
#         return {"status": "rejected", "reason": "الشكوى غير واضحة أو عامة جدًا"}
#     else:
#         return {"status": "rejected", "reason": "الشكوى لا تتوافق مع التصنيفات المعتمدة"}



# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch

# app = FastAPI()

# # تحميل النموذج
# model_name = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

# # تعريف نموذج البيانات
# class Complaint(BaseModel):
#     description: str

# # الكلمات المفتاحية لتحديد التصنيفات
# categories_keywords = {
#     "الإنارة": ["إنارة", "ضوء", "أعمدة", "إنارة الشوارع", "إضاءة"],
#     "الحفر": ["حفرة", "حفر", "مطب", "طريق مكسور", "شقوق"],
#     "النفايات": ["قمامة", "نفايات", "زبالة", "حاوية"],
#     "المياه": ["ماء", "تسرب", "أنابيب", "مواسير"],
#     "الكهرباء": ["كهرباء", "أسلاك", "محول", "انقطاع كهرباء"]
# }

# def classify_by_keywords(text: str):
#     for category, keywords in categories_keywords.items():
#         if any(kw in text for kw in keywords):
#             return category
#     return "غير مصنف"

# @app.post("/analyze")
# def analyze_complaint(complaint: Complaint):
#     inputs = tokenizer(complaint.description, return_tensors="pt", truncation=True, padding=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#         logits = outputs.logits
#         predicted_class = torch.argmax(logits, dim=1).item()

#     if predicted_class == 2:
#         # الشكوى واضحة، نصنفها حسب الكلمات المفتاحية
#         category = classify_by_keywords(complaint.description)
#         if category != "غير مصنف":
#             return {"status": "accepted", "category": category}
#         else:
#             return {"status": "accepted", "category": "أخرى"}
#     elif predicted_class == 1:
#         return {"status": "rejected", "reason": "الشكوى غير واضحة أو عامة جدًا"}
#     else:
#         return {"status": "rejected", "reason": "الشكوى لا تتوافق مع التصنيفات المعتمدة"}

# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch

# app = FastAPI()

# # تحميل النموذج
# model_name = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

# # تعريف نموذج البيانات
# class Complaint(BaseModel):
#     description: str

# # الكلمات المفتاحية لتحديد التصنيفات
# categories_keywords = {
#     "الإنارة": ["إنارة", "ضوء", "أعمدة", "إنارة الشوارع", "إضاءة"],
#     "الحفر": ["حفرة", "حفر", "مطب", "طريق مكسور", "شقوق"],
#     "النفايات": ["قمامة", "نفايات", "زبالة", "حاوية"],
#     "المياه": ["ماء", "تسرب", "أنابيب", "مواسير"],
#     "الكهرباء": ["كهرباء", "أسلاك", "محول", "انقطاع كهرباء"]
# }

# def classify_by_keywords(text: str):
#     for category, keywords in categories_keywords.items():
#         if any(kw in text for kw in keywords):
#             return category
#     return "غير مصنف"

# @app.post("/analyze")
# def analyze_complaint(complaint: Complaint):
#     inputs = tokenizer(complaint.description, return_tensors="pt", truncation=True, padding=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#         logits = outputs.logits
#         predicted_class = torch.argmax(logits, dim=1).item()

#     if predicted_class == 2:
#         # الشكوى واضحة، نصنفها حسب الكلمات المفتاحية
#         category = classify_by_keywords(complaint.description)
#         if category != "غير مصنف":
#             return {"status": "accepted", "category": category}
#         else:
#             return {"status": "accepted", "category": "أخرى"}
#     elif predicted_class == 1:
#         return {"status": "rejected", "reason": "الشكوى غير واضحة أو عامة جدًا"}
#     else:
#         return {"status": "rejected", "reason": "الشكوى لا تتوافق مع التصنيفات المعتمدة"}

# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import pipeline
# import uvicorn
# from huggingface_hub import login

# # 🔐 سجّل الدخول بالتوكن
# login(token="") 

# app = FastAPI()

# MODEL_ID = "Noor22Tak/autotrain-yvqbc-dyfvv"
# classifier = pipeline("text-classification", model=MODEL_ID, token="hf_your_token_here")

# class ComplaintRequest(BaseModel):
#     description: str

# @app.get("/")
# def home():
#     return {"message": "🚀 مصنف الشكاوى يعمل بنجاح!"}

# @app.post("/classify")
# def classify_complaint(request: ComplaintRequest):
#     result = classifier(request.description)
#     label = result[0]["label"] if result else "غير واضحة"
#     return {"label": label}

# if __name__ == "__main__":
#     uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


# Worked ------------------------------------------------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from requests.exceptions import RequestException

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/Noor22Tak/autotrain-8hhp1-f1j5d"
HF_TOKEN = ""

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

class InputText(BaseModel):
    description: str

@app.post("/predict")
def predict(data: InputText):
    try:
        payload = {"inputs": data.description}
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        result = response.json()
        return {"result": result}
    except RequestException as e:
        # Catch any error related to the request (e.g., connection error, timeout)
        return {"error": f"Request failed: {e}"}
    except ValueError:
        # Catch errors related to JSON decoding
        return {"error": "Failed to decode the response JSON"}
    except Exception as e:
        # Catch any other general exceptions
        return {"error": f"An unexpected error occurred: {e}"}
