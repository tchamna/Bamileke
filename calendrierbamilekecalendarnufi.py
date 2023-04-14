# -*- coding: utf-8 -*-
"""CalendrierBamilekeCalendarNufi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FSwpHSuiLbRVlb0-krlZ9Gj-NB6bMuq6

Author: Shck Ca᷅mnà' (Tchamna), Resulam, www.resulam.com

# Lié'nzɑ̄ pí Mɑ̄ŋū : Day and Month Definition
"""

Language = "Nufi"

Days_Nufi = ["Líé'nkwè'","Nkɑ́ɑ́ntēē","Nzêngòò","Ncômntēē","Nzîngū","Nzîsō","Nsû'kwɑ̀","Nthʉ̄'ntāā"]

Month_Nufi = ["Ngù'fī","Nkùɑ̀nʉ̀ɑ̀","Mbàkngòfāt","Sò'njɑ̀ɑ̀","Njwēnɑ̌hntà'","Mòmòshʉ̄","Ntûmbhìngòfāt","Mɑ̂ngà'nshì",
              "Kùkū'", "Ndʉ̌'nzɑ̄","Nkhʉ̀ɑ̀nʉ̀ɑ̀","Ncátmɑ̄ŋū"]

Month_Eng = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

Month_Nufi_Eng = dict(zip(Month_Eng,Month_Nufi))

"""# Function Definition"""

import pandas as pd 

def calendar_days(begin_nufi_day, year,month, max_day):

  """
  begin_nufi_day is one of the following days:

  "Líé'nkwè'",
  "Nkɑ́ɑ́ntēē",
  "Nzêngòò",
  "Ncômntēē",
  "Nzîngū",
  "Nzîsō",
  "Nsû'kwɑ̀",
  "Nthʉ̄'ntāā"
  
  """

  import calendar
  import pandas as pd 

  from datetime import datetime
  
  beg_date_string = f"{year}-{month}-{1}"
  beg_day_of_week = datetime.strptime(beg_date_string, "%Y-%m-%d").strftime("%A")
  Month_str = datetime.strptime(beg_date_string, "%Y-%m-%d").strftime("%B")

  dict_day_num = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
  start_day_num = dict_day_num[beg_day_of_week]
  # display the calendar
  # print(calendar.month(year, month))

  cal = calendar.monthcalendar(year, month)
  # print(*cal)
  days_int = [item for sublist in cal for item in sublist]
  days_list = []
  Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  Days_Nufi = ["Líé'nkwè'","Nkɑ́ɑ́ntēē","Nzêngòò","Ncômntēē","Nzîngū","Nzîsō","Nsû'kwɑ̀","Nthʉ̄'ntāā"]
  start_day_num_nufi = Days_Nufi.index(begin_nufi_day)

  days_int = [item for sublist in cal for item in sublist]
  days_list = []

  for n in range(0,max_day):
      
    temp = [f"{Month_str} {days_int[n+start_day_num-1]} {str(year)}", Days[(n+start_day_num-1)%7],Days_Nufi[(n+start_day_num_nufi)%8]]
    days_list.append(temp)
  # print(days_list)
  df = pd.DataFrame(days_list)
  df.columns = ["Date","Day(Eng)","Day(Nufi)"]
  return df

###############################################################################################
#                                                                                             #
##############################################################################################
# Days_Nufi = ["Líé'nkwè'","Nkɑ́ɑ́ntēē","Nzêngòò","Ncômntēē","Nzîngū","Nzîsō","Nsû'kwɑ̀","Nthʉ̄'ntāā"]
def calendar_nufi(df, next_month_index, year=2023, month=6, Number_of_days = 31):    
  # Days_June = 30
  start_day_nufi = Days_Nufi[next_month_index]
  max_day = Number_of_days

  Date_df = calendar_days(start_day_nufi,year,month, max_day)
  df = pd.concat([df,Date_df],axis=0)

  next_month_index = (Number_of_days%8 + Days_Nufi.index(start_day_nufi))%8

  return df, next_month_index

