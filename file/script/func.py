# GCT DEFAULT SCRIPT FILE (PYTHON)
# ///////////////////////////////////////////////////////////////

# 导入
import sys

# 变量定义
data: dict = {}  # 该字典用于存储脚本需要输出的数据
args = sys.argv  # 使用此方式接收参数

# 函数定义
# 此处编写数据生成逻辑,将生成的数据存储到data字典即可
# ///////////////////////////////////////////////////////////////


def build() -> None:
    pass


# ///////////////////////////////////////////////////////////////

# 函数调用和数据输出
if __name__ == "__main__":
    build()
    print(data.__str__())
