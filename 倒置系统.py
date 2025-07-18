import time
import random

print("正在初始化系统...")
time.sleep(2)
print("检测到严重错误！")
time.sleep(1)

errors = [
    "硬盘故障",
    "内存泄漏",
    "CPU过热",
    "病毒入侵",
    "系统文件损坏"
]

for i in range(5):
    print(f"错误: {random.choice(errors)} - 代码 0x{random.randint(1000, 9999):X}")
    time.sleep(0.5)

print("\n正在尝试修复...")
for i in range(1, 101):
    print(f"进度: {i}%", end='\r')
    time.sleep(0.05)

print("\n\n修复失败！你的电脑将在10秒后自爆！")
for i in range(10, 0, -1):
    print(f"{i}...", end=' ')
    time.sleep(1)

print("\n\n骗你的啦！😄")
