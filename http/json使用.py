import json


def main() -> None:
    data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
    print('DATA:', repr(data))

    # 变为字符串，sort_keys 可使 key 有序
    data_string = json.dumps(data, sort_keys=True)
    print('JSON:', data_string)
    # 字符串解析成数据结构
    print(json.loads(data_string))


if __name__ == '__main__':
    main()
