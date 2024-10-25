
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('/path/to/your/file.xlsx')
data.columns = data.columns.str.strip()
summary = data.groupby(['Age', 'risk group']).size().unstack(fill_value=0)
new_colors = ['#E69F00', '#56B4E9', '#F0E442']

fig, ax = plt.subplots(figsize=(18, 10))
summary.plot(kind='bar', stacked=True, color=new_colors, ax=ax, edgecolor='black', linewidth=1)
ax.set_xlabel('Age', fontsize=28, color='black')
ax.set_ylabel('Count', fontsize=28, color='black')
ax.tick_params(axis='x', labelsize=20, colors='black')
ax.tick_params(axis='y', labelsize=20, colors='black')
ax.set_xticklabels(summary.index.astype(int), rotation=90, color='black')

legend = ax.legend(title='Risk Group', fontsize=18, edgecolor='black', title_fontsize='20', facecolor='white')
for text in legend.get_texts():
    text.set_color('black')

ax.grid(False)
plt.show()
