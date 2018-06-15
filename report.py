import xml.etree.ElementTree as ET

# 从 xml 文件中读取，用 getroot 获取根节点，根节点也是 Element 对象
report = ET.parse('report.xml')
testsuites = report.getroot()

for testsuite in testsuites:
    # 取 testsuite 名称
    name = testsuite.attrib['name']
    # 查找子节点中为 testcase 的节点
    for testcase in testsuite.findall('testcase'):
            # 把 testsuite 名称添加在 testcase 名称前面
            testcase.set('name', name + ': ' + testcase.attrib['name'])

# 需要指定编码为 utf-8
report.write("report.xml", encoding='utf-8')
