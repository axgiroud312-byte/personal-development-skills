# 中文开发技能

一套轻量的中文开发方法：把想法变成清楚的任务，再集中完成前后端实现。参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills)，按个人工作习惯精简维护。

按当前问题选择技能，不要求每次走完整流程。小改动直接实施；需要交接、持续推进或多人协作时，以 Issue 作为执行工作单。Spec 负责必要的整体方案，Issue 负责当前具体结果；文档为开发服务，不为文档齐全增加工作。

## 九个入口各管什么

| 当前需要 | 技能 | 产出与存在价值 |
| --- | --- | --- |
| 想法还不清楚 | [grilling](skills/grilling/SKILL.md) | 用问题和选项确定关键需求，已有答案不重问。 |
| 业务含义有歧义 | [domain-modeling](skills/domain-modeling/SKILL.md) | 统一术语、关系与规则，避免前后端各自理解。 |
| 需要整体方案 | [to-spec](skills/to-spec/SKILL.md) | 明确范围、模块协作与结果；按复杂度使用一份或多份 Spec。 |
| 想先看到整套产品 | [design-ui](skills/design-ui/SKILL.md) | 完整前端原型与对应 Token，展示页面组织、视觉和交互。 |
| 要把计划变成可执行任务 | [to-tickets](skills/to-tickets/SKILL.md) | 写清单项结果、局部方案和真实依赖，维护 Issue。 |
| 要完成一项功能或修复 | [implement](skills/implement/SKILL.md) | 集中完成当前实现，按职责回交或收尾。 |
| 要连续做完整个目标 | [implement-spec](skills/implement-spec/SKILL.md) | 管依赖、分工、整合和整体交付，复用单项实施方法。 |
| 想知道刚才做了什么 | [explain-work](skills/explain-work/SKILL.md) | 依据成果解释用途、原因、工作方式和实际验证范围。 |
| Agent 找不到项目入口 | [setup-project-skills](skills/setup-project-skills/SKILL.md) | 维护真实路径、命令、少量长期约定和唯一状态入口。 |

`implement` 与 `implement-spec` 共用一份[开发与交付约定](skills/implement/references/development.md)，整体开发只增加协调职责。`implement-spec` 需要配套 `implement`；其他入口可独立使用，衔接技能不可用时完成相同的必要梳理即可。

## 怎样连起来

从已有材料进入即可：需求不清才讨论，业务不清才建模，整体方案不清才写 Spec，视觉不清才做原型。`to-tickets` 把已定范围写成任务；`implement` 完成单项，`implement-spec` 连续推进一组任务；最后需要理解结果时再讲解。

小改动无需 PRD、Spec 和 Issue 三件套。一项连贯能力通常一份 Spec；大项目先细化近期范围，必要时按能力与依赖拆多份，远期保留概要。设计或调查尚未完成也能先列任务，只阻塞真正依赖它们的实现。

前后端通过同一份接口与状态约定衔接：Spec 说明模块和数据如何连接，Issue 写足本次接口、字段、错误及依赖解除条件。原型、本地模拟和真实接口接入分别说明；依赖任务拿到实际代码或成果后再继续，不能只凭“已完成”消息整合。

## 共同的工作习惯

代码和实际行为说明现状，用户已确认需求决定目标；两者冲突时记录差异与处理。每项业务、技术或设计决定只维护一份有效正文，其余引用，变化更新相应来源和受影响任务。

以集中开发为主，必要测试、验证与构建在本次授权目标或用户明确要求交付的阶段收尾统一做。中途 Issue、提交或批次结束不自动触发测试，不默认 TDD、覆盖率任务或反复打包。保留已有测试与强制 CI，开发中只按需要运行预览、定位阻碍；具体交付与清理规则见共用约定。

### 完整前端原型

`design-ui` 覆盖本次范围内全部页面层级、导航、打开方式、布局密度、视觉、组件、状态与动效，按用户指定参考、组件、字体字重、背景与配色制作。交付一个 `docs/design/design-board.html` 和一份 `docs/design/design-token.md`；组件与开源库来源放在 HTML 内，Token 从实际采用的样式提取。原型做好即可看，不默认附加验收报告或测试流程。

### 可裁剪的参考

- [Spec 模板](skills/to-spec/references/spec-template.md)：本次想实现什么、想要什么、不想要什么，以及整体方案与结果。
- [Issue 模板](skills/to-tickets/references/issue-template.md)：同样先说明三项需求，再补足局部实施和交接信息。
- [好设计与坏设计](skills/design-ui/references/design-quality.md)：用具体对照帮助设计取舍。

模板是起点，可以合并段落、沿用已有项目格式，不强制填满。项目配置只记录必要事实和少量长期默认；已有状态入口直接沿用，没有时按平台选择一个，避免进度散在多处。

## 安装与更新

需要 Node.js 22.20 或更新的受支持版本（含 npm / npx）、Git，并能访问 npm 与 GitHub。使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装的是 Agent 的工作方法，项目组件依赖在开发时按需处理。

为 Codex 全局安装全部九个技能：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill '*' --agent codex -g
```

只用于当前项目时，在项目目录运行并去掉 `-g`。需要交互选择技能和 Agent 时省略 `--skill` 与 `--agent`；只查看列表可用 `--list`。其他 Agent 标识见[支持列表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

部分安装时，连续开发入口必须带上共用实现技能：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill implement-spec implement --agent codex -g
```

Skills CLI 按所选技能目录安装，不会根据 Markdown 引用自动补齐依赖；不要只复制 `implement-spec`。其他技能可单选安装。更新时在原安装范围重跑相同命令，先保存自己修改过的副本。

旧版 `grill-with-docs` 已并入 `grilling`，重装不自动移除旧入口。确实安装过旧版时可运行下列命令，并按原范围及 Agent 调整参数；移除前核对目标：

```sh
npx skills@latest remove grill-with-docs --agent codex -g
```

安装或更新后在目标项目开启新会话；需要建立项目约定时再使用 `setup-project-skills`，已有约定够用则直接开发。

## 维护

保持九个入口职责清楚，`SKILL.md` 以 120 行以内为目标，篇幅服从必要内容。重复规则维护一个来源，配套参考必须有明确读取时机；新增能力先检查能否扩展已有入口，再决定是否增加技能。

修改正文时同步中文显示信息和本页；迁移时核对相对引用与安装依赖。既有[评测记录](EVALUATION.md)和[十轮记录](evaluation/ten-rounds-2026-10-26.md)仅说明历史实验，不是每次开发的默认步骤，也不证明当前版本在所有模型上的表现。
