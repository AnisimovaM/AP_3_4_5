import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/dataset.csv')

df.columns = ["Date", "Celsius temperature", "Pressure", "Direction", "Speed"]

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

df = df.dropna().reset_index(drop=True)

df['Fahrenheit temperature'] = 9/5 * df['Celsius temperature'] + 32


def describe_column(df: pd.DataFrame, parametr: str) -> pd.Series | None:
    """
    Получение статистической информации
    Args:
      df: Dataframe с исходными значениями
      parametr: имя столбца фрейма данных, для которого находится статистическое описание
    Returns:
      Ряд, содержащий статистическое описание
    """
    if parametr in df.columns:
        return df[parametr].describe()
    else:
        return None


def filter_celsius_temp(df: pd.DataFrame, celsius_temp: int) -> pd.DataFrame:
    """
    Фильтрация по столбцу температура в градусах Цельсия
    Args:
      df: Dataframe с исходными значениями
      celsius_temp: температура в градусах Цельсия
    Returns:
      Dataframe с днями, в течение которых температура не ниже заданной
    """
    return df[df["Celsius temperature"] >= celsius_temp]


def filter_by_date(df: pd.DataFrame, end_date: str, start_date: str) -> pd.DataFrame:
    """
    Фильтрация по дате
    Args:
      df: Dataframe с исходными значениями
      start_date: Дата начала
      end_date: Дата окончания
    Returns:
      Dataframe с днями в диапазоне [start_date; end_date]
    """
    start_date = pd.to_datetime(start_date, format='%Y-%m-%d')
    end_date = pd.to_datetime(end_date, format='%Y-%m-%d')
    return df[(start_date <= df["Date"]) & (df["Date"] <= end_date)]


def average_monthly_temperature(df: pd.DataFrame, parametr: str) -> pd.Series | None:
    """
    Группировка по месяцам с вычислением среднего значения температуры
    Args:
      df: Dataframe с исходными значениями
      parametr: Столбец, указывающий, какая температура берется
    Returns:
      Ряд, показывающий среднее значение за все месяцы

    """
    if parametr in ["Celsius temperature", 'Fahrenheit temperature']:
        return df.groupby(df.Date.dt.month)[parametr].mean()






