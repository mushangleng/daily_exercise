from lxml import etree

# 1 完整模式
def func1():
    response = '''
        <div>
            <p><name>张三</name><age>10</age></p>
            <p><name>李四</name><age>20</age></p>
            <p><name>王五</name><age>30</age></p>
            <p><name>赵六</name><age>40</age></p>
            <p><name>马七</name><age>50</age></p>
        </div>
    '''

    html = etree.HTML(response)
    name_list = html.xpath('//p/name/text()')
    age_list = html.xpath('//p/age/text()')
    print(name_list)
    print(age_list)

    for name, age in zip(name_list, age_list):
        print(name, age, sep='----')
# func1()



# 2 瑕疵模式 错了一点 并且是最后一个(自动修复功能)
def func2():
    response = '''
        <div>
            <p><name>张三</name><age>10</age></p>
            <p><name>李四</name><age>20</age></p>
            <p><name>王五</name><age>30</age></p>
            <p><name>赵六</name><age>40</age></p>
            <p><name>马七</name><age>50</a></
        </div>
    '''

    html = etree.HTML(response)
    name_list = html.xpath('//p/name/text()')
    age_list = html.xpath('//p/age/text()')

    age_list = [age.strip() for age in age_list]  # 列表推导式  .strip() 去掉前后空白字符

    print(name_list)
    print(age_list)

    for name, age in zip(name_list, age_list):
        print(name, age, sep='----')

# func2()

# 3 数据丢失模式 通用的模板
def func3():
    response = '''
        <div>
            <p>
                <name>张三</name>
                <age>10</age>
            </p>
            <p><name>李四</name><age></age></p>
            <p><name></name><age>30</age></p>
            <p><name>赵六</name><age>40</age></p>
            <p><name></name><age>50</age></p>
        </div>
    '''

    html = etree.HTML(response)

    p_list = html.xpath('//div/p')

    for p in p_list:
        name = p.xpath('.//name/text()')  # . 表示在当前范围去找
        name = "".join(name)
        name = name if name != '' else 'null'  # 三元运算符

        age = p.xpath('.//age/text()')  # . 表示在当前范围去找
        age = "".join(age)
        age = age if age != '' else 'null'
        print(name, age)

# func3()

# 4 标签丢失模式 通用的模板
def func4():
    response = '''
        <div>
            <p>
                <age>10</age>
            </p>
            <p><name>李四</name></p>
            <p><name>王五</name><age>30</age></p>
            <p></p>
            <p><name>马七</name><age>50</age></p>
        </div>
    '''

    html = etree.HTML(response)

    p_list = html.xpath('//div/p')
    print(p_list)
    for p in p_list:
        name = p.xpath('.//name/text()')  # . 表示在当前范围去找
        name = "".join(name)
        name = name if name != '' else 'null'  # 三元运算符

        age = p.xpath('.//age/text()')  # . 表示在当前范围去找
        age = "".join(age)
        age = age if age != '' else 'null'
        print(name, age)
# func4()

# 5 花里胡哨模式 通用的模板
def func5():
    response = '''
        <div>
            <p>
                <name>张三</name>
                <age>10</age>
            </p>
            <p><xingming>李四</xingming><age>20</age></p>
            <p><name>王五</name><nianling>30</nianling></p>
            <p><name>赵六</name><nianling>40</nianling></p>
            <p><name>马七</name><age>50</age></p>
        </div>
    '''

    html = etree.HTML(response)

    p_list = html.xpath('//div/p')

    for p in p_list:
        name_1 = p.xpath('.//name/text()')
        name_2 = p.xpath('.//xingming/text()')
        name = name_1 if name_1 != [] else name_2
        name = ''.join(name)

        age_1 = p.xpath('.//age/text()')
        age_2 = p.xpath('.//nianling/text()')
        age = age_1 if age_1 != [] else age_2
        age = ''.join(age)
        print(name, age, sep='    ')


func5()
