# Auto Image Enhancer & Crop Tool

A Python script that automatically crops white/light borders from images and enhances their quality (sharpness, contrast, and brightness). Perfect for preparing product images or cleaning up scanned documents.

## Features

-   **Smart Cropping**: Automatically detects and trims white or light-colored borders.
-   **Image Enhancement**:
    -   Increases Sharpness (1.3x)
    -   Boosts Contrast (1.2x)
    -   Adjusts Brightness (1.1x)
-   **Batch Processing**: Processes all `.jpg`, `.jpeg`, and `.png` files in the `input_images` folder at once.
-   **High Quality Output**: Saves results as high-quality JPEGs in the `output_images` folder.

## Prerequisites

-   Python 3.x
-   Pillow (Python Imaging Library)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Guruprasath911/auto-image-enhancer-crop-tool.git
    cd auto-image-enhancer-crop-tool
    ```

2.  Install the required dependency:
    ```bash
    pip install Pillow
    ```

## Usage

1.  Place your images inside the `input_images` folder. (Create the folder if it doesn't exist).
2.  Run the script:
    ```bash
    python auto_image_enhancer.py
    ```
3.  Find your processed images in the `output_images` folder.

## Configuration

You can tweak the enhancement settings by modifying the values in `auto_image_enhancer.py`:

```python
# Adjust these values in the script
smart_crop(image, tolerance=240) # Higher tolerance (0-255) removes more 'near-white' colors
enhance_image(image, sharpness=1.3, contrast=1.2, brightness=1.1)
```

## License

This project is open-source and available for personal and commercial use.
