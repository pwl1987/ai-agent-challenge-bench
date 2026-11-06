# AI Agent Challenge Bench

面向 AI 编程 Agent 的可复现挑战基准。V0.1 只接受可自动执行、可审计、可重放的评分证据。

## V0.1 闭环

1. 挑战以 `schema/challenge.schema.json` 描述输入、环境、硬门槛、评分维度和证据要求。
2. Agent 在隔离工作区按挑战指令实现，运行公共测试骨架并输出机器可读结果。
3. 评分器先检查硬门槛，再计算功能、算法、交互、工程质量分；无法复现或证据不足时标记 `UNSCORED`。
4. CI 校验所有挑战文档、Schema、测试骨架和 YAML 结构，禁止把主观评价写成自动分数。

## 目录

- `CHARTER.md`：项目章程与治理边界。
- `SPEC.md`：完整评分规范。
- `schema/challenge.schema.json`：挑战定义 Schema。
- `protocol/EXECUTION_AND_SCORING.md`：执行、证据、复现与抗作弊协议。
- `challenges/`：首批代表性挑战。
- `tests/skeleton/`：公共测试骨架约定与示例。
- `scoring/score.py`：确定性评分器；证据不足输出 `UNSCORED`。\n- `schema/result.schema.json`：机器可读结果 Schema。\n- `tests/skeleton/`：公共结果样例与可执行评分测试。\n- `prompts/manual/`：人工复制到 Agent 的完整提示词。\n- `prompts/automated/`：后续自动化 Runner 约定。\n- `.github/workflows/validate.yml`：机器文件和评分器校验。

## 状态

V0.1 是规范与公共骨架版本，不声称任何 Agent 已获得实测分数；没有运行证据就不生成排行榜。
