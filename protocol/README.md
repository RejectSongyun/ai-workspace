# AIP v0.2.2

AIP 不规定软件应该怎么写；AIP 规定 AI 应该怎样认识、修改和记忆一个软件项目。

## 三层边界

| 层 | 内容 | 权威 |
| --- | --- | --- |
| AIP Protocol | 检索、任务范围、执行、知识生命周期、审核、追踪及抽象数据契约 | 协作过程 |
| Project Model | 技术元数据、模块、Architecture、Rule、Feature、ADR、索引 | 人工批准决定代表设计意图；生成记录批准前是候选 |
| Source Reality | 实际代码、配置、测试、构建、Git | 当前实现事实；测试结果只证明其覆盖范围 |

协议不假设源码结构，不根据技术元数据选择行为。规则 statement 是不透明文本；协议只检查字段、来源、范围、状态和审核，具体规则由项目定义。

## 使用

统一模板位于 `../templates/project/`。初始化工具为 `../tools/Initialize-AipProject.ps1`，默认预览，增加 `-Apply` 写入。已有 `.ai` 或 `AGENTS.md` 时拒绝覆盖，请在临时目录生成后增量合并。

新项目建议放 `../projects/`，现有项目路径不受限制。填写 `.ai/project.yaml` 的项目身份与已核验路径；technology 可完全省略，extensions 是可选开放元数据，均不影响协议运行。未知源码与验证命令保持空值，不猜测。

项目 `.ai/protocol/` 和 `.ai/schema/` 是初始化时固定的协议及契约快照；以 workspace `protocol/` 为发布来源，禁止在 adapters 中复制协议。升级现有项目时先比较差异，按既有授权和审核要求采用，不自动覆盖。

一次任务：建立 Task Scope → 按 Index 检索相关 Architecture/Rule/ADR → 核验 Source Reality → 最小修改并验证 → 提交候选结果和证据 → 人工审核。任务完成不自动晋升长期知识；高等级设计变更审核见 review.yaml，知识 provenance/stale 规则见 knowledge.yaml。

Preserve History, Minimize Context：历史保留，按需检索。YAML/Schema 是约定而非强制执行器；批准真实性、语义符合性与失效传播仍需 Agent 和人工核验。

## v0.2.1：独立协议演进

项目可以为 AIP 提供证据，但项目不能直接修改 AIP。

项目快循环保留原有知识审批；独立慢循环及唯一治理规范见 [evolution/README.md](../evolution/README.md) 和 [governance.yaml](../evolution/governance.yaml)。项目快照只携带 [evolution.yaml](evolution.yaml) 的边界与路由，不复制演进档案。

该增量只建立演进基础设施与边界，不表示生产实验已通过，也不自动批准将来的改进。版本 0.2.1 标识本次用户明确要求的配置增量；已有项目 0.2 快照保持不变。

## v0.2.2：Context Investment Must Compound

[insight.yaml](insight.yaml) 是洞察触发、R0–R3 预算、候选路由的唯一规则来源。Product 是任务结果，Knowledge 是项目认知增量，Insight 是生产机制洞察；各自生命周期与审批分离，不要求每次产生三份文档。

主任务验证、Review、交付后按证据判断是否执行可选 Insight Pass。简单任务默认 R0；有价值的触发可请求 R1，高价值/失败/关键纠偏可请求 R2，协议问题可请求 R3。Runtime 按已批准策略或授权人授予有限预算；没有授权即 R0。模板在 [templates/](templates/)，契约在 [schema/](schema/)。YAML 只定义契约，不代表已实现自动调度或自动计量。

候选进入现有项目知识审批或独立 Evolution Loop；Context Critique 提供 Resolver 相关性、实际使用和关键证据的比较。Context ROI 是质量约束下的多目标改进，不能以更多输出文本代替收益。
