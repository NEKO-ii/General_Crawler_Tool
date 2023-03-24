# 图标设置函数
# ///////////////////////////////////////////////////////////////
import os


class IconSetter:
    """图标设置工具类
    """

    @staticmethod
    def set_svg_icon(icon_name):
        icon_path = os.path.normpath(os.path.join(os.path.abspath(os.getcwd()), "ui/resources/icons/", icon_name))
        if os.path.exists(icon_path) is False: icon_path = icon_path.replace(icon_name, "no_icon.svg")
        # print(icon_path)
        return icon_path

    @staticmethod
    def set_image(image_name):
        image_path = os.path.normpath(os.path.join(os.path.abspath(os.getcwd()), "ui/resources/images/", image_name))
        if os.path.exists(image_path) is False: image_path = image_path.replace(image_name, "no_image.png")
        return image_path
