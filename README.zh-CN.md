# HTML Brifing

<p align="center">
  <a href="README.md"><img src="assets/lang-en.svg" alt="Read in English" width="132" height="40"></a>
  <a href="README.zh-CN.md"><img src="assets/lang-zh.svg" alt="切换到简体中文" width="132" height="40"></a>
</p>

![HTML Brifing：项目证据、清晰叙事与离线汇报](assets/cover.zh-CN.svg)

组合你已有的设计、图表、图像、文字和浏览器技能，把项目材料做成有证据支撑的 HTML 汇报。适合需要解释工作机制与结果的技术团队、研究者和业务实践者。

**一个入口，保留已有技能，交付可查看、可操作的解释。**

[安装](#1-安装) · [试用请求](#3-使用) · [下载 v0.2.0](https://github.com/thejaytang/html-brifing/releases/tag/v0.2.0) · [能力映射](plugins/html-brifing/skills/html-brifing/references/capabilities.md)

标识符有意保留为 `html-brifing`。这是技能编排插件，不是幻灯片编辑器或自动依赖管理器。

## 1. 安装

需要支持插件的 Codex、文件访问能力和已授权的项目工作区。实际渲染验收需要浏览器。插件内置 5 个技能，包含作者维护的学术写作、科研绘图和结果表技能。外部配套技能及运行依赖不会自动安装。

```sh
codex plugin marketplace add thejaytang/html-brifing --ref v0.2.0
codex plugin add html-brifing@html-brifing
```

安装后开启**新聊天**，必要时选择 **HTML Brifing**，先运行一次 `$html-brifing-setup`：检查 5 个内置技能，并完整建议下方 8 组配套能力，区分可用、缺失和未知。随后用 `$html-brifing` 制作汇报。主技能也会引导首次使用者完成检查；安装插件本身不会自动执行设置钩子。已有设计、ImageGen、写作与图表技能无需删除或覆盖。如果保留了旧的个人汇报技能，每个任务选择一个汇报主入口。

使用发布压缩包时，解压并进入 `html-brifing-0.2.0` 目录，然后运行：

```sh
codex plugin marketplace add .
codex plugin add html-brifing@html-brifing
```

两条安装路径选择一条即可。更新和切换来源见[维护说明](docs/maintenance.md)。压缩包包含插件市场入口；不要只取内层插件目录来执行上述安装流程。

## 2. 内置技能与配套建议

插件详情页应列出 **5 个技能**。外部配套技能仍显示在各自安装项下，不计入本插件的技能数量。已有个人版本会保留；明确指定已有版本时优先使用，否则使用本插件内置版本。

| 内置技能 | 用途 | 来源与许可 |
|---|---|---|
| [html-brifing](plugins/html-brifing/skills/html-brifing/SKILL.md) | 叙事、设计统筹、图解、交互与交付验收 | Jay Tang；MIT |
| [html-brifing-setup](plugins/html-brifing/skills/html-brifing-setup/SKILL.md) | 首次使用盘点与完整配套建议 | Jay Tang；MIT |
| [academic-humanizer](plugins/html-brifing/skills/academic-humanizer/SKILL.md) | 保留事实与证据边界的学术表达 | [作者维护的上游](https://github.com/thejaytang/academic-humanizer)；[MIT 与上游署名](plugins/html-brifing/skills/academic-humanizer/LICENSE) |
| [academic-research-plotting](plugins/html-brifing/skills/academic-research-plotting/SKILL.md) | 科研图表选择、样式、检查与导出 | [作者维护的上游](https://github.com/thejaytang/academic-research-plotting)；[MIT](plugins/html-brifing/skills/academic-research-plotting/LICENSE) |
| [research-results-tables](plugins/html-brifing/skills/research-results-tables/SKILL.md) | 数值核对与实证结果表 | Jay Tang；[MIT](plugins/html-brifing/skills/research-results-tables/LICENSE) |

所需参考资料、绘图脚本和预设一起打包。运行绘图脚本需要 Matplotlib；缺失时按项目约定在隔离环境中安装依赖。安装技能不等于安装 Python 依赖。

首次使用建议补齐以下 **8 组配套能力**，每份汇报按实际需要调用。已有技能保留；仅在获得授权后安装缺失项。

| 外部配套技能 | 来源与作者 | 职责 |
|---|---|---|
| Impeccable | [pbakaus](https://github.com/pbakaus/impeccable) | 主视觉系统与视觉审查 |
| UI UX Pro Max | [nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 补充设计参考 |
| Humanizer | [blader](https://github.com/blader/humanizer) | 普通文字优化 |
| GSAP Skills | [GreenSock](https://github.com/greensock/gsap-skills) | 动效与对象连续性 |
| ImageGen | [OpenAI 技能](https://github.com/openai/skills/blob/main/skills/.system/imagegen/SKILL.md) | 位图插画、图片编辑与透明素材 |
| Playwright 或可用的宿主浏览器 | [OpenAI 技能](https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md) | 实际渲染与交互验收 |
| Ponytail | [DietrichGebert](https://github.com/DietrichGebert/ponytail) | 简洁且完整的代码实现 |
| Visualize | OpenAI 宿主插件目录；未核实独立公开仓库 | 对话内可视化探索 |

Academic Humanizer 是作者维护的衍生工作，原有 AIScientists-Dev、Kiterlin 等署名与来源说明均保留。完整来源及早期工作流借鉴见[来源说明](plugins/html-brifing/skills/html-brifing/references/sources.md)。

## 3. 使用

下列为示例请求，不代表已测量的业务效果：

| 场景与输入 | 请求 | 预期交付及成功条件 |
|---|---|---|
| 有项目说明与测试记录的技术项目 | “使用 $html-brifing，为不熟悉项目的同事制作 10 分钟离线 HTML 汇报。” | 上下文、设计、机制与实测结果完整；最终文件经过离线打开验收 |
| 交互混乱的已有汇报 | “使用 $html-brifing，修复这份 HTML 的嵌套说明，保留叙事和视觉方向。” | 局部修复；受影响对象的选择、切换和折叠没有残留说明 |
| 需要形象解释的概念 | “使用 $html-brifing，用 ImageGen 插画与可编辑标签解释这个机制。” | 检查后的概念图、精确标签和完整素材包；生成工具缺失时说明缺口 |
| 仍处在讨论阶段 | “使用 $html-brifing，审阅材料并只给提纲。” | 基于证据的提纲；不实施、不安装、不发布 |

可直接用浏览器打开[虚构离线示例](examples/offline-routing.html)，查看绑定到对象的展开说明。它不连接真实排程系统。

## 4. 如何组合

![流程：证据与听众目标进入主技能，按需使用已有技能统一制作，再验收最终文件](assets/workflow.zh-CN.svg)

主技能确定听众、论证和证据，选择当前可用的相关辅助技能，统一它们的输出，并验收最终汇报。图示说明工作流程，不代表自动执行引擎。

| 能力 | 优先复用的技能 | 提供什么 |
|---|---|---|
| 视觉系统 | Impeccable，按需参考 UI UX Pro Max | 统一层级、布局、字体与状态 |
| 数据图表与表格 | academic-research-plotting、research-results-tables 或等价技能 | 明确指标、忠实图表与核对后的结果表 |
| 位图视觉表达 | ImageGen | 场景、对象、插画、图片编辑和透明素材 |
| 精确关系表达 | 原生 HTML/SVG 与内置图解规则 | 可编辑标签、架构、字段映射和交互 |
| 有解释作用的动效 | 所需的 GSAP 技能 | 对象连续性与联动状态 |
| 文字 | Humanizer 或 academic-humanizer | 保持事实含义的自然表达 |
| 代码实现 | 项目规则；可用时使用 Ponytail | 不牺牲验收的简洁完整实现 |
| 验收 | 宿主浏览器工具或 Playwright | 实际渲染、操作与交付检查 |
| 聊天内探索 | 可用时使用 Visualize | 对话内预览，与离线交付物分开 |

辅助技能缺失时采用已写明的基础路径。必要的浏览器或图像生成工具缺失时保留明确缺口。技能文件本身不提供模型、运行环境、凭据或服务权限；不得静默切换到付费 ImageGen API。

## 5. 沉淀的实践经验

- 先让陌生听众理解业务上下文，再进入实现细节。
- 主视图保留方案核心，次要说明绑定到具体对象。
- 控件改变证据、操作或输出，不能只改变装饰。
- 跨场景保持对象身份，正确清理嵌套展开和选中状态。
- 把测试方法、观察结果与可支持的结论放在一起。
- 验收移动或解压后的最终包；开发服务器运行或 Mac 截图不能证明 Windows 离线验收。

[经验沉淀说明](plugins/html-brifing/skills/html-brifing/references/experience.md)区分通用经验与可覆盖的标题、导航、动效偏好。仓库不包含私有业务数据或项目截图。

## 6. 适用范围、兼容性与限制

适用于项目汇报、研究解释、技术演示和讲者控制的 HTML 报告。生产应用使用网站开发流程，可编辑 PPTX 使用原生演示流程，纯文字周报使用普通写作流程。

| 环境 | 范围 |
|---|---|
| macOS 上的 Codex | 本次发布目标；实际安装与包验证证据见验证记录 |
| Windows / Linux | 文件和资源可迁移，但尚未验证原生安装和渲染验收 |
| 其他技能宿主 | 不声明兼容；需适配并验证宿主工具和插件格式 |
| ImageGen、GSAP 等辅助能力 | 外部可选能力；本次发布未逐一运行所有组合 |
| 离线输出 | 新建独立本地汇报的制作要求，逐份验收；插件安装本身可能联网 |

Agent 根据规则执行工作流，插件不保证确定性的技能调度或所有输出都正确。技能说明以英文为主，详细交付清单保留中文。两份 README 描述相同能力，不等于已验证双语运行表现。

## 7. 开发、证据与来源

```sh
python3 scripts/check_package.py
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.lock
.venv/bin/python -m unittest discover -s tests
```

检查工具只需要 Python 3.10+ 标准库。完整测试还会运行内置绘图脚本；锁文件记录本次 Python 3.12 macOS 测试环境。其他系统需使用对应的虚拟环境执行路径，原生验收尚未验证。结构检查不代替浏览器验收。贡献前阅读 [AGENTS.md](AGENTS.md)、[当前状态](PROJECT_STATE.md)和[发布验证记录](project-support/evaluation-0.2.0.md)。复现报告请说明场景、状态、窗口和输入，不附私有材料。

[来源与可选上游](plugins/html-brifing/skills/html-brifing/references/sources.md)区分借鉴来源、推荐技能和宿主文档。外部配套技能保持独立；内置的作者维护衍生技能保留上游许可与署名。

[MIT 许可](LICENSE)，版权所有 2026 Jay Tang，覆盖本仓库原创规则、图形和检查工具。外部技能、库和服务保留各自条款。欢迎通过 [Issues](https://github.com/thejaytang/html-brifing/issues) 反馈。
