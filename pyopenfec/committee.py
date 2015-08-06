from . import utils
from .filing import Filing
from .report import Report
from .aggregates import (CommitteeTotals, AggregateScheduleAByZip,
                         AggregateScheduleAByState, AggregateScheduleABySize,
                         AggregateScheduleAByContributor)
from .transaction import ScheduleATransaction, ScheduleBTransaction


class Committee(utils.PyOpenFecApiPaginatedClass):

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
        self._history = None
        self._totals = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{name} {id}".format(name=self.name,
                                            id=self.committee_id))

    def __str__(self):
        return repr("{name} {id}".format(name=self.name,
                                         id=self.committee_id))

    @property
    def history(self):
        if self._history is None:
            self._history = {}
            resource_path = 'committee/{cid}/history'.format(cid=self.committee_id)
            for hp in CommitteeHistoryPeriod.fetch(resource=resource_path):
                self._history[hp.cycle] = hp
        return self._history

    @property
    def totals(self):
        if self._totals is None:
            self._totals = {}
            resource_path = 'committee/{cid}/totals'.format(cid=self.committee_id)
            for ct in CommitteeTotals.fetch(resource=resource_path):
                self._totals[ct.cycle] = ct
        return self._totals

    @utils.default_empty_list
    def select_filings(self, **kwargs):
        return [f for f in Filing.fetch(committee_id=self.committee_id, **kwargs)]

    @utils.default_empty_list
    def all_filings(self):
        return [f for f in Filing.fetch(committee_id=self.committee_id)]

    @utils.default_empty_list
    def select_reports(self, **kwargs):
        resource_path = 'committee/{cid}/reports'.format(cid=self.committee_id)
        return [r for r in Report.fetch(resource=resource_path,
                                        committee_id=self.committee_id,
                                        **kwargs)]

    @utils.default_empty_list
    def all_reports(self):
        resource_path = 'committee/{cid}/reports'.format(cid=self.committee_id)
        return [r for r in Report.fetch(resource=resource_path,
                                        committee_id=self.committee_id)]

    @utils.default_empty_list
    def select_receipts(self, **kwargs):
        return [t for t in ScheduleATransaction.fetch(
            committee_id=self.committee_id, **kwargs)]

    @utils.default_empty_list
    def all_receipts(self):
        return [t for t in ScheduleATransaction.fetch(
            committee_id=self.committee_id)]

    @utils.default_empty_list
    def select_contributions(self, **kwargs):
        return [t for t in ScheduleATransaction.fetch(
            contributor_id=self.committee_id, **kwargs)]

    @utils.default_empty_list
    def all_contributions(self):
        return [t for t in ScheduleATransaction.fetch(
            contributor_id=self.committee_id)]

    @utils.default_empty_list
    def select_disbursements(self, **kwargs):
        return [t for t in ScheduleBTransaction.fetch(
            committee_id=self.committee_id, **kwargs)]

    @utils.default_empty_list
    def all_disbursements(self):
        return [r for r in ScheduleBTransaction.fetch(
            committee_id=self.committee_id)]

    @utils.default_empty_list
    def total_receipts_by_state(self, **kwargs):
        resource = 'committee/{cid}/schedules/schedule_a/by_state'.format(
            cid=self.committee_id)
        return [a for a in AggregateScheduleAByState.fetch(
            resource=resource, **kwargs)]

    @utils.default_empty_list
    def total_receipts_by_size(self, **kwargs):
        resource = 'committee/{cid}/schedules/schedule_a/by_size'.format(
            cid=self.committee_id)
        return [a for a in AggregateScheduleABySize.fetch(
            resource=resource, **kwargs)]

    @utils.default_empty_list
    def total_receipts_by_zip(self, **kwargs):
        resource = 'committee/{cid}/schedules/schedule_a/by_zip'.format(
            cid=self.committee_id)
        return [a for a in AggregateScheduleAByZip.fetch(
            resource=resource, **kwargs)]

    @utils.default_empty_list
    def total_receipts_by_contributor(self, **kwargs):
        resource = 'committee/{cid}/schedules/schedule_a/by_contributor'.format(
            cid=self.committee_id)
        return [a for a in AggregateScheduleAByContributor.fetch(
            resource=resource, **kwargs)]


class CommitteeHistoryPeriod(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.city = None
        self.committee_id = None
        self.committee_type = None
        self.committee_type_full = None
        self.cycle = None
        self.cycles = None
        self.designation = None
        self.designation_full = None
        self.expire_date = None
        self.name = None
        self.organization_type = None
        self.organization_type_full = None
        self.party = None
        self.party_full = None
        self.state = None
        self.state_full = None
        self.street_1 = None
        self.street_2 = None
        self.treasurer_name = None
        self.zip = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{name} [{comm_id}] ({period})".format(
            name=self.name,
            comm_id=self.committee_id,
            period=self.two_year_period))

    def __str__(self):
        return repr("{name} [{comm_id}] ({period})".format(
            name=self.name,
            comm_id=self.committee_id,
            period=self.two_year_period))
