from PIL import Image
import numpy as np

def reconstruct_image(share1_path, share2_path, output_path):
    s1 = Image.open(share1_path).convert('L')
    s2 = Image.open(share2_path).convert('L')

    s1 = np.array(s1, dtype=np.uint8)
    s2 = np.array(s2, dtype=np.uint8)

    # Superimpose the two shares
    combined = np.minimum(s1, s2)

    Image.fromarray(combined).save(output_path)

    print('Image reconstructed successfully!')

if __name__ == '__main__':
    reconstruct_image(
        'sample-images/share1.png',
        'sample-images/share2.png',
        'sample-images/reconstructed.png'
    )
