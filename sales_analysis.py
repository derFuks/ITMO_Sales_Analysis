# Импорт библиотек
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Настройка визуализации
plt.style.use('ggplot')
# %matplotlib inline

# Загрузка данных
sales_df = pd.read_csv('sales_data.csv')

print(" ✅ Данные успешно загружены!")
print(sales_df.head())

#Анализ данных
print("\nИнформация о данных:")
print(sales_df.info())

print("\nОписание числовых столбцов:")
print(sales_df.describe())

print("\n📍 Пропущенные значения по столбцам")
print(sales_df.isnull().sum())

# Создаю столбец 'Revenue' = Quantity * Price
sales_df['Revenue'] = sales_df['Quantity'] * sales_df['Price']

# Преобразую колонку 'Date' в datetime формат и получаю месяц и день недели
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
sales_df['Month'] = sales_df['Date'].dt.month
sales_df['Weekday'] = sales_df['Date'].dt.weekday
print("\n✅ Подготовка данных завершена.")
print(sales_df.head())

#Группирую продажи по категориям и суммируем выручку по ним
category_revenue = sales_df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print("\n💰 Выручка по категориям товаров:")
print(category_revenue)
# Пайчарт по категориям
plt.figure(figsize=(8,8))
plt.pie(category_revenue, labels=category_revenue.index, autopct='%1.1f%%', startangle=140)
plt.title('Доля выручки по категориям товаров')
plt.axis('equal')  # чтобы круг получился кругом
startangle=140
plt.show()


# Группирую продажи по месяцам и суммируем выручку
month_revenue = sales_df.groupby('Month')['Revenue'].sum().sort_values(ascending=True)
print("\n💰 Выручка по месяцам:")
print(month_revenue)
# Визуализация выручки по месяцам
plt.figure(figsize=(10,6))
sns.lineplot(x=month_revenue.index, y=month_revenue.values, marker='o')
plt.title('Выручка по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Выручка')
plt.xticks(range(1,13))
plt.grid(True)
plt.show()

# Топ продуктов
top_products = sales_df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\n🏆 Топ-5 товаров:")
print(top_products)

# Выводы

print("\n📋 Финальные выводы:")

print("1. Категория с наибольшей выручкой —", category_revenue.idxmax(), 
      "с выручкой в размере", f"{category_revenue.max():,.2f} тугриков.")

print("2. Самый продаваемый товар —", top_products.idxmax(), 
      "с количеством продаж:", top_products.max())

print("3. Наибольшая выручка наблюдалась в", month_revenue.idxmax(), "месяце.")

print("\nФинито!")