Areas=['bed',112.0,'hall',113.5,'bath',189.5,'kit',789.0,'liv',230.0,['pool',117.9,112.7],['grg',112.0]]
print(Areas)
pool_area=['pool',117.9,112.7]
garage_area=['grg',112.0]
list3=[]
#list3.append(pool_area)
#list3.append(garage_area)
#print(list3[:])
for item in Areas:
    if type(item)==str or type(item)==float:
        list3.append(item)
    else:
        for subitem in item:
          list3.append(subitem)

#list3.extend(pool_area)
#list3.extend(garage_area)
print(list3[:])
list6=[]
list5=[1,[2],[[3],[4],5],6]
for value in list5:
    if type(value)==int:
        list6.append(value)
    else:
        for valuesub in value:
            if type(valuesub) == int:
                list6.append(valuesub)
            else:
                for valuesubsub in valuesub:
                     list6.append(valuesubsub)

print(list6[:])

list7=[[[1,2,3],[4,5]],6]
list8=[]
for value in list7:
    if type(value)==int:
        list8.append(value)
    else:
        for valuesub in value:
            if type(valuesub) == int:
                list8.append(valuesub)
            else:
                for valuesubsub in valuesub:
                     list8.append(valuesubsub)
print(list8[:])


