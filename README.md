# Gapminder 2007: GDP per Capita vs. Life Expectancy  
<img width="1000" height="600" alt="Gapminder_2007_World_Development_bubble_chart" src="https://github.com/user-attachments/assets/babe541e-916b-4d4f-82c1-16b7945fc0e3" />


A Python data visualization project analyzing global development metrics (GDP per capita, life expectancy, and population) using Gapminder data from 2007.  

---

## 📊 Key Features  
- **Bubble Chart Visualization**:  
  - **X-axis**: GDP per capita (log scale).  
  - **Y-axis**: Life expectancy (years).  
  - **Bubble size**: Population (scaled).  
  - **Color-coded**: By continent (Asia, Africa, Europe, Americas, Oceania).  
- **Highlighted Countries**: Labels for China, India, and the USA.  

---

## 📁 Project Structure  
```bash
Gapminder_2007_GDP_per_capita_vs_life_expectancy/  
├── archive/  
│   └── gapminder.csv          # Raw dataset (country, population, GDP, life expectancy)  
├── output/  
│   └── Gapminder_2007_World_Development_bubble_chart.png  # Generated plot  
└── Plotter.py                # Script to process data and generate visualization  
```

---

## 🛠️ Installation  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/sepehr-amooei/Gapminder_2007.git  
   cd Gapminder_2007_GDP_per_capita_vs_life_expectancy  
   ```

2. **Install dependencies**:  
   ```bash
   pip install pandas matplotlib  
   ```

---

## 🚀 Usage  
Run the visualization script:  
```bash
python Plotter.py  
```

### What the Script Does:  
1. Loads data from `archive/gapminder.csv`.  
2. Filters for 2007 metrics (GDP per capita, life expectancy, population).  
3. Generates a bubble chart with:  
   - Log-scaled GDP axis.  
   - Continent-based color mapping.  
   - Annotated key countries.  

---

## 📈 Data Insights  
- **Higher GDP correlates with longer life expectancy** (e.g., Europe/USA vs. Africa).  
- **Population disparities**: Large bubbles (China, India) show scale vs. economic output.  

---

## 📜 Dataset Source  
Data sourced from [Gapminder](https://www.gapminder.org/data/), containing:  
| Column         | Description                  |  
|----------------|------------------------------|  
| `country`      | Nation name.                 |  
| `population`   | Total population.            |  
| `continent`    | Region.                      |  
| `life_exp`     | Life expectancy (years).     |  
| `gdp_cap`      | GDP per capita (PPP$).       |  


