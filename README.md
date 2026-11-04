# 中文开发技能

这套技能围绕同一件事工作：逐步理解用户真实意图，主动调查实际情况，让判断有依据，并随着交流和新发现持续修正。假设建立在已经理解的需求上，帮助把目标做成可用的成果。

你决定目标和重要取舍，Agent 自主选择调查与实现方法。需求在写 Issue 前对齐，Spec 沉淀目标和总体方案，Issue 深化为明确的实施任务，implement 集中完成开发。根据任务组合这些职责，简单且明确的工作直接推进。

## 什么时候用哪个技能

| 你想做什么 | 技能 | 得到什么 |
| --- | --- | --- |
| 推敲想法和关键选择 | [grilling](skills/grilling/SKILL.md) | 对关键决策、边界与假设逐步形成共同理解 |
| 确定目标与总体设计 | [to-spec](skills/to-spec/SKILL.md) | 有依据的目标、总体方案和架构，按需附设计产物 |
| 把方案深化成任务 | [to-tickets](skills/to-tickets/SKILL.md) | 将已对齐的需求补足为明确、可直接执行的任务 |
| 完成功能或修复 | [implement](skills/implement/SKILL.md) | 自主实施、集中开发、少测试，必要检查后交付 |
| 连续完成多个 Issue | [implement-spec](skills/implement-spec/SKILL.md) | 协调依赖、分工与整合，统一收尾 |
| 探索和完善界面 | [design-ui](skills/design-ui/SKILL.md) | 符合当前需求的交互原型、Token 等设计表达 |
| 判断界面效果 | [design-quality](skills/design-quality/SKILL.md) | 用布局表达信息，结合实际页面判断 AI slop |
| 让项目找到工作依据 | [setup-project-skills](skills/setup-project-skills/SKILL.md) | 融入 `AGENTS.md` 的职责、资料位置和工作原则 |
| 听懂刚才做了什么 | [explain-work](skills/explain-work/SKILL.md) | 通俗的结果、原因和使用说明 |

`to-spec`、`to-tickets`、`design-ui`、`setup-project-skills` 保留手动入口。已授权任务中的调查、设计补充、修改和讨论可以连续处理；例如 Spec 可以直接包含需求所需的原型或 Token。

这四个入口保留 `disable-model-invocation: true` 和 `policy.allow_implicit_invocation: false`。客户端支持这些开关时，由客户端控制调用；其他客户端按技能正文约定使用。

## 持续理解与形成方案

用户的表达、给出的材料与项目实际情况共同帮助 Agent 理解需求。调查什么、调查多深、什么时候讨论，由尚未弄清的问题及其对结果的影响决定。能查清的事实主动查，涉及用户意图和重要取舍的疑问带着具体发现与建议讨论。

`grilling` 借鉴 [Matt Pocock 的 grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) 对决策及其关联的深入追问；问题随当前理解和用户回答展开，表达方式和数量适应讨论需要。

Spec 将这些认识沉淀为目标、总体方案和设计架构，说明各部分怎样共同实现需求。本次范围内的需求、边界、关键行为和影响需求的假设在编写 Issue 前明确，已有结论直接沿用。

Issue 在确定的需求上补足具体做法、衔接关系和完成标准，形成可直接执行的任务。细化时发现需求仍有疑问，就回到讨论与 Spec 解决，再继续写任务。任务可以依赖其他任务的成果，但所需输入与预期结果应明确。

各类产物都由模型根据任务自主组织，采用合适的结构、详略和表达方式。小需求可以集中表达，大项目可以拆成相互索引的文档，读者按需要展开相关内容。

## 资料放在哪里

| 资料 | 默认位置 | 用途 |
| --- | --- | --- |
| 项目入口 | `AGENTS.md` | 工作原则、技能职责与实际资料位置 |
| Spec | `docs/specs/` | 目标、总体方案和设计架构 |
| Issue | 远程 Issue；未配置任务平台时用 `docs/issues/` | 可执行方案、任务进展和实际结果 |
| HTML 原型 | `docs/design/design-board.html` | 可操作的界面与交互表达 |
| Design Token | `docs/design/design-token.md` | 设计采用或提议的共用样式及其用途 |

已有资料沿用原处，新文件按实际需要建立。每项结论在合适的位置维护，其他位置引用。讨论与工作解释在聊天中交付。

远程 Issue 可用时在远程维护；暂时访问受阻时，在聊天保留待发布草稿与具体阻碍。`setup-project-skills` 将项目实际资料位置和协作原则融入 `AGENTS.md`。

## 设计与实施

设计产物、展示范围和细化顺序由当前需求决定。需要交互原型时，默认使用可独立打开的 HTML；Token 可以按需求直接定义，也可以从实际样式提取。设计方案、原型与 Token 保持对应，如实说明已确定和仍待讨论的部分。用户停止时保留当前成果，之后继续完善。

让布局、分组、对齐与视觉层级清楚表达信息和操作，把文字留给必要内容：

Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining.

[AI slop 清单](skills/design-quality/references/design-quality.md) 保留指定的负面设计参考，结合真实页面判断问题。

`implement` 与 `implement-spec` 按已经确定的 Issue 自主落实工程细节，集中开发、少做测试。中途的实际错误或技术疑问小范围核实；关联工作完成后统一整合与必要验证，检查通过后推进交付。

执行中出现用户需求变更，或实际证据使原方案无法成立时，先对齐变更并修订相关 Spec 与 Issue，再继续受影响的实施，其他明确的任务继续。

文档与代码不一致时，查清原因并沿用合适的现有惯例，重要调整写回对应资料，交付时说明差异。成果与验证按实际情况表述，有 Issue 时同步任务结果。

## 安装与更新

准备好 Node.js/npm、Git 及 npm、GitHub 访问能力，用 [Skills CLI](https://github.com/vercel-labs/skills) 为 Codex 全局安装：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill '*' --agent codex -g
```

重新运行可更新同一范围；去掉 `-g` 则安装到当前项目。更新前整合安装副本里的自定义修改。其他客户端按实际支持的 Agent 名称调整参数。

`implement-spec` 与同源同版本的 `implement` 配套安装：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill implement implement-spec --agent codex -g
```

保留技能内部的参考文件、显示配置和兄弟目录关系，更新后核对实际入口。仓库维护按 [AGENTS.md](AGENTS.md) 执行，结构检查使用 `python -X utf8 -B scripts/verify_skill_links.py`；真实使用效果在实际任务中观察。

这套技能最初参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills)，按个人使用经验持续维护。
