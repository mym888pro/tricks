import time

print("高级密码检测工具 v2.0")
print("请输入你的密码以进行安全检查:")

password = input("密码: ")

print("分析中...")
time.sleep(2)

print(f"检测到密码强度: {len(password)*10}%")
time.sleep(1)

print("正在上传到服务器...")
for i in range(1, 101):
    print(f"进度: {i}%", end='\r')
    time.sleep(0.03)

print("\n\n谢谢！你的密码已经被安全地... 呃... 分析完毕！")
print("开玩笑的，我其实没有保存你的密码 😉")
print(f"你输入的密码长度是: {len(password)} 个字符")
