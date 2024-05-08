#Pypoll script
from collections import defaultdict

# Read the CSV file
with open('Resources\election_data.csv', 'r') as file:
    lines = file.readlines()[1:]  # Skip the header
    total_votes = len(lines)
    candidate_votes = defaultdict(int)

    # Calculate total votes and store votes for each candidate
    for line in lines:
        candidate = line.strip().split(',')[2]
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won
results = {candidate: {'percentage': votes / total_votes * 100, 'votes': votes} for candidate, votes in candidate_votes.items()}

# Find the winner
winner = max(results, key=lambda x: results[x]['votes'])

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in results.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")