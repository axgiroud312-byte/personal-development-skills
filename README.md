# 中文开发技能

九个中文技能，用于澄清需求、编写规格、制作原型、拆分任务和完成开发。参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills)，由用户独立维护。

小改动直接做，复杂工作按需要使用技能。用户决定目标和重要取舍，Agent 在授权范围内自主处理工程问题。Spec 定整体开发规格，Issue 写具体任务与方案，实施技能集中完成开发、少做重复测试；不要求每次任务走完全部流程。

## 技能入口

| 当前需要 | 技能 | 调用方式与交付 |
| --- | --- | --- |
| 完成明确功能或修复 | [implement](skills/implement/SKILL.md) | 结合任务和实际情况自主实施，集中开发、必要验证 |
| 连续完成多个任务 | [implement-spec](skills/implement-spec/SKILL.md) | 按需协调依赖、分工、整合与收尾 |
| 写开发规格 | [to-spec](skills/to-spec/SKILL.md) | 主动调用，写整体方案、明确约束与完成标准 |
| 拆分开发任务 | [to-tickets](skills/to-tickets/SKILL.md) | 主动调用，写具体实施方案、真实依赖与预期结果 |
| 先看设计效果 | [design-ui](skills/design-ui/SKILL.md) | 主动调用，先交 HTML 原型，满意后提取 Token |
| 识别常见 AI 味界面 | [design-quality](skills/design-quality/SKILL.md) | 按需读取 AI slop 清单，不额外生成文件 |
| 理清需求与关键选择 | [grilling](skills/grilling/SKILL.md) | 按需提问，在聊天交付结论 |
| 写入技能流程与文档位置 | [setup-project-skills](skills/setup-project-skills/SKILL.md) | 主动调用，只更新项目 `AGENTS.md` 中对应内容 |
| 听懂刚才的工作 | [explain-work](skills/explain-work/SKILL.md) | 按需在聊天解释结果、原因与验证范围 |

四个手动入口只由用户主动调用；一次调用后的补充、修改和确认可继续处理，无需反复点名。开发涉及 UI、范围较大或缺少文件，都不自动启动这些专项流程。其他技能可以读取已有材料、维护受影响内容和安排内部步骤，不能借用等价方法绕过调用边界另造专项产物。

手动入口保留 `disable-model-invocation: true` 和 `policy.allow_implicit_invocation: false`。不支持这些开关的客户端仍需遵守正文约定，不能把元数据当作宿主已强制执行的证明。

## 项目只按需保留这些资料

| 位置 | 内容边界 |
| --- | --- |
| 根目录 `AGENTS.md` | 保留已有项目指令；本套技能只补充使用流程、文档位置和工作准则 |
| `docs/specs/<主题>.md` | 本规格的目标、范围、行为、技术方案、依赖、完成标准和未决选择 |
| 远程 Issue，或 `docs/issues/<标识>.md` | 本任务的要求、局部方案、依赖、结果和进展；正文只维护一处 |
| `docs/design/design-board.html` | 本次范围的页面、交互与视觉原型，组件和来源说明放在文件内 |
| `docs/design/design-token.md` | 从用户已确认原型提取的实际共用 Token |

这些是允许的产物，不是必备清单。已有同类文件沿用其位置；新项目采用上表默认位置。项目指令统一在 `AGENTS.md`，已有其他客户端入口只作必要引用，不复制规则。

`setup-project-skills` 只把技能流程、文档位置和简短协作原则写进 `AGENTS.md`，不承担技术栈、启动命令、CI 或交付方式配置，也不修改其他客户端入口。

## 文档与自主判断

从实际问题出发：用户当前目标和明确约束决定要做什么，代码与运行结果用于核实现状。Spec、Issue 记录当前共识和方案，在容易混淆处说明明确要求、工程选择与假设；具体方案需要写清，但非强制细节可以依据新事实调整。

文档冲突、方案过时或过去的方法失败时先查证，默认沿用现有实现惯例，不延续已证实的错误。Agent 在授权范围内自主解决，实质变化回写对应规格或任务，并说明依据；不能因为代码尚未实现而忽略新需求。

重要假设、方向变化和实质副作用用简短说明让用户看见。历史与记忆需要核实，推断不能覆盖用户明确选择。涉及目标、明确约束、关键体验或未授权的重要影响时由用户决定；不受影响的工作继续，已有授权不重复确认。收到纠正先调整失效的理解，不继续沿错误方向堆补丁。

不另生成术语表、领域文档、讨论记录、状态文件、计划总览、开发指南或总结报告，也不将它们塞进 Spec 或 Issue。业务歧义在对话中解决；规格只描述本功能实际需要的行为与约束，任务只描述本任务需要的内容。实际进展更新对应 Issue，没有 Issue 就在聊天交接。

远程任务功能可用时，直接维护远程 Issue。已配置但暂时无法访问时，在聊天给出待发布草稿和阻碍，不静默建立本地副本。仅配置 Git 远端不等于任务功能已经可用。

本仓库自身保留必要的 `SKILL.md`、显示配置、Spec/Issue 模板、AI slop 参考和结构检查脚本；不另外维护历史评测报告。

## 设计与开发衔接

[AI slop 参考](skills/design-quality/references/design-quality.md) 只按编号描述具体坏表现，重点包括文字堆砌、自我状态和第一人称文案、无关 AI 组件、对齐与功能层级混乱，以及无意义的渐变、外框、描边、阴影和光效。不提供好设计示范或固定替代套路。

调用 `design-ui` 后，先制作可打开的 HTML 原型，按反馈修改同一份文件；用户满意后，再从该版实际样式提取一份 Token 文档。仅要草图就只交草图。正式开发参考原型与 Token，不要求共用原型源码，原型完成也不等于正式前端完成。

[Spec 模板](skills/to-spec/references/spec-template.md) 只承接规格，[Issue 模板](skills/to-tickets/references/issue-template.md) 只承接任务。已有 Spec 时，Issue 引用相应章节并补局部差异；没有 Spec 也能完成明确任务，不为开工补齐全套文件。

执行方法集中在 `implement`，`implement-spec` 复用并负责跨任务整合。按授权目标集中开发，Issue、提交或内部步骤结束不自动触发测试和收尾。普通检查留到目标收尾；实际错误或会影响大量后续工作的关键假设，可先做足以判断的小检查。

优先复用已有检查，不默认 TDD、覆盖率任务或新测试框架；测试与构建须服务于本次改动，已有强制 CI 保留。相关检查通过后，只有新改动、失败或未解决的问题才扩大或重复验证。按实际结果说明完成、模拟、未验证和用户验收，不能降低要求来宣布完成。

## 安装与更新

需要可用的 Node.js/npm、Git 及 npm、GitHub 访问能力。通过 [Skills CLI](https://github.com/vercel-labs/skills) 为 Codex 全局安装：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill '*' --agent codex -g
```

重新运行可更新同一安装范围；去掉 `-g` 则安装到当前项目。先检查安装副本中是否有自定义修改，整合后再更新，不覆盖未处理的改动。其他客户端按实际支持的 Agent 名称调整参数。

`implement-spec` 必须与同源同版本的 `implement` 一起安装：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill implement implement-spec --agent codex -g
```

保留各技能内部的 `references/`、`agents/` 和兄弟目录关系，不能只复制主文件。其余入口可独立使用；缺少辅助技能时沿用现有依据，不因此启动手动专项流程。安装更新后核对实际入口，移除不再使用的旧入口。

## 仓库维护

按 [AGENTS.md](AGENTS.md) 更新技能、显示信息与引用。运行 `python -X utf8 -B scripts/verify_skill_links.py` 检查结构、调用元数据与本地链接；该检查不证明模型行为或实际设计质量，不额外产出报告。
