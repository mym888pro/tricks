import sys

print("想退出这个程序？试试看吧！")

while True:
    try:
        command = input("请输入 'exit' 退出: ")
        if command.lower() == 'exit':
            print("哈哈，骗你的！")
            # 这里可以添加一些有趣的消息
            print("3...")
            import time
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("开玩笑的，再来一次吧！")
    except KeyboardInterrupt:
        print("\n按Ctrl+C也没用哦！")
    except EOFError:
        print("\n这样也不行！")
