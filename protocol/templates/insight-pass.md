# Insight Pass（可选候选记录）

规则唯一来源：项目固定协议 `insight.yaml`。R0 不需填本模板。

- Task / source revision / Review evidence / Primary Output reference:
- Trigger / signal reference / grant reference / granted R-level:
- Actual extra tokens / elapsed seconds / tool calls（未知写原因）:
- Status: completed / stopped / deferred；停止原因:

## 反事实检查

只回答与证据相关的问题；无依据可跳过，不为填表追加探索。

1. 重做 Task 时，提前知道什么可减少探索？引用事实、路径和版本。
2. Resolver 漏了什么？是索引、范围、过时信息还是检索策略问题？
3. 哪些 Context 无用？区分未使用、已判无关与未知，避免事后偏见。
4. 什么可核验事实能避免同类失败？反例和替代解释是什么？
5. 发现仅属于本项目，还是可能属于 AIP？可推广性仍缺哪些证据？
6. Human 在哪里提供关键判断？保留原反馈引用，不把纠正扩大成永久规则。
7. AIP 哪个流程成本偏高、收益不足？先比较不变、项目修复、简化、合并或移除。

## 路由（每条独立记录）

| ID | 事实/假设 | evidence + hash + event ID | 预期收益与反例 | disposition | candidate reference |
| --- | --- | --- | --- | --- | --- |

disposition 只允许 project_insight_candidate / aip_observation_candidate / discard_noise。
项目候选复用既有知识模板；协议候选复用 workspace observation 模板。
Context Critique / Failure Analysis / Pattern Discovery 均是证据，不是审批。
空产出是有效结果；不创建占位候选，不以数量评价收益。
