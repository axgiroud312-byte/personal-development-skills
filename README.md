# 中文开发技能

这套技能帮助你推敲想法、记录决定、组织开发任务，并把实现整合为一个 PR。你决定目标和重要取舍，Agent 主动调查实际情况，在确定的范围内自主处理工程细节。

## 四个主入口

| 你想做什么 | 技能 | 得到什么 |
| --- | --- | --- |
| 推敲想法和关键选择 | [grill-me](skills/grill-me/SKILL.md) | 按决策依赖分轮追问，每问给出建议，逐步形成清楚的决定 |
| 把讨论沉淀为 Spec | [to-spec](skills/to-spec/SKILL.md) | 结合当前对话和实际代码，记录问题、解决方案、用户故事与已确定的实现决定 |
| 把 Spec 变成开发任务 | [to-tickets](skills/to-tickets/SKILL.md) | 按完整用户功能组织的简洁 Issue，带明确预期行为和真实依赖 |
| 把任务交付为一个 PR | [implement-pr](skills/implement-pr/SKILL.md) | 独立子 Agent 开发、集成分支汇总、统一验证和全局审查后的一个 PR |

四个主入口均由你手动调用，按需求自行衔接。已有清楚的决定、Spec 或开发 Issue 时，直接选择对应入口即可。每次调用完成自己的职责；入口内已授权的调查、修改和补充工作连续完成。

`grill-me` 先追问前置条件已清楚的决策，随着回答展开下一层问题。能从项目中查明的事实由 Agent 自己调查，问题集中在你的意图与取舍。

`to-spec` 整理已经形成的决定，结合代码核实现状。Spec 以问题、解决方案、用户故事、已确定的实现决定为主，其他内容按需补充。

`to-tickets` 先按完整功能尽量合并任务，同一功能的 UI、API、状态与数据改动放在同一张票里，细步骤写在票内。只有独立交付价值、真实阻塞关系或单次独立上下文确实容不下时才拆票，票数随任务决定。Issue 聚焦开发目标、范围、预期行为、实施依据与依赖。

`implement-pr` 按真实依赖安排任务，每项任务使用新的独立子 Agent、worktree 和分支，随后合入一个集成分支。主 Agent 在整体完成后统一执行必要测试、验证与构建，再由新的独立 Agent 做全局审查并处理发现的问题，最终交付一个 PR。开发进展写回 Issue，整体验证与审查记录写入 PR 或同一交付记录；PR 的合并由用户决定。

## 设计与项目辅助

| 你想做什么 | 技能 | 得到什么 |
| --- | --- | --- |
| 探索和完善界面 | [design-ui](skills/design-ui/SKILL.md) | 符合当前需求的交互原型、Token 等设计表达 |
| 比较同一组件的多个方案 | [component-variants](skills/component-variants/SKILL.md) | 结合当前组件库生成不同版本，演示交互状态并可视化选择 |
| 判断界面效果 | [design-quality](skills/design-quality/SKILL.md) | 用布局表达信息，结合实际页面判断 AI slop |
| 让项目找到工作依据 | [setup-project-skills](skills/setup-project-skills/SKILL.md) | 融入 `AGENTS.md` 的技能职责、手动入口与实际资料位置 |
| 听懂刚才做了什么 | [explain-work](skills/explain-work/SKILL.md) | 通俗的结果、原因和使用说明 |

`design-ui`、`setup-project-skills` 也保留手动调用；`component-variants`、`design-quality`、`explain-work` 延续各自现有触发方式。共六个手动入口使用 `disable-model-invocation: true` 和 `policy.allow_implicit_invocation: false`，客户端支持时由客户端控制调用。

按需使用 `setup-project-skills` 记录项目约定，其他技能可直接使用。

设计让布局、分组、对齐与视觉层级清楚表达信息和操作，把文字留给必要内容：

Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining.

[AI slop 清单](skills/design-quality/references/design-quality.md) 保留连续编号的负面设计参考，结合真实页面判断问题。原型、Token 和展示范围按需求组织，保持相互对应，按反馈持续完善；用户停止时保留当前成果。

`component-variants` 结合当前组件库探索同一组件的多个方向，通过可切换预览展示交互状态、适用场景和取舍，用户选定后继续细化。该流程参考 [Emil Kowalski 的 prototype](https://github.com/emilkowalski/skills/blob/main/skills/prototype/SKILL.md)。

## 资料放在哪里

优先沿用项目已有的权威资料与任务入口，每份正文在一个位置维护，其他位置引用。

| 资料 | 位置与用途 |
| --- | --- |
| 项目入口 | `AGENTS.md`：工作原则、技能职责与实际资料位置 |
| Spec | 已有关联 Spec 原位更新。新 Spec 优先使用项目已配置的任务系统，可建立独立的 Spec Issue；未配置远程入口时用 `docs/specs/<slug>.md`。已有 `docs/specs/` 权威来源时继续沿用 |
| 开发 Issue | 远程任务系统；未配置远程入口时用 `docs/issues/<feature>/<NN>-<slug>.md`，一票一文件。记录开发任务、依赖、进展与实现结果 |
| 交付记录 | 一个 PR 或同一交付记录：集成结果、整体验证、构建与全局审查结论 |
| HTML 原型 | 默认 `docs/design/design-board.html`，表达可操作的界面与交互 |
| Design Token | 默认 `docs/design/design-token.md`，记录共用样式及其用途 |

Spec Issue 用于记录方案与决定，开发 Issue 用于执行任务；标签沿用项目已有配置。任务系统已配置但暂时无法访问时，在聊天保留待发布内容并说明实际阻碍。讨论与工作解释在聊天中交付。

## 工作原则

第一性原理大于一切，遇到问题先查根源。用户的表达、给出的材料和实际代码共同构成判断依据，调查深度随当前问题决定。

常规工程选择在确定的任务范围内自主处理。新事实使原方案无法成立或用户改变目标时，说明影响并修订相关决定与任务，其他明确工作继续。文档与代码有差异时查明原因，将重要调整写回对应资料。

集中完成开发，实际错误与影响后续工作的技术疑问做小范围核实；整体完成后统一必要检查。检查与审查结论按实际结果表述。

## 安装与更新

准备好 Node.js/npm、Git 及 npm、GitHub 访问能力，用 [Skills CLI](https://github.com/vercel-labs/skills) 为 Codex 全局安装：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill '*' --agent codex -g
```

也可以单独安装需要的技能，例如：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill implement-pr --agent codex -g
```

重新运行可更新同一范围；去掉 `-g` 则安装到当前项目。更新前整合安装副本里的自定义修改。其他客户端按实际支持的 Agent 名称调整参数，安装时保留技能自身的参考文件和显示配置。

从本仓库旧版更新时，入口对应为 `grilling` → `grill-me`，`implement` / `implement-spec` → `implement-pr`。用 [Skills CLI 的移除命令](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-remove) 清理本仓库旧入口，再运行上面的安装命令。全局 Codex 安装对应：

```sh
npx skills@latest remove grilling implement implement-spec --agent codex -g
```

项目级安装去掉 `-g`，并将项目 `AGENTS.md` 中的旧入口名称更新为上述新名称。

仓库维护按 [AGENTS.md](AGENTS.md) 执行，结构检查使用 `python -X utf8 -B scripts/verify_skill_links.py`；真实使用效果在实际任务中观察。

四个主入口参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills) 并按个人工作方式调整，来源与许可见 [第三方说明](THIRD_PARTY_NOTICES.md)。
