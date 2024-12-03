import pandas as pd
import json

# Основной словарь тикеров акций
main_tickers_dict = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Alphabet Inc.',
    'AMZN': 'Amazon.com Inc.',
    'TSLA': 'Tesla Inc.',
    'FB': 'Meta Platforms Inc.',
    'NFLX': 'Netflix Inc.',
    'BRK.B': 'Berkshire Hathaway Inc.',
    'JNJ': 'Johnson & Johnson',
    'V': 'Visa Inc.'
}

# Дополнительный словарь тикеров акций
additional_tickers = {
    'NVDA': 'NVIDIA Corporation',
    'JPM': 'JPMorgan Chase & Co.',
    'WMT': 'Walmart Inc.',
    'DIS': 'The Walt Disney Company',
    'PG': 'Procter & Gamble Company'
}

# Объединение обоих словарей
combined_tickers = {**main_tickers_dict, **additional_tickers}

# Создание DataFrame для объединенного словаря
tickers_df = pd.DataFrame(list(combined_tickers.items()), columns=['Ticker', 'Company Name'])

# Сохранение объединенного словаря в CSV файл
combined_csv_file_path = 'combined_tickers_dictionary.csv'
tickers_df.to_csv(combined_csv_file_path, index=False)

# Сохранение объединенного словаря в JSON файл
combined_json_file_path = 'combined_additional_tickers.json'
with open(combined_json_file_path, 'w') as json_file:
    json.dump(combined_tickers, json_file, indent=4)

print(f"Объединенный словарь сохранен в: {combined_csv_file_path}")
print(f"Объединенный словарь в формате JSON сохранен в: {combined_json_file_path}")
