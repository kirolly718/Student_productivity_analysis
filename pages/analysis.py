"""
Страница детального анализа успеваемости.
Содержит расширенную статистику и визуализацию.
"""

import streamlit as st
import matplotlib.pyplot as plt
from utils.data_processor import analyze_grades

# Заголовок страницы
st.title("Детальный анализ успеваемости")

# Проверяем, есть ли данные в session state (переданные с главной страницы)
if 'df' in st.session_state:
    # Получаем DataFrame из session state
    df = st.session_state.df
    # Анализируем данные с помощью функции из utils
    stats = analyze_grades(df)
    
    # Раздел расширенной статистики
    st.subheader("Расширенная статистика")
    st.write("Распределение оценок по каждому предмету:")
    
    # Список предметов для анализа
    subjects = ['Источниковедение', 'Журналистика', 'Программирование', 'Менеджмент']
    
    # Создаем гистограммы распределения оценок для каждого предмета
    for subject in subjects:
        st.write(f"**{subject}:**")
        # Строим bar chart с количеством каждой оценки
        st.bar_chart(df[subject].value_counts().sort_index())
        
else:
    # Если данных нет, показываем предупреждение
    st.warning("Перейдите на главную страницу и загрузите данные для анализа")