# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/5/30 10:15

import csv
import os
import numpy as np
from sklearn.cluster import KMeans

# 3.4第三步
directory = "process_embedding" # 目录名
strings_list = []  # 存放进程
vectors_list = []  # 存放进程对应的向量
# 获取目录下所有文件名
# file_names = []
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    # if os.path.isfile(filepath):
    #     file_names.append(filename)

    # 打开文件
    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        for row in reader:
            strings_list.append(filename + '_' + row[0])
            vectors_list.append(row[1])

    # 将向量形式的字符串转换为浮点数向量
    global vectors
    vectors = []
    for vector_str in vectors_list:
        vector = np.fromstring(vector_str.strip('[]').replace('\n', ''), sep=' ').tolist()
        vectors.append(vector)

# 打印第一列
# print(len(strings_list))
# print(len(vectors))


# 使用k-means算法对向量进行聚类
kmeans = KMeans(n_clusters=146, random_state=0).fit(vectors)
# 根据聚类结果生成key列表
keys = [str(i) for i in range(146)]
# 将service_lst中的元素根据聚类结果分组
clustered_services = {key: [] for key in keys}
for i, label in enumerate(kmeans.labels_):
    clustered_services[str(label)].append(strings_list[i])
# 输出聚类结果
for key, services in clustered_services.items():
    print(f"Cluster {key}:{services}")
print('------------------------------------------------------------------------------------------------------')



# 3.4第四步
# 得到全局模型
with open('global_process_embedding/global_process_embedding.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['service', 'embedding'])

    # 遍历每个簇
    for cluster_id, data_files in clustered_services.items():
        # 计算该簇中所有数据所包含进程的词向量
        cluster_process_name = []  # 每一个聚类中的每一个进程名
        cluster_embeddings = []  # 每一个聚类中的每一个进程向量
        merged_cluster_process = []
        merged_cluster_vectors_norm = []
        for data_file in data_files:
            # print(data_file)
            file = data_file.split('.csv_')[0]  # 获取_前面的部分作为文件名
            process_name = data_file.split('.csv_')[1]  # 获取_后面的部分作为进程名
            # print(cluster_id, file, process_name)  # 聚类中心，文件名，进程名
            with open('process_embedding/' + file + '.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                # 读取 csv 文件的每一行
                for row in csv_reader:
                    # print(row[0],process_name)
                    # 判断是否是第一列，并检查第一列是否是 process_name
                    if row[0] == process_name:
                        cluster_process_name.append(row[0])
                        cluster_embeddings.append(row[1])
                        break
        # print(len(cluster_process_name), len(cluster_embeddings))

        # 在每一个聚类中，保留唯一进程，把进程名相同的元素对应的词向量合并起来
        for item in cluster_process_name:
            if item not in merged_cluster_process:
                merged_cluster_process.append(item)
        # print(merged_cluster_process)

        for item in merged_cluster_process:
            cluster_vectors = []
            for i in range(len(cluster_process_name)):
                if cluster_process_name[i] == item:
                    cluster_vectors.append(cluster_embeddings[i])
            # print(item, cluster_vectors)

            # 将向量形式的字符串转换为浮点数向量
            cluster_vectors_norm = []
            for i in cluster_vectors:
                item_norm = np.fromstring(i.strip('[]').replace('\n', ''), sep=' ').tolist()
                cluster_vectors_norm.append(item_norm)
            # print(item, cluster_vectors_norm)

            # merged_cluster_vectors_norm = []
            cluster_vectors_norm_aggr = []
            merged_vector = np.mean(cluster_vectors_norm, axis=0)
            cluster_vectors_norm_aggr.append(merged_vector)
            merged_cluster_vectors_norm.append(cluster_vectors_norm_aggr)
        # print(merged_cluster_process, merged_cluster_vectors_norm)


        for i in range(len(merged_cluster_process)):
            writer.writerow([merged_cluster_process[i], merged_cluster_vectors_norm[i]])
            # print([merged_cluster_process[i], merged_cluster_vectors_norm[i]])






