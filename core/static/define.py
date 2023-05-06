# 全局定义相关内容在此处声明
# ///////////////////////////////////////////////////////////////


class Define:
    """全局定义类
    """

    class LocalConfigState:
        RP: str = "RP"
        R: str = "R"
        P: str = "P"
        N: str = "N"
        FL: str = "FL"
        U: str = "U"

    class RequestMethod:
        GET: str = "get"
        POST: str = "post"
        PUT: str = "put"
        DELETE: str = "delete"
        HEAD: str = "head"
        OPTIONS: str = "options"

        def get_list(self) -> list:
            return [self.GET, self.POST, self.PUT, self.DELETE, self.HEAD, self.OPTIONS]

    # 软件信息
    # ///////////////////////////////////////////////////////////////
    APP_NAME: str = "General Crawler Tool"
    VERSION: str = "V1.0.2 DEV"
    COPYRIGHT: str = "Copyright (c) 2022 NEKO-ii"

    # 全局变量
    # ///////////////////////////////////////////////////////////////
    PATH_SETTINGS: str = "file\\settings"
    PATH_THEMES: str = "file\\themes"
    PATH_CACHE: str = "file\\cache"
    PATH_HELP: str = "file\\help"

    TYPE_COLOR: dict = {
        "default": "#aaaabb",
        "success": "#20cc5f",
        "info": "#6c99f4",
        "warn": "#f0f020",
        "error": "#ff4040",
    }
    TYPE_ICON: dict = {
        "default": "",
        "success": "[√]",
        "info": "[▣]",
        "warn": "[▲]",
        "error": "[⨂]",
    }
    TYPE_ICON_LIST: list = ["[√]", "[▣]", "[▲]", "[⨂]"]
    LOCAL_CONF_STATE_TYPE: dict = {"success": [LocalConfigState.RP, LocalConfigState.R, LocalConfigState.P], "error": [LocalConfigState.N, LocalConfigState.FL], "warn": [LocalConfigState.U]}

    # 默认主题
    # ///////////////////////////////////////////////////////////////
    DEFAULT_THEMES: dict = {
        "theme_name": "default",
        "window_size": {
            "startup": [1400, 720],
            "minimum": [960, 540]
        },
        "navigation": {
            "minimum_width": 50,
            "maximum_width": 240,
            "margins": [0, 0, 0, 0]
        },
        "right_column": {
            "minimum_width": 0,
            "maximum_width": 240
        },
        "time_animation": 500,
        "color": {
            "dark_1": "#1b1e23",
            "dark_2": "#1e2229",
            "dark_3": "#21252d",
            "dark_4": "#272c36",
            "bg_1": "#2c313c",
            "bg_2": "#343b48",
            "bg_3": "#3c4454",
            "icon_color": "#c3ccdf",
            "icon_hover": "#dce1ec",
            "icon_pressed": "#6c99f4",
            "icon_active": "#f5f6f9",
            "context_color": "#568af2",
            "context_hover": "#6c99f4",
            "context_pressed": "#3f6fd1",
            "text_title": "#dce1ec",
            "text_foreground": "#8a95aa",
            "text_description": "#4f5b6e",
            "text_active": "#dce1ec",
            "white": "#f5f6f9",
            "pink": "#ff007f",
            "green": "#00ff7f",
            "red": "#ff5555",
            "yellow": "#f1fa8c"
        }
    }

    # 窗口及组件名称定义
    # ///////////////////////////////////////////////////////////////

    # 用户协议
    # ///////////////////////////////////////////////////////////////
    AGREEMENT: str = \
        "This program is ONLY for learning or AC use, DO NOT used for illegal and commercial purposes. " \
        "Any third party users use this procedure illegal operations belong to individual behavior, " \
        "Has nothing to do with the developer. ANYONE has the right to supervise the use of the program " \
        "and submit the illegal usage to the legal department. " \
        "Other questions, please contact the developer: lntu.NEKO@outlook.com or https://github.com/NEKO-ii"

    # 文件默认内容
    # ///////////////////////////////////////////////////////////////
    FILE_DEFAULT_CONTENT: dict = {
        # 配置文件样例
        "configuration":
        '{\n'
        '    "urls": [],\n'
        '    "request_method": "get",\n'
        '    "verify": true,\n'
        '    "encoding": "UTF-8",\n'
        '    "data_form": {},\n'
        '    "data_form_script": {},\n'
        '    "timeout": 10.0,\n'
        '    "headers": {\n'
        '        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"\n'
        '    },\n'
        '    "cookie_update_enable": false,\n'
        '    "cookies": {},\n'
        '    "user_agent_pool": [],\n'
        '    "ip_proxy_pool": [],\n'
        '    "pretreatment_enable": false,\n'
        '    "pretreatment_setting": {\n'
        '        "tag_name": "",\n'
        '        "attrs": {}\n'
        '    },\n'
        '    "data_type": "text",\n'
        '    "parser_enable": false,\n'
        '    "parser_text_setting": {},\n'
        '    "file_save_enable": false,\n'
        '    "file_save_setting": {\n'
        '        "save_path": "default",\n'
        '        "text": {\n'
        '            "file_type": "txt",\n'
        '            "file_name": "default",\n'
        '            "page_cut_enable": false,\n'
        '            "limit_per_page": 0\n'
        '        },\n'
        '        "bin": {\n'
        '            "file_type": "png",\n'
        '            "file_name": "default"\n'
        '        }\n'
        '    }\n'
        '}\n',
        # 默认设置文件
        "settings":
        '{\n'
        '  "sleep": {\n'
        '    "enable": true,\n'
        '    "time": 3.0\n'
        '  },\n'
        '  "parser_message_out": {\n'
        '    "enable": false,\n'
        '    "mode": "err"\n'
        '  },\n'
        '  "asynchronous": {\n'
        '    "enable": false,\n'
        '    "ctrip_limit": 10\n'
        '  },\n'
        '  "folder_path": {\n'
        '    "file_input_path": "default",\n'
        '    "file_output_path": "default",\n'
        '    "configuration_path": "default",\n'
        '    "script_path": "default",\n'
        '    "temp_file_path": "default",\n'
        '    "log_path": "default"\n'
        '  },\n'
        '  "system_log_recording": {\n'
        '    "enable": false,\n'
        '    "log_file_name": "default"\n'
        '  },\n'
        '  "hide_title_bar": true,\n'
        '  "font": {\n'
        '    "family": "Segoe UI",\n'
        '    "title_size": 10,\n'
        '    "text_size": 9\n'
        '  },\n'
        '  "theme_name": "default"\n'
        '}\n',
        # 主要帮助文档
        "help_main":
        "",
        # 网略请求帮助文档
        "help_request":
        "",
        # 数据解析帮助文档
        "help_parse":
        '--title begin--\n'
        'CrAuto Parse 数据解析帮助文档\n'
        '版本: 2022.03.03\n'
        '--title end--\n'
        '\n'
        '--all begin--\n'
        '--pretreatment begin--\n'
        '网络响应所返回的内容可能包含过多数据, 本程序提供方法对响应内容做预处理, 可缩小数据提取的范围\n'
        '若需要进行预处理, 将 Conf.json 配置文件中 pretreatment@enable 设置为 true\n'
        '预处理基于 bs4(BeautifulSoup)@find_all 方法\n'
        '参数字典:\n'
        'tagName(str):   需要得到的目标标签名\n'
        '    "tagName": "div"\n'
        'attrs(dict):    标签属性参数\n'
        '    attrs: {\n'
        '        "class": "item",\n'
        '        "id": "1234"\n'
        '    }\n'
        '--pretreatment end--\n'
        '\n'
        '--parse begin--\n'
        '对于网页端返回的数据, 本程序将其分为三个类型[普通文本, json 文本, 二进制数据]\n'
        '针对不同的数据类型, 程序提供了不同的针对性解析方法, 在 Conf.json@parseLogic 中设置\n'
        '每一项设置的键使用特定格式: number@name 例如: 1@bs4 表示每行第一列数据由 bs4 解析方法得到\n'
        '\n'
        '"parseLogic": {\n'
        '    "onUse": "text",                // 使用的解析模式\n'
        '    "text": {\n'
        '        "1@bs4": {                  // 基于 bs4@select 方法, 支持 CSS 选择器\n'
        '            "selector": "",\n'
        '            "attribute": "@text",   // 查找属性, @text 为包含的文本\n'
        '            "index": "@all",        // 查找结果如有多个, 返回第几个, "@all" 为返回全部\n'
        '            "sep": " "              // 多值时填充字符, 默认为空格\n'
        '        },\n'
        '        "2@re": {                   // 基于 re@findall 方法, 支持正则表达式\n'
        '            "regular": "",\n'
        '            "flags": 0,             // 标志位 [S I M L U X], 默认为0\n'
        '            "index": "@all",        // 查找结果如有多个, 返回第几个, "@all" 为返回全部\n'
        '            "sep": " "              // 多值时填充字符, 默认为空格\n'
        '        },\n'
        '        "3@xpath": {                // 基于 lxml@etree 支持 xPath 语法\n'
        '            "xpath": "",\n'
        '            "mode": "html"          // 解析模式, html 或 xml\n'
        '            "index": "@all",        // 查找结果如有多个, 返回第几个, "@all" 为返回全部\n'
        '            "sep": " "              // 多值时填充字符, 默认为空格\n'
        '        }\n'
        '    },\n'
        '    "json": {},\n'
        '    "bin": {}\n'
        '}\n'
        '\n'
        '--parse_text begin--\n'
        '[普通文本: text]\n'
        '针对普通文本, 程序提供三种解析方法[bs4, re, xpath]\n'
        '\n'
        '--parse_text_bs4 begin--\n'
        '[bs4] 基于 bs4@select 方法, 支持 CSS 选择器\n'
        'selector:                     --标签匹配语句, 不能为空\n'
        '*   selector: "span"           +通过标签名查找\n'
        '*   selector: ".title"         +通过 class 属性值查找, 找到 class = "title" 的所有结果\n'
        '*   selector: "#1234"          +通过 id 值查找, 找到 id = "1234" 的所有结果\n'
        '*   selector: "span.title#1234"+组合查找, 找到 span 标签中 class = "title" 且 id = "1234" 的所有结果\n'
        '                                不使用[]进行属性匹配时, 组合查找不需要使用空格\n'
        '*   selector: \'span[alt="..."]\'+查找属性, 找到 span 标签中 alt 属性值为 ... 的所有结果\n'
        '*   selector: "span>p"         +查找 span 标签包含的所有 p 标签\n'
        'attribute:                    --返回匹配到的标签的内容, 默认为文本内容 @text\n'
        '*   attribute: xxx             +返回特定属性的值, 如: href 返回匹配到的标签中的 href 属性的值\n'
        '*   attribute: @text           +返回匹配到的标签中包含的文本\n'
        'index:                        --多内容选中项, 默认为全部 @all\n'
        '*   index: 1                   +若匹配到多个内容, 选择其中第1个\n'
        '*   index: @all                +选择匹配到的全部内容\n'
        'sep:                          --多内容间填充字符, 默认为空格\n'
        '*   sep: "+"                   +多内容之间以 + 分隔\n'
        '--parse_text_bs4 end--\n'
        '\n'
        '--parse_text_re begin--\n'
        '[re] 基于 re@findall 方法, 支持正则表达式匹配\n'
        'regular:          --正则表达式, 不能为空\n'
        'flags:            --标志位, 默认为0\n'
        '*   flags: "I"     +使匹配对大小写不敏感\n'
        '*   flags: "L"     +做本地化识别(locale-aware)匹配\n'
        '*   flags: "M"     +多行匹配\n'
        '*   flags: "S"     +使 . 匹配包括换行在内的所有字符\n'
        '*   flags: "U"     +根据 Unicode 字符集解析字符, 这个标志影响 \\w, \\W, \\b, \\B\n'
        '*   flags: "X"     +该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解\n'
        'index:            --多内容选中项, 默认为全部 @all\n'
        '*   index: 1       +若匹配到多个内容, 选择其中第1个\n'
        '*   index: @all    +选择匹配到的全部内容\n'
        'sep:              --多内容间填充字符, 默认为空格\n'
        '*   sep: "+"       +多内容之间以 + 分隔\n'
        '--parse_text_re end--\n'
        '\n'
        '--parse_text_xpath begin--\n'
        '[xpath] 基于 lxml@etree@xpath 方法, 支持 xPath 语法匹配\n'
        'xpath:            --xPath 语法, 不能为空, 末尾不加 /text() 或 /@... 的话视为 /text()\n'
        'mode:             --解析模式, ["html", "xml"]\n'
        'index:            --多内容选中项, 默认为全部 @all\n'
        '*   index: 1       +若匹配到多个内容, 选择其中第1个\n'
        '*   index: @all    +选择匹配到的全部内容\n'
        'sep:              --多内容间填充字符, 默认为空格\n'
        '*   sep: "+"       +多内容之间以 + 分隔\n'
        '[xPath: 用例]\n'
        '- *                 匹配任何一个节点\n'
        '- name              选择一个标签\n'
        '- /                 加在开头表示从根节点选取, 也用于元素之间的分割符\n'
        '- //                跳过多个层级选取一个节点, 不考虑其位置\n'
        '- .                 选择当前节点\n'
        '- ..                选取当前节点的父节点\n'
        '- /text()           必须加在表达式末尾, 表示选取始末标签之间的文本\n'
        '- /@                必须加在表达式末尾, 表示选取一个标签属性的值\n'
        '- name[index]       索引定位, 表示选取标签名相同的多个同层并列标签的第几个\n'
        '                    div[3]                  表示选取同层多个 div 标签的第三个, index 值从1开始\n'
        '                    div[last()]             表示选取同层多个 div 标签的最后一个, 支持减法运算\n'
        '                    div[last() - 1]         表示选取同层多个 div 标签的倒数第二个\n'
        '                    div[position() >= 5]    表示选取同层多个 div 标签中从第五个到最后一个\n'
        '- name[name2 >= 10]                 定位含有子标签 name2 且 name2 子标签的值大于等于10的名为 name1 的标签\n'
        '- name[@class=\'value\']              属性定位, div[@id=\'passw\'] 表示定位一个含有属性 id 且值为 passw 的 div 标签\n'
        '- name[contains(@class, "val")]     模糊定位, 定位到 class 属性值中包含 val 的名为 name 的标签\n'
        '- name[starts-with(@class, "val")]  模糊定位, 定位到 class 属性值中以 val 开头的名为 name 的标签\n'
        '- |                                 语法段连接, 表示获取满足左边或右边语法的节点(或)\n'
        '--parse_text_xpath end--\n'
        '--parse_text end--\n'
        '\n'
        '\n'
        '--parse_json begin--\n'
        '--parse_json end--\n'
        '\n'
        '\n'
        '--parse_bin begin--\n'
        '--parse_bin end--\n'
        '--parse end--\n'
        '--all end--\n',
        # 用户脚本帮助文档
        "help_script":
        ""
    }

    # Json文件注释内容
    # ///////////////////////////////////////////////////////////////
    FILE_JSON_TOP_COMMENT: dict = {}
    FILE_JSON_BOTTOM_COMMENT: dict = {
        # 配置样例文件注释
        "configuration":
        '/*\n'
        'Help Document:\n'
        '1. 请保证每个设置键的正确, 否则程序将无法识别和读取\n'
        '2. Cookie 的自动更新*可能*会影响到爬虫以外的正常登陆\n'
        '3. 请严格按照 Robot 协议使用爬虫, 非法使用后果自负\n'
        '\n'
        'Key Dictionary:\n'
        'urls:                  需要爬取的url,可填写多条\n'
        'request_method:        请求方式\n'
        'verify:                证书验证启用\n'
        'encoding:              编码方式\n'
        'data_form:             post表单\n'
        'data_form_script:      若使用自定义脚本构建 post 表单, 则设置脚本文件名以及参数列表\n'
        '  ∟ "fName":"args":    自定义脚本文件名以及向脚本传递的参数列表\n'
        'timeout:               超时时间,单位:秒\n'
        'headers:               网络请求头设置\n'
        'cookie_update_enable:  启用cookie自动更新\n'
        'cookies:               用户身份指纹设置\n'
        'user_agent_pool:       请求机器标识池,设置多条避免单机请求过量,若使用单一标识可直接在headers中设置\n'
        'ip_proxy_pool:         网络代理池,使用分布式ip代理,避免单一ip请求过量被封禁\n'
        'parser_enable:         启用数据解析\n'
        'data_type:             数据类型\n'
        'pretreatment_enable:   数据切分启用\n'
        'pretreatment_setting:  数据切分设置\n'
        '  ∟ tag_name:          查找标签名\n'
        '  ∟ attrs:             标签属性名和值\n'
        'parser_text_setting:   文本解析设置\n'
        '  ∟ text:              普通文本解析设置\n'
        '  ∟ bin:               二进制内容解析设置\n'
        'file_save_enable:      启用文件保存\n'
        'file_save_setting:     数据存储设置\n'
        '  ∟ text:              文本内容存储设置\n'
        '  ∟ bin:               二进制内容存储设置\n'
        '*/\n',
        # 设置文件注释
        "settings":
        '/*\n'
        'Help Document:\n'
        '1. 请保证每个设置键的正确, 否则程序将无法识别和读取\n'
        '2. 请按照注释提示进行编写, 以保证正确读取\n'
        '3. 请严格按照 Robot 协议使用爬虫, 非法使用后果自负\n'
        '\n'
        'Data Dictionary:\n'
        'sleep:                  请求间隔设置\n'
        '  ∟ time:               间隔时间, 需要大于等于1, 实际间隔时间为设置时间的 +- 最大 0.5s\n'
        'asynchronousCoroutines: 异步协程设置\n'
        '  ∟ loopLimit:          同步事件循环量, 过大可能导致目标服务器反爬\n'
        'parseMessageOut:        是否启用解析提示信息输出\n'
        '  ∟ mode:               输出模式, all: 全部, err: 仅错误, succ: 仅成功\n'
        '  ∟ errLimit:           错输数量阈值, 超过后解析暂停\n'
        'database:               数据库配置\n'
        '  ∟ onUse:              使用的数据库\n'
        'path:                   路径设置\n'
        'logFile:                日志设置\n'
        '  ∟ fileName:           日志文件名, default 默认为系统运行时间\n'
        '*/\n'
    }

    # Dat文件注释内容
    # ///////////////////////////////////////////////////////////////
    # 起始
    FILE_DAT_TOP_COMMENT: dict = {
        "local_configuration": '# TYPE: LIST\n'
        '# [NAME,PATH,UPDATE_TIME,STATUS,COMMENT]\n'
        '# STATUS => [RP:ALL_PASS][R:ONLY_HTTP_REQUEST][P:ONLY_DATA_PARSE][E:ERROR]\n\n',
        "custom_script": '# TYPE: LIST\n'
        '# [NAME,TYPE,PATH,UPDATE_TIME,COMMENT]\n'
        '# TYPE => [PYTHON,JS]\n\n'
    }
    # 结尾
    FILE_DAT_BOTTOM_COMMENT: dict = {}
