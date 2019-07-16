from statistics import mean, mode


def main() -> None:
    data = [1, 2, 2, 5, 10, 12]
    # 计算平均值
    print('{:0.2f}'.format(mean(data)))
    # 计算数据集中出现最多的数据点
    print(mode(data))


if __name__ == '__main__':
    main()
