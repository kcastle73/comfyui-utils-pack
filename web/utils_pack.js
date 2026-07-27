import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "ResolutionSelector.Extension",
    async nodeCreated(node) {
        console.log("UtilsPack.Extension: nodeCreated", node);
        // 只处理我们定义的那个节点
        if (node.comfyClass !== "ResolutionSelectorNode") return;

        // 找到下拉菜单 (mode) 和数值输入框 (int_value)
        const resolutionWidget = node.widgets.find(w => w.name === "resolution");
        const widthWidget = node.widgets.find(w => w.name === "width");
        const heightWidget = node.widgets.find(w => w.name === "height");
        if (!resolutionWidget || !widthWidget || !heightWidget) return;

        // 定义一个映射，将选项映射到对应的整数值
        const valueMap = {
            "720p": 1,
            "1080p": 1.5,
            "2k": 2,
            "4K": 3,
            "8k": 6,
            "custom": 0
        };

        // 保存原有的回调函数
        const origCallback = resolutionWidget.callback;
        // 覆盖下拉菜单的回调函数
        resolutionWidget.callback = function (value) {
            // 调用原有回调（如果有）
            if (origCallback) origCallback.call(this, value);

            // 核心逻辑：根据选择的值，更新 width 和 height 控件
            if (value) {
                // const [width, height] = [
                //     valueMap[value] * 720 || 512,
                //     valueMap[value] * 80 * 16 || 512
                // ];
                widthWidget.value = valueMap[value] * 720 || 512;
                heightWidget.value = valueMap[value] * 80 * 16 || 512;
            }
        };
    }
});