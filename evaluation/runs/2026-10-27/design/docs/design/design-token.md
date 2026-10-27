# 订阅管理 · 设计 Token

对应文件：`design-board.html`。以下值直接取自本版 HTML 的 `:root`、实际选择器与交互代码；未另建独立主题。目标窗口为 **1440 × 900**，仅制作桌面布局。

## 1. 继承的参考变量

保留项目 `design-reference.html` 中全部六个变量的名称和值。

| 名称 | 实际值 | 用途与对应位置 |
| --- | --- | --- |
| `--bg` | `#f7f7f2` | `body` 与 `.sidebar` 的基础背景 |
| `--text` | `#17251f` | 正文、标题；成功反馈浮层的深色背景 |
| `--accent` | `#28775b` | 主要按钮、当前导航、选中标签、原生复选框与单选框 |
| `--nav-width` | `224px` | 页面左列宽度；成功反馈的横向定位计算 |
| `--row-height` | `44px` | 列表与扣款记录表格的 `th, td` 高度 |
| `--motion-duration` | `200ms` | 弹窗、抽屉与遮罩的打开和关闭动画；关闭延时由此 CSS 变量读取 |

## 2. 颜色

| 名称 | 实际值 | 用途与对应位置 |
| --- | --- | --- |
| `--surface` | `#ffffff` | `.panel`、表单控件、弹窗与抽屉背景；主要按钮与成功反馈文字 |
| `--surface-subtle` | `#f1f4ee` | 表头、次级悬停、缩写方块、浮层操作区、提醒预览 |
| `--surface-hover` | `#f4f7f1` | 表格行悬停与次要按钮悬停 |
| `--muted` | `#617067` | 描述、字段说明、表头、辅助信息、非当前标签 |
| `--border` | `#d6ded7` | 导航分隔、容器边框、表格横线、普通分隔线 |
| `--border-strong` | `#b7c5bc` | 控件与次要按钮边框、面包屑分隔符 |
| `--accent-soft` | `#e7f0e8` | 当前导航、选中页码、有效筛选、续订中状态、选中单选项 |
| `--accent-hover` | `#206249` | 主要按钮与文字按钮的悬停颜色 |
| `--accent-pressed` | `#194e3a` | 主要按钮按下颜色 |
| `--focus` | `rgba(40, 119, 91, .22)` | `:focus-visible` 的焦点外圈 |
| `--warning` | `#946315` | `.status.paused` 的文字与状态点 |
| `--warning-bg` | `#fff3da` | 已暂停状态背景 |
| `--neutral` | `#5f6b64` | `.status.cancelled` 的文字与状态点 |
| `--neutral-bg` | `#edf0ec` | 已取消状态背景 |
| `--danger` | `#a83d35` | `.control:user-invalid` 的边框 |
| `--danger-bg` | `#fff4f1` | `.control:user-invalid` 的背景 |
| `--backdrop` | `rgba(23, 37, 31, .28)` | 原生 `dialog::backdrop` 遮罩 |

状态同时使用文字、颜色与小圆点表达；没有只依赖颜色的业务状态。没有图片背景或渐变。

## 3. 字体与排版

### 字体来源

`--font-family` 的实际值为：

```css
system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
"Hiragino Sans GB", "Microsoft YaHei", sans-serif
```

由用户操作系统实际解析与渲染，无 `@font-face`、无下载字体、无联网依赖。`system-ui` 优先，后续名称提供系统及中文回退；具体使用哪种字形、700 字重是否由系统字体提供或合成，取决于运行环境。按钮、输入框与下拉框通过 `font: inherit` 继承这套字体。

