# 中文开发技能

用中文说清目标，让 Agent 按需完成方案、前端原型、任务拆分与前后端实现。共九个技能，参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills)，由用户独立维护。

**围绕结果和 Issue 开发，先集中实现，必要测试与构建留到交付收尾。** 小改动直接做，复杂工作再补方案和任务；技能是可选工具，不是一张必须全部走完的流程表。

## 怎么选

| 当前需要 | 使用技能 | 交付什么 |
| --- | --- | --- |
| 明确的小功能或修复 | [implement](skills/implement/SKILL.md) | 实现与按授权交付 |
| 一组需要分工、跟踪的工作 | [to-tickets](skills/to-tickets/SKILL.md) | 有目标、局部方案、依赖与预期结果的 Issue |
| 按目标连续完成多个任务 | [implement-spec](skills/implement-spec/SKILL.md) | 统一安排依赖、整合、收尾与整体交付 |
| 需要先理清整体方案 | [to-spec](skills/to-spec/SKILL.md) | 一份或多份适合范围的规格 |
| 需要理清页面结构或看完整前端效果 | [design-ui](skills/design-ui/SKILL.md) | 按范围交结构草图，或完整 HTML 原型与实际 Token 文档 |
| 想法或关键选择尚不清楚 | [grilling](skills/grilling/SKILL.md) | 问题与选项、已定结论及未知项 |
| 业务对象、关系或规则有歧义 | [domain-modeling](skills/domain-modeling/SKILL.md) | 当前范围的统一业务定义 |
| 需要配置项目入口 | [setup-project-skills](skills/setup-project-skills/SKILL.md) | 简短项目索引与唯一状态入口 |
| 做完后需要听懂结果 | [explain-work](skills/explain-work/SKILL.md) | 结果、原因、关键流程与证据范围 |

日常可以只用 `implement`；需要跟踪时加 `to-tickets`，连续多任务交给 `implement-spec`。其余在对应问题出现时使用，不需要逐个调用或逐阶段确认。

## 从想法到可用功能

- **小改动：** 直接实施，已有依据足够就复用，不补 PRD、Spec、Issue 全套文件。
- **一项完整能力：** 需要时先写 Spec；涉及界面先做或复用原型，再拆必要 Issue 并实施。
- **较大项目：** 以 PRD/已有计划为整体依据，划分多份 Spec，近期细化、远期保留范围与依赖，持续完成已授权目标。

这些工作可以往返调整。业务含义在技术模块设计前核对，设计影响接口时回写方案；Spec 和任务划分不等于页面划分。Issue 优先承接一条用户可见流程，让前端、接口和数据协作形成可用结果；原型、模拟和真实接入分别记录；共用基础设施按真实依赖安排，不机械拆成互不衔接的前后端清单。

原始需求和 Issue 足以实施就不强求 Spec；已有 Spec 时，Issue 引用具体章节，只补本任务边界、局部差异和交接，不再复制整套契约与完成标准。只为需要独立交接的成果拆任务，普通选型、查证和配置留在方案或实现任务内。

## 几条共同原则

代码和实际行为用于判断现状，已确认的新需求决定目标；文档不一致时沿用现有惯例并说明差异，不能因新功能尚未实现就忽略它。

每项决定只保留一份正文：业务含义归领域记录，整体方案与共同接口归 Spec，页面与视觉归原型和 Token，实际数值与组件实现归源码，单项要求与结果归 Issue。现有文件能承接就原位更新，其他位置引用；不要求每类都有独立文件。

事实由 Agent 调查，既定约束内的可逆选型自行决定并说明依据；补齐缺失模块不等于替换现有技术栈。只有真正改变目标、业务规则、用户权利或授权范围的选择才提问。`grilling` 每题只给问题和两个或更多选项，不附建议或解释。

## 集中开发与收尾

不默认采用 TDD。完整执行方法集中在 [implement](skills/implement/SKILL.md)，`implement-spec` 读取并复用，只增加跨任务的协调职责。测试、验证与构建按最终改动和交付需要，在授权目标或用户明确要求单独交付的阶段收尾处理；Issue、提交、内部批次不自动成为验证节点。已有测试与强制 CI 保留，当前阻碍的最小复现、预览启动与不可逆操作前的保护按需进行。

独立任务由执行者收尾；连续开发由主 Agent 合并安排，子任务先回交实现和待收尾事项。交付区分本地、提交推送和 PR，沿用授权；未验证不能写成通过，PR 请求不自动授权合并。成果保存、临时工作树和其他修改的保护也按 `implement` 执行。

## 完整前端原型

`design-ui` 按需先用一次性 HTML 草图或 ASCII 线框明确页面层级、导航与内容尺寸、分栏、密度和打开关系；只要求草图就按范围交付，已授权完整设计则继续，不默认停等批准。结构明确后先复用或定义实际 Token，再制作组件与页面；完整原型保留指定参考、全部页面与子页、分页、字体字重、背景配色、状态和可重看的动效，正式业务接入留给实现。

完整设计默认只交付 `docs/design/design-board.html` 和 `docs/design/design-token.md`。草图可完善为最终 HTML 或由其接替，无需长期维护两套。HTML 先展示产品页面，来源与模拟限制放在折叠说明区；样式变量先定义、组件统一引用，Token 文档在完成后从实际样式整理。做好即交付，反馈修改时同步，不附加质量报告。

## 模板与设计参考

| 文件 | 用途 |
| --- | --- |
| [Spec 模板](skills/to-spec/references/spec-template.md) | 本次想实现什么、想要什么、不想要什么，以及业务、技术方案、依赖和结果 |
| [Issue 模板](skills/to-tickets/references/issue-template.md) | 同样先说明三问，再写可接手的局部方案、依赖、预期结果和实际交接 |
| [好坏设计参考](skills/design-ui/references/design-quality.md) | 用具体好坏对照帮助判断视觉取舍，不作为验收清单 |
| [设计系统与组件规则](skills/design-ui/references/design-system.md) | 制作前读取，统一 Token、排版间距、组件、状态与适配；已有约定优先 |

使用时按范围裁剪或映射已有模板，不为填空发明内容。

## 项目配置

`setup-project-skills` 在项目的 `AGENTS.md` 或 `CLAUDE.md` 维护一份简短索引，指向真实文件和查到的命令，不复制正文与进度。当前任务要求优先，项目已确认约定覆盖个人全局偏好和技能默认；未确定部分再沿用偏好。前后端技术栈、设计组件、任务平台、交付方式和已有收尾命令都能在这一处调整；专业技能按需链接，临时选择不自动变成长期默认。

状态沿用现有入口；无约定时，有 GitHub 用固定“项目当前状态”Issue，没有则用 `STATUS.md`。README 与索引指向同处，由主 Agent 在接手、关键变化与暂停/结束时更新，区分设计、实现、待验证、分支可用、主线可用与用户验收；不承诺后台自动刷新。

## 安装与更新

需要 Node.js 22.20 或更新的受支持版本（含 npm/npx）、Git，以及 npm 和 GitHub 访问能力。通过 [Skills CLI](https://github.com/vercel-labs/skills) 安装，例如为 Codex 全局安装全部技能：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill '*' --agent codex -g
```

`-g` 表示所有项目可用，去掉则装到当前项目；重新运行相同命令可更新原范围。安装副本有自己修改的内容时先保存。交互选择可省略 `--skill` 与 `--agent`，只查看目录可加 `--list`；其他 Agent 名称见 [支持列表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

除 `implement-spec` 外，各入口都能独立使用，其他技能缺失时可完成同职责的梳理。**`implement-spec` 必须与同源同版本的 `implement` 一起安装**；它读取后者复用执行方法。按 Issue 开发的最小组合可用：

```sh
npx skills@latest add axgiroud312-byte/personal-development-skills --skill to-tickets implement implement-spec --agent codex -g
```

已安装但缺少依赖时，运行这条命令统一更新相应技能。安装源应保留每个技能内的 `references/`、`agents/` 及兄弟目录相对关系，不能只复制 `SKILL.md`。

旧版 `grill-with-docs` 已合并进 `grilling`，升级不会自动删除旧入口；确认安装范围后，可用 `npx skills@latest remove grill-with-docs --agent codex -g` 移除。新安装无需处理，项目级或其它 Agent 相应调整参数；不要误删仍被其它 Agent 使用的副本。

## 维护与评估

主文件保留职责、流程和读取时机，模板与设计参考单独维护。中文说明以能读懂、能执行为准，以 120 行以内为目标，效果优先；改动同步显示信息和引用，不靠超长行压缩。

用户要求循环优化时才运行多路线评估，记录真实依据与未验证项；结构检查不能证明模型行为。本次 [迭代评估](evaluation/toloop-2026-10-27.md) 包含新旧版实际任务对照与限制；已有 [四轮记录](EVALUATION.md) 和 [十轮记录](evaluation/ten-rounds-2026-10-26.md) 保留为历史，不构成日常任务的默认流程。技能源的维护约定见 [AGENTS.md](AGENTS.md)。
