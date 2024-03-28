from os import listdir
from sys import argv

from PIL import Image


def list_images_from_dir(path):
    files = listdir(path)
    files.sort()

    for file in files:
        yield f'{path}/{file}'


def convert_images(path):
    converted_images = []

    for file in list_images_from_dir(path):
        with Image.open(file) as image:
            converted_images.append(image.convert('RGB'))

    return converted_images


def save_images_to_pdf(name, path):
    converted_images = convert_images(path)

    cover = converted_images.pop(0)  # get cover image

    cover.save(
        f'{name}', save_all=True,
        append_images=converted_images,
    )


if __name__ == '__main__':
    params = argv.copy()
    params.pop(0)

    name, path = params

    save_images_to_pdf(name, path)
