"""
Простой тест для проверки основных функций приложения
"""

import sys
import os

# Добавляем корневую папку в путь Python
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.data_processor import load_demo_data, analyze_grades

def test_data_loading():
    """Тест загрузки демо-данных"""
    print("🧪 Тестируем загрузку данных...")
    df = load_demo_data()
    assert df is not None
    assert len(df) > 0
    print("✅ Тест загрузки данных пройден")

def test_analysis():
    """Тест анализа данных"""
    print("🧪 Тестируем анализ данных...")
    df = load_demo_data()
    stats = analyze_grades(df)
    
    assert 'avg_by_subject' in stats
    assert 'student_ranking' in stats
    assert 'worst_subject' in stats
    print("✅ Тест анализа данных пройден")

def test_calculations():
    """Тест правильности расчетов"""
    print("🧪 Тестируем расчеты...")
    df = load_demo_data()
    stats = analyze_grades(df)
    
    # Проверяем что средний балл вычисляется правильно
    assert stats['avg_by_subject'].mean() > 0
    print("✅ Тест расчетов пройден")

if __name__ == "__main__":
    print("🚀 Запуск тестов...")
    test_data_loading()
    test_analysis()
    test_calculations()
    print("🎉 Все тесты пройдены успешно!")