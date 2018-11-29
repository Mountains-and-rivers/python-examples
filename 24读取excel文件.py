"""读取 excel 文件。

操作 excel 文件的话，建议直接使用 pandas 。
"""

import xlrd


def main() -> None:
    path = ''
    workbook = xlrd.open_workbook(path)
    # sheet索引从0开始
    sheet1 = workbook.sheet_by_index(0)
    # 获取第4行内容
    rows = sheet1.row_values(3)
    # 获取第1列内容
    cols = sheet1.col_values(0)
    # 转换为字典
    d = dict(zip(sheet1.col_values(0), sheet1.col_values(1)))


if __name__ == '__main__':
    main()
