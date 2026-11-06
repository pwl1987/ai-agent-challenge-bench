# S01｜蚂蚁军团智能寻路与动态避障（人工复制版，长提示词）

你是一名资深群体智能算法工程师、实时仿真工程师和软件交付负责人。请在当前空项目目录中制作一个完整、可运行、可复现、可被独立脚本评测的蚂蚁军团寻路系统。挑战版本固定为 ant-pathfinding v0.2.0。

## 一、交付与运行

请先检查当前目录，不要假设已有代码。优先交付 Python 3.11+ 命令行项目，只使用标准库或明确锁定版本的轻量依赖。不得联网调用外部服务，不得读取项目目录以外的秘密文件，不得修改公共测试或评分脚本来制造通过。

必须支持从 JSON 文件或 stdin 读取输入，将唯一机器可读结果写到 stdout，将人类可读日志写到 stderr，并在干净环境中用一条命令运行。提交 README、依赖锁定、源码、公共测试和运行样例。无法运行时返回明确的 UNSCORED，不得伪造成功。

建议结构：src/、tests/public/、evidence/、README.md。

## 二、任务目标

实现二维网格上的蚂蚁军团寻路。蚂蚁从起点出发，尝试到达终点，在障碍、分叉和动态变化环境中通过信息素或等价的群体搜索机制形成可解释路径。

至少支持 1、10、100、1000 只蚂蚁；4 邻域和 8 邻域；静态障碍；按固定时间表变化的动态障碍；信息素蒸发、沉积、探索/利用权衡；提前收敛；最佳路径、迭代次数、运行耗时和确定性摘要。

不得把 A* 或 BFS 的结果硬编码成蚂蚁算法结果。可以提供传统算法作为 baseline，但必须明确区分。

## 三、输入契约

输入 JSON 至少包含 width、height、obstacles、start、goal、ants、iterations、seed、neighborhood、dynamic_obstacles（可选）和 algorithm。

验证坐标边界、起终点可通行、障碍去重、数值有限和安全资源上限。起点等于终点必须返回长度为 0 的合法结果。完全不可达必须返回 UNREACHABLE，不能伪造路径。

## 四、真实算法状态

每只蚂蚁必须有当前位置、已走路径、访问状态和是否到达状态；网格必须维护信息素；每轮必须执行蒸发、成功路径沉积、启发式决策和探索/利用决策。

每轮顺序固定为：应用动态障碍、推进蚂蚁、检查越界/障碍/重复访问/到达、沉积信息素、蒸发并裁剪、记录统计、判断停止。

邻居排序必须固定，不能依赖集合遍历、线程调度或当前时间随机数。动态障碍出现后要重新检查现有路径，不能继续报告穿过新障碍的旧路径。并行实现必须提供 deterministic 模式。

## 五、结果契约

stdout 只能输出一个 JSON 对象，至少包含 challenge_id、challenge_version、status、reason、seed、width、height、neighborhood、ants、iterations、iterations_executed、path、path_length、path_cost、best_iteration、reached_ants、wall_seconds、algorithm、parameters、determinism_hash 和 diagnostics。

status 至少支持 SOLVED、UNREACHABLE、INVALID_INPUT、RESOURCE_LIMIT、UNSCORED。path 必须从 start 到 goal，每一步符合邻域规则且不经过当前障碍。determinism_hash 必须由规范化结果或关键状态计算，不能随机生成。耗时不得纳入确定性哈希。

diagnostics 至少包含 invalid_moves、non_finite_count、pheromone_min、pheromone_max。所有统计必须来自真实运行状态，不得写死。

## 六、测试矩阵

必须实际运行并验证结果契约：起点等于终点、直线路径、唯一窄通道、多分叉多解、完全不可达、非法输入、4/8 邻域差异、动态障碍、相同 seed 连续两次、不同 seed、1000 只蚂蚁压力场景、超限资源和 NaN/Infinity 防护。

重复运行时允许 wall_seconds 不同，但规范化结果和确定性哈希必须一致。stdout 必须可被严格 JSON 解析。

## 七、性能与资源

至少报告 32×32/100 只蚂蚁、128×128/1000 只蚂蚁和项目实际安全上限。报告网格、蚂蚁数、迭代数、耗时、峰值内存（若能测量）、每轮平均耗时和 deterministic 状态。

设置明确上限，超限返回 RESOURCE_LIMIT，不得卡死。不得通过减少蚂蚁数、跳过迭代或伪造统计掩盖性能问题。

## 八、复现证据

完成后显示项目树和主要入口，展示安装、运行和测试命令，运行全部公共测试，固定 seed 连续运行两次并比较，运行一组压力测试，检查 git diff 和 git status，生成 evidence/summary.json。

summary 至少包含 challenge_id、challenge_version、提交 SHA、精确命令、测试通过/失败数量、输入摘要、运行时版本、性能数据、复现哈希、未完成项和无法评测原因。非 Git 目录的 SHA 写 null。

## 九、抗作弊边界

只输出预先写死路径、只运行 BFS/A* 却声称蚁群、按测试文件名分支、修改测试或评分器、依赖当前时间或外部服务、忽略障碍检查、写死统计、只给伪代码或截图，均不得计为通过。baseline 可以存在，但必须显式标注。

## 十、最终回复

最终只报告已创建文件、冷启动命令、公共测试命令、固定 seed 复现命令、测试摘要、性能摘要和未完成项。不要自行给官方分数；无法验证的部分必须标记为 UNSCORED。
