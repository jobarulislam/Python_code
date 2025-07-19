from math import radians, sin, cos, sqrt, atan2
print (f"Hello Friends !!")
dhaka = (23.8041, 90.4152)
khulna = (22.8373, 89.5400)
baltimore = (39.2905, 76.6104)
melbourne = (37.8136, 144.9631)
print (f"Niloy's location : {khulna}")
print (f"Nabil's location : {baltimore}")
print (f"Soshe's location : {melbourne}")

def haversine(co1 , co2):
  R = 6371
  lat1 , lon1 = map (radians, co1)
  lat2 , lon2 = map (radians, co2)

  dlat = lat2 - lat1
  dlon = lon2 - lon1

  a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

  c = 2 * atan2(sqrt(a), sqrt(1 - a))

  return R * c

distence1 = haversine(dhaka , khulna)
distence2 = haversine(dhaka , baltimore)
distence3 = haversine(dhaka , melbourne)

if distence1 > distence2 and distence1 > distence3:
  print (f"Niloy is the furthest away")

elif distence2 > distence1 and distence2 > distence2:
  print (f"Nabil is the furthest away")

else:
  print (f"Soshe is the furthest away")
