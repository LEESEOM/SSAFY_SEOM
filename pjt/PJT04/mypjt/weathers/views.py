from django.shortcuts import render
from io import BytesIO
import  matplotlib.pyplot as plt
import base64
import pandas as pd

csv_path = 'weathers/data/austin_weather.csv'

def problem1(request):
    data_frame = pd.read_csv(csv_path)
    context = {
        'data_frame' : data_frame
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)

    df['Date'] = pd.to_datetime(df['Date'])
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['TempHighF'])
    plt.plot(df['Date'], df['TempAvgF'])
    plt.plot(df['Date'], df['TempLowF'])
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(('High Temperature', 'Average Temperature', 'Low Temperature'))

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace("\n", '')
    buffer.close()
    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    df = pd.read_csv(csv_path)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    temp_high = df.groupby('Month').mean('TempHighF')

    monthly_data = df.groupby('Month').agg({
        'TempHighF': 'mean',
        'TempAvgF': 'mean',
        'TempLowF': 'mean'
    }).reset_index()

    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['Month'], temp_high)

    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.xticks(range(0, len(monthly_data['Month']), 5))
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(('High Temperature', 'Average Temperature', 'Low Temperature'))
    
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace("\n", '')
    buffer.close()

    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    df = pd.read_csv(csv_path)
    df['Events'] = df['Events'].replace(r'^\s*$', 'No Events', regex=True)
    data = df['Events']

    rain = 0
    no_event = 0
    thunderstorm = 0
    fog = 0
    snow = 0

    for i in data:
        if 'No Events' in i:
            no_event += 1
            continue
        if 'Rain' in i:
            rain += 1
        if 'Thunderstorm' in i:
            thunderstorm += 1
        if 'Fog' in i:
            fog += 1
        if 'Snow' in i:
            snow += 1

    x= ['No Events','Rain','Thunderstorm','Fog','Snow']
    y= [no_event, rain, thunderstorm, fog, snow]

    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.xlabel('Events')
    plt.ylabel('Counts')
    plt.title('Events Counts')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace("\n", '')
    buffer.close()

    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem4.html', context)