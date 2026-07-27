# from .utils_pack import ResolutionSelectorNode as ResolutionSelector
# # 必须指定前端文件夹
# WEB_DIRECTORY = "./web" 

# NODE_CLASS_MAPPINGS = {
#     "UtilsPack": ResolutionSelector,
# }

WEB_DIRECTORY = "./web" 

from .utils_pack import NODE_CLASS_MAPPINGS as nodes_mappings
from .utils_pack import NODE_DISPLAY_NAME_MAPPINGS as nodes_display

NODE_CLASS_MAPPINGS = {**nodes_mappings}
NODE_DISPLAY_NAME_MAPPINGS = {**nodes_display}