"""处理 URL 编码"""

from urllib import parse


def main() -> None:

    # url 中的非 assci 会显示成 `%XX` 形式
    url = 'https://www.yelp.com/biz/dr-h%C3%A9ctor-m-mayol-san-juan-2'
    print(parse.unquote(url))


if __name__ == '__main__':
    main()
