import csv


def main() -> None:

    # 如果遇逗号，会用双引号包裹
    # 如果遇双引号，用两个逗号代替
    rows = [
        {'class': 1, 'name': 'xiaoming,,,"', 'sex': 'male', 'height': 168, 'year': 23},
        {'class': 1, 'name': 'xiaohong', 'sex': 'female', 'height': 162, 'year': 22},
        {'class': 2, 'name': 'xiaozhang', 'sex': 'female', 'height': 163, 'year': 21},
        {'class': 2, 'name': 'xiaoli', 'sex': 'male', 'height': 158, 'year': 21},
    ]

    headers = rows[0].keys()

    with open('test2.csv', 'w', newline='')as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


if __name__ == '__main__':
    main()
