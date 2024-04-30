import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Solar Radiation (SRAD)':    0.257716,
    'Temperature (T)':    0.219856,
    'Relative Humidity (RH)':    0.334814,
    'Pressure (P)':    0.187613
}

plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(20, 15))
plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', colors=sns.color_palette('Set2'), textprops={'fontsize': 30}, explode=[0.05, 0.05, 0.05, 0.05], startangle=75)
plt.title('Importance of parameters', fontsize=50)
plt.axis('equal')
plt.savefig('C:\\Users\\Masloriy\\Desktop\\NPF_project_urban\\NPF_project_urban\\png\\\pie_chart.png', dpi=300)