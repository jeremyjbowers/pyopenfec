from pyopenfec import utils

class Candidate(utils.PyOpenFecApiClass):

    def __init__(self, **kwargs):
        self.active_through = None
        self.candidate_id = None
        self.candidate_status = None
        self.candidate_status_full = None
        self.cycles = None
        self.district = None
        self.election_years = None
        self.incumbent_challenge = None
        self.incumbent_challenge_full = None
        self.name = None
        self.office = None
        self.office_full = None
        self.party = None
        self.party_full = None
        self.state = None

        for k,v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("%s (%s)" % (self.name, self.candidate_id))

    def __str__(self):
        return repr("%s (%s)" % (self.name, self.candidate_id))