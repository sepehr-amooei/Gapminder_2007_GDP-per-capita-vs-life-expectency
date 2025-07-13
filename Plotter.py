import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

df_gapminder_raw = pd.read_csv('archive/gapminder - gapminder.csv')
df_lifeExp_GDPperCap_2007 = df_gapminder_raw[['country', 'population','continent', 'life_exp', 'gdp_cap']]


plt.figure(figsize=(10,6))
plt.scatter(
    df_lifeExp_GDPperCap_2007['gdp_cap'], df_lifeExp_GDPperCap_2007['life_exp'],
    s= df_lifeExp_GDPperCap_2007['population'] / 1e6,
    c= df_lifeExp_GDPperCap_2007['continent'].map({
        'Asia':'yellow',
        'Europe':'green',
        'Americas':'blue',
        'Africa':'red',
        'Oceania':'purple'
    }),alpha = 0.8
)
continent_colors = {
    
        'Asia':'yellow',
        'Europe':'green',
        'Americas':'blue',
        'Africa':'red',
        'Oceania':'purple'
    
}
legend_handles = [Patch(color=color, label=continent) for continent, color in continent_colors.items()]
plt.xscale('log')
plt.xlabel('GDP per Capita (PPP$, log scale)')
plt.ylabel('Life Expectancy (years)')
plt.title('World Development in 2007 (Gapminder)')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])
plt.legend(handles=legend_handles, title='Continent', loc='upper left', frameon=True)


plt.text(4959.114854, 72.961, 'China', fontsize=9, ha='center', va='center')
plt.text(2452.210407, 64.698, 'India', fontsize=9, ha='center', va='center')
plt.text(42951.65309, 78.242, 'USA', fontsize=9, ha='center', va='center',c='white')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.savefig('output/Gapminder_2007_World_Development_bubble_chart')
plt.show()
