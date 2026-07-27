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

    # 输出类型
    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "pixels")
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self, resolution, width, height):
        return (width,height, width * height)

class GetSystemDateNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("date",)
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self):
        return (datetime.now().strftime("%Y-%m-%d"),)

class GetCurrentTimeNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("time",)
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self):
        return (datetime.now().strftime("%H%M%S"),)


NODE_CLASS_MAPPINGS = {
    "ResolutionSelectorNode": ResolutionSelectorNode,
    "GetSystemDateNode": GetSystemDateNode,  
    "GetCurrentTimeNode": GetCurrentTimeNode, 
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionSelectorNode": "Resolution Selector",
    "GetSystemDateNode": "Get System Date",   
    "GetCurrentTimeNode": "Get Current Time", 
}