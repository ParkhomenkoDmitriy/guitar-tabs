import os
from docx import Document


def extract_images_from_docx(docx_path, output_dir):
    # Проверка существования файла
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"The file {docx_path} does not exist.")

    # Создание выходной директории, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = Document(docx_path)

    # Извлечение изображений из документа
    for i, rel in enumerate(doc.part.rels.values()):
        if "image" in rel.target_ref:
            img_data = rel.target_part.blob
            img_filename = os.path.join(output_dir, f"image_{i}.png")
            with open(img_filename, "wb") as img_file:
                img_file.write(img_data)
            print(f"Saved {img_filename}")
