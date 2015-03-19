# Answer quiz questions related to music and 
# Import stuff from musicbrainz Code

from musicbrainz import *

def num_of_bands_wth_name(bandName):
    '''
    Find how many bands are named bandName from music brainz
    '''
    results = query_by_name(ARTIST_URL, query_type["simple"], bandName)
    bands = results["artists"]
    numOfbands = 0
    for b in bands:
        if b["name"] == bandName:
            numOfbands += 1
            
    return numOfbands

# QUEEN band   
rQueen = query_by_name(ARTIST_URL, query_type["simple"], "Queen")

# Beatles Spanish alias
def get_spanish_alias(bandName):
    rBeatles = query_by_name(ARTIST_URL, query_type["simple"], bandName)
    for alias in rBeatles["artists"][0]["aliases"]:
        if alias["locale"] == "es":
            return alias["name"]


#Nirvana disambiguation
rNirvana = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")

#One direction beginnings
rOneDirection = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")

# Answers:
print "Number of bands with name First Aid Kit: {}".format(num_of_bands_wth_name("First Aid Kit"))
print "Begin area name for Queen: {}".format(rQueen["artists"][0]["begin-area"]["name"])
print "Beatles Spanish alias: {}".format(get_spanish_alias("Beatles"))
print "Nirvana disambiguation: {}".format(rNirvana["artists"][0]["disambiguation"])
print "One Direction Formed: {}".format(rOneDirection["artists"][0]["life-span"]["begin"])