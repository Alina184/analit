#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')
df.info()





print(df['lunch'].value_counts())
print('Мы проверяем гипотезу что если человек принимает еду в школе его результаты выше?')
result_math_standart = df[df['lunch']=='standard']['math score'].mean()
result_math_free = df[df['lunch']=='free/reduced']['math score'].mean()
result_reading_standart = df[df['lunch']=='standard']['reading score'].mean()
result_reading_free = df[df['lunch']=='free/reduced']['reading score'].mean()
result_writing_standart = df[df['lunch']=='standard']['writing score'].mean()
result_writing_free = df[df['lunch']=='free/reduced']['writing score'].mean()

print('Результат с едой по математике', round(result_math_standart, 2))
print('Результат с едой по чтению', round(result_reading_standart, 2))
print('Результат с едой по письму', round(result_writing_standart, 2))

print('Результат без еды по математике', round(result_math_free, 2))
print('Результат без еды по чтению', round(result_reading_free, 2))
print('Результат без еды по письму', round(result_writing_free, 2))

print('Данная гипотеза подтверждена с едой результаты выше')




print("С помощью круговой диаграммы мы хотим проверить гипотезу о том что большинство людей питается перед экзаменом")
s = df['lunch'].value_counts()
s.plot(kind = 'pie')
plt.show()
print("Мы подтвердили данную гипотезу, так как на круговой диаграмме мы можем наблюдать что больше 50% ребят питается перед экзаменом")

#print('С помощью этой диаграммы мы хотимпроверить гипотезу, которая гласит о том, что если перед экзаменом покушать то и результаты будут выше нежели мы не покушаем')
#s = pd.Series(data=[result_math_standart, result_reading_standart, result_writing_standart, result_math_free, result_reading_free, result_writing_free,],
#index = ['Результат с едой по математике', 'Результат с едой по чтению', 'Результат с едой по письму', 'Результат без еды по математике', 'Результат без еды по чтению','Результат без еды по письму'])
#s.plot(kind = "barh")
#plt.show()
#print("Наша гипотеза была подтверждена, у ребят, которые покушали результаты намного выше и лучше чем у других")

#s = pd.Series(data=[result_math_standart, result_reading_standart, result_writing_standart, result_math_free, result_reading_free, result_writing_free,],
#index = ['Результат с едой по математике', 'Результат с едой по чтению', 'Результат с едой по письму', 'Результат без еды по математике', 'Результат без еды по чтению','Результат без еды по письму'])
#s.plot(kind = "bar")
#plt.show()

print("С помощью диаграммы рассеяния мы хотим проверить гипотизу, котора гласит о том,что ребята сдавшие экзамены по математике хорошо смогут так же хорошо сдать экзамены по письму ")
df.plot(x = 'math score', y = 'writing score',kind = 'scatter')
plt.show()
print('Мы подтвердили данную гипотезу, на диаграмме мы можем увидеть чем выше результаты по математике,тем выше результаты по письму')
