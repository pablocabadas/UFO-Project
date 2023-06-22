# UFO sightings in Spain

![Alt text](Images/wM1aNIXSqB8GSeQY38LOUHYMYIw.jpg)

## Itroduction
In this project, we have analyzed the areas in Spain where UFO (Unidentified Flying Object) sightings have been reported. Our goal was to identify the regions with higher UFO activity and provide insights into the most favorable locations for witnessing these events. To achieve this, we utilized a database containing records of UFO activities in Spain from 1538 to 2023.

## Data Processing
The selected database primarily consists of geolocations (longitude and latitude), the year of the event, and four common incident types: "Cow incidents," "Crop circle found," "Alien sighted," and "Abduction event." However, to ensure clean and accurate data, we performed data processing using Python.

First, we cleaned the database by removing any NaN (Not a Number) values. Additionally, we enriched the data by adding a frequency range for each sighting event. This range represents the cumulative count of activities that occurred within each event type, providing us with a measure of their importance.

To enhance the location information, we employed the geopy library in conjunction with the Nominatim online service. These tools enabled us to obtain precise coordinates (latitude and longitude) or specific addresses based on the available data.

Implementing the function that extracts the relevant information from the nested dictionaries obtained from geopy posed a challenge. However, we refined the code to extract the desired values, such as provinces and autonomous communities for each sighting. This allowed for more effective filtering and analysis of the data.

## Data Visualization
Once the data was processed and ready for analysis, we visualized it using Tableau. The geographical positioning of the sightings on a map provided us with a clearer understanding of their distribution across Spain.

![Alt text](<Images/Captura de Pantalla 2023-06-22 a las 15.33.18.png>)

To further determine the regions with the highest number of sightings, we created a plot displaying the provinces and their corresponding sighting counts. This visualization aided in identifying the areas of interest.

![Alt text](<Images/Captura de Pantalla 2023-06-22 a las 15.33.40.png>)

Given the substantial number of sightings in Andalucía, we focused on the provinces within this region to gain a more detailed perspective and make informed decisions.

![Alt text](<Images/Captura de Pantalla 2023-06-22 a las 15.33.52.png>)

## Conclusion
Based on our analysis, the province of Cordoba emerged as the top location for UFO sightings. However, it is essential to consider that the majority of these sightings occurred over 50 years ago. This historical data may not provide reliable information about current sighting possibilities.

![Alt text](<Images/Captura de Pantalla 2023-06-22 a las 15.34.01.png>)

To make a more informed decision, we examined the activity trends in the last three decades, broken down by decade.

![Alt text](<Images/Captura de Pantalla 2023-06-22 a las 15.34.10.png>)

From this analysis, we observed that the provinces of León, Zaragoza, and Jaén had the highest UFO activity, especially after 2010. When ranked based on sighting frequencies, the order would be as follows:

1. León
2. Zaragoza
3. Jaén

![Alt text](<Images/Captura de Pantalla 2023-06-22 a las 15.34.20.png>)

In conclusion, to maximize the chances of experiencing UFO sightings, we recommend considering León as the top choice due to its recent sightings, followed by Zaragoza and Jaén. Cordoba, despite having a high number of sightings, may have a slightly lower probability of occurrence.

## Tableau Link

https://public.tableau.com/views/ufo-project/BestUFOplace?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link