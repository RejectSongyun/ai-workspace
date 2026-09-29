# AGENTS.md 接入

项目根入口读取 `.ai/project.yaml`，随后读取 protocol_path 中的 protocol.yaml/includes，并通过 context_index 检索项目记录。入口示例见 ../templates/project/AGENTS.md。不在入口维护另一套协议。
