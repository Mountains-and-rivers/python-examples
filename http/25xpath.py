"""xpath 选取标签文字的三种方法，各有用途。"""

from lxml import etree


s = """\
<table>
  <tr>
    <td>1aa</td>
    <td>1bb</td>
    <td>1cc</td>
    <td></td>
    <td>
      <font>1ee</font>
    </td>
    <td>
      <font>1ff</font>
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

    # 选取标签文字的三种方法

    # 1. text()
    # 可以看到，当一个节点没有文字时，它没有 text() 节点，所以会被跳过
    # 不会选取子标签的文字，但当前标签下的文字（如换行）会被选取
    print(selector.xpath('.//table//tr[1]/td/text()'))

    # 2. text 属性
    # 当标签为空会返回 None
    # 不会选取子标签的文字，但当前标签下的文字（如换行）会被选取
    container1 = selector.xpath('.//table//tr[1]/td')
    print([e.text if e.text else '' for e in container1])

    # 3. string()
    # 会选取空标签，也会选取子标签内容，和当前标签内容拼接在一起
    container2 = selector.xpath('.//table//tr[2]/td')
    print([e.xpath('string(.)') for e in container2])


if __name__ == '__main__':
    main()
