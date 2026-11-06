# R01｜六足机器人自主行走、抓杯与倒水（单文件 HTML 长提示词）

你是一名资深实时图形工程师、机器人运动规划工程师和技术美术。请制作一个完整的单文件 HTML，展示六足机器人从起点行走到容器、抓取左杯、移动到右杯并倒水的连续过程。最终只交付完整 HTML，不输出解释，不省略代码。

## 一、交付与运行

HTML、CSS、业务 JavaScript 和 shader 全部内联。只允许固定版本 Three.js 及官方 addons，或浏览器原生 API。不得使用外部图片、视频、模型、字体、音频或网络 API。通过本地 HTTP 服务打开即可运行；WebGL2 不可用时显示可读错误。

初始加载后显示暂停的 3D 场景：机身、六条腿、两个杯子、地面和障碍。提供明显播放按钮；初始化失败不得无限等待。

## 二、统一坐标与时间轴

明确竖直轴、机器人坐标、杯子坐标和地面坐标。固定 seed=19450806，重播不重抽。

演示时间 t∈[0,60]：

0–8 秒展示机器人、左右杯和地形；
8–22 秒执行交替三角步态到左杯；
22–30 秒对准、夹紧并抬升；
30–42 秒携杯移动到右杯；
42–50 秒倾斜容器并结算液体；
50–60 秒放回、释放并展示统计。

阶段可重叠，但不得用预录动画跳过状态。

## 三、机器人与步态

建立机身、六条腿、每腿至少三个关节、足端、关节限位和夹爪。实现正运动学、足端逆运动学或明确的落点求解；记录支撑腿/摆动腿、机身姿态、稳定性和碰撞。

支持平地、坡面、台阶和障碍。每个固定仿真步检查足端穿透、支撑多边形、重心投影、关节越限、滑移和倾覆。不可达或倾覆必须进入失败状态并记录原因。

## 四、抓取与液体状态

抓取必须有接近、闭合、附着确认、抬升和释放状态，杯子不能瞬移。液体可以用粒子或体积守恒近似，但必须维护 requestedVolume、carriedVolume、deliveredVolume、spilledVolume、remainingVolume 和 volumeError。

成功条件：机器人到达、抓取确认、未倾覆、目标杯有效，且 deliveredVolume/requestedVolume≥0.8。空杯、掉杯、目标不可达和液体误差过大必须有明确失败状态。

## 五、交互与评测接口

提供播放/暂停、重播、单步、0.5×/1×/2×、时间轴、电影镜头/自由观察、低/高画质、显示骨架和诊断面板。

通过 window.demo 暴露 ready、pause()、play()、reset()、step(count)、seek(seconds)、setQuality("low"|"high") 和 getState()。

getState 至少包含 seed、time、playing、seeking、cameraMode、gaitPhase、jointCount、robotPose、reachedGoal、grasped、tiltedOver、requestedVolume、deliveredVolume、spilledVolume、remainingVolume、collisionCount、unstableStepCount、fixedDt、simulationStep、nonFiniteCount 和 determinismHash。

## 六、测试、性能与证据

测试平地成功、坡面、台阶、不可达、抓取失败、倾覆、空杯、目标杯不可用、液体守恒和固定 seed 重播。报告低/高画质平均帧时间、固定步耗时、活跃粒子数、内存（若可测量）和资源上限。

提交 README、运行命令、测试命令、截图/录屏、evidence/summary.json 和已知限制。无法实际运行的部分标记 UNSCORED。

## 七、抗作弊

不得抓取后瞬移杯子、直接写入 deliveredVolume、只播放预设动画、用 HUD 冒充 3D、写死成功统计或忽略倾覆/碰撞。不要宣称真实硬件控制或工程级流体预测。