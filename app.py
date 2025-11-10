"""
Главная страница приложения для анализа успеваемости студентов.
Точка входа в Streamlit приложение.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.data_processor import load_demo_data, analyze_grades  # ← ЭТО НОВЫЙ ИМПОРТ!

# Настройка страницы Streamlit
st.set_page_config(
    page_title="Анализ успеваемости", 
    page_icon="🎓", 
    layout="wide"  # Широкий layout для лучшего отображения
)

# Демо-данные
demo_data = {
    'student': ['Иванов', 'Петров', 'Сидорова', 'Козлов', 'Смирнова'],
    'math': [4, 3, 5, 3, 4],
    'physics': [5, 4, 5, 3, 5], 
    'programming': [5, 4, 5, 4, 5],
    'history': [3, 4, 5, 3, 4]
}

# Загрузка файла
uploaded_file = st.file_uploader("Загрузи CSV файл с оценками", type=['csv'])

if uploaded_file is not None:
    # Читаем загруженный файл
    df = pd.read_csv(uploaded_file)
    st.success("Файл успешно загружен!")
else:
    # Используем демо-данные
    df = pd.DataFrame(demo_data)
    st.info("Используются демо-данные")

# Показываем данные
st.subheader("Данные студентов")
st.dataframe(df, use_container_width=True)

# Статистика
st.subheader("Статистика успеваемости")

# Средние оценки
st.write("Средние оценки по предметам:")
avg_grades = df.select_dtypes(include='number').mean()
st.write(avg_grades)

# Лучшие студенты
st.write("Рейтинг студентов по среднему баллу:")
df['average'] = df.select_dtypes(include='number').mean(axis=1)
top_students = df[['student', 'average']].sort_values('average', ascending=False)
st.dataframe(top_students, use_container_width=True)

# Анализ проблем
st.subheader("Анализ проблемных зон")

# Находим предмет с самой низкой средней оценкой
worst_subject = avg_grades.idxmin()
worst_score = avg_grades.min()

# Находим студентов с самыми низкими оценками
weak_students = df[df['average'] < 4.0]['student'].tolist()

st.write(f"Самый сложный предмет: {worst_subject} (средний балл: {worst_score:.2f})")
if weak_students:
    st.write(f"Студенты, нуждающиеся в помощи: {', '.join(weak_students)}")
else:
    st.write("Все студенты успевают хорошо")

# Визуализация
st.subheader("Визуализация данных")

# График средних оценок по предметам
fig1, ax1 = plt.subplots(figsize=(10, 6))
colors = ['#ff6b6b' if x == worst_score else '#4ecdc4' for x in avg_grades]
avg_grades.plot(kind='bar', ax=ax1, color=colors)
ax1.set_title('Средние оценки по предметам\n(красным выделен самый сложный предмет)')
ax1.set_ylabel('Средний балл')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

# График успеваемости студентов
fig2, ax2 = plt.subplots(figsize=(12, 6))
df.set_index('student')[['math', 'physics', 'programming', 'history']].plot(
    kind='bar', ax=ax2, width=0.8
)
ax2.set_title('Успеваемость студентов по предметам')
ax2.set_ylabel('Оценка')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig2)

# Заключение
st.markdown("---")
st.subheader("Решенные проблемы:")
st.write("""
Автоматизация - больше не нужно считать вручную  
Визуализация - данные понятны с первого взгляда  
Выявление проблем - сразу видно, где нужна помощь  
Экономия времени - анализ за секунды вместо часов
""")