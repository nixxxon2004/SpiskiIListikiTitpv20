
import random
import time

def min_max():
        for i in range (len(vozrast)):
            if vozrast[i] == min(vozrast):
                print(min(vozrast)," ",imena[i])
        for i in range (len(vozrast)):
            if imena[i] == max(vozrast):
                print(max(vozrast), " ", imena[i])
def top():
    best_value = 0
    imena_max = []
    top_names = []
    top_score = []
    dyadki_copy = imena.copy()
    vozrast_copy = vozrast.copy()
    for x in vozrast:
    	if x > best_value: 
    		best_value = x
    top_score.append(best_value)
    for x in vozrast:
           if x == best_value:
               index = vozrast.index(x)
               imena_max.append(dyadki_copy[index])
               top_names.append(dyadki_copy[index])
               break
    while best_value > 0:
    	try:
    		best_value -= 1
    		index = vozrast_copy.index(best_value)
    		top_names.append(dyadki_copy[index])
    		top_score.append(vozrast_copy[index])
    		vozrast_copy.pop(index)
    		dyadki_copy.pop(index)
    		if(best_value <= 0):
    			break
    	except:
    		if(best_value <= 0):
    			break
    		continue
    return top_names, top_score
def sred():
        print("Средний возраст старых пенсионеров",(sum(vozrast)/len(vozrast)))
imena = ["Тамара","Валентин","Олег","Валера","Наталья","Михаил","Степан","Кирилл","Александр","Мария","Кристина","Анна","Валерия","Людмила","Алексей","Иван"]
random.shuffle(imena)
vozrast=list(range(60,100,random.randint(10,15) ))
while True:
		print("1 -  Составить список пенсионеров и вывести его на экран \n2 - Найти средний возраст работников; "
              "\n3 -  Отобразить список 10 самых молодых работников фирмы;\n4 -Осуществить поиск работников по году рождения и выведи список на экран ; "
              "\n5 - Добавить имена в список")
		a = input()
		if a == "1":
				print(imena)
		elif a == "2":
				sred()
		elif a == "3":
					print(top())
	
