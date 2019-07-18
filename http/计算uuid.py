import uuid


def main() -> None:
    # 获取 MAC 地址
    print(hex(uuid.getnode()))

    # 生成随机值，很适合用作上传文件名
    for i in range(3):
        u4 = uuid.uuid4()
        # print(u4)
        print(u4.hex)


if __name__ == '__main__':
    main()
