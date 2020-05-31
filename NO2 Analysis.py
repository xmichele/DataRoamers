#!/usr/bin/env python
# coding: utf-8

#Majority of the code referred from : http://www.acgeospatial.co.uk/sentinel-5p-and-python/

from netCDF4 import Dataset
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
from mpl_toolkits.basemap import Basemap

def plotsentineldata(sp5_nc_file):
            #Read NO2 data from input Sentinel 5 datafile
            fh = Dataset(sp5_nc_file, mode='r')
            print (fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'])

            lons = fh.groups['PRODUCT'].variables['longitude'][:][0,:,:]
            lats = fh.groups['PRODUCT'].variables['latitude'][:][0,:,:]
            no2 = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'][0,:,:]
            print (lons.shape)
            print (lats.shape)
            print (no2.shape)

            no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'].units

            lon_0 = lons.mean()
            lat_0 = lats.mean()

            m = Basemap(width=5000000,height=3500000,
                        resolution='l',projection='stere',\
                        lat_ts=40,lat_0=lat_0,lon_0=lon_0,llcrnrlon=-6.318324,llcrnrlat=50.400431,urcrnrlon=2.196464,urcrnrlat=53.510295)

            xi, yi = m(lons, lats)

            #Plot region of interest (zoom)
            #llcrnrlon=-1.3444499,llcrnrlat=50.992881,urcrnrlon=0.950932,urcrnrlat=52.133844
            #50.400431, -6.318324, 53.510295, 2.196464

            # Plot Data
            cs = m.pcolor(xi,yi,np.squeeze(no2),norm=LogNorm(), cmap='jet')

            # Add Grid Lines
            m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
            m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

            # Add Coastlines, States, and Country Boundaries
            m.drawcoastlines()
            m.drawstates()
            m.drawcountries()

            # Add Colorbar
            cbar = m.colorbar(cs, location='bottom', pad="10%")
            cbar.set_label(no2_units)

            # Add Title
            plt.title('NO2 in atmosphere')
            plt.show()
            return
