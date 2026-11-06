# 人工复制提示词总目录

使用方式：先复制目标文件中的完整任务提示词到 Agent；Agent 完成后按仓库评分协议提交结果和证据。提示词是人工执行资产，不要求 CI 对自然语言正文做校验。

统一写作标准：[PROMPT_AUTHORING_STANDARD.md](./PROMPT_AUTHORING_STANDARD.md)。S01 已按该标准改写为长提示词样板。

## 已整理的首批提示词

| 编号 | 主题 | 文件 |
|---|---|---|
| S01 | 蚂蚁军团智能寻路 | [ant-pathfinding.md](./ant-pathfinding.md)（长提示词样板） |
| R01 | 六足机器人倒水 | [hexapod-water-transfer.md](./hexapod-water-transfer.md) |
| R01-A~F | 六足机器人分级拆解 | [hexapod-levels.md](./hexapod-levels.md) |
| R02 | 机械臂抓取/绘画/倒水 | [robotic-arm.md](./robotic-arm.md) |
| G01 | 3D 魔方求解 | [rubiks-cube-3d.md](./rubiks-cube-3d.md) |
| C03 | 3D 水流与瀑布 | [3d-fluid-waterfall.md](./3d-fluid-waterfall.md) |
| W01 | 程序化 3D 城市 | [procedural-city.md](./procedural-city.md) |
| S02 | 万鸟齐飞/无人机蜂群 | [boids-flock.md](./boids-flock.md) |
| P01 | 物理沙盒 | [physics-sandbox.md](./physics-sandbox.md) |
| P02 | 宇宙引力沙盒 | [gravity-sandbox.md](./gravity-sandbox.md) |

## 规划中的完整挑战矩阵

V0.1 先保留 12 类 × 5 个挑战的目录位，逐项补充同等粒度的完整提示词和可执行测试：

- swarm：群体智能与蜂群
- robotics：机器人与运动规划
- fluids：流体、液体与材料
- physics：物理沙盒与动力学
- characters：角色、动画与行为
- worlds：程序化世界与城市
- games：可交互游戏机制
- graphics：渲染、光照与几何
- ecosystems：生态与环境仿真
- space：航天、轨道与宇宙
- media：音视频与多模态处理
- algorithms：经典算法与优化

每个新挑战必须补齐：目标、约束、输入/输出、硬门槛、证据要求、复现方法、抗作弊说明、性能指标和未评测边界。