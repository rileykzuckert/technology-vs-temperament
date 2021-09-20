import pandas as pd, numpy as np, matplotlib.pyplot as plt, statsmodels.api as sm
# screentime dfs
index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [338, 447.9, 363.6, 408.9, 497.3, 501.7, 486.5]
df_preteen = pd.Series(data, index)
df_preteen.plot.bar()

index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [420.65, 370.9, 375.2, 345.7, 345, 337.3, 410.9]
df_teen = pd.Series(data, index)
df_teen.plot.bar()

# temperament dfs
index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [16.6, 17.3, 16.9, 16.2, 14.9, 17.1, 16.5]
df_preteen = pd.Series(data, index)
df_preteen.plot.bar()

index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [15.1, 15.7, 15.8, 15.7, 14.6, 14.2, 15.4]
df_teen = pd.Series(data, index)
df_teen.plot.bar()

# plot
data = [338.00, 447.9, 363.6, 408.9, 497.3, 501.7, 486.5]
index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_preteen = pd.Series(data, index)
df_preteen.plot(color='lightseagreen', label='Screentime')
plt.grid()
plt.xlabel('Day of the Week', weight='bold')
plt.ylabel('Number of Minutes Spent on Phone', weight='bold', color='lightseagreen')
plt.yticks(color='lightseagreen')
ax = plt.gca()
ax.set_facecolor('ghostwhite')
ax2=plt.twinx()
data2 = [16.6, 17.3, 16.9, 16.2, 14.9, 17.1, 16.5]
ax2.plot(data2, color='orchid', label='Temperament')
ax2.set_ylabel('Degree of Self-Reported Mood', weight='bold', color='orchid')
ax2.tick_params(axis='y', labelcolor='orchid')
plt.title('Relationship Between Screentime and Temperament of 13-14 Year Olds', weight='bold')

data = [420.65, 370.9, 375.2, 345.7, 345.0, 337.3, 410.9]  
index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_preteen = pd.Series(data, index)
df_preteen.plot(color='lightseagreen', label='Screentime')
plt.grid()
plt.xlabel('Day of the Week', weight='bold')
plt.ylabel('Number of Minutes Spent on Phone', weight='bold', color='lightseagreen')
plt.yticks(color='lightseagreen')
ax = plt.gca()
ax.set_facecolor('ghostwhite')
ax2=plt.twinx()
data2 = [15.1, 15.7, 15.8, 15.7, 14.6, 14.2, 15.4]
ax2.plot(data2, color='orchid', label='Temperament')
ax2.set_ylabel('Degree of Self-Reported Mood', weight='bold', color='orchid')
ax2.tick_params(axis='y', labelcolor='orchid')
plt.title('Relationship Between Screentime and Temperament of 20-21 Year Olds', weight='bold')
