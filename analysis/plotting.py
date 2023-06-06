import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import os

# Read in warm-edge timeseries data
timeseries = pd.read_csv("WE_6x6_timeseries.tsv", sep="\t")

# Read in short-long-term data
shortlong = pd.read_csv("WE_6x6_shortlongterm.tsv", sep="\t")

# plotting parameters
plt.rcParams["axes.labelsize"] = 15

# plot zmar across time
sns.lineplot(data=timeseries, x='Time passed (in Generations)', y='zmar', markers=True, hue='% habitat loss', palette='Reds')
sns.scatterplot(data=timeseries, x='Time passed (in Generations)', y='zmar',  hue='% habitat loss', markers=True, palette='Reds', legend=False, s=100)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(rotation=45)
plt.savefig("WE_6x6_timeseries_Zmar.pdf", format='pdf', transparent=True)

# plot % pi
sns.lineplot(data=long_short_habitat_frag, x='% habitat loss', y='% pi', style="feature", markers=True, hue='feature', palette='Reds')
sns.scatterplot(data=long_short_habitat_frag, x='% habitat loss', y='% pi', hue='feature', markers=True, palette='Reds', legend=False, s=100)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig("WE_shortlongterm_pi.pdf", format='pdf', transparent=True)

# plot number of segregating sites
sns.lineplot(data=long_short_habitat_frag, x='% habitat loss', y='% num_segregating', style="feature", markers=True, hue='feature', palette='Reds')
sns.scatterplot(data=long_short_habitat_frag, x='% habitat loss', y='% num_segregating', hue='feature', markers=True, palette='Reds', legend=False, s=100)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig("WE_shortlongterm_segsites.pdf", format='pdf', transparent=True)
