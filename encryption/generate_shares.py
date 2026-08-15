import random
from PIL import Image
import numpy as np

def generate_shares(input_image_path, share1_path, share2_path):
    # Open image and convert to grayscale
    img = Image.open(input_image_path).convert('L')

    # Convert to binary image (black and white)
    img = img.point(lambda x: 0 if x < 128 else 255, '1')

    img_array = np.array(img, dtype=np.uint8)
    h, w = img_array.shape

    share1 = np.zeros((h, w), dtype=np.uint8)
    share2 = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            pixel = img_array[i, j]
            r = random.randint(0, 1)

            if pixel == 0:  # Black pixel
                if r == 0:
                    share1[i, j] = 0
                    share2[i, j] = 255
                else:
                    share1[i, j] = 255
                    share2[i, j] = 0
            else:  # White pixel
                if r == 0:
                    share1[i, j] = 0
                    share2[i, j] = 0
                else:
                    share1[i, j] = 255
                    share2[i, j] = 255

    Image.fromarray(share1).save(share1_path)
    Image.fromarray(share2).save(share2_path)

    print('Shares generated successfully!')

if __name__ == '__main__':
    generate_shares(
        'sample-images/original.png',
        'sample-images/share1.png',
        'sample-images/share2.png'
    )
