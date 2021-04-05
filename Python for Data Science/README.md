# Python for Data Science

1. Read in the `gapminder_clean.csv` data as a `pandas` `DataFrame`.
2. Filter the data to include only rows where `Year` is `1962` and then make a scatter plot comparing `'CO2 emissions (metric tons per capita)'` and `gdpPercap` for the filtered data. 
3. On the filtered data, calculate the pearson correlation of `'CO2 emissions (metric tons per capita)'` and `gdpPercap`. What is the Pearson R value and associated p value?
4. On the unfiltered data, answer "In what year is the correlation between `'CO2 emissions (metric tons per capita)'` and `gdpPercap` the strongest?" Filter the dataset to that year for the next step...
5. Using `plotly` or `bokeh`, create an interactive scatter plot comparing `'CO2 emissions (metric tons per capita)'` and `gdpPercap`, where the point size is determined by `pop` (population) and the color is determined by the `continent`. 



1. What is the relationship between `continent` and `'Energy use (kg of oil equivalent per capita)'`? A one way ANOVA test was performed for every year. If a significant difference was observed a Tukey’s test was performed to identify significantly different continents 
2. Is there a significant difference between Europe and Asia with respect to `'Imports of goods and services (% of GDP)'` in the years after 1990? A t test was performed to investigate the difference in Imports of goods and services (% of GDP) for Europe and Asia in the years after 1990. No significant (a <= 0.05) difference was found.
3. What is the country (or countries) that has the highest `'Population density (people per sq. km of land area)'` across all years? (i.e., which country has the highest average ranking in this category across each time point in the dataset?) The largest average population density (people per sq. km of land area) was found in Macao SAR, China.
4. What country (or countries) has shown the greatest increase in `'Life expectancy at birth, total (years)'` since 1962? The largest percent increase of life expectancy at birth from 1962 to 2007 found in Bhutan






