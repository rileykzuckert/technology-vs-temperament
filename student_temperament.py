import pandas as pd, numpy as np, matplotlib.pyplot as plt, statsmodels.api as sm
# create table
index = ['13-14', '20-21']
columns = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [[16.6, 17.3, 16.9, 16.2, 14.9, 17.1, 16.5], [15.1, 15.7, 15.8, 15.7, 14.6, 14.2, 15.4]]
df = pd.DataFrame(data, index, columns)
df

index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [16.6, 17.3, 16.9, 16.2, 14.9, 17.1, 16.5]
df_preteen = pd.Series(data, index)
df_preteen.plot.bar()

index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [15.1, 15.7, 15.8, 15.7, 14.6, 14.2, 15.4]
df_teen = pd.Series(data, index)
df_teen.plot.bar()

# plot
df_preteen.plot(color='mediumpurple')
df_teen.plot(color='deepskyblue')
plt.title('Temperament of Students', weight='bold')
plt.xlabel('Day of the Week', weight='bold')
plt.ylabel('Degree of Self-Reported Mood', weight='bold')
plt.legend(['13-14 years old', '20-21 years old'], loc='lower left')
plt.grid()
ax = plt.gca()
ax.set_facecolor('ghostwhite')
