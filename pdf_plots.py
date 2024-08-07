import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# Load the tips dataset from Seaborn
tips = sns.load_dataset('tips')

# Create a PDF file to save the plots
with PdfPages('visualization_tutorial.pdf') as pdf:
    # Line Plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=tips, x='total_bill', y='tip', hue='sex')
    plt.title('Line Plot')
    pdf.savefig()  # Save the current figure
    plt.close()

    # Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', style='sex')
    plt.title('Scatter Plot')
    pdf.savefig()
    plt.close()

    # Bar Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
    plt.title('Bar Plot')
    pdf.savefig()
    plt.close()

    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data=tips, x='total_bill', kde=True, hue='sex')
    plt.title('Histogram')
    pdf.savefig()
    plt.close()

    # Box Plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
    plt.title('Box Plot')
    pdf.savefig()
    plt.close()

    # Violin Plot
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)
    plt.title('Violin Plot')
    pdf.savefig()
    plt.close()

    # Heatmap
    pivot_table = tips.pivot_table(index='day', columns='time', values='total_bill', aggfunc=np.mean)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, cmap='coolwarm', cbar_kws={'label': 'Average Total Bill'})
    plt.title('Heatmap')
    pdf.savefig()
    plt.close()

    # Pair Plot
    pair_plot = sns.pairplot(tips, hue='sex')
    pair_plot.fig.suptitle('Pair Plot', y=1.02)
    pdf.savefig(pair_plot.fig)
    plt.close()

    # Joint Plot
    joint_plot = sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex', hue='sex')
    joint_plot.fig.suptitle('Joint Plot', y=1.02)
    pdf.savefig(joint_plot.fig)
    plt.close()

    # Clustermap
    plt.figure(figsize=(10, 8))
    clustermap = sns.clustermap(pivot_table, annot=True, cmap='coolwarm', figsize=(10, 8), cbar_kws={'label': 'Average Total Bill'})
    plt.title('Clustermap')
    pdf.savefig(clustermap.fig)
    plt.close()

print("PDF tutorial created successfully!")
