# ai-bootcamp

六个月 AI 转岗实训代码库（主线：AI＋工程仿真，代理模型 → PINN → 多保真 → 算子学习）。
每周一小步，模块配 pytest 测试，环境用 uv 锁定。

## 环境

Python 3.13.9，依赖由 uv 管理。首次克隆后一条命令还原环境：

```bat
uv sync
```

## 结构

- `src/ai_bootcamp/` 核心模块
- `tests/` pytest 测试
- `data/` 数据集
- `notes/` 学习笔记

## 跑测试

```bat
uv run pytest -q
```

## 进度

- W1（环境与仓库）：本仓库上线
- W2（工程化语法）：类型注解 · dataclass · pytest
- W3（Git 工作流）：分支 · 合并 · 回滚演练
