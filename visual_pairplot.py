sns.pairplot(train[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived')
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()
