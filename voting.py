"""
TASK: Create a VotingSystem class.

Requirements:
1. The class should allow registering candidates.
2. Each candidate should start with 0 votes.
3. The class should allow voters (using voter IDs) to cast votes.
   - Ensure one voter cannot vote more than once.
4. Provide a method to display election results.

Example Usage:
    election = VotingSystem()
    election.register_candidate("Alice")
    election.register_candidate("Bob")
    election.vote("Voter1", "Alice")
    election.vote("Voter2", "Bob")
    election.vote("Voter3", "Alice")
    print(election.results())  # {"Alice": 2, "Bob": 1}
    print(election.winner()) # Alice
"""

class VotingSystem:

    def __init__(self):
        self.candidates = []
        self.voters = set()
        self.results = {}

    def register_candidate(self, candidate):
        if candidate in self.candidates:
            print("Candidate with name already exist")
            return

        self.candidates.append(candidate)
        self.results.update({candidate: 0}) 

    def vote(self, voter, candidate):
        if voter not in self.voters:
            if candidate in self.candidates:
                self.voters.add(voter)
                self.results.update({candidate: self.results[candidate] + 1})
            else:
                print("Candidate is not part of the election")

        else:
            print("Voter has voted already")

    def result(self):
        return self.results

    def winner(self):
        top_votes = 0
        winner = []
        for votes in self.results.values():
            if votes > top_votes:
                top_votes = votes
            
        for candidate in self.results:
            if self.results[candidate] == top_votes:
                winner.append(candidate)
        return winner

election = VotingSystem()
election.register_candidate("Alice")
election.register_candidate("Bob")
election.vote("Voter1", "Alice")
election.vote("Voter2", "Bob")
election.vote("Voter3", "Alice")

print(election.result())  # {"Alice": 2, "Bob": 1}
print(election.winner())

