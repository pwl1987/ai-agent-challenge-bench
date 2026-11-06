# 公共测试骨架

每个挑战至少提供 `tests/public`，包含：正常路径、边界输入、不可达/失败输入、固定种子重复运行和输出 Schema 校验。测试只断言公开契约，不泄露隐藏测试输入或参考解。

推荐结果结构：

```json
{"status":"PASS","challenge_id":"...","challenge_version":"v0.1.0","commit_sha":"...","score":null,"reasons":[],"metrics":{"wall_seconds":0.0}}
```

骨架不得自行给出总分；总分只由版本化评分器在硬门槛通过后生成。
