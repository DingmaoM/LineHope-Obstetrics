import os

import pandas as pd
file_path = "./log"
if os.path.exists(file_path):
    print("文件存在")
else:
    os.mkdir(file_path)