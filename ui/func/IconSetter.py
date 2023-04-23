# 图标设置函数
# ///////////////////////////////////////////////////////////////
import os


class IconSetter:
    """图标设置工具类
    """

    @staticmethod
    def setSvgIcon(iconName):
        iconPath = os.path.normpath(os.path.join(os.path.abspath(os.getcwd()), "ui/resources/icons/", iconName))
        if os.path.exists(iconPath) is False: iconPath = iconPath.replace(iconName, "no_icon.svg")
        # print(icon_path)
        return iconPath

    @staticmethod
    def setImage(imageName):
        imagePath = os.path.normpath(os.path.join(os.path.abspath(os.getcwd()), "ui/resources/images/", imageName))
        if os.path.exists(imagePath) is False: imagePath = imagePath.replace(imageName, "no_image.png")
        return imagePath
