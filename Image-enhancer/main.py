from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

def enhance_image(image_path, enhancement_factor=2.0):
    
    image = Image.open(image_path)

   
    enhancer = ImageEnhance.Color(image)
    # enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(enhancement_factor)
    enhanced_image.save('high_quality.jpg')

    return enhanced_image

original_image_path = 'low_quality.jpg'


enhancement_factor = 2.0
enhanced_image = enhance_image(original_image_path, enhancement_factor)


fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].set_title('Original Image')
axes[1].set_title('Enhanced Image')
axes[0].imshow(Image.open(original_image_path))
axes[1].imshow(enhanced_image)
plt.show()
