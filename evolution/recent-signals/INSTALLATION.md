# last30days 接入记录 — 2026-09-28

- 官方版本：3.25.0；安装 CLI：skills 1.7.0；Node 24.19.0；Python 3.12.14。
- 安装：C:\Users\14604\.agents\skills\last30days；Codex skills/list 返回 scope=user、enabled=true、无错误。
- 下载源：https://codeload.github.com/mvanhorn/last30days-skill/zip/refs/heads/main 。main 为移动分支，本次用逐文件 SHA-256 固定已安装内容，不声称固定了 Git commit。
- 原定远程 CLI 安装因 Git 下载卡住被终止；改由官方 CLI 从官方压缩包解压目录 --copy 安装，source=null，因此自动远程更新尚未建立。
- 安装文件与下载源码逐文件 SHA-256 对比一致（清单保存在本次交付 outputs/installed-skill-sha256.json）。
- 官方 preflight：safe=true、status=ready、Cookie off、凭据均 false、local_writes=[]。
- 官方 doctor 已执行：退出 0 代表诊断完成，不代表所有可选来源健康；付费来源未配置，多个可选 CLI 缺失。未安装可选依赖，未执行 setup。
- 两次真实引擎查询（一次直接验证、一次从工作区入口调用）：context engineering，30 天窗口，HN 免费公开来源，均 exit=0、source_status.hackernews=ok、4 条结果。
- 单源、quick 检索仅证明安装/调用链有效，不代表全面技术结论，更不是生产有效性证据；无 AIP 改进自动晋升。
- workspace protocol/ 及其他所有已有文件 SHA-256 不变，仅 AGENTS.md 与 evolution/README.md 追加入口，原字节前缀保留。
- 临时结果位于 tmp/recent-signals/ 下唯一目录。无 Cookie 读取、凭据写入、付费 API、外部发布、原文件删除或覆盖。

调用、候选门禁、更新限制及卸载见 README.md。
