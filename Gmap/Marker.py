import folium
from Locate import *
# Map method of folium return Map object 
Userloc=GetUserGeoLocation()
hosname=[]

# Here we pass coordinates of User  
# and starting Zoom level = 11 
my_map2 = folium.Map(location = Userloc, zoom_start = 30) 
HospitalLoc=GetHospitalLocation()
#we now obtain a list of hospital names and locations  
for valu in HospitalLoc:
    #Splitting the hospital name from location
    hosname.append(valu.pop(0))
# save method of Map object will create a map 
# Creating multiple Parachute Marker with hospitalname popups   
folium.Marker(location = Userloc,popup ="You", icon=folium.Icon(color='red',icon_color='white',icon='cloud')).add_to(my_map2) 

for loc,Hsname in zip(HospitalLoc,hosname):
    folium.Marker(location = loc,popup =Hsname,draggable=True).add_to(my_map2) 
    
    # save as html 

my_map2.save("Hospitals.html")
