from pyopenfec import utils


class Committee(utils.PyOpenFecApiClass):

    def __init__(self, **kwargs):
        self.candidate_ids = None
        self.committee_id = None
        self.committee_type = None
        self.committee_type_full = None
        self.designation = None
        self.designation_full = None
        self.expire_date = None
        self.first_file_date = None
        self.last_file_date = None
        self.name = None
        self.organization_type = None
        self.organization_type_full = None
        self.party = None
        self.party_full = None
        self.state = None
        self.treasurer_name = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{name} {id}".format(name=self.name,
                                            id=self.committee_id))

    def __str__(self):
        return repr("{name} {id}".format(name=self.name,
                                         id=self.committee_id))
