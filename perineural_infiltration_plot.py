
import matplotlib.pyplot as plt

# Data preparation
perineural_success_proportion = [436 / (436 + 131), 131 / (436 + 131)]
perineural_failure_proportion = [27 / (27 + 16), 16 / (27 + 16)]

# Creating a figure for whisker plot
fig, ax = plt.subplots()

# Creating a box plot-like structure using whiskers for the proportion of No and Yes
box_perineural = plt.boxplot([perineural_success_proportion, perineural_failure_proportion], 
                             patch_artist=True, positions=[1, 2], widths=0.6,
                             medianprops=dict(color="black"))

# Customizing colors to darker pastel brown for success and lighter pastel orange for failure
colors_perineural = ['#8b4513', '#ffa07a']
for patch, color in zip(box_perineural['boxes'], colors_perineural):
    patch.set_facecolor(color)

# Customizing the plot
ax.set_xticklabels(['Biochemical failure-free', 'Biochemical failure'], fontsize=12)
ax.set_ylabel('Proportion', fontsize=14)
ax.set_ylim(0, 1)

# Removing title and grid lines
ax.set_title('')
ax.grid(False)

# Customizing aesthetics
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adding statistical significance for Perineural Infiltration
p_value_perineural = 0.043
x_coords_perineural = [1, 2]
y_max_perineural = 0.9
ax.plot(x_coords_perineural, [y_max_perineural, y_max_perineural], color="black", lw=1.5)
ax.text(sum(x_coords_perineural) / 2, y_max_perineural + 0.05, f'p = {p_value_perineural}', ha='center', va='bottom', fontsize=12)

plt.show()
