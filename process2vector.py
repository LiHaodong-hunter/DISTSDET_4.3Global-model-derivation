# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/5/24 11:02

import csv
import socket
import query_process
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import WhitespaceTokenizer
import gensim
from gensim.models import KeyedVectors
import fasttext
import fasttext.util

# nltk.download('punkt')

# Google’s word2vec embedding
# model = KeyedVectors.load_word2vec_format('word2vec_model/GoogleNews-vectors-negative300.bin', binary=True, encoding='UTF-8')
# print(model['AJRouter'])
# for index, service in enumerate(query_process.services):
#     try:
#         print(index+1, service, model[service])
#     except:
#         pass


# Facebook’s fastText embeddings
ft = fasttext.load_model('word2vec_model/cc.en.300.bin')
# print(ft.get_word_vector('AJRouter'))
# with open('process_embdeding.txt', 'w') as f:
#     service_lst = []
#     service_embedding_lst = []
#     for index, service in enumerate(query_process.services):
#         service_embedding = ft.get_word_vector(service)
#         # print(index + 1, service, service_embedding)
#         service_lst.append(service)
#         service_embedding_lst.append(service_embedding)
#         f.write(service + ': ' + str(service_embedding) + '\n')
#         # f.write(str(service_embedding))

# 获取主机名
hostname = socket.gethostname()
path = 'process_embedding'

with open(path + '/' + hostname + '_process_embedding.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['service', 'embedding'])
    for index, service in enumerate(query_process.services):
        service_embedding = ft.get_word_vector(service)
        writer.writerow([service, service_embedding])



# # 将进程转换为文本
# for service in query_process.services:
#     # service['name'] = service['name'][:-4]
#     # service['cmdline'] = " ".join(service['cmdline'][:-4]).split(':\\').split('\\')
#     # service['cmdline'] = ' '.join(' '.join(service['cmdline'][:-4].split('\\')).split(':', 1))
#     # service['username'] = ' '.join(re.split(r"[\W\d]+", service['username']))  # 匹配特殊字符和数字
#     # service = f"pid: {service['pid']} name:{service['name']} status:{service['status']} cmdline:{service['cmdline']} username:{service['username']} cpu_percent:{service['cpu_percent']} memory_percent:{service['memory_percent']} create_time:{service['create_time']} num_threads:{service['num_threads']}"
#     service = f"{service['pid']} {service['name']} {service['status']} {service['cmdline']} {service['username']} {service['cpu_percent']} {service['memory_percent']} {service['create_time']} {service['num_threads']}"
#     # service = f"{service['name']} {service['status']} {service['cmdline']} {service['username']}"
#     print(service)
#
#     # Google’s word2vec embedding
#     # 分词
#     # 指定空格分词器为分词方法
#     # tokenizer = WhitespaceTokenizer()
#     # tokens = tokenizer.tokenize(service.lower())
#     # print(tokens)
#
#     # 定义词向量模型
#     # model = gensim.models.KeyedVectors.load_word2vec_format('word2vec_model/cc.en.300.bin', binary=True)
#
#     # 将单词转换为向量
#     # vectors = []
#     # for token in tokens:
#     #     try:
#     #         # print(token, model[token])
#     #         vectors.append(model[token])
#     #     except KeyError:
#     #         continue
#             # 如果单词不在词向量模型的词汇表中，则跳过
#     # print(vectors)
#
#     # 计算平均向量
#     # if vectors:
#     #     service_vector = sum(vectors) / len(vectors)
#     # else:
#     #     service_vector = None
#     # print(service_vector)
#
#     # Facebook’s fastText embeddings
#     ft = fasttext.load_model('word2vec_model/cc.en.300.bin')
#     service_embedding = ft.get_word_vector(service)
#     print(service_embedding)
