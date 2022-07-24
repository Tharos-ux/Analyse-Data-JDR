import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# duration = vertical


def plotter_colormap(matrix, legend: str, filename: str, labels_x: list[str], labels_y: list[str], lb_x, lb_y, shift):
    """Plots a matrix as a cmap

    Args:
        matrix (numpy.array): a 2D numpy array
        legend (str): title and save name
        labels_x (list[str]): labels of the x-axis
        labels_y (list[str]): labels of the y-axis
    """
    fig = plt.figure()
    cm = plt.get_cmap('rainbow')
    ax = fig.add_subplot(111)
    cax = ax.matshow(matrix, cmap=cm)
    # plt.title(legend)
    plt.xticks(rotation=90)
    plt.yticks(fontsize=9)
    plt.xticks(fontsize=9)
    plt.xlabel(lb_x)
    plt.ylabel(lb_y)
    ax.yaxis.labelpad = shift
    ax.set_xticks([i for i in range(len(labels_x))])
    ax.set_yticks([i for i in range(len(labels_y))])
    ax.set_xticklabels([labels_x[i] for i in range(len(labels_x))])
    ax.set_yticklabels([labels_y[i] for i in range(len(labels_y))])
    ax.tick_params(axis=u'both', which=u'both', length=0)
    for i in range(len(labels_x)):
        for j in range(len(labels_y)):
            c = matrix[j, i]
            if c > 0:
                ax.text(i, j, str(c), va='center', ha='center')
    cbar = fig.colorbar(cax)
    cbar.ax.set_title(f'$N = {sum(matrix.sum(axis=0))}$')
    plt.savefig(f"{filename}_colormap.png",
                bbox_inches='tight', transparent=True)


filepath = "E:/Ressources_Chroniques/ROLLS_03/dataframe/dm_survey_original_results.csv"


df = pd.read_csv(filepath)

kfreq = 'How often do you run 5th Edition Dungeons and Dragons games?'
kdur = 'How long do your games run?'
kprep = 'How long does it take you to prepare for each gaming session?'

frequency = df[kfreq]
duration = df[kdur]
preparation = df[kprep]

keys_frequency = ['More than twice a week', 'Twice a week',
                  'Once a week', 'Twice a month', 'Once a month', 'Less than monthly']
keys_duration = ['About an hour', 'About two hours', 'About three hours',
                 'About four hours', 'About six hours', 'About eight hours', 'Longer than eight hours']
keys_preparation = ["I don't prepare at all", 'About 15 minutes', 'About 30 minutes',
                    'About an hour', 'About two hours', 'About three hours', 'About four hours', 'More than four hours']

keys_frequency_fr = ['Sup. deux par semaine', 'Deux par semaine',
                     'Une par semaine', 'Deux par mois', 'Une par mois', "Moins d'une par mois"]
keys_duration_fr = ['Une heure', 'Deux heures', 'Trois heures',
                    'Quatre heures', 'Six heures', 'Huit heures', 'Plus de 8 heures']
keys_preparation_fr = ["Sans préparation", 'Quinze minutes', 'Trente minutes',
                       'Une heure', 'Deux heures', 'Trois heures', 'Quatre heures', 'Plus de quatre heures']

frequency_duration = [
    [0 for _ in range(len(keys_frequency))] for _ in range(len(keys_duration))]

for index, row in df.iterrows():
    pos_x, pos_y = keys_frequency.index(
        row[kfreq]), keys_duration.index(row[kdur])
    frequency_duration[pos_y][pos_x] += 1

plotter_colormap(np.asarray(frequency_duration),
                 "Frequency vs Duration", 'freq_dur_fr', keys_frequency_fr, keys_duration_fr, "Fréquence", "Durée", -320)


preparation_duration = [
    [0 for _ in range(len(keys_preparation))] for _ in range(len(keys_duration))]

for index, row in df.iterrows():
    pos_x, pos_y = keys_preparation.index(
        row[kprep]), keys_duration.index(row[kdur])
    preparation_duration[pos_y][pos_x] += 1

plotter_colormap(np.asarray(preparation_duration),
                 "Preparation vs Duration", 'prep_dur_fr', keys_preparation_fr, keys_duration_fr, "Préparation", "Durée", -378)


preparation_frequency = [
    [0 for _ in range(len(keys_preparation))] for _ in range(len(keys_frequency))]

for index, row in df.iterrows():
    pos_x, pos_y = keys_preparation.index(
        row[kprep]), keys_frequency.index(row[kfreq])
    preparation_frequency[pos_y][pos_x] += 1

plotter_colormap(np.asarray(preparation_frequency),
                 "Preparation vs Frequency", 'prep_freq_fr', keys_preparation_fr, keys_frequency_fr, "Préparation", "Fréquence", -408)
