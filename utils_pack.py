from datetime import datetime

class ResolutionSelectorNode:
    @classmethod
    def INPUT_TYPES(cls):
        # 定义下拉选项和数值输入框
        return {
            "required": {
                "resolution": (["720p", "1080p", "2k", "4K","8k","custom"], {"default": "2k"}),
                "width": ("INT", {"default": 2560, "min": 256, "max": 38400}),
                "height": ("INT", {"default": 1440, "min": 256, "max": 38400}),
            }
        }

    # 输出类型为整数
    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "pixels")
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self, resolution, width, height):
        # 节点执行时，直接返回当前 int_value 的值
        return (width,height, width * height)

class GetSystemDateNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    # 输出类型为整数
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("date",)
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self):
        return (datetime.now().strftime("%Y-%m-%d"),)
        # now=datetime.now()
        # date_str = now.strftime(date_format)
        # return (date_str,)

class GetCurrentTimeNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    # 输出类型为整数
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("time",)
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self):
        return (datetime.now().strftime("%H%M%S"),)
        # now = datetime.now()
        # time_str = now.strftime(time_format)
        # return (time_str,)


# 文件末尾
NODE_CLASS_MAPPINGS = {
    "ResolutionSelectorNode": ResolutionSelectorNode,
    "GetSystemDateNode": GetSystemDateNode,   # 添加这一行
    "GetCurrentTimeNode": GetCurrentTimeNode,   # 添加这一行
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionSelectorNode": "Resolution Selector",
    "GetSystemDateNode": "Get System Date",   # 可选显示名称
    "GetCurrentTimeNode": "Get Current Time",   # 可选显示名称
}