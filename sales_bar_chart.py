import matplotlib.pyplot as plt
import numpy as np

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = [34200, 51800, 29400, 47600, 38900]

colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(products, sales, color=colors, width=0.6, edgecolor="white", linewidth=0.8)

for bar, value in zip(bars, sales):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 600,
        f"${value:,}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        color="#333333",
    )

ax.set_title("Sales by Product", fontsize=16, fontweight="bold", pad=20, color="#222222")
ax.set_xlabel("Product", fontsize=13, labelpad=10)
ax.set_ylabel("Sales (USD)", fontsize=13, labelpad=10)

ax.set_ylim(0, max(sales) * 1.15)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#cccccc")
ax.spines["bottom"].set_color("#cccccc")
ax.tick_params(colors="#555555", labelsize=11)
ax.yaxis.grid(True, linestyle="--", alpha=0.5, color="#cccccc")
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig("sales_bar_chart.png", dpi=150, bbox_inches="tight")
print("Chart saved to sales_bar_chart.png")
plt.show()
