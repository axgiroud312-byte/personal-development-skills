# 中文开发技能

用中文说明要做什么，Agent 根据任务选择技能。七个开发技能可以分别使用、按需要组合；`explain-work` 负责讲清刚才的工作，`setup-project-skills` 负责配置项目约定。

设计参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills)，内容由用户独立维护。

## 安装

需要 Node.js 22.20 或更新的受支持版本（包含 npm / npx）和 Git，并能访问 npm 与 GitHub。

使用 [Skills CLI](https://github.com/vercel-labs/skills) 直接从本仓库安装，无需单独发布 npm 包。在要使用技能的项目目录中运行：

```sh
npx skills add axgiroud312-byte/personal-development-skills
```

默认安装到当前项目；交互运行时可选择技能和目标 Agent。需要所有项目都能使用时，追加 `-g`。

先查看可安装的技能，不执行安装：

```sh
npx skills add axgiroud312-byte/personal-development-skills --list
```

也可以明确指定技能和目标 Agent。例如，将 Issue、单项开发和整套开发三个技能安装到当前项目，供 Codex 使用：

```sh
npx skills add axgiroud312-byte/personal-development-skills --skill to-tickets implement implement-spec --agent codex
```

给 Codex 全局安装全部 9 个技能：

```sh
npx skills add axgiroud312-byte/personal-development-skills --skill '*' --agent codex -g
```

只给 Codex 全局安装工作讲解技能：

```sh
npx skills add axgiroud312-byte/personal-development-skills --skill explain-work --agent codex -g
```

其他 Agent 的标识见 [安装器文档](https://github.com/vercel-labs/skills#supported-agents)。安装后在目标 Agent 中开启新会话，使用下面的中文表达。

## 技能一览

| 你可以这样说 | 对应技能 |
| --- | --- |
| 帮我把这个想法问清楚，先讨论 | `grilling`：理清需求 |
| 边讨论边把确定的内容记下来 | `grill-with-docs`：讨论并记录 |
| 统一一下业务术语和关系 | `domain-modeling`：理清业务概念 |
| 把已有方案整理成 Spec | `to-spec`：整理需求规格 |
| 根据这段计划直接拆任务 | `to-tickets`：拆分开发任务 |
| 把这个问题修好／完成这项任务 | `implement`：完成一项开发 |
| 按方案把整套功能连续做完 | `implement-spec`：连续完成整套开发 |
| 讲讲刚才做了什么／做完后解释一下 | `explain-work`：解释工作结果、原理与验证范围 |
| 为这个项目配置技能使用约定 | `setup-project-skills`：配置项目技能 |

## 按需要组合

已有明确任务时直接实施；需要澄清时先讨论；需要保留设计时写 Spec；需要组织多项工作时拆任务。领域建模可在任意阶段进行。技能使用当前对话、已有文档或任务，不检查前一个技能是否执行过。

Spec 保存目标和已确定的设计，包括模块、接口、数据结构、API 约定与验证决定。Issue 描述具体交付、依赖、必要的任务细节和验收方法，引用 Spec 中已有的决定。两者和领域模型都随已确认的变化更新。

项目配置已明确时直接使用开发技能。需要建立或调整文档位置、任务跟踪或验证约定时，使用 `setup-project-skills`；它不规定每次开发的阶段顺序。

## 工作完成后的讲解

需要理解刚才的工作时使用 [`explain-work`](skills/explain-work/SKILL.md)。它可以接在开发、设计、配置、部署、文档或研究工作后，也可以在你追问时单独使用。讲解从结果与用途开始，再按需要说明主要变化及原因、关键运作流程、实际验证与限制。

例如：“把这个问题修好，做完后解释一下。”先按 `implement` 完成任务，再按 `explain-work` 解释结果；“按方案把整套功能做完，最后讲清楚。”则先按 `implement-spec` 完成整体交付，再解释整体结果。

只问“刚才改了什么”或“为什么这么改”时，依据已有改动和执行证据讲解，必要时补充只读检查。解释请求本身不授权新的修改或发布。“解释一下”只有明确指向刚才的工作时才使用这个技能；普通知识问答、翻译和尚未执行的新方案不属于它的范围。

本技能借鉴 [Google 开发者文档写作指南](https://developers.google.com/style) 的表达原则，并加入工作完成状态与验证证据的要求；日常使用不需要重复检索指南。

## Issue、开发与交付

Issue 写清目标、范围、必要依据、验收和关联。父子关系表示所属目标，阻塞关系表示必须等待的任务；正文保持当前要求，评论记录关键变化，完成实施后回链 PR。

`implement` 负责一项任务：读取 Issue → 实施 → 按项目设置验证 → 提交推送 → 创建或更新 PR → 保存交付结果 → 清理。

`implement-spec` 负责多个任务：整理依赖 → 持续推进可执行任务 → 核对和整合 → 更新整体 PR → 保存试用结果 → 清理本次临时工作树与产物。

用户要求“做完后解释”时，在完成上述实际工作后按需衔接 `explain-work`；只要求解释已有工作时直接讲解。讲解依据实际结果，不代替实施、验收或用户确认。

清理以改动已推送且被实际 PR 覆盖、所需交付物已保存为前提。保留主工作区、未交付修改和 PR 远端分支，并报告真实残留。测试和审查分别按项目设置；技能不额外引入运行框架或后台轮询服务。

## 维护

在 `skills/<技能名>/SKILL.md` 修改行为，在对应的 `agents/openai.yaml` 修改中文显示信息。各技能无需共享规则文件即可使用。

各 Agent 的技能目录通过目录链接读取这里的同一份源文件。新增技能或迁移维护目录时核对这些链接，保留其他技能。已打开的会话可能仍持有旧上下文，实际触发效果需在新会话中确认。
