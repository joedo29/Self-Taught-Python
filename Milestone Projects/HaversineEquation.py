# Author: Joe Do
# March 26, 2018
# Haversine equation to calculate distance between two cities

from pygeocoder import Geocoder
import numpy as np
import sys

# Calculate distance between two points
def get_distance(locationA, locationB):
    # Haversine formula:
    # a        = sin²(Δφ/2) + cos φ1 * cos φ2 * sin²(Δλ/2)
    # c        = 2 * atan2( √a, √(1−a) )
    # distance = R * c

    earth_radius = 6371.0 # https://en.wikipedia.org/wiki/Earth_radius
    latitude     = np.deg2rad(locationB[0] - locationA[0])
    longtitude   = np.deg2rad(locationB[1] - locationA[1])
    a            = np.sin(latitude/2)**2 + \
                   np.cos(np.deg2rad(locationA[0])) * np.cos(np.deg2rad(locationB[0])) * \
                   np.sin(longtitude/2)**2
    c            = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return earth_radius * c

# Return latitude and longtitude of a location
def get_lat_long(city):
    return Geocoder.geocode(city)[0].coordinates

# Wrapper function
def main():
    #get first city
    cityA = str.lower(input('Enter the first city: '))
    #get second city
    cityB = str.lower(input('Enter the second city: '))
    #get units
    units = ''
    while (units != 'km') & (units != 'm'):
        print('Type distance units (miles or kilometers): ')
        units = str.lower(input())
        if units in ['KM', 'Km', 'km', 'Kilometer', 'Kilometers', 'kilometers', 'kilometer']:
            units = 'km'
        elif units in ['m', 'Mile', 'Miles', 'mile', 'miles']:
            units = 'm'
        else:
            print('Incorrect unit, please try again!')

    #find the distance in km
    try:
        distance = get_distance(get_lat_long(cityA), get_lat_long(cityB))
        #display the distance
        if units == 'km':
            print (str(distance),' km')
        else:
            print (str(distance * 0.621371192), ' miles')
    except:
        print('Sorry we couldn''t locate these cities. Please double check your cities input!')

if __name__ == '__main__':
    main()
