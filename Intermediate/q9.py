# Calculate batting average ?
# completed innings = total innings - not-out innings


Runs_scored = int(input("Enter the total runs scored by a player over all the matches :"))
total_innings = int(input("Enter the total of times a player has entered the field :"))
not_out = int(input("Enter the number of matches the player was not out :"))

completed_innings = total_innings - not_out

batting_avg = Runs_scored // completed_innings

print("The total average batting of a batsmen is",batting_avg,"runs")