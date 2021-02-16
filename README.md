# Lahman-Dashboard
Creating a visual interactive dashboard for the Lahman Historical baseball Database


![plot](images/App_Overview.png)

Lahman Database can be accessed at the following location:

http://www.seanlahman.com/baseball-archive/statistics/



Each of the following Dashboard utilize User's Input to narrow the range of included individuals and historical data.

This can be done by Years, Teams, Leagues, Players, Positions, or any combination the user seeks.


To adjust the graph output the user has the ability to select both the  x-axis and y-axis values as well as the color grouping of the represented scatter and violin plots.

![plot](images/App_Guide.gif)





# Lahman Batting Stat Dashboard:

Active Link:

https://lahman-batting.herokuapp.com/

File: *'lahmanBatting.py'*

Data: *'Lahman_Batting_Combined.csv'*



The data was compiled from:

All Historical Batting Stats : *'baseballdatabank-master/core/Batting.csv'*

All Historical Player Apperances : *'baseballdatabank-master/core/Appearances.csv'*

All Historical Player Information : *'baseballdatabank-master/core/People.csv'*

All Historical Team Information : *'baseballdatabank-master/core/Teams.csv'*

Data File Created using:
*'Combine Batting Data.py'*



Simple Batting Correlation Plot:
![plot](images/batting_correlation_plot_2015-2020.png)

Plot created usiing: *'Analysis.py'*






# Lahman Pitching Stat Dashboard:

Active Link:

https://lahman-pitching.herokuapp.com/

File: 'lahmanPitching.py'

Data: *'Lahman_Pitching_Combined.csv'*



The data was compiled from:

All Historical Pitching Stats : *'baseballdatabank-master/core/Pitching.csv'*

All Historical Player Apperances : *'baseballdatabank-master/core/Appearances.csv'*

All Historical Player Information : *'baseballdatabank-master/core/People.csv'*

All Historical Team Information : *'baseballdatabank-master/core/Teams.csv'*

Data File Created using:
*'Combine Pitching Data.py'*


Simple Pitching Correlation Plot:
![plot](images/pitching_correlation_plot_2015-2020.png)

Plot created usiing: *'Analysis.py'*





# Lahman Combined Batting and Pitching Stat Dashboard:

Active Link:

https://lahman-combined.herokuapp.com/


File: 'lahmanMerged.py'

Data: *'Lahman_Combined.csv'*



The data was compiled from:

All Historical Batting Stats : *'baseballdatabank-master/core/Batting.csv'*

All Historical Pitching Stats : *'baseballdatabank-master/core/Pitching.csv'*

All Historical Player Apperances : *'baseballdatabank-master/core/Appearances.csv'*

All Historical Player Information : *'baseballdatabank-master/core/People.csv'*

All Historical Team Information : *'baseballdatabank-master/core/Teams.csv'*

Data File Created using:
*'Merge Batting and Pitching.py'*



## Contributing
Pull requests are welcome. For changes, please open an issue first to discuss what you would like to change or add.

## License
[MIT](https://choosealicense.com/licenses/mit/)
