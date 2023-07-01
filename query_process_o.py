#coding=utf-8
# 机 构：中国科学院大学
# 程序员：李浩东
# 时 间：2023/5/23 10:57

import psutil

# 获取所有服务进程列表
# processes = psutil.process_iter()
processes = psutil.win_service_iter()
services = []

for process in processes:
    services.append(process.name())

print(len(services))
print(services)

# 获取所有进程列表
# processes = psutil.process_iter()

# # 遍历进程列表，筛选出服务进程
# services = []
# services1 = []
# for process in processes:
#     try:
#         # if process.status() == "running" and not process.name().startswith("System"):  # 检查一个进程是否正在运行，并且该进程不是系统进程
#         if not system_process_pattern.match(process.name().lower()):  # 该进程不是系统进程
#             services.append({
#                 "name": process.name()
#             })
#             services1.append({
#             "pid": process.pid,
#             "name": process.name(),
#             "status":process.status(),
#             "cmdline": " ".join(process.cmdline()).replace("[", "").replace("]", ""),
#             "username": process.username(),
#             "cpu_percent": process.cpu_percent(),
#             "memory_percent": process.memory_percent(),
#             "create_time": process.create_time(),
#             "num_threads": process.num_threads(),
#             })
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass
#
# # 打印服务进程列表
# # print("服务进程列表：")
# print(len(services))
# print(services)
# print(len(services1))
# print(services1)
# # print('---------------------------------------')
# # for i, service in enumerate(services):
# #     print(i, service)