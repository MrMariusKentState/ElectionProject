from flask_app.config.MySQLconnect import MySQLConnection;


class Election2020:
    def __init__(self, data):
        self.id = data['id']
        self.state = data['State']
        self.candidateR = data['Candidate(R)']
        self.popvoteR = data['Pop_vote(R)']
        self.evR = data['EV(R)']
        self.candidateD = data['Candidate(D)']
        self.popvoteD = data['Pop_vote(D)']
        self.evD = data['EV(D)']

    @classmethod
    def get_all_votes(cls):
        query = "SELECT * FROM 2020_election";
        results = MySQLConnection('electionproject').query_db(query)
        votes = []
        for item in results:
            votes.append(cls(item))
        return votes

    @classmethod
    def get_one_state(cls, data):
        query = "SELECT * FROM 2020_election WHERE id = %(id)s";
        result = MySQLConnection('electionproject').query_db(query,data)
        return cls(result[0])