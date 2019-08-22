import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='Unused Image Remover: Unused image removal tool for image annotation work')
    parser.add_argument('image_dir', help='Input the image directory. (e.g. ./images)')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete the images.')

    args = parser.parse_args()
    image_dir = args.image_dir
    delete_flag = args.delete

    unused_images = find_unused_images(image_dir)
    for img in unused_images:
        print(img)
        if delete_flag:
            p = Path(image_dir) / img
            p.unlink()

    if delete_flag:
        print(f'\nRemoved {len(unused_images)} images.')
    else:
        print(f'\n{len(unused_images)} unused images were found.')
        print('To actually delete it, specify "-d" as an argument.')


def find_unused_images(image_dir: str) -> list:
    p = Path(image_dir)
    texts = []
    for txt in p.glob('*.txt'):
        texts.append(txt.name.split('.')[0])
    texts.sort()

    unused_images = []
    for img in p.glob('*.jpeg'):
        if img.name.split('.')[0] not in texts:
            unused_images.append(img.name)

    unused_images.sort()
    return unused_images


if __name__ == '__main__':
    main()
