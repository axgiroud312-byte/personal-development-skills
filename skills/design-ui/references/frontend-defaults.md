# 前端默认搭配：通用 SaaS、工作台与 Agent 界面

这是用户选定的默认组合。新项目或新增能力尚未有明确方案时采用；用户当前要求与项目已确定的技术方案优先。已有项目先适配和复用，不因本表自动迁移技术栈或替换组件。

所有组件共用一套颜色、字体、间距、圆角和状态规则。同一种能力优先使用同一个方案，按页面与功能需要引入依赖；表中列出不代表全部安装。项目中选用的版本、组件、来源及必要例外记录在 Spec 或组件清单，后续任务沿用。

| 能力 | 默认方案 | 使用边界 |
| --- | --- | --- |
| 工程基础 | React + TypeScript + Tailwind CSS v4 | 作为新前端工程基础；路由、构建工具与应用外壳沿用项目决定 |
| 基础控件 | shadcn | 按钮、输入框、选择器、菜单、弹窗、标签页等统一采用并复用项目变体 |
| 图标 | Lucide | 新项目统一图标体系；已有项目遵循实际配置，不在局部混入第二套图标 |
| 动画 | Motion；简单悬停、颜色变化使用 CSS | 按交互需要选用，沿用减少动效规则，不为简单效果增加动画逻辑 |
| 普通布局 | CSS Grid / Flex | 根据内容和响应式需要布局 |
| 可调整宽度的分栏 | shadcn Resizable，底层 react-resizable-panels | 有可调整分栏需求时使用；普通布局仍用 Grid / Flex |
| 表单 | shadcn Field / FieldGroup + React Hook Form + Zod | 分别负责控件组织与反馈、表单状态、数据校验 |
| 数据表格 | shadcn Table + TanStack Table | Table 提供展示，TanStack Table 按需管理排序、筛选、分页等表格行为 |
| 仪表盘图表 | shadcn Chart + Recharts | 有图表需求时引入，消费统一的图表与状态颜色 |
| 日期选择与处理 | shadcn Calendar + Popover，按官方 Date Picker 方式组合；date-fns | 日期处理统一使用 date-fns，组件 API 以项目版本对应的官方示例为准 |
| 拖拽与排序 | dnd-kit | 有拖拽需求时加入，并处理键盘操作；不与分栏调整或节点画布混为一类 |
| 界面共享状态 | Zustand | 用于需要跨组件共享的界面状态；局部状态按组件需要处理 |
| 服务端数据获取与缓存 | TanStack Query | 管理服务端数据及缓存，不把同一份服务端数据重复当作 Zustand 的独立真相 |
| Agent 界面 | shadcn 当前 AI Elements 组合模式及聊天组件 | 按当前官方文档及项目消息协议组合，不照搬不相容的旧版示例 |
| AI 流式 Markdown | Streamdown | 负责流式 Markdown 呈现，与消息传输和状态管理分工 |
| 新建聊天接口的流式连接与消息状态 | AI SDK | 已有 Agent 后端先适配其协议和已有客户端，不为了套用 SDK 重写后端协议 |
| 节点式工作流画布 | React Flow | 需要节点连线编辑器时加入 |
| 玻璃效果 | Tailwind / 原生 CSS | 统一封装一个玻璃面板样式，消费共享 Token，避免每页各写一套 |
| 页面起点 | shadcn 官方 Blocks 优先 | 再按需要补充相容的社区区块，记录明确来源并融入本项目设计 |

## 使用与维护

- 先确定本页需要哪些能力，再核对项目现有依赖、锁文件与已安装组件。选型清单说明直接复用、按需新增或有理由的例外；用户已选的默认组合无需反复比较排行榜。
- Zustand 管界面共享状态，TanStack Query 管服务端资源与缓存，AI SDK 或既有 Agent 适配层管理消息流与消息状态。保持职责清楚，避免把同一数据复制到多个独立状态源后分别维护。
- 组件、区块与聊天组合在使用时读取当前官方文档，并与实际版本、shadcn 底层组件体系、导入别名和图标配置匹配。此表规定方案选择，不固定安装命令或 API 写法，不混用不同版本的示例。
- Motion、dnd-kit、React Flow 分别服务于动效、拖放和节点连线编辑；只在存在对应需求时加入。表格、图表、日期和聊天能力同样按需使用。
- 改变某项已确定方案时记录原因，并同步设计规范、Spec、受影响的 Issue 与实现。保持全产品的 Token、尺寸、变体及操作反馈一致。

## 官方文档入口

- [Resizable](https://ui.shadcn.com/docs/components/resizable)、[React Hook Form 表单](https://ui.shadcn.com/docs/forms/react-hook-form)、[Data Table](https://ui.shadcn.com/docs/components/data-table)
- [Chart](https://ui.shadcn.com/docs/components/chart)、[Date Picker](https://ui.shadcn.com/docs/components/date-picker)、[官方 Blocks](https://ui.shadcn.com/blocks)
- [AI Elements](https://ui.shadcn.com/docs/ai-elements)、[Streamdown](https://streamdown.ai/docs)、[AI SDK 流协议](https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol)
- [Motion](https://motion.dev/docs/react)、[dnd-kit](https://dndkit.com/react/quickstart/)、[React Flow](https://reactflow.dev/learn)
