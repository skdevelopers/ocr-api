import os
import time
from uuid import uuid4
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_temp_file(file_bytes: bytes, filename: str) -> str:
    unique_name = f"{uuid4().hex}_{filename}"
    path = os.path.join(UPLOAD_DIR, unique_name)
    with open(path, "wb") as f:
        f.write(file_bytes)
    return path

def extract_text_from_image(image: Image.Image, lang="eng+ara") -> str:
    # Preprocess image (improves accuracy!)
    gray = image.convert("L")  # convert to grayscale
    return pytesseract.image_to_string(gray, lang=lang)

def convert_pdf_to_images(pdf_bytes: bytes, dpi=300) -> list[Image.Image]:
    return convert_from_bytes(pdf_bytes, dpi=dpi)

def clean_uploads(older_than_seconds=3600):
    now = time.time()
    for fname in os.listdir(UPLOAD_DIR):
        path = os.path.join(UPLOAD_DIR, fname)
        if os.path.isfile(path) and now - os.path.getmtime(path) > older_than_seconds:
            os.remove(path)
