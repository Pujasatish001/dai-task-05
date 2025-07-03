sns.countplot(x='Survived', hue='Sex', data=train)
plt.title("Survival by Gender")
plt.show()
