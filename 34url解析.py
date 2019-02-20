from urllib import parse


def main():
    url = 'http://www.walgreens.com/locator/walgreens-801+canal+st-new+orleans-la-70112/id=15615:1080'

    # result 是个具名元组
    result = parse.urlparse(url)
    print(result)
    a, b, c, d, e, f = result
    print(a, b, c, d, e, f)
    a = result.scheme
    b = result.netloc
    c = result.path
    d = result.params
    e = result.query
    f = result.fragment
    print(a, b, c, d, e, f)


if __name__ == '__main__':
    main()
