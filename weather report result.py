Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================================== RESTART: C:\Users\Rahul\OneDrive\Desktop\SlashMark Internship\weather analysi\weather_data_analysis.py ==========================================
   MinTemp  MaxTemp  Rainfall  ...  RainToday  RISK_MM RainTomorrow
0      8.0     24.3       0.0  ...         No      3.6          Yes
1     14.0     26.9       3.6  ...        Yes      3.6          Yes
2     13.7     23.4       3.6  ...        Yes     39.8          Yes
3     13.3     15.5      39.8  ...        Yes      2.8          Yes
4      7.6     16.1       2.8  ...        Yes      0.0           No

[5 rows x 22 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 366 entries, 0 to 365
Data columns (total 22 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   MinTemp        366 non-null    float64
 1   MaxTemp        366 non-null    float64
 2   Rainfall       366 non-null    float64
 3   Evaporation    366 non-null    float64
 4   Sunshine       363 non-null    float64
 5   WindGustDir    363 non-null    object 
 6   WindGustSpeed  364 non-null    float64
 7   WindDir9am     335 non-null    object 
 8   WindDir3pm     365 non-null    object 
 9   WindSpeed9am   359 non-null    float64
 10  WindSpeed3pm   366 non-null    int64  
 11  Humidity9am    366 non-null    int64  
 12  Humidity3pm    366 non-null    int64  
 13  Pressure9am    366 non-null    float64
 14  Pressure3pm    366 non-null    float64
 15  Cloud9am       366 non-null    int64  
 16  Cloud3pm       366 non-null    int64  
 17  Temp9am        366 non-null    float64
 18  Temp3pm        366 non-null    float64
 19  RainToday      366 non-null    object 
 20  RISK_MM        366 non-null    float64
 21  RainTomorrow   366 non-null    object 
dtypes: float64(12), int64(5), object(5)
memory usage: 63.0+ KB
None
          MinTemp     MaxTemp    Rainfall  ...     Temp9am     Temp3pm     RISK_MM
count  366.000000  366.000000  366.000000  ...  366.000000  366.000000  366.000000
mean     7.265574   20.550273    1.428415  ...   12.358470   19.230874    1.428415
std      6.025800    6.690516    4.225800  ...    5.630832    6.640346    4.225800
min     -5.300000    7.600000    0.000000  ...    0.100000    5.100000    0.000000
25%      2.300000   15.025000    0.000000  ...    7.625000   14.150000    0.000000
50%      7.450000   19.650000    0.000000  ...   12.550000   18.550000    0.000000
75%     12.500000   25.500000    0.200000  ...   17.000000   24.000000    0.200000
max     20.900000   35.800000   39.800000  ...   24.700000   34.500000   39.800000

[8 rows x 17 columns]
