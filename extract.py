import fitz
import os

pdfs = [
    "F77-Mach-2-Specsheet_copy.pdf",
    "F77-Superstreet-Specsheet_copy.pdf",
    "X-47-Specsheet.pdf",
]

os.makedirs("extracted/images", exist_ok=True)
os.makedirs("extracted/text", exist_ok=True)

for pdf in pdfs:
    base = os.path.splitext(pdf)[0]
    doc = fitz.open(pdf)
    print(f"\n===== {pdf} ({doc.page_count} pages) =====")
    all_text = []
    for i, page in enumerate(doc):
        txt = page.get_text()
        all_text.append(f"----- PAGE {i+1} -----\n{txt}")
        # render image at 2x for clarity
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_path = f"extracted/images/{base}_p{i+1}.png"
        pix.save(img_path)
        print(f"  page {i+1}: {len(txt)} chars text, image -> {img_path}")
    with open(f"extracted/text/{base}.txt", "w") as f:
        f.write("\n\n".join(all_text))
    doc.close()

print("\nDONE")
