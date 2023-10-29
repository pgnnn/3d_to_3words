# 3d_to_3words
used python and flask to create this
given a lat,long, altitude, then it will generate uniqe 3words with upper or small letters and viceversa also will workd

max height of a floor is 10 to 14 feet means 3m to 4.2m
height of highest residential house is around 3000m. so, (2**10)*3 ~ 3000m, that how we are covering all the altitudes and for every 3m of altitude there will be a unique combination of upper and small characters based on binary number of (alt//3)
