"""xpath 选取标签文字的三种方法，各有用途。"""

from lxml import etree


s = """\
<table>
  <tr>
    <td>
      1aa
      <font>1bb</font>
      1cc
    </td>
    <td>
    </td>
    <td>
      1dd
    </td>
  </tr>
  <tr>
    <td></td>
    <td>2bb</td>
    <td>2cc</td>
    <td>2dd</td>
    <td><font>2ee</font></td>
    <td><font>2ff</font></td>
  </tr>
  <tr>
  </tr>
</table>"""


def main() -> None:
    # HTML 会自动补全丢失的标签，并且加上 <html> 和 <body> 标签
    selector = etree.HTML(s)
    print(etree.tounicode(selector))
    print('*' * 50)

    # 选取标签文字的三种方法

    # 1. text()
    # 可以看到，当一个节点没有文字时，它没有 text() 节点，所以会被跳过
    # 不会选取子标签的文字，但当前标签下的文字（如换行）会被选取
    # 内容会被标签分隔成一个个列表元素
    print(selector.xpath('.//table//tr[1]/td[1]/text()'))
    print('*' * 50)
    # 多个标签文字，依次排列成列表
    print(selector.xpath('.//table//tr[1]/td/text()'))
    print('*' * 50)

    # 2. text 属性
    # 当标签为空会返回 None
    # 不会选取子标签的文字，但当前标签下的文字（如换行）会被选取
    # 如果当前标签下有文字和子标签，
    # 只会返回子标签前面的文字
    container = selector.xpath('.//table//tr[1]/td[1]')
    print([e.text for e in container])
    print('*' * 50)
    container = selector.xpath('.//table//tr[1]/td')
    print([e.text for e in container])
    print('*' * 50)

    # 3. string()
    # 会选取空标签，也会选取子标签内容，和当前标签内容拼接在一起
    print(selector.xpath('string(.//table//tr[1]/td[1])'))
    print('*' * 50)
    # 这种用法错误，不能正确显示文字，需要精确到单个标签
    print(selector.xpath('string(.//table//tr[1]/td)'))
    print('*' * 50)
    # 正确用法
    container = selector.xpath('.//table//tr[1]/td')
    print([e.xpath('string(.)') for e in container])
    print('*' * 50)
    container = selector.xpath('.//table//tr[2]/td')
    print([e.xpath('string(.)') for e in container])
    print('*' * 50)


if __name__ == '__main__':
    main()
