from PIL import Image
from app.utils import convert_pdf_to_images, extract_text_from_image

async def process_file(file):
    content = await file.read()
    text = ""

    if file.filename.lower().endswith(".pdf"):
        images = convert_pdf_to_images(content)
        for img in images:
            text += extract_text_from_image(img) + "\n"
    else:
        img = Image.open(file.file)
        text = extract_text_from_image(img)

    return text.strip()
