# Protocol Evolution Loop · v0.x

项目可以为 AIP 提供证据，但项目不能直接修改 AIP。
AIP 不规定软件应该怎么写；AIP 规定 AI 应该怎样认识、修改和记忆一个软件项目。

## 两个独立闭环

- 快循环：Session → Task → Human Review → Project Knowledge。沿用项目固定协议中的知识审批，只改变该项目的知识；项目批准不能授权协议发布。
- 慢循环：Production Trace → Protocol Observation → Pattern Analysis → Proposal → Experiment → Benchmark/Evaluation → Human Approval → Protocol Release。
- 简写：Projects → Evidence → Observation → Proposal → Benchmark → Human Approval → AIP Version。

唯一治理门禁在 [governance.yaml](governance.yaml)。项目侧入口为 [protocol/evolution.yaml](../protocol/evolution.yaml)，只定义边界和路由，不复制治理细节。

## 目录与操作

1. 在 observations/ 复制 TEMPLATE.yaml，引用已脱敏的真实 Task、Review、diff、日志或测量，固定 revision/hash。原始 Trace 留在项目；记录来源和独立事件身份，不能将 AI 自己的总结计为额外证据。
2. 在 observation.analysis 中做 Pattern Analysis：区分项目局部问题与协议机制问题，列出反例、替代解释和适用范围。单次事件可建立观察或安全实验，但不能据此改变所有项目。
3. 在 proposals/ 建立提案，关联观察，提出可证伪假设、精确候选差异、收益/成本与事先约定的指标预算。没有通用性依据的内容退回 Project Model。
4. 在 experiments/ 建立隔离实验，candidate/ 保存候选协议差异或快照，固定 baseline 和 candidate hash；明确选入/排除案例、对照条件、重复次数和停止条件。不得覆盖 workspace protocol/ 或项目固定协议。
5. 在 benchmarks/ 保存输入、预期/禁止行为及评判方式，执行 baseline/candidate 对照，记录原始结果、失败、未知及局限。现有抽象案例是待执行的测试规格，不是已经验证有效的证据。
6. 在 releases/ 起草发布记录，汇总 accepted/rejected/deprecated changes、证据、评估、兼容性、回退与人工审批。先验证精确内容，再由人审批，最后按获批内容应用稳定协议；应用者可为 AI，但不能自行作出批准决定。
7. 在 changelog/ 追加记录，保留被弃用/移除规则及替代关系。项目按固定版本继续运行；升级须逐项目审查差异和显式采用，不自动传播。

## Schema 与模板

[schemas/README.md](schemas/README.md) 定义 YAML 数据使用的 JSON Schema 2020-12 契约；五类模板可直接复制。TEMPLATE 是草稿，不可当作正式证据、测试结果或批准。真实记录必须替换占位值；字段完整不代表事实真实。
[failure-taxonomy.yaml](failure-taxonomy.yaml) 为通用错误分类；[metrics.yaml](metrics.yaml) 为指标口径。协议规则使用 proposal.change 契约，项目 rule.schema.json 仍只管理项目规则。

## 轻量运行与限制

只需 Markdown、YAML 和可选 Git。目录本身不强制权限，也不能验证审批人身份；Agent 与人工 review 执行门禁。没有后台自动发布、数据库或自动学习进程。Git 可用于固定快照；没有 Git 时用逐文件 SHA-256 清单和保留副本，不能声称已经提交或打 tag。
默认不将演进档案加载进项目上下文，只在明确的协议维护任务中按引用检索。证据脱敏、最小摘录、保留来源；敏感数据留在原受控位置。

## Insight Harvest 证据入口

Production Task → 可选 Insight Harvest → Context Critique / Failure Analysis / Pattern Discovery → AIP Observation → Proposal → Experiment/Benchmark → Human Approval → Release。

前置预算与路由统一见 [insight.yaml](../protocol/insight.yaml)，不改变本目录门禁。无失败的机会使用 [INSIGHT-TEMPLATE.yaml](observations/INSIGHT-TEMPLATE.yaml)。反思只提出候选；不能靠自身观察自我强化规则。Context precision/recall 和 cost/efficiency 代理口径见 [metrics.yaml](metrics.yaml)，沿用原有 tokens/files/tool calls，披露采样与未知值。

Recent Signals 前置候选入口见 [recent-signals/README.md](recent-signals/README.md)；外部热度不是 Production Trace，不自动修改稳定 AIP。
