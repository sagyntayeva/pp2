import pandas as pd
import numpy as np

# Фиксируем случайное зерно для воспроизводимости результатов
np.random.seed(42)

# Формируем данные о путешественниках
data = {
    "Traveler_ID": range(1, 21),
    "Destination": np.random.choice(
        ["Paris", "Tokyo", "Rome", "Istanbul", "New York", "Dubai"],
        size=20
    ),
    "Days_Spent": np.random.randint(2, 14, size=20),
    "Total_Cost": np.random.randint(500, 5000, size=20),
    "Age": np.random.randint(18, 60, size=20),
    "Travel_Type": np.random.choice(
        ["Solo", "Family", "Friends", "Couple"],
        size=20
    ),
    "Transport_Mode": np.random.choice(
        ["Plane", "Train", "Car", "Bus"],
        size=20
    ),
    "Satisfaction_Rating": np.random.randint(1, 6, size=20)  # шкала 1–5
}

# Создаём DataFrame
df = pd.DataFrame(data)

# Выводим первые строки таблицы
print(df.head())
