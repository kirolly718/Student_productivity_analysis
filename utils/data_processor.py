"""
Модуль для обработки данных об успеваемости студентов.
Содержит функции для загрузки и анализа данных.
"""

import pandas as pd
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def load_demo_data():
    """
    Загружает демонстрационные данные об успеваемости студентов.
    """
    logger.info("Загрузка демонстрационных данных")
    
    demo_data = {
        'student': ['Алексеев', 'Бобров', 'Поливода', 'Подвойский', 'Гламуров', 'Лапушкин', 'Менделеев'],
        'Источниковедение': [4, 3, 5, 3, 4, 5, 4],
        'Журналистика': [5, 4, 5, 3, 5, 4, 3], 
        'Программирование': [5, 4, 5, 4, 5, 5, 4],
        'Менеджмент': [3, 4, 5, 3, 4, 5, 5]
    }
    
    df = pd.DataFrame(demo_data)
    logger.info(f"Загружено {len(df)} записей")
    return df

def analyze_grades(df):
    """
    Анализирует DataFrame с оценками и вычисляет различные статистики.
    """
    logger.info("Начало анализа данных")
    
    stats = {}
    
    try:
        # Вычисляем средние оценки по каждому предмету
        stats['avg_by_subject'] = df.select_dtypes(include='number').mean()
        logger.info("Вычислены средние оценки по предметам")
        
        # Добавляем колонку с средним баллом для каждого студента
        df['average'] = df.select_dtypes(include='number').mean(axis=1)
        stats['student_ranking'] = df[['student', 'average']].sort_values('average', ascending=False)
        logger.info("Составлен рейтинг студентов")
        
        # Находим самый сложный предмет
        stats['worst_subject'] = stats['avg_by_subject'].idxmin()
        stats['worst_score'] = stats['avg_by_subject'].min()
        logger.info(f"Самый сложный предмет: {stats['worst_subject']}")
        
        # Находим студентов с низкой успеваемостью
        stats['weak_students'] = df[df['average'] < 4.0]['student'].tolist()
        if stats['weak_students']:
            logger.warning(f"Студенты с низкой успеваемостью: {stats['weak_students']}")
        else:
            logger.info("Нет студентов с низкой успеваемостью")
            
    except Exception as e:
        logger.error(f"Ошибка при анализе данных: {e}")
        raise
    
    logger.info("Анализ данных завершен успешно")
    return stats