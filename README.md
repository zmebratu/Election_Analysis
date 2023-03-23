# Election Analysis

## Overview of Project
The primary objective of this project was to assist Tom, an employee of the Colorado board of elections, in conducting an election audit for the congressional precinct of the mentioned US state. Our goal was to report on the following data:

* Total number of votes cast.
* Total number of votes for each candidate.
* Percentage of votes for each candidate.
* Winner of the election based on the popular vote.

To automate this process, we utilized Python so that the code can be reused for other types of elections such as congressional, local, and senatorial districts. The data for this analysis was gathered from three different sources of voting methods:

* Mail-in ballots, which were hand-counted at the central office.
* Punch cards, which were collected and tabulated by a machine before sending the results to the central office.
* Direct recording electronic (DRE) systems, which used memory cards that were sent to the central office and read by a computer.

With this information presented, we can now proceed to discuss the analysis results.

## Results
* For this congressional election there were 369,711 votes casted.
* Of those votes, 24,801 were from Arapahoe which made 6.7% of the total votes casted. Jefferson had 38,855 voters’ turnout or 10.5%. Denver on the other hand had 82.8% of the votes or 306,055.
* The county with the largest number of votes was Denver. 
* Candidate Raymon received 11,606 or 3.1% of the total votes. Diana obtained 272,892 or 73.8% of the ballot. While Charles received 85,213 or 23% of the total votes.
* Out of 369,711 votes, Diana was unanimously elected with a vote count of 272,892. She had a winning percentage of 73.8%.

## Summary
As mentioned earlier, the Python script we created can be adapted to suit other election scenarios with appropriate modifications.

The script can be adjusted to cater for the following:
* Instead of counties, we can analyze states, regions or countries.
* Rather than just candidate names, we can create a function that identifies the political party of each candidate.
Using this script for future elections offers several benefits, including faster and more straightforward reporting and publication of results. Reusing code is advantageous as it saves time and resources and eliminates redundancy. Additionally, the script can run on any operating system, machine or platform, making it convenient for use in any work environment. 
