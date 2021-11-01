import cv2
import tqdm
from webcolors import rgb_to_hex


def img_to_hex(path_to_file) -> list:
    """
    :param path_to_file:
    :return list made of hex colours:
    """
    BG2_img = cv2.imread(path_to_file)
    RGB_img = cv2.cvtColor(BG2_img, cv2.COLOR_BGR2RGB)

    hex_list = []
    tqdm_rgb_list = tqdm.tqdm(RGB_img, desc="Converting image pixels to HEX colours", colour="#ff00ff")
    for pixel in tqdm_rgb_list:
        for colour in pixel:
            colour_as_tuple = tuple(colour.tolist())
            colour_as_hex = rgb_to_hex(colour_as_tuple)
            if colour_as_hex not in hex_list:
                hex_list.append(colour_as_hex)

    return hex_list
