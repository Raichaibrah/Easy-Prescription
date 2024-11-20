from geopy.distance import geodesic
from geopy.geocoders import Nominatim

def fonction_1(ville, pharmacies):
    R=[]
    for pharmacie in pharmacies:
        if pharmacie.ville == ville:
            R.append(pharmacie)
    return R

def fonction_2(user, rayon, pharmacies):
    R = []
    geolocator = Nominatim(user_agent="localisation py")
    location = geolocator.geocode("user.adresse user.ville")
    latitude, longitude = user.adresse
    for pharmacie in pharmacies:
        point1, point2 = (latitude, longitude), (pharmacie.latitude, pharmacie.longitude)
        d = geodesic(point1, point2).kilometers
        if d<rayon:
            R.append((pharmacie, d))
    R.sort(key=lambda x: x[1])
    return R