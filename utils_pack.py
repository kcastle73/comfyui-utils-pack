from datetime import datetime
import os

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

class GetFormattedSystemDateNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "format_str": ("STRING", {"default": "%Y-%m-%d %H:%M:%S"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self, format_str):
        return (datetime.now().strftime(format_str),)

class ExtractFileNameNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"default": "", "multiline": False, "label": "File Path"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self, file_path):
        return (os.path.splitext(os.path.basename(file_path))[0],)


NODE_CLASS_MAPPINGS = {
    "ResolutionSelectorNode": ResolutionSelectorNode,
    "GetFormattedSystemDateNode": GetFormattedSystemDateNode,  
    "ExtractFileNameNode": ExtractFileNameNode, 
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionSelectorNode": "Resolution Selector",
    "GetFormattedSystemDateNode": "Get Formatted System Date",   
    "ExtractFileNameNode": "Extract File Name", 
}