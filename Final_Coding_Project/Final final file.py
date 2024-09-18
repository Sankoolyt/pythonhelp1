"""
Created on Fri May 24 12:22:51 2024
@author: EL SANTIIIII
"""
import numpy as np,matplotlib.pyplot as plt,matplotlib.image as pim,numpy.ma as ma,pandas as pd
locations, th, th2=['Figueira da Foz']*5+['Valle Hermoso']*5+['Toulouse France']*5,0.5,.95
years = [1984, 1994, 2004, 2014,2022] * 3
def imach_grey(ogimage):
    return .299 * .299*ogimage[:,:,0]+.587*ogimage[:,:,1]+.114*ogimage[:,:,2]
for x in range(15):
    loc_1,curr_loc,yr, =pim.imread('Figueira ({}).png'.format(x+1)),locations[x],years[x]
    plt.subplot(4, 4, x + 1)
    plt.title("{} in the year: {}".format(curr_loc,yr));masks = ma.masked_greater(loc_1, th)
    #plt.hist(np.ndarray.flatten(loc_1[:,:,0]), color='red',histtype='step',bins=200)
    #plt.hist(np.ndarray.flatten(loc_1[:,:,1]), color='green',histtype='step',bins=200)
    #plt.hist(np.ndarray.flatten(loc_1[:,:,2]), color='blue',histtype='step',bins=200)
    #plt.imshow(imach_grey(loc_1),cmap='Greys_r',vmin=0,vmax=1)
    plt.imshow(masks[:, :, 2], cmap='Greys'); pixel_counter = np.shape(loc_1)
    plt.colorbar()
    xpixels = pixel_counter[0] * pixel_counter[1]
    npixels = np.sum(loc_1[:, :, 0] >= th) - np.sum(loc_1[:, :, 0] >= th2)
    print(yr,' The number of population pixels in ',curr_loc,' is around ',npixels)
dates=['1984-1-1','1994-1-1','2003-1-1','2014-1-1','2022-1-1']
pops0,pop1=[314746,325514,327213,299877,373594,],[420871,279209,765902,1106234,802781]
pops2, datee = [700334, 719187, 700619, 756044, 724199], pd.to_datetime(dates)
plt.figure(); plt.grid(); pops_ind = [pops0,pop1,pops2]
for x in range(3):
    plt.plot(datee,pops_ind[x],label=locations[x*5])
plt.xlabel('years'); plt.ylabel('Gentrification'); plt.legend()

plt.Figure()
plt.plot(datee, pop1, label='Toulouse population', color='crimson')
fig_1 = [570953,701368, 818723, 941676,1049246]
plt.grid()
popo = ['1984-1-1','1994-1-1', '2004-1-1', '2014-1-1', '2022-1-1']
deits = pd.to_datetime(popo)
plt.plot(deits, fig_1,label='Toulouse changing demographic vs census', color = 'lime')
plt.legend()
print(60055/51306)