#!/usr/bin/env python
__author__ = 'aub3'


# code taken from
import math
def get_distance(lat1, long1, lat2, long2):
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians

    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) =
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth
    # in your favorite set of units to get length.
    # MODIFIED TO return distance in miles
    return arc*3960.0

if __name__ == '__main__':
    from pprint import pprint
    distances = []
    error_count  = 0
    for line in file('example_data.csv'):
        line = line.strip().split(',')
        plong,plat,dlong,dlat=line[-4:]
        plong = float(plong)
        plat = float(plat)
        dlong = float(dlong)
        dlat = float(dlat)
        try:
            distances.append(get_distance(plat,plong,dlat,dlong))
        except:
            error_count += 1
            print plong,plat,dlong,dlat
            print error_count
    print error_count
    distances.sort(reverse=True)
    print "number of distances","maximum distance","minimum distance"
    print len(distances),max(distances),min(distances) # distance is measured in miles
    "Top 50 distances, obvious outliers"
    pprint(distances[:50])

