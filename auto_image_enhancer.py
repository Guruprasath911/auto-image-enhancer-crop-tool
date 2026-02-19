from PIL import Image, ImageChops, ImageEnhance
import os

# === Folder paths ===
input_folder = "input_images"
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

# === Smart crop to remove light/white edges ===
def smart_crop(image, tolerance=240):
    gray = image.convert("L")
    mask = gray.point(lambda x: 0 if x > tolerance else 255, mode='1')
    bbox = mask.getbbox()
    return image.crop(bbox) if bbox else image

# === Enhance image quality ===
def enhance_image(image, sharpness=1.3, contrast=1.2, brightness=1.1):
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(sharpness)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    return image

# === Process all images ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        image = Image.open(input_path).convert("RGB")
        cropped = smart_crop(image, tolerance=240)
        enhanced = enhance_image(cropped)  # Enhance after cropping

        enhanced.save(output_path, "JPEG", quality=100, subsampling=0)

print("Done! Cropped and enhanced images saved to:", output_folder)
