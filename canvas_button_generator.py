#eng3
#course = "31069"
#eng4
#course = "31073"
#phys
#course = "30987"
#capstone
course = "31082"

str1 = "<a style=\"background-color: #f97a07; border: 1px solid #0b0e07; font-size: 35px; padding: 9px 23px; text-align: center; margin: 30px 50px; display:block; text-decoration: none; color: #ffffff;\" href="
str2 = " data-api-endpoint=\"https://cvilleschools.instructure.com/api/v1/courses/"
str25 = "/modules\" data-api-returntype=\"[Module]\">"
str26 = " <img src=\"https://cvilleschools.instructure.com/courses/"
str3 = "/files/"
str4 = "/download?wrap=1\" alt=\"assignments\" width=\"55\" height=\"55\" data-api-endpoint=\"https://cvilleschools.instructure.com/api/v1/courses/"
str5 = "\" data-api-returntype=\"File\" /></a>"

#eng 3
#links = ["https://cvilleschools.instructure.com/courses/" + course + "/modules",
#         "https://charlottesvilleschools.zoom.us/j/81013522117",
#         "https://charlottesvilleschools.zoom.us/my/drshields"]
#phys
#links = ["https://cvilleschools.instructure.com/courses/" + course + "/modules",
#         "https://charlottesvilleschools.zoom.us/meeting/81459666176",
#         "https://charlottesvilleschools.zoom.us/my/drshields"]
#capstone
links = ["https://cvilleschools.instructure.com/courses/" + course + "/modules",
         "https://charlottesvilleschools.zoom.us/meeting/88921166863",
         "https://charlottesvilleschools.zoom.us/my/drshields"]
#eng4
#links = ["https://cvilleschools.instructure.com/courses/" + course + "/modules",
#         "https://charlottesvilleschools.zoom.us/meeting/83482605350",
#         "https://charlottesvilleschools.zoom.us/meeting/86184753524",
#         "https://charlottesvilleschools.zoom.us/my/drshields"]

#eng 3, phys, capstone
txt = ["Assignments", "Class Meetings", "Office Hours"]
#eng 4
#txt = ["Assignments", "1st Period Class Meetings", "4th Period Class Meetings", "Office Hours"]

#eng3
#imgs = ["1659567", "1659566", "1659566"]
#eng4
#imgs = ["1663081", "1663094", "1663094", "1663094"]
#phys
#imgs = ["1663096", "1663098", "1663098"]
#capstone
imgs = ["1663101", "1663102", "1663102"]

for i, link in enumerate(links):
    out = str1 + link + str2 + course + str25 + txt[i] + str26 + course + str3 + imgs[i] + str4 + course + str5
    print(out)
