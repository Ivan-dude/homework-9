my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
for item in range(len(my_list)):
    if my_list[item] > a:
        print(my_list[item])
    else:
         if my_list[item] < a:
            break
        #print("число не подходит")