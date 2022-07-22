print("---")
print("title : \"MQM 2022 Photo Gallery\"")
print("date: 2020-03-14T15:40:24+06:00")
print("description : \"MQM 2022 Photo Gallery\"")
print("draft : false")
print("layout : \"gallery\"")
print("gallery_items:")
print("- name : \"MQM Participants\"")
print(f"  image : \"images/gallery/MQM_GroupPhoto.jpg\"")
print("  categories : [\"Conference Photos\", \"All Participants\"]")
print("- name : \"MQM Volunteers\"")
print(f"  image : \"images/gallery/MQMVolunteers.jpg\"")
print("  categories : [\"Conference Photos\", \"Volunteers\"]")
for i in range(1,66):
  if i==49:
    continue
  print("- name : \"MQM Conference Photos\"")
  print(f"  image : \"images/gallery/MQM_Photo-{i}.jpg\"")
  print("  categories : [\"Conference Photos\"]")


# Mondal pics
piclist = [
"IMG_5459.JPG", "IMG_5472.JPG", "IMG_5473.JPG", "IMG_5486.JPG",
"IMG_5490.JPG", "IMG_5491.JPG", "IMG_5495.JPG", "IMG_5501.JPG", 
"IMG_5505.JPG", "IMG_5509.JPG", "IMG_5521.JPG", "IMG_5522.JPG",
"IMG_5524.JPG", "IMG_5526.JPG", "IMG_5528.JPG"]

for i in piclist:
  print("- name : \"MQM Conference Photos\"")
  print(f"  image : \"images/gallery/{i}\"")
  print("  categories : [\"Conference Photos\", \"Banquet\"]")

print("---")
