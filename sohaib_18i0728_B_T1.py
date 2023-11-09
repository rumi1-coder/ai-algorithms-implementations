Areas=['bedroom',100.2,'hallway',212.5,'bathroom',300.2,'kitchen',120.4,'livingroom',300.7]
print(Areas)
float_areas=Areas.copy()
str_areas=Areas.copy()

for i in float_areas:
  if type(i)==str:
    float_areas.remove(i)
for i in str_areas:
  if type(i)==float:
    str_areas.remove(i)

print(str_areas[:])
print(f'{str_areas[0]},{float_areas[0]}')