| 名称 | 实际值 | 用途与对应位置 |
| --- | --- | --- |
| `--font-weight-body` | `400` | 正文、表头、控件、状态标签 |
| `--font-weight-heading` | `700` | 标题、`strong`、品牌文字、选中导航/页码/标签、详情金额、缩写方块 |
| `--font-size-xs` | `12px` | 表头、状态、辅助说明、面包屑、计费单位、分页说明、来源区 |
| `--font-size-sm` | `13px` | 页面描述、设置子导航、表单标签、成功反馈、返回按钮 |
| `--font-size-base` | `14px` | 正文、表格内容、按钮、紧凑工具栏标题 |
| `--font-size-lg` | `16px` | 区块标题、详情缩写方块 |
| `--font-size-metric` | `24px` | 详情金额 |
| `--font-size-title` | `28px` | 页面 `h1` |
| `--line-height-body` | `1.5` | 正文；14px 对应 21px 行高 |
| `--line-height-heading` | `1.25` | 标题；28px 页面标题对应 35px 行高 |
| `--tracking-heading` | `-.025em` | 页面标题、浮层标题与详情指标 |
| `--tracking-meta` | `.01em` | 侧栏分组说明 |

以下排版值为选择器中的直接声明，没有额外创建变量：

| 对应位置 | 实际值 |
| --- | --- |
| `h2`（浮层标题） | `20px / 1.25`，700 |
| `.panel-heading h2` | `16px / 1.25`，700，字间距 `0` |
| `.table-heading h2` | `14px / 1.25`，700，字间距 `0` |
| `.brand-name` | `19px`，700，字间距 `-.02em` |
| `.service-mark` | `10px`，700，字间距 `-.02em` |
| `.detail-metric dd` | 行高 `1.3`，最小高度 `32px` |
| `.detail-metric dd.date-value` | `20px`，700 |
| `.control` | 行高 `20px` |
| `.button` | 行高 `1` |
| `.sources-content code` | `11px`；浏览器默认代码字体 |
| `.numeric` | `font-variant-numeric: tabular-nums`，用于金额、日期、分页与数量 |

## 4. 桌面布局与密度

### 全局布局

| 名称或选择器 | 实际值 | 对应位置与行为 |
| --- | --- | --- |
| `body` | `grid-template-columns: 224px minmax(0, 1fr)` | 固定左导航与自适应内容列 |
| `body` | `min-width: 1080px; min-height: 100vh` | 保持桌面布局；窄于 1080px 时横向滚动 |
| `--page-padding` | `32px` | `main` 四周内边距 |
| `.sidebar` | `position: sticky; top: 0; height: 100vh` | 侧栏随页面保持可见 |
| `.sidebar` | `padding: 24px 16px` | 侧栏内边距 |
| `.brand` | 高 `36px`，下间距 `38px`，左右内边距 `8px` | 品牌与主导航的分组 |
| `.nav-children` | 左外边距 `21px`，左内边距 `13px`，左边框 `1px` | 设置的二级导航缩进 |
| `.breadcrumb` | 最小高 `18px`，下间距 `20px`，内部间距 `8px` | 当前层级 |
| `.page-header` | 下间距 `24px`，内容间距 `24px` | 标题与主要操作 |
| `.page-description` | 顶部间距 `8px` | 标题下说明 |
| `#view` | `flex: 1` | 首屏优先呈现产品，折叠来源位于底部 |
| `.sources` | 顶部外边距 `32px`、内边距 `16px`、上边框 `1px` | 折叠组件与来源说明 |
| `.sources-content` | `max-width: 960px` | 展开后的说明阅读宽度 |

在 1440px 宽窗口下，内容列为 `1440 - 224 = 1216px`，扣除左右 32px 内边距后的内容宽为 **1152px**。

### 表格与分页