def nufi_calendar_yearly(next_month_index, year = 2023, days_Feb=28):
    
  df = pd.DataFrame()

  # print(next_month_index)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=1, Number_of_days = 31)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=2,  Number_of_days = days_Feb)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=3, Number_of_days = 31)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=4, Number_of_days = 30)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=5, Number_of_days = 31)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=6, Number_of_days = 30)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=7, Number_of_days = 31)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=8, Number_of_days = 31)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=9, Number_of_days = 30)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=10, Number_of_days = 31)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=11, Number_of_days = 30)

  df, next_month_index = calendar_nufi(df, next_month_index, year=year,month=12, Number_of_days = 31)

  df.to_csv("Nufi_Calendar_2023.csv",encoding="utf 8 - sig")

  return df, next_month_index





# February 2023: 28 days (common year)
# February 2024: 29 days (leap year)
# February 2025: 28 days (common year)
# February 2026: 28 days (common year)
# February 2027: 28 days (common year)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Example usage
year = 2023
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")





def calendar_nufi_many_years(This_year,End_year,month_index):

  import pandas as pd 
  """
  This calendar will give you all the days in the year calendar_year
  And the calendar history from 2023 to calendar_year
  
  Days_Nufi = ["Líé'nkwè'","Nkɑ́ɑ́ntēē","Nzêngòò","Ncômntēē","Nzîngū","Nzîsō","Nsû'kwɑ̀","Nthʉ̄'ntāā"]

  """
  # Note: The initial date is what determine the remaining date!
  # You should know what date corresponds to, say, January 1, 2023
  # In my case, January 1, 2023 = Líé'nkwè', that is why Days_Nufi[0] = Líé'nkwè'
  # If for example, I am in 2025, and January 1, 2025 = Ncômntēē, then, I will pick
  # month_index = 3, because Days_Nufi[3] = Ncômntēē, and I will change the variable This_year to 2025

  # # INITIAL DATE
  # month_index = 0 # Days_Nufi[0] = "Líé'nkwè'"
  # This_year = 2023 # We are in 2023, the year of creation of this script

  # month_index = 3 # Days_Nufi[3] = "Ncômntēē"
  # This_year = 2025 # 

  

  ddf = pd.DataFrame()
  for year in range(This_year,End_year+1):
    if is_leap_year(year):
      days_Feb_ = 29
    else:
      days_Feb_ = 28
    df, month_index = nufi_calendar_yearly(month_index, year = year,days_Feb=days_Feb_)
    ddf = pd.concat([ddf,df], axis=0)
  return df, ddf


# INITIAL DATE
month_index = 0 # Days_Nufi[0] = "Líé'nkwè'"
This_year = 2023 # We are in 2023, the year of creation of this script

# month_index = 3 # Days_Nufi[3] = "Ncômntēē"
# This_year = 2025 # 

#END YEAR
End_year = 2200

calendar_end_year, calendar_history = calendar_nufi_many_years(This_year,End_year,month_index)



calendar_history

def fromEng_toNufi_Date(x):

  Month = x.split(" ")[0]
  Day = x.split(" ")[1]
  Year = x.split(" ")[2]

  if int(Day) == 1:
      return f"Ntûmbhì līē', {Month_Nufi_Eng[Month]}, Ngù' {Year}"

  return f"līē' {Day}, {Month_Nufi_Eng[Month]}, Ngù' {Year}"

calendar_history["Nufi_Date"] = calendar_history["Date"].apply(fromEng_toNufi_Date)
calendar_history["Nufi_Full_Date"] = calendar_history["Day(Nufi)"] + ", " + calendar_history["Nufi_Date"]

calendar_history

"""# Today's Date in Nufi"""

import datetime, time 

# Get the current date
now = datetime.datetime.now()

# Format the current date as a year-month-day string
Today = now.strftime("%B %d %Y")

mask_today = calendar_history["Date"] == Today

nufi_date_series = calendar_history[mask_today]["Nufi_Full_Date"]
eng_date_series = calendar_history[mask_today]["Day(Eng)"]

Today_day_nufi = "date introuvable" if len(nufi_date_series) ==0 else list(nufi_date_series)[0] 
Today_day_Eng = "date introuvable" if len(eng_date_series) ==0 else list(eng_date_series)[0] 

print("Zè'é mɑ́ " + Today_day_nufi)
time.sleep(4)
print("Yáá mɑ̀ lāhā ?" )
time.sleep(4)
print("Zēn zǎ mɑ́ Shck Ca᷅mnà' (Tchamna)" )



"""# Lǒ' Pɑ̌' yāā : Save as a CSV"""

calendar_history.to_csv(f"{Language}calendar_history_2023_{End_year}.csv",encoding= "utf 8 - sig")

