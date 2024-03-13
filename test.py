import psutil
import os

pid = os.getpid()
process = psutil.Process(pid)
memory_info = process.memory_info()

print(f"进程占用的内存：{memory_info.rss/1024/1024} Mbs")