| 名称或选择器 | 实际值 | 对应位置 |
| --- | --- | --- |
| `--toolbar-height` | `56px` | 列表工具栏最小高度 |
| `.table-toolbar` | `padding: 8px 20px` | 标题、数量与筛选按钮 |
| `--row-height` | `44px` | 表头、订阅行、扣款记录行 |
| `th, td` | `padding: 0 20px` | 表格单元格水平留白 |
| `table` | `width: 100%; table-layout: fixed; border-collapse: collapse` | 固定列分配、合并分隔线 |
| `.subscription-table col` | `38% / 18% / 20% / 14% / 10%` | 名称 / 金额 / 续订日期 / 状态 / 操作 |
| `.subscription-table` 最后一列 | `text-align: right` | 操作列右对齐 |
| `.records-table col` | `24% / 22% / 36% / 18%` | 扣款日期 / 金额 / 对应周期 / 结果 |
| `.service-mark` | `26 × 26px`，与名称间距 `12px` | 列表中的服务缩写 |
| `.service-name` | 单行省略，`text-overflow: ellipsis` | 长名称仍保留完整详情入口与无障碍名称 |
| `--pager-height` | `60px` | 分页区最小高度 |
| `.pager` | `padding: 12px 20px` | 分页说明与分页按钮组 |
| `.page-number` | 最小 `32 × 32px` | 页码按钮 |
| `.page-arrow` | 最小高 `32px`、水平内边距 `8px` | 上一页、下一页 |
| `PAGE_SIZE`（脚本常量） | `5` | 初始 12 条数据对应 3 页，第三页 2 条 |
| `.empty-state` | `padding: 48px 24px` | 无匹配订阅、无扣款记录 |

### 详情与设置

| 名称或选择器 | 实际值 | 对应位置 |
| --- | --- | --- |
| `.detail-heading .service-mark` | `48 × 48px`，圆角 `12px` | 详情标题缩写方块 |
| `.tabs` | 标签间距 `24px`，底部边框 `1px`，下间距 `24px` | 概览 / 扣款记录 |
| `.tab` | 最小高 `44px`，水平内边距 `4px`，选中下划线 `2px` | 原生按钮实现的页内标签 |
| `.panel-heading` | `padding: 20px 24px` | 详情、设置区块标题 |
| `.detail-metrics` | `grid-template-columns: 1fr 1fr 1fr; padding: 24px` | 金额、续订日期、状态三列 |
| `.detail-metric` | 水平内边距 `24px`，列间边框 `1px` | 第一列去左内边距与左边框 |
| `.detail-info` | `1fr 1fr`；行间距 `24px`、列间距 `32px`；内边距 `24px` | 详情字段两列，备注跨两列 |
| `--settings-width` | `880px` | 通用与提醒表单最大宽度 |
| `.setting-row` | `minmax(0, 1fr) 240px`，列间距 `32px` | 左侧标签说明，右侧控件 |
| `.setting-row` | 左右外边距 `24px`、垂直内边距 `20px` | 设置条目密度 |
| `.settings-actions` | 顶部间距 `20px`，内部间距 `16px` | 说明与恢复默认 / 保存设置 |
| `.reminder-preview` | 内边距 `16px`；外边距 `20px 24px 24px` | 提醒时间示例 |

## 5. 间距与控件

### 间距变量

| 名称 | 实际值 | 主要使用位置 |
| --- | --- | --- |
| `--space-1` | `4px` | 状态单位间距、标签内边距、说明小间距 |
| `--space-2` | `8px` | 按钮图标间距、按钮组、字段标签与控件间距 |
| `--space-3` | `12px` | 导航图标间距、按钮水平内边距、列表缩写与名称间距 |
| `--space-4` | `16px` | 详情标题间距、双列表单间距、提醒预览内边距 |
| `--space-5` | `20px` | 表格左右留白、设置行内边距、弹窗字段间距 |
| `--space-6` | `24px` | 面板内容内边距、详情与设置分组、弹窗与抽屉内边距 |
| `--space-8` | `32px` | 设置列间距、抽屉分组间距、来源区上间距 |

### 控件尺寸与交互外观

| 名称或选择器 | 实际值 | 用途 |
| --- | --- | --- |
| `--control-height` | `36px` | 普通按钮与原生输入框/下拉框最小高度 |
| `--nav-item-height` | `40px` | 左侧一级导航最小高度 |
| `.nav-subitem` | 最小高 `36px` | 通用与提醒二级导航 |
| `.control` | `padding: 7px 10px`，边框 `1px` | 文本、金额、日期、时间、下拉框 |
| `select.control` | 右内边距 `32px` | 为浏览器原生箭头预留空间 |
| `input[type="checkbox"], input[type="radio"]` | `16 × 16px` | 原生选择控件，`accent-color: var(--accent)` |
| `.button.icon-button` | `32 × 32px` | 弹窗 / 抽屉关闭按钮 |
| `.field-grid` | 等宽两列，列间距 `16px` | 新增弹窗中的金额与计费周期 |
| `.input-with-prefix input` | 左内边距 `29px` | 人民币符号与金额输入分离 |
| `.radio-option` | 内边距 `12px`、内部间距 `12px`、下间距 `8px` | 抽屉原生单选项的点击区域 |
| `.status` | 最小高 `24px`，内边距 `2px 7px`，内部间距 `5px` | 三种订阅状态与扣款成功状态 |
| `.status::before` | `5 × 5px`，圆形 | 状态辅助圆点 |
| `--disabled-opacity` | `.45` | 禁用分页按钮、固定货币控件、关闭提醒时的相关控件 |

日期选择器、时间选择器、下拉菜单与表单校验提示使用浏览器原生行为；系统弹出部分的字形与外观由运行环境决定，不模拟第三方组件。

## 6. 圆角、边框、阴影与焦点

| 名称或选择器 | 实际值 | 用途与对应位置 |
| --- | --- | --- |
| `--radius-sm` | `4px` | 服务缩写方块、状态标签、文字按钮 |
| `--radius-md` | `8px` | 控件、普通按钮、导航、提醒预览、成功反馈 |
| `--radius-lg` | `12px` | 表格与内容面板、居中弹窗、详情缩写方块 |
| `.drawer` | `border-radius: 0` | 紧贴窗口右侧的抽屉 |
| `--border-width` | `1px` | 常规边框与分隔线 |
| `.tab` | `border-bottom: 2px solid` | 选中标签的强调下划线 |
| `--focus-width` | `3px` | `:focus-visible` 外圈 |
| `:focus-visible` | `outline-offset: 2px` | 焦点外圈与控件的间隔 |
| `--shadow-modal` | `0 20px 64px rgba(23, 37, 31, .18)` | 居中新增弹窗 |
| `--shadow-drawer` | `-12px 0 48px rgba(23, 37, 31, .14)` | 右侧筛选抽屉 |
| `--shadow-toast` | `0 6px 24px rgba(23, 37, 31, .14)` | 成功反馈 |

正文容器和表格不添加阴影，使用边框与背景分层。悬停时次要按钮使用 `--surface-hover` 与 `--muted` 边框，主要按钮使用 `--accent-hover`；按下时主要按钮使用 `--accent-pressed`。选中导航、筛选与页码使用 `--accent-soft`。表单错误使用 `.control:user-invalid` 和浏览器原生校验消息。

## 7. 浮层尺寸与层级

| 名称或选择器 | 实际值 | 用途 |
| --- | --- | --- |
| `--modal-width` | `480px` | 新增订阅弹窗 |
| `.modal` | `max-width: calc(100vw - 64px); max-height: calc(100vh - 64px)` | 留出窗口边缘，内容超出时可滚动 |
| `--drawer-width` | `384px` | 筛选抽屉的宽度与最大宽度 |
| `.drawer` | `position: fixed; inset: 0 0 0 auto; height: 100vh; max-height: 100vh; margin: 0` | 右侧满高抽屉 |
| `.drawer-body` | `flex: 1; overflow: auto` | 抽屉内容区可滚动，底部操作区保留 |
| `.dialog-heading` | 内边距 `24px 24px 20px` | 浮层标题、说明与关闭按钮 |
| `.dialog-fields` | 内边距 `0 24px 24px`，字段间距 `20px` | 新增表单 |
| `.dialog-actions` | 内边距 `16px 24px`，按钮间距 `8px` | 浮层底部操作区 |
| `--z-sidebar` | `10` | 固定位置的左侧导航 |
| `--z-toast` | `30` | 成功反馈浮层 |
| 原生 `dialog.showModal()` | 浏览器 top layer | 弹窗和抽屉位于页面层级上方；背景由浏览器置为不可交互 |
| `.toast` | 距底 `28px`，最大宽 `600px`，内边距 `12px 16px` | 内容列中水平居中，`left: calc(50% + var(--nav-width) / 2)`，再平移 `-50%` |

弹窗和抽屉没有虚构 `z-index` Token，使用原生模态顶层。关闭按钮、取消、Esc 与遮罩点击均关闭当前浮层。关闭后恢复触发控件的焦点；当界面重绘时，回到对应的新增 / 筛选按钮。原生 `dialog` 负责模态键盘焦点范围。

## 8. 动效

| 名称 | 实际值 | 用途 |
| --- | --- | --- |
| `--motion-duration` | `200ms` | 弹窗、抽屉及遮罩的进入与退出 |
| `--motion-easing` | `ease-out` | 浮层动画与控件过渡 |
| `--motion-delay` | `0ms` | 浮层无额外等待 |
| `--hover-duration` | `120ms` | 普通按钮的背景 / 边框 / 文字颜色过渡，以及导航背景过渡 |

| 动效及触发 | 开始 → 结束 | 实际实现 |
| --- | --- | --- |
| 点击“新增订阅” | 透明度 `0 → 1`；`translateY(12px) scale(.985) → translateY(0) scale(1)` | `.modal[open]` 触发 `modal-in` |
| 关闭新增弹窗 | 上述值反向 | `.is-closing` 触发 `modal-out`，200ms 后调用 `close()` |
| 点击“筛选” | `translateX(100%) → translateX(0)` | `.drawer[open]` 触发 `drawer-in` |
| 关闭筛选抽屉 | `translateX(0) → translateX(100%)` | `.is-closing` 触发 `drawer-out`，200ms 后调用 `close()` |
| 任一浮层打开 / 关闭 | 遮罩背景 `transparent ↔ rgba(23, 37, 31, .28)` | `backdrop-in / backdrop-out` |

上述动画均为 `200ms ease-out 0ms both`，关闭后清理退出类，每次重新打开都可重看。页面切换、分页与页内标签没有额外动画。

### 减少动态效果

在 `@media (prefers-reduced-motion: reduce)` 下：

- 所有元素、`::before`、`::after` 的动画时长、动画延迟、过渡时长都设为 `0ms !important`。
- 原生 `dialog::backdrop` 的动画时长单独设为 `0ms !important`。
- `scroll-behavior` 设为 `auto`。
- JavaScript 使用同一媒体查询，将关闭等待时间设为 `0`，不额外等待 200ms。

成功反馈显示 **3600ms** 后隐藏，这是脚本中的停留时间，不属于进入 / 退出动效；反馈使用 `role="status"` 与 `aria-live="polite"`。

## 9. 本版状态的对应位置

此节记录实际已落地的状态与 Token 使用位置，便于后续开发保持一致。

| 状态 | 页面或触发 | 视觉与行为 |
| --- | --- | --- |
| 默认列表 | 首次打开 | 12 条本地样例，每页 5 条；当前页高亮，首页“上一页”禁用 |
| 当前层级 | 左侧导航 / 面包屑 | 当前页使用强调背景；详情保留“全部订阅”的所属位置；设置明确高亮通用或提醒 |
| 页内选中 | 详情概览 / 扣款记录 | 强调文字、700 字重、2px 下划线；支持左右方向键、Home、End |
| 有效筛选 | 应用状态或周期筛选 | 筛选按钮使用强调边框与浅绿背景，显示条件数；列表保留实际条件文案 |
| 筛选草稿 | 打开抽屉后修改 | 即时更新结果数量；应用才更新列表，取消保持原列表与分页 |
| 空列表 | “已取消”加“每年” | 空态文案与“清除筛选”按钮；分页显示 0 项 |
| 无扣款记录 | 新增订阅后进入扣款记录 | 原位空态，不生成虚假扣款记录 |
| 校验错误 | 提交空字段、无效金额或纯空格名称 | 浏览器原生校验；无效控件使用错误边框 / 背景 |
| 成功 | 新增或保存设置 | 深色成功反馈；数据与设置仅在当前打开期间有效 |
| 禁用 | 首页 / 末页分页、固定 CNY、关闭提醒后的时间设置 | 原生 `disabled`，透明度 `.45`，`not-allowed` 光标 |

所有组件与数据均在单个 HTML 内；没有第三方组件库、外部字体、真实订阅平台接口、登录、持久化或通知发送。
