# 去除JSON字符串注释
# ///////////////////////////////////////////////////////////////
from re import findall

def remove_json_comments(json_str: str) -> str:
    """去除JSON字符串中的注释,包括行注释(//)与块注释(/**/)

    Args:
        json_str (str): 原始JSON字符串

    Returns:
        str: 去除注释后的JSON字符串
    """
    pos = 0
    b_pos = 0
    flg = '/'
    is_math_model = False

    while (True):
        pos = json_str.find(flg, pos)
        if pos > -1:
            if is_math_model:
                json_str = json_str[:b_pos - 1] + json_str[pos + len(flg):]
                pos = b_pos
                is_math_model = False
                flg = '/'
                continue

            line_begin_pos = json_str.rfind('\n', 0, pos)
            line_str = json_str[line_begin_pos:pos]
            num = len(findall('"', line_str))

            if num % 2 == 0:
                if json_str[pos + 1] == '*':
                    flg = '*/'
                    is_math_model = True
                    b_pos = pos
                    continue
                elif json_str[pos + 1] == "/":
                    line_end_pos = json_str.find('\n', pos)
                    json_str = json_str[:pos - 1] + json_str[line_end_pos:]
                    continue

            pos = pos + 1
        else:
            break

    return json_str
