# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/6/19 14:24

import pandas as pd
import numpy as np
import os

# 加载全局模型
global_model = pd.read_csv('global_process_embedding\\global_process_embedding.csv')

local_model_path = "process_embedding"

for filename in os.listdir(local_model_path):
    filepath = os.path.join(local_model_path, filename)
    # 读取本地模型
    local_model = pd.read_csv(filepath)
    # 使用全局模型更新本地模型
    local_model = global_model.copy()
    # 保存更新后的本地模型
    local_model.to_csv(filepath, index=False)

print("模型更新完成。")