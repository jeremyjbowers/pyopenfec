from collections import defaultdict

from . import utils
from .committee import Committee


class Candidate(utils.PyOpenFecApiPaginatedClass):

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
        self._history = None
        self._committees = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{name} {id}".format(name=self.name,
                                            id=self.candidate_id))

    def __str__(self):
        return repr("{name} {id}".format(name=self.name,
                                         id=self.candidate_id))

    @property
    def history(self):
        if self._history is None:
            self._history = {}
            resource_path = 'candidate/{cid}/history'.format(cid=self.candidate_id)
            for hp in CandidateHistoryPeriod.fetch(resource=resource_path):
                self._history[hp.two_year_period] = hp
        return self._history

    @property
    def most_recent_cycle(self):
        return max(self.cycles)

    @property
    def committees(self):
        if self._committees is None:
            committees_by_cycle = defaultdict(list)
            for committee in Committee.fetch(candidate_id=self.candidate_id):
                for cycle in committee.cycles:
                    committees_by_cycle[cycle].append(committee)
            self._committees = dict(committees_by_cycle)
        return self._committees


class CandidateHistoryPeriod(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.address_city = None
        self.address_state = None
        self.address_street_1 = None
        self.address_street_2 = None
        self.address_zip = None
        self.candidate_id = None
        self.candidate_inactive = None
        self.candidate_status = None
        self.candidate_status_full = None
        self.cycles = None
        self.district = None
        self.election_years = None
        self.expire_date = None
        self.form_type = None
        self.incumbent_challenge = None
        self.incumbent_challenge_full = None
        self.load_date = None
        self.name = None
        self.office = None
        self.office_full = None
        self.party = None
        self.party_full = None
        self.state = None
        self.two_year_period = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{name} [{cand_id}] ({period})".format(
            name=self.name,
            cand_id=self.candidate_id,
            period=self.two_year_period))

    def __str__(self):
        return repr("{name} [{cand_id}] ({period})".format(
            name=self.name,
            cand_id=self.candidate_id,
            period=self.two_year_period))
