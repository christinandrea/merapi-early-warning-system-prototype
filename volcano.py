from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random

def evacuation(d1,d2,d3):
    if d1 < d2 or d1 < d3:
        print("Best evacuation is in Sawangan")
    elif d2 < d3 or d2 < d1:
        print("Best evacuation is in Dukun")
    elif d3 < d1 or d3 < d2:
        print("Best evacuation is in Mranggen")


def kondisi():
    print ("Kondisi Gunung Berapi")
    print ("-----------------------")
    print ("Getaran : ", getaran)
    print ("Deformasi Tanah : ", deformasi_tanah)
    print ("Aktivitas Kawah : ", kawah)

    if kawah == "Berkabut":
        print ("Warna Asap : ", warna)
        print ("Ketebalan Asap : ", tebal)
        

def randomise (data, key):
    x = random.choice(data[key])
    return x

def tuple_gen(var1,var2):
    emp1 = []
    emp1.append(float(var2))
    emp1.append(float(var1))
    tup = tuple(emp1)
    return tup

def cek_aktivitas(dist_mount, deformasi_tanah, getaran, kawah, warna, tebal):
        if dist_mount<=10.0:
            kondisi()
            if getaran == "< 1.5 SR":
                if kawah == "Berkabut":
                    if warna == "Terang":
                        if tebal == True:
                            print("Status: Normal")
                        else:
                            print("Status: Normal")
                    else:
                        if tebal == True:   
                            print("Status: Normal")
                        else:
                            print("Status: Normal")
                else:
                    print("Status: Normal")
            elif  getaran == "1.5 SR - 3.5 SR":
                if deformasi_tanah == True:
                    if kawah == "Berkabut":
                        if warna == "Terang":
                            if tebal == True:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                            else:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                        else:
                            if tebal == True:   
                                print("Status: Siaga")
                                print("Silahkan Mencari Tempat Evakuasi Terdekat")
                                evacuation(dist1, dist2, dist3)
                            else:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                    else:
                        print("Status: Normal")
                else:
                    if kawah == "Berkabut":
                        if warna == "Terang":
                            if tebal == True:
                                print("Status: Normal")
                            else:
                                print("Status: Normal")
                        else:
                            if tebal == True:   
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                            else:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                    else:
                        print("Status: Normal")
            elif  getaran == "> 3.5 SR":
                if deformasi_tanah == True:
                    if kawah == "Berkabut":
                        if warna == "Gelap":
                            if tebal == True:
                                print("Status: Siaga")
                                print("Silahkan Mencari Tempat Evakuasi Terdekat")
                                evacuation(dist1, dist2, dist3)
                            elif tebal == False:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                        elif warna == "Terang":
                            if tebal == True:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                            elif tebal == False:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)

                    elif kawah == "Tidak Berkabut":
                        print("Status: Normal")

                elif deformasi_tanah == False:
                    if kawah == "Berkabut":
                        if warna == "Gelap":
                            if tebal == True:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                            elif tebal == False:
                                print("Status: Waspada")
                                print("Disarankan Evakuasi")
                                evacuation(dist1, dist2, dist3)
                        elif warna == "Terang":
                            if tebal == True:
                                print("Status: Normal")
                            elif tebal == False:
                                print("Status: Waspada")
                                evacuation(dist1, dist2, dist3)
                    else:
                        print("Status: Normal")
        else:
            kondisi()
            print("Anda berada diluar jangkauan letusan")

try:
    geolocator = Nominatim(user_agent="GetLoc")
    addr = input("Address : ")
    city = input("City : ")
    country = input("Country : ")
    location = geolocator.geocode(addr+","+city+","+country)
    longUser = float(location.latitude)
    latUser = float(location.longitude)
    mount = "Gunung Merapi,Yogyakarta,Indonesia"
    mount_loc = geolocator.geocode(mount)
    mount_lat = float(mount_loc.latitude)
    mount_long = float(mount_loc.longitude)

    data_location = {"Name":["Sawangan","Dukun","Mranggen"],
    "Longitude":["110.39235831626016","110.37533734339334","110.3400719"],
    "Latitude":["-7.4937679500000005","-7.54226065","-7.5859438"]}

    emp = {}

    for i in range(len(data_location)):
        loc = data_location["Name"][i]
        long = data_location["Longitude"][i]
        lat = data_location["Latitude"][i]
        emp[loc] = tuple_gen(long,lat)

    locUser = tuple_gen(latUser,longUser)
    loc1 = emp['Sawangan']
    loc2 = emp['Dukun']
    loc3 = emp['Mranggen']
    locMountain = tuple_gen(mount_long,mount_lat)
    dist1 = geodesic(locUser,loc1).km
    dist2 = geodesic(locUser,loc2).km
    dist3 = geodesic(locUser,loc3).km
    dist_mount = geodesic(locUser,locMountain).km


    data = {"Category" : ["High","Intermediate","Low"],
    "Deformasi Tanah":[True, False],
    "Getaran":["< 1.5 SR", "1.5 SR - 3.5 SR", "> 3.5 SR"],
    "Aktivitas Kawah":["Berkabut","Tidak Berkabut"], 
    "Warna Asap":["Terang","Gelap"],
    "Ketebalan Asap":[True,False]}


    deformasi_tanah = randomise(data, "Deformasi Tanah")
    getaran = randomise(data, "Getaran")
    kawah = randomise(data, "Aktivitas Kawah")
    warna  = randomise(data, "Warna Asap")
    tebal = randomise(data,"Ketebalan Asap")

    cek_aktivitas(dist_mount,deformasi_tanah, getaran, kawah, warna, tebal)
    
except:
    print("Cek kembali data anda")

#TC1 = High
#TC2 = Intermediate
#TC3 = Low
