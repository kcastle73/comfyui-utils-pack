# comfyui-utils-pack

ComfyUI 实用工具节点集合，提供分辨率选择、日期格式化、文件名提取等常用功能。

## 安装

1. 将本仓库克隆到 ComfyUI 的 `custom_nodes` 目录：

   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/<your-username>/comfyui-utils-pack.git
   ```

2. 重启 ComfyUI 即可生效。

## 节点说明

所有节点归属于 **UtilsPack** 分类。

### Resolution Selector

分辨率选择器，快速选择常用分辨率或自定义宽高。

**输入：**

| 参数 | 类型 | 说明 |
|---|---|---|
| `resolution` | 下拉选择 | 预设分辨率：720p、1080p、2K、4K、8K、custom |
| `width` | INT | 宽度，范围 256 - 38400，默认 2560 |
| `height` | INT | 高度，范围 256 - 38400，默认 1440 |

**输出：**

| 名称 | 类型 | 说明 |
|---|---|---|
| `width` | INT | 实际宽度 |
| `height` | INT | 实际高度 |
| `pixels` | INT | 总像素（width × height）|

### Get Formatted System Date

获取当前系统日期和时间，支持自定义格式。

**输入：**

| 参数 | 类型 | 说明 |
|---|---|---|
| `format_str` | STRING | 日期格式字符串，默认 `%Y-%m-%d %H:%M:%S` |

**输出：**

| 名称 | 类型 | 说明 |
|---|---|---|
| (无) | STRING | 格式化后的日期时间字符串 |

**常用格式参考：**

| 格式 | 示例输出 |
|---|---|
| `%Y-%m-%d %H:%M:%S` | `2026-07-31 14:30:00` |
| `%Y-%m-%d` | `2026-07-31` |
| `%H:%M:%S` | `14:30:00` |
| `%Y%m%d_%H%M%S` | `20260731_143000` |

### Extract File Name

从完整文件路径中提取文件名（不含扩展名）。

**输入：**

| 参数 | 类型 | 说明 |
|---|---|---|
| `file_path` | STRING | 完整文件路径 |

**输出：**

| 名称 | 类型 | 说明 |
|---|---|---|
| `filename` | STRING | 提取的文件名（不含扩展名）|

**示例：**

| 输入 | 输出 |
|---|---|
| `/path/to/image.png` | `image` |
| `./data/model_v2.safetensors` | `model_v2` |

## 目录结构

```
comfyui-utils-pack/
├── __init__.py          # 插件入口，节点注册
├── utils_pack.py        # 节点实现
├── web/
│   └── utils_pack.js    # 前端资源
├── README.md            # 本文档
├── CONTRIBUTING.md      # 贡献指南
└── CHANGELOG.md         # 变更记录
```

## 贡献

欢迎提交 Issue 和 Pull Request。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

MIT License
