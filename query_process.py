# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/6/20 15:04

import os

def read_dir(dirname, services):
    """
    递归地读取指定目录及其子目录下的所有文件，并将每个文件中的PName字段写入process_names列表中。
    """
    if not os.path.exists(dirname):
        return
    for filename in os.listdir(dirname):
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            read_dir(filepath, services)
        elif os.path.isfile(filepath):
            print(filepath)
            with open(filepath, 'r') as f:
                for line in f:
                    data = eval(line.strip())
                    if 'FileName' in data and 'System32' not in data['FileName']:
                            services.add(data['PName'])
                    # if 'PName' in data:
                    #     services.add(data['PName'])


services = set()
dirname = "D:\\研究所项目\\DARPA数据集处理\\DARPA数据集_decompression\\arena"
read_dir(dirname, services)
print(len(services), services)
# with open('process_name.txt', 'w') as f:
#     for pname in process_names:
#         f.write(pname + '\n')
#         print(pname)