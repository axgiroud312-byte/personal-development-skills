# 中文开发技能

这套技能帮助你把想法变成可用功能。核心流程是：**Spec 写整体规格，Issue 写具体任务，implement 集中完成开发。** 简单修改可以直接实施。

你决定目标和重要取舍，Agent 根据已有方案和实际代码处理工程细节。完成一组相关工作后，统一做必要检查并交付。

## 什么时候用哪个技能

| 你想做什么 | 技能 | 得到什么 |
| --- | --- | --- |
| 把想法说清楚 | [grilling](skills/grilling/SKILL.md) | 在聊天中明确目标和关键选择 |
| 写整体开发方案 | [to-spec](skills/to-spec/SKILL.md) | 目标、范围、方案和完成标准 |
| 把方案拆成任务 | [to-tickets](skills/to-tickets/SKILL.md) | 有具体做法、依赖和结果的 Issue |
| 完成功能或修复 | [implement](skills/implement/SKILL.md) | 可使用的成果和实际检查结果 |
| 连续完成多个任务 | [implement-spec](skills/implement-spec/SKILL.md) | 统一安排、整合和交付的成果 |
| 先看界面效果 | [design-ui](skills/design-ui/SKILL.md) | HTML 原型，满意后提取 Token |
| 找出界面中的 AI 味问题 | [design-quality](skills/design-quality/SKILL.md) | 结合实际页面判断 AI slop |
| 让项目知道这套流程 | [setup-project-skills](skills/setup-project-skills/SKILL.md) | 写入 `AGENTS.md` 的流程和文档位置 |
| 听懂刚才做了什么 | [explain-work](skills/explain-work/SKILL.md) | 通俗的结果、原因和使用说明 |

`to-spec`、`to-tickets`、`design-ui`、`setup-project-skills` 由你主动调用。一次任务里的补充、修改和确认可以连续处理；普通开发按需要读取和更新已有资料。

这四个入口保留 `disable-model-invocation: true` 和 `policy.allow_implicit_invocation: false`。客户端支持这些开关时，由客户端控制调用；其他客户端按技能正文约定使用。

## 文档放在哪里

| 资料 | 默认位置 | 写什么 |
| --- | --- | --- |
| 项目入口 | `AGENTS.md` | 这套技能的流程、文档位置和工作准则，保留项目已有指令 |
| Spec | `docs/specs/<主题>.md` | 整体开发规格与共同要求 |
| Issue | 远程 Issue；未配置任务平台时用 `docs/issues/<标识>.md` | 具体任务、方案和进展 |
| 原型 | `docs/design/design-board.html` | 页面、交互、组件和来源说明 |
| Design Token | `docs/design/design-token.md` | 已确认原型实际使用的共用样式值 |

按当前任务产出所需资料，已有同类文件沿用原位置。讨论和工作解释直接在聊天交付。每项信息保留一份正文，其他位置引用。

远程 Issue 可用时直接在远程维护；暂时访问受阻时，在聊天保留待发布草稿和具体阻碍。先核实任务功能可用，再选择任务位置。

`setup-project-skills` 将这张资料地图和技能流程写进项目 `AGENTS.md`，让后续 Agent 能找到工作依据。

## 怎样协作

用户当前目标和明确要求决定工作方向。Agent 阅读相关代码、资料和实际结果，自主处理工程细节；重要假设和方案变化用短句说明，方便你纠正。涉及目标、明确要求、关键体验或新增重要影响的取舍，由你决定，其余工作继续。

遇到文档过时或实现矛盾时，先查清原因，沿用合适的现有做法，修正已证实的错误。重要调整写回对应 Spec 或 Issue，完成后说明差异。

集中完成相关开发，目标收尾统一必要检查。中途遇到实际错误，或一个关键疑问会影响大量后续工作，先做足以判断的小检查。检查通过后继续交付；新改动和新问题按影响复查。测试优先复用项目现有安排，新增测试用来确认具体行为或防止已知问题再次出现。

结果按实际情况说明：代码已改、真实运行、模拟检查、等待验证、用户验收。有对应 Issue 时，将进展和结果写回该 Issue；其他任务在聊天中交接。

## 设计怎样交给开发

`design-ui` 先交一个可打开的 HTML，按你的反馈修改同一版。你确认满意后，再从实际样式提取一份 Token 文档。正式开发参考布局、交互和样式值，在项目中完成真实业务。

[AI slop 清单](skills/design-quality/references/design-quality.md) 保留你指定的负面设计参考，按实际页面判断问题。[Spec 模板](skills/to-spec/references/spec-template.md) 帮助写清整体方案，[Issue 模板](skills/to-tickets/references/issue-template.md) 帮助把任务交给下一位执行者。

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
