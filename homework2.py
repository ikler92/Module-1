#count_of_homeworks = "12"
#time_for_work = "1.5"
#name_of_course = "Python"
#time_for_one_task = "0/125"
#print("Курс: " + name_of_course + ', ' + "всего задач:" + count_of_homeworks + ', ' + "затрачено часов: " + time_for_work + ', ' + "среднее время выполнения " + time_for_one_task + "часа")

count_of_homeworks = 12
time_for_work = 1.5
name_of_course = "Python"
time_for_one_task = time_for_work / count_of_homeworks
print("Курс: " + str(name_of_course) + "," ,"всего задач:" + str(count_of_homeworks) + ",","затрачено часов: " + str(time_for_work) + ",","среднее время выполнения " + str(time_for_one_task) ,"часа.")