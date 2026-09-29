# 数据契约

JSON Schema 2020-12 校验 YAML 解析后的对象。project、task、candidate、rule 定义结构，不解释技术语义。rule 的 type/level/scope 是项目定义值；statement 不做技术词汇匹配。长期知识批准时 provenance 必须填写真实证据；null 占位不能代表审核通过。Schema 校验不证明批准真实性或规则语义符合性。

## Insight 契约

`insight-signal.schema.json` 和 `context-critique.schema.json` 为可选 Task 附件，模板见协议 `templates/`。模板中的 UNSET 不是有效证据或批准。
Critique 的 provided/missing 使用唯一 item ID；actually_used/decisive 必须引用两者并集，unnecessary 必须引用 provided。missing 是初次检索缺失，之后补取可实际使用；decisive 须有结果证据。相同 ID 不能同时 provided/missing 或 actually_used/unnecessary。Schema 校验结构，引用/语义/预算授权真实性由 Runtime 或人工检查。路径相对项目根目录；外部引用明确写绝对路径。
