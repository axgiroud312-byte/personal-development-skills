# 中文开发技能

这套技能帮助你推敲想法、记录决定、组织开发任务，并把关界面质量。你决定目标和重要取舍，Agent 主动调查实际情况，在确定的范围内自主处理工程细节。

## 三个主入口

| 你想做什么 | 技能 | 得到什么 |
| --- | --- | --- |
| 推敲想法和关键选择 | [grill-me](skills/grill-me/SKILL.md) | 按决策依赖分轮追问，每问给出建议，逐步形成清楚的决定 |
| 记录会改变结果的取舍 | [to-spec](skills/to-spec/SKILL.md) | 短规格，只补原需求缺的决定和能区分方案的例子 |
| 为实际依赖或交接拆工单 | [to-tickets](skills/to-tickets/SKILL.md) | 接手者知道由谁交付什么、到哪里看验收场景 |

三个入口按需手动调用。需求和预期都清楚时，直接开发；一次调用内已授权的工作连续完成。

- “设置保存后重开就丢了，修一下。” 在当前目录复现、修复，再重开确认。
- “失败后点重放时，流程可能已经更新了。” 若用哪一版仍需选择，用 `grill-me` 讨论；确定后，`to-spec` 把决定补在原需求旁。
- “执行器这周交付，下周另一位同事接定时调度。” 用 `to-tickets` 写清调度方依赖的运行入口，工单引用已有验收场景。

## 设计与项目辅助

| 你想做什么 | 技能 | 得到什么 |
| --- | --- | --- |
| 判断界面效果 | [design-quality](skills/design-quality/SKILL.md) | 用布局表达信息，结合实际页面判断 AI slop |
| 让项目找到工作依据 | [setup-project-skills](skills/setup-project-skills/SKILL.md) | 项目 `AGENTS.md` 里的启动方式、验证入口、资料位置、系统红线和项目例外 |

`setup-project-skills` 也保留手动调用；`design-quality` 延续现有触发方式。共四个手动入口使用 `disable-model-invocation: true` 和 `policy.allow_implicit_invocation: false`，客户端支持时由客户端控制调用。

按需使用 `setup-project-skills` 记录项目约定，其他技能可直接使用。

设计让布局、分组、对齐与视觉层级清楚表达信息和操作，把文字留给必要内容：

Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining.

[AI slop 清单](skills/design-quality/references/design-quality.md) 保留连续编号的负面设计参考，结合真实渲染页面判断层级、排版破损、状态反馈与 AI slop 问题。

## 资料放在哪里

优先沿用项目已有的权威资料与任务入口，每份正文在一个位置维护，其他位置引用。

| 资料 | 位置与用途 |
| --- | --- |
| 项目入口 | `AGENTS.md`：工作原则、技能职责与实际资料位置 |
| Spec | 已有关联 Spec 原位更新。新 Spec 优先使用项目已配置的任务系统，可建立独立的 Spec Issue；未配置远程入口时用 `docs/specs/<slug>.md`。已有 `docs/specs/` 权威来源时继续沿用 |
| 开发 Issue | 远程任务系统；未配置远程入口时用 `docs/issues/<feature>/<NN>-<slug>.md`，一票一文件。记录本票交付的成果、依赖和进展 |

Spec Issue 用于记录方案与决定，开发 Issue 用于执行任务；标签沿用项目已有配置。任务系统已配置但暂时无法访问时，在聊天保留待发布内容并说明实际阻碍。讨论在聊天中交付。

## 工作原则

第一性原理大于一切，遇到问题先查根源。用户的表达、给出的材料和实际代码共同构成判断依据，调查深度随当前问题决定。

常规工程选择在确定的任务范围内自主处理。新事实使原方案无法成立或用户改变目标时，说明影响并修订相关决定与任务，其他明确工作继续。遇到文档与代码不一致时，沿用现有实现的惯例，完成后列出具体差异。

先做能直接验证本次改动的最小检查。检查失败或改动影响其他功能时，再扩大范围。交付或验证确实需要时才构建。

## 安装与更新

本仓库 `main` 分支的 `skills/` 是这些技能的唯一维护基线。技能改动合入后，本地安装从这里同步。

准备好 Node.js/npm、Git 及 npm、GitHub 访问能力，用 [Skills CLI](https://github.com/vercel-labs/skills) 为 Codex 全局安装：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill '*' --agent codex -g
```

也可以单独安装需要的技能，例如：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill to-spec --agent codex -g
```

重新运行可更新同一范围；去掉 `-g` 则安装到当前项目。更新前整合安装副本里的自定义修改。其他客户端按实际支持的 Agent 名称调整参数，安装时保留技能自身的参考文件和显示配置。

从本仓库旧版更新时，入口对应为 `grilling` → `grill-me`；`implement`、`implement-spec`、`implement-pr`、`design-ui`、`component-variants`、`explain-work` 已移除。用 [Skills CLI 的移除命令](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-remove) 清理本仓库旧入口，再运行上面的安装命令。全局 Codex 安装对应：

```sh
npx skills@latest remove grilling implement implement-spec implement-pr design-ui component-variants explain-work --agent codex -g
```

项目级安装去掉 `-g`，并将项目 `AGENTS.md` 中的旧入口名称更新为上述新名称。

仓库维护按 [AGENTS.md](AGENTS.md) 执行，结构检查使用 `python -X utf8 -B scripts/verify_skill_links.py`；真实使用效果在实际任务中观察。

三个主入口参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills) 并按个人工作方式调整，来源与许可见 [第三方说明](THIRD_PARTY_NOTICES.md)。
