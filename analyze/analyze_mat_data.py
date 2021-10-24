"""分析クラスファイル
"""

import scipy.io
from scipy.signal import hilbert
import numpy as np
from PIL import Image


class AnalyzeMatData:
    DB_CONST = 20
    DYNAMIC_RANGE = 60
    IMAGE_RANGE = 255
    SAVE_IMAGE_EXT = 'png'

    def read_mat(self, path: str) -> dict:
        try:
            data = scipy.io.loadmat(path)
        except:
            data = {}

        return data

    def convert_data2image(self, data: np.ndarray) -> Image:
        db_data = self.DB_CONST * np.log10(np.abs(hilbert(data)))
        db_data_norm = db_data - np.max(db_data)
        db_data_norm[db_data_norm < - self.DYNAMIC_RANGE] = - self.DYNAMIC_RANGE
        db_data_norm = (db_data_norm + self.DYNAMIC_RANGE) * self.IMAGE_RANGE / self.DYNAMIC_RANGE
        pil_image = Image.fromarray(db_data_norm)

        return pil_image

    def save_image_list(self, image_list: list, path: str) -> bool:


        try:
            for i in range(len(image_list)):
                image_list[i].convert("RGB").save(path + f'{i:03d}.' + self.SAVE_IMAGE_EXT)
            success = True
        except:
            success = False

        return success
