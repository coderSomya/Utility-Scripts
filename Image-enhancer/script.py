from PIL import Image
import matplotlib as plt

# Open the image file
image = Image.open("bg.png")

# Increase the image quality by saving it with a higher quality setting
image.save("high_quality_bg.png", quality=95)  # You can adjust the quality value (0-100) as needed

# Close the image
image.close()
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].set_title('Original Image')
axes[1].set_title('Enhanced Image')
axes[0].imshow(Image.open('bg.png'))
axes[1].imshow('high_quality_bg.png')
plt.show()