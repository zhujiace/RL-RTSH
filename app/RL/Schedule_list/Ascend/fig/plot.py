import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =========================
# 配置
# =========================
csv_path = "257_1.3_1000eps_5t_test_default.csv"
save_path = "train_return_plot.png"
title = "Training Return"
xlabel = "Step"
ylabel = "Return"

# 只显示多少 step 以前
max_step = 460

# 平滑系数：越大越平滑，推荐 0.90 ~ 0.97
smoothing = 0.93


def smooth_curve(values, weight=0.93):
    values = np.asarray(values, dtype=float)
    if len(values) == 0:
        return values

    smoothed = np.zeros_like(values)
    smoothed[0] = values[0]
    for i in range(1, len(values)):
        smoothed[i] = weight * smoothed[i - 1] + (1 - weight) * values[i]
    return smoothed


# =========================
# 读取数据
# =========================
df = pd.read_csv(csv_path)

# 只保留 Step <= 500
df = df[df["Step"] <= max_step].copy()

steps = df["Step"].to_numpy()
values = df["Value"].to_numpy()
smoothed = smooth_curve(values, smoothing)


# =========================
# 绘图
# =========================
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=160)

ax.plot(
    steps,
    values,
    linewidth=1.2,
    alpha=0.25,
    label="Raw return"
)

ax.plot(
    steps,
    smoothed,
    linewidth=2.8,
    label="Smoothed return"
)

ax.set_title(title, fontsize=16, pad=14, weight="bold")
ax.set_xlabel(xlabel, fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)

ax.grid(True, linestyle="--", linewidth=0.8, alpha=0.35)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend(frameon=False, fontsize=11, loc="upper left")

plt.tight_layout()
plt.savefig(save_path, dpi=300, bbox_inches="tight")
# plt.show()