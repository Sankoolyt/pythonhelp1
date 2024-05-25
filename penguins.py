##Created on Sun May 19 16:29:42 2024
##@author: EL SANTI CARA FACHERA FACHERITA
import pandas as pd, numpy as np, matplotlib.pyplot as plt, scipy.stats as sps
data = pd.read_csv('penguins.csv')  # beginning of highly efficient code
uniq_spec, uniq_loc=np.unique(data['species']), np.unique(data['island'])
iterate, data_clean = ['species','island','sex'], data.dropna()
## i could iterate by columns but that'd be harder to do, besides I know what I'm looking for
cols_specie=['skyblue','hotpink','crimson','indigo','orange','gold','black',
             'cornflowerblue','peru','lime','skyblue']
plt.figure()  ## pie figures
remaining_colors = cols_specie.copy()  # some kind stranger on stack overflow did this
for x in range(3):
    count_every = data_clean[iterate[x]].value_counts()  # the printable variable
    unique_values = count_every.index.tolist() # some kind stranger on stack overflow did this
    plt.subplot(3,2,x+1)
    color_slice = [remaining_colors.pop(0) for _ in unique_values] #this too
    male, species = x, x 
    plt.pie(count_every,labels=count_every.index,
            colors=color_slice,autopct='%.3f%%',shadow=True,radius=1.25,
            textprops={'size':'larger','color':'teal'})
    plt.title('membership by {}'.format(iterate[x]), y=1.08)
    print('there count of penguins by {} is:\n'.format(iterate[x]), count_every)
plt.subplot(3,2,4) ## end of highly efficient code cause i've been working on this for 3 hours
bill_test = np.linspace(np.min(data_clean['bill_length_mm']),
                        np.max(data_clean['bill_length_mm']),10)
slope1, intercept1, r1, _, _ = sps.linregress(data_clean['bill_length_mm'],
                                           data_clean['bill_depth_mm'])
bill_pred = slope1 * bill_test + intercept1
for j in range(2):
    subset = data_clean['sex'] == unique_values[j]
    plt.scatter(data_clean['bill_length_mm'][subset],  data_clean['bill_depth_mm'][subset],
                c = cols_specie[j], alpha=.6, label = unique_values[j],)
    plt.legend()
plt.plot(bill_test,bill_pred,color='cornflowerblue',linewidth=3,label='reg line')
plt.title('Genders compared to the bill length and bill depth with a regression line')

slope, intercept, r, _, _ = sps.linregress(data_clean['body_mass_g'],
                                           data_clean['flipper_length_mm'])

mass_test = np.linspace(np.min(data_clean['body_mass_g']),
                        np.max(data_clean['body_mass_g']),10)

flip_pred = slope * mass_test + intercept
index_Adelie, index_Chinstrap = data_clean['species']=='Adelie', data_clean['species']=='Chinstrap'
index_Gentoo = data_clean['species']=='Gentoo'
index_gender = data_clean['sex'] == 'male'
indexes = (index_Adelie, index_Chinstrap, index_Gentoo)
plt.subplot(3,2,5)
for x in range(3):
    plt.scatter(data_clean['body_mass_g'][indexes[x]],
                data_clean['flipper_length_mm'][indexes[x]],
                c=cols_specie[x],s=100,marker='3',label=uniq_spec[x])
plt.plot(mass_test,flip_pred,color='salmon',linewidth=3,label='reg line')
plt.xlabel('body mass in g')
plt.ylabel('flipper length in mm')
plt.legend()
plt.title('body mass vs flipper length prediction for every species')
'''
We create a copy of the cols_specie list using remaining_colors = cols_specie.copy().
Inside the loop, we get the unique values from count_every using
 unique_values = count_every.index.tolist().
We then assign colors to each unique value by popping colors from the
 remaining_colors list: colors = [remaining_colors.pop(0) for _ in unique_values].
We use the colors list when creating the pie chart: plt.pie(count_every,
labels=count_every.index, colors=colors, ...).
'''