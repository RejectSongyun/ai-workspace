# YAML 记录契约

这些 JSON Schema 2020-12 验证同名 YAML 数据：observation、proposal、experiment、benchmark、release 和 failure。五类目录中的 TEMPLATE.yaml 是结构有效的草稿；UNSET、TEMPLATE、null 和 not_run 不能作为正式发布依据。

路径契约：记录内 reference.path 统一相对 workspace 根目录；外部证据用明确的绝对路径或 URI，并注明固定 revision/hash。Schema 不能证明外部路径可访问、哈希正确、证据真实或审批身份。

提交审核前人工/Agent 需检查：所有占位值已替换；引用可定位且 revision/hash 相符；事件去重；分类与 failure-taxonomy 一致；指标分母/样本数/缺失值齐全；实验与 baseline 可比较；失败和反例保留。
release 状态为 approved/released 时必须有明确批准；released 还需实际应用 hash 与时间。发布前应另核对 approved_artifact_sha256 等于 artifact_manifest 的 SHA-256，且清单中的逐文件 hash 等于待应用内容。例外路径必须同时有非空 exception_reason 和人工 exception_approved=true；不能用结构验证代替此审核。

项目 protocol/schema/rule.schema.json 继续描述项目知识规则；不得将本目录的协议生命周期套用到项目规则上。

Insight 接入：observation_kind 可选，旧记录仍有效；无失败的机会/模式必须填 opportunity/pattern 且 failure: null，使用 observations/INSIGHT-TEMPLATE.yaml。保留已有 evidence、impact、suspected_cause、analysis 字段；非失败假设可描述收益成因，不制造失败事实。Context Critique 以 production_trace 或 measurement evidence 引用 Task 附件、版本及独立事件 ID；同一事件的 signal/critique/summary 不能重复计数。
