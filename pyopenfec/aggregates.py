from . import utils


class CommitteeTotals(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.all_loans_received = None
        self.all_other_loans = None
        self.allocated_federal_election_levin_share = None
        self.candidate_contribution = None
        self.committee_id = None
        self.contribution_refunds = None
        self.contributions = None
        self.coordinated_expenditures_by_party_committee = None
        self.coverage_end_date = None
        self.coverage_start_date = None
        self.cycle = None
        self.disbursements = None
        self.exempt_legal_accounting_disbursement = None
        self.fed_candidate_committee_contributions = None
        self.fed_candidate_contribution_refunds = None
        self.fed_disbursements = None
        self.fed_election_activity = None
        self.fed_operating_expenditures = None
        self.fed_receipts = None
        self.federal_funds = None
        self.fundraising_disbursements = None
        self.independent_expenditures = None
        self.individual_contributions = None
        self.individual_itemized_contributions = None
        self.individual_unitemized_contributions = None
        self.loan_repayments = None
        self.loan_repayments_candidate_loans = None
        self.loan_repayments_made = None
        self.loan_repayments_other_loans = None
        self.loan_repayments_received = None
        self.loans = None
        self.loans_made = None
        self.loans_made_by_candidate = None
        self.loans_received = None
        self.loans_received_from_candidate = None
        self.net_contributions = None
        self.net_operating_expenditures = None
        self.non_allocated_fed_election_activity = None
        self.nonfed_transfers = None
        self.offsets_to_fundraising_expenditures = None
        self.offsets_to_legal_accounting = None
        self.offsets_to_operating_expenditures = None
        self.operating_expenditures = None
        self.other_disbursements = None
        self.other_fed_operating_expenditures = None
        self.other_fed_receipts = None
        self.other_loans_received = None
        self.other_political_committee_contributions = None
        self.other_receipts = None
        self.political_party_committee_contributions = None
        self.receipts = None
        self.refunded_individual_contributions = None
        self.refunded_other_political_committee_contributions = None
        self.refunded_political_party_committee_contributions = None
        self.repayments_loans_made_by_candidate = None
        self.repayments_other_loans = None
        self.shared_fed_activity = None
        self.shared_fed_activity_nonfed = None
        self.shared_fed_operating_expenditures = None
        self.shared_nonfed_operating_expenditures = None
        self.total_independent_contributions = None
        self.total_independent_expenditures = None
        self.total_offsets_to_operating_expenditures = None
        self.transfers_from_affiliated_committee = None
        self.transfers_from_affiliated_party = None
        self.transfers_from_nonfed_account = None
        self.transfers_from_nonfed_levin = None
        self.transfers_from_other_authorized_committee = None
        self.transfers_to_affiliated_committee = None
        self.transfers_to_other_authorized_committee = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{cid} totals ({c} cycle, {csd}-{ced})".format(
            cid=self.committee_id,
            c=self.cycle,
            csd=self.coverage_start_date,
            ced=self.coverage_end_date
        ))

    def __str__(self):
        return repr("{cid} totals ({c} cycle, {csd}-{ced})".format(
            cid=self.committee_id,
            c=self.cycle,
            csd=self.coverage_start_date,
            ced=self.coverage_end_date
        ))


class AggregateScheduleAByContributor(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.committee_id = None
        self.contributor_id = None
        self.contributor_name = None
        self.cycle = None
        self.image_number = None
        self.total = None
        self.year = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def fetch(cls, **kwargs):
        if 'resource' not in kwargs:
            kwargs['resource'] = 'schedules/schedule_a/by_contributor'

        super(AggregateScheduleAByContributor, cls).fetch(**kwargs)


class AggregateScheduleABySize(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.committee_id = None
        self.count = None
        self.cycle = None
        self.size = None
        self.total = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def fetch(cls, **kwargs):
        if 'resource' not in kwargs:
            kwargs['resource'] = 'schedules/schedule_a/by_size'

        super(AggregateScheduleABySize, cls).fetch(**kwargs)


class AggregateScheduleAByState(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.committee_id = None
        self.count = None
        self.cycle = None
        self.state = None
        self.total = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def fetch(cls, **kwargs):
        if 'resource' not in kwargs:
            kwargs['resource'] = 'schedules/schedule_a/by_state'

        super(AggregateScheduleAByState, cls).fetch(**kwargs)


class AggregateScheduleAByZip(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.committee_id = None
        self.count = None
        self.cycle = None
        self.zip = None
        self.total = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def fetch(cls, **kwargs):
        if 'resource' not in kwargs:
            kwargs['resource'] = 'schedules/schedule_a/by_zip'

        super(AggregateScheduleAByZip, cls).fetch(**kwargs)
