import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

# ==========================================
# R1 & R2: Model Definition & Transition Matrix
# ==========================================
STATES = ["Focused", "Distracted", "Burned Out"]
OBSERVATIONS = ["High Score", "Average Score", "Low / Missed"]

P = np.array([
    [0.70, 0.20, 0.10],  # From Focused
    [0.30, 0.50, 0.20],  # From Distracted
    [0.20, 0.35, 0.45]   # From Burned Out
])

# 1. Verify P is a valid stochastic matrix
def verify_transition_matrix(matrix, state_names):
    print("Transition Matrix P:")
    print(matrix)
    print("\nVerification:")
    
    # Check non-negativity and upper bound
    valid_bounds = np.all((matrix >= 0) & (matrix <= 1))
    print(f"- All entries in [0, 1]: {valid_bounds}")
    
    # Check row sums equal 1
    row_sums = matrix.sum(axis=1)
    for name, total in zip(state_names, row_sums):
        print(f"- Row sum for '{name}': {total:.2f}")
    
    all_rows_sum_to_one = np.allclose(row_sums, 1.0)
    print(f"- Every row sums to 1: {all_rows_sum_to_one}")
    assert valid_bounds and all_rows_sum_to_one, "Invalid transition matrix!"

verify_transition_matrix(P, STATES)

# 2. Draw State-Transition Diagram
def draw_transition_diagram(matrix, state_names, filename="state_transition_diagram.png"):
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-1.8, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")

    # Node positions (triangle layout)
    positions = {
        0: (0.0, 1.15),     # Focused (Top)
        1: (-1.35, -0.85),  # Distracted (Bottom-Left)
        2: (1.35, -0.85)    # Burned Out (Bottom-Right)
    }
    colors = ["#4CAF50", "#FF9800", "#E53935"]
    radius = 0.42

    # Draw nodes
    for i, name in enumerate(state_names):
        x, y = positions[i]
        circle = Circle((x, y), radius, facecolor=colors[i], edgecolor="#222222", linewidth=2, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, name, ha="center", va="center", color="white",
                fontsize=11, fontweight="bold", zorder=4)

    # Helper to draw curved edges between distinct nodes
    def draw_edge(i, j, prob, rad=0.18, label_offset=(0, 0)):
        x1, y1 = positions[i]
        x2, y2 = positions[j]
        arrow = FancyArrowPatch(
            (x1, y1), (x2, y2),
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>,head_length=8,head_width=5",
            shrinkA=radius * 72, shrinkB=radius * 72,
            color="#333333", linewidth=1.6, zorder=2
        )
        ax.add_patch(arrow)

        # Midpoint + perpendicular offset for label
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        dist = np.hypot(dx, dy)
        nx, ny = -dy / dist, dx / dist  # normal vector
        lx = mx + nx * (rad * 1.15) + label_offset[0]
        ly = my + ny * (rad * 1.15) + label_offset[1]

        ax.text(lx, ly, f"{prob:.2f}", ha="center", va="center", fontsize=10,
                fontweight="bold", color="#111111",
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#cccccc"))

    # Draw all off-diagonal transitions
    for i in range(len(state_names)):
        for j in range(len(state_names)):
            if i != j and matrix[i, j] > 0:
                draw_edge(i, j, matrix[i, j], rad=0.22)

    # Draw self-loops
    loop_configs = {
        0: ((0.0, 1.85), (-0.18, 1.54), (0.18, 1.54), -1.8),    # Top loop
        1: ((-1.95, -1.30), (-1.70, -0.65), (-1.45, -1.25), 1.8), # Bottom-left loop
        2: ((1.95, -1.30), (1.45, -1.25), (1.70, -0.65), 1.8),    # Bottom-right loop
    }
    for i, (label_pos, start, end, rad) in loop_configs.items():
        if matrix[i, i] > 0:
            loop = FancyArrowPatch(
                start, end,
                connectionstyle=f"arc3,rad={rad}",
                arrowstyle="-|>,head_length=7,head_width=4",
                color="#333333", linewidth=1.6, zorder=2
            )
            ax.add_patch(loop)
            ax.text(label_pos[0], label_pos[1], f"{matrix[i, i]:.2f}",
                    ha="center", va="center", fontsize=10, fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#cccccc"))

    plt.title("Student Academic State-Transition Diagram (Weekly)", fontsize=14, fontweight="bold", pad=10)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
    print(f"\nSaved diagram to {filename}")

draw_transition_diagram(P, STATES)