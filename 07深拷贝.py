"""深拷贝字典或列表例子。
"""

import copy
import json


def main() -> None:
    d = {'a': [1, 2, 3], 'b': {'a': 1, 'b': [1, 2, 3]}}
    # 这种方法可以支持字典和列表及以外的引用类型嵌套
    d2 = copy.deepcopy(d)
    # 可以看到修改没有影响 d，所以是深拷贝
    d2['a'].append(4)
    d2['b']['a'] = 2
    d2['b']['b'].append(4)
    print(d)
    print(d2)

    print('*' * 50)

    # 另一种深拷贝方法，利用 json 序列和反序列化，但只支持字典和列表的嵌套
    d3 = json.loads(json.dumps(d))
    d3['a'].append(4)
    d3['b']['a'] = 2
    d3['b']['b'].append(4)
    print(d)
    print(d3)


if __name__ == '__main__':
    main()
