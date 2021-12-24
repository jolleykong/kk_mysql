'''
内容大纲：
    1. 模块的定义与分类
        # 什么是模块？
            # 一个模块就是一个py文件。
    2. import
    3. 第一次导入模块发生的二三事
    4. 被导入模块有独立的名称空间
    5. 为模块起别名
    6. 导入多个模块
    7. from .. import .. 
    8. from .. import .. 的使用
    9. from .. import .. 与 import 对比
    10. 一行导入多个
    11. from .. import *
    12. py文件的两种功能
    13. 模块的搜索路径
'''
'''
1. 模块的定义与分类
    # 什么是模块？
        # 一个模块就是一个py文件。
            # 代码不可能存在单独一个文件中
                # 维护性差
                # 效率低，加载慢
            # 将代码按照一定规则分成多个文件，每个文件各自包含若干函数。这些函数可能存在相同功能，或相似功能，即：代码冗余、重复。
            # 应该将这些雷同函数提取出来，存放在单独一个文件中，根据需要随用随拿（加载导入）
                # 节省代码
                # 容易维护，结构组织更加清晰
        # 一个模块就是一个py文件，这个模块存储了相似功能、相似函数的集合体。

    # 模块的分类
        # 内置模块（标准库），py解释器自带的。大概200多种，如：time、os、sys等。
        # 第三方模块（第三方库），通过pip install 安装的非官方库，都叫第三方模块。约6000种。
        # 自定义模块，自己写的模块。



2. import
    # 当引用一个模块文件的时候，实际上将模块文件执行了一遍，加载到内存，
    # 多次引用也只会在第一次引用时完成加载。
    # 可以根据条件决定导入的模块， （if... import .. else import ..


3. 第一次导入模块发生的二三事
    # 1. 将模块文件加载到内存（加载到内存就说明已经执行一遍了）
    # 2. 在内存中创建一个以 模块文件名 命名的名称空间： 此时，执行文件自己有一个名称空间， 被引用的模块文件有一个自己的名称空间。 两个名称空间是独立的。
    # 3. 通过”模块名称空间名字.“等方式引用此模块的名字（变量、函数名、类名等）

    # 坑： 通过import引入的模块，不易产生覆盖效果。即：通过模块命名空间.的方式引用模块的名字时，一定一定是从此模块中寻找。
    # 因为它有自己的独立的名称空间，与当前执行文件的名称空间没有关系。这样的话，引入模块的名称空间并不能从当前执行文件中拿到东西。但反过来可以。

        import kk1
        # kk1.name == return 'aa'
        # name == 'koko'
        # print(name)       # == koko
        # print(kk1.name)   # == aa ，二者不会覆盖。



4. 被导入模块有独立的名称空间
5. 为模块起别名
        # 书写方便
        # 简化代码
    # import xxx as yy
    # yy.func_name~

        # 统一化接口结构思想
            # if dbtype == 'mysql':
            #     import mysql_ as db
            # elif dbtype == 'oracle':
            #     import oracle_ as db

            # db.sqlprase()   # 统一化接口结构。

6. 导入多个模块
    # 不推荐，不规范。
        #import tim,os,sys   
    # 规范的还是一个一个import。 更清晰，便于管理和阅读、维护。




7. from .. import .. 
    # 容易冲突
    # 引用后，可以通过globals() 看到， 模块中的对象被复制到了当前的全局名称空间中。
    # 实际上，是将被引用模块的全局空间中将被引用的具体对象（函数等）的变量与值的对应关系，复制到执行文件的全局名称空间里。
    # 这样的话，就容易与当前执行文件产生覆盖效果。
    # 但是好处是，引用后可以直接通过函数名调用。
    # 有一个坑：被引用模块的函数如果用到了一些变量，这些变量依然从被引用模块的名称空间中查找，而不是从执行文件的名称空间中查找变量。




8. from .. import .. 的使用
    # 也可以使用as 取别名
    # 多行导入多个
        # from ... import ..
        # from ... import ..
        # from ... import ..



9. from .. import .. 与 import 对比

10. 一行导入多个 from ... import *
    # 尽量别用， from ... import *
        # 全部将被引用的名称空间里的函数复制过来，无用功。
        # 容易覆盖。
    # from ... import * 与 __all__ 配合使用
        # 使用__all__ 控制 * 的范围。
        # 在模块中添加一个声明（一般在最上面） __all__ = ['func1','func2'...]  列表中配置函数名
        # 之后再通过from ... import * 的方式导入，导入的就是list中指定的函数了。
        # 可以通过这种方式，将特别常用，又数量较多的函数一句话加载，又不造成无用的负担。


11. py文件的两种功能
    # 当脚本使用，代码的容器。执行文件。
    # 当模块使用，被执行文件。

    # 被引用时是被执行文件，但是调试时，就是脚本了。

    # 控制py文件角色功能，通过 __name__ 来控制
        # 用来控制py文件在不同的应用场景下执行不同的逻辑功能。或在模块文件中测试代码。
        # 脚本执行时，返回为 __main__
        # 被动执行时，返回为 模块名

        # if __name__ == '__main__':
        #       pass
        # 这样只有在调试阶段，也就是主动执行时，才会执行后面的动作，而不影响被引用时的执行结果。


12. 模块的搜索路径
    # 内存 --> 内置模块 --> sys.path 
        # 向sys.path的结果中加入需要的路径即可
        # sys.path 是一个list， 既然是list，就可以append。 但是模块多的话，路径多的话，就疯了。其实需要标准规划模块的目录位置，就好了。
        # 


>>> print(sys.path)
['', '/opt/homebrew/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', '/opt/homebrew/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9', '/opt/homebrew/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', '/opt/homebrew/lib/python3.9/site-packages']
'''
import sys
print(sys.path)