# 贡献指南

感谢你为 comfyui-utils-pack 做出贡献！

## 开发环境

1. 确保已安装 ComfyUI 并正常运行
2. 将本仓库链接到 `custom_nodes` 目录
3. 修改代码后重启 ComfyUI 即可看到效果

## 添加新节点

新节点需添加到 `utils_pack.py`，遵循以下规范：

### 1. 定义节点类

```python
class YourNodeName:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # 输入参数定义
            }
        }

    RETURN_TYPES = ("TYPE1", "TYPE2")
    RETURN_NAMES = ("output1", "output2")
    FUNCTION = "execute"
    CATEGORY = "UtilsPack"

    def execute(self, param1, param2):
        # 实现逻辑
        return (result1, result2)
```

### 2. 注册节点

在文件底部的映射表中注册：

```python
NODE_CLASS_MAPPINGS = {
    # ... 已有节点
    "YourNodeName": YourNodeName,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # ... 已有节点
    "YourNodeName": "Your Node Display Name",
}
```

### 编码规范

- 使用 4 空格缩进
- 类名使用 `PascalCase`，函数/变量名使用 `snake_case`
- 节点类统一使用 `execute` 作为执行方法名
- 所有节点归类到 `UtilsPack` 分类
- 输入参数添加合理的默认值和范围限制
- 中文注释用于说明参数用途

### 提交规范

提交信息建议使用以下格式：

- `feat: 添加新节点 XXX`
- `fix: 修复 XXX 节点的问题`
- `docs: 更新文档`
- `refactor: 重构 XXX`

## 测试

修改后请在 ComfyUI 中验证：

1. 重启 ComfyUI
2. 在节点搜索中确认新节点出现在 **UtilsPack** 分类下
3. 连接节点测试输入/输出是否正常
