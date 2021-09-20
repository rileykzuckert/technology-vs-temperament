import pandas as pd, numpy as np, matplotlib.pyplot as plt, statsmodels.api as sm
# create table
index = ['13-14', '20-21']
columns = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [[338, 447.9, 363.6, 408.9, 497.3, 501.7, 486.5], [420.65, 370.9, 375.2, 345.7, 345, 337.3, 410.9]]
df = pd.DataFrame(data, index, columns)
df

index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [338, 447.9, 363.6, 408.9, 497.3, 501.7, 486.5]
df_preteen = pd.Series(data, index)
df_preteen.plot.bar()

index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [420.65, 370.9, 375.2, 345.7, 345, 337.3, 410.9]
df_teen = pd.Series(data, index)
df_teen.plot.bar()

# plot
df_preteen.plot(color='mediumpurple')
df_teen.plot(color='deepskyblue')
plt.title('Phone Screentime of Students', weight='bold')
plt.xlabel('Day of the Week', weight='bold')
plt.ylabel('Number of Minutes Spent on Phone', weight='bold')
plt.legend(['13-14 years old', '20-21 years old'], loc='upper left')
plt.grid()
ax = plt.gca()
ax.set_facecolor('ghostwhite')
