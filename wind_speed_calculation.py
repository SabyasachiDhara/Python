import pandas as pd
import numpy as np


data = pd.read_csv("speed.csv")


wind_u=data["u-vector"]
wind_v=data["v-vector"]

#Your given speed formula(Speed(single day observation)=sqrt(wind_u(single day observation)^2 + wind_v(single day observation)^2))
data["Speed"] = np.sqrt((wind_u*wind_u) + (wind_v*wind_v))

#View data after adding Speed column
print(data)

#Average speed per day(I have done this for only 2 days as data given, you can add more just changing the time range)
average_speed_2010_12_31 = data.Speed[(data['date'] >= '2010-12-31 19:00:00-05:00') & (data['date'] <= '2010-12-31 23:00:00-05:00')].mean()
average_speed_2011_01_01 = data.Speed[(data['date'] >= '2011-01-01 00:00:00-05:00') & (data['date'] <= '2011-01-01 23:00:00-05:00')].mean()

print("\nAverage speed on 2010-12-31 = ",average_speed_2010_12_31)
print("Average speed on 2011-01-01 = ",average_speed_2011_01_01)
