import matplotlib.pyplot as plt

labels = ['Black', 'Coloured', 'Indian', 'Mixed', 'Portuguese', 'Unknown', 'White']
sizes = [169, 1, 12, 5, 2, 3, 398]
colors_final = ['#a1c9f4', '#ffb482', '#8de5a1', '#ff9f9b', '#017374', '#debb9b', '#006400']

fig, ax = plt.subplots()
wedges, _ = ax.pie(sizes, startangle=90, colors=colors_final, wedgeprops=dict(linewidth=1.5, edgecolor='black'))
ax.axis('equal')

plt.legend(wedges, labels, title="Categories", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1), fontsize=12, title_fontsize=14)

plt.show()
