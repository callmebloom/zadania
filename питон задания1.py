list = [1, 2, 3, 4, 5]
print ("сумма элементов списка=", sum(list))

list = [2, 4, 6, 8]
print ("наибольший элемент:", max(list))

list = [3, 5, 7, 5, 7, 9]
print ("только уникальные элементы:", set(list))

lista = [1, 4, 7, 0]
listb = [2, 5, 8, 10]
dvavodnom = lista+listb
print ("два в одном: ", str (dvavodnom))

animals = ("cat", "dog", "bird", "fox")
index = animals.index("bird")
print ("индекс нужного элемента: ", index)

tuplea = (1,3,5,7)
tupleb = (2,4,6,8)
vmeste = tuplea+tupleb
print ("два в одном: ",vmeste)

cars = ("supra", "skyline", "silvia", "miata")
carss = list (cars)
carss.remove("supra")
print ("с удаленным элементом: ",carss)

tuple1 = (1, 3, 6, 3, 8, 3)
print ("кол-во 3: ", tuple1.count(3))









