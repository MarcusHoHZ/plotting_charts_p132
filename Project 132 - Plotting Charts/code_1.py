import csv
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

rows = []

f = pd.read_csv("star_with_gravity(p132).csv")

mass = f["Mass"].to_list()
radius = f["Radius"].to_list()
dist = f["Distance"].to_list()
gravity = f["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()
plt.plot(radius,mass)
plt.title("Radius vs Mass")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()


plt.plot(mass,gravity)

plt.title("Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()