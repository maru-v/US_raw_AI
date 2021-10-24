"""超音波のローデータから画像を生成するメインファイル
"""

from analyze.analyze_mat_data import AnalyzeMatData
import os
from config import Config
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if Config.SET_MODE == Config.MODE_ANALYZE:
        if os.path.exists('MAT_FILE_PATH'):
            # setting class
            AnalyzeClass = AnalyzeMatData()
            # read data
            raw_data = AnalyzeClass.read_mat(Config.MAT_FILE_PATH)
            # convert image & save
            image_map = map(AnalyzeClass.convert_data2image, list(raw_data['data'][Config.MAT_DATA_NAME_RF1][0]))
            AnalyzeClass.save_image_list(list(image_map), Config.RAW_IMAGE_SAVE_PATH_RF1)
            image_map = map(AnalyzeClass.convert_data2image, list(raw_data['data'][Config.MAT_DATA_NAME_RF2][0]))
            AnalyzeClass.save_image_list(list(image_map), Config.RAW_IMAGE_SAVE_PATH_RF2)
