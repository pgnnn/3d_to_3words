# 3d_to_3words**
3D Coordinates to 3-Word Addresses: Revolutionizing Navigation**
used python and flask to create this
given a lat,long, altitude, then it will generate uniqe 3words with upper or small letters and viceversa also will workd

Built a website that simplifies 3D navigation by converting coordinates into just 3 words, eliminating the need for latitude, longitude, and altitude(above sea level) input.
Ideal for delivery agents navigating apartments and future drone delivery systems, this innovative solution enhances precision and user-friendliness for exploring any location in 3D.


max height of a floor is 10 to 14 feet means 3m to 4.2m
height of highest residential house is around 3000m. so, (2**10)*3 ~ 3000m, that how we are covering all the altitudes and for every 3m of altitude there will be a unique combination of upper and small characters based on binary number of (alt//3)
