from . import utils
from .transaction import ScheduleATransaction, ScheduleBTransaction


class Filing(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.amendment_indicator = None
        self.beginning_image_number = None
        self.candidate_id = None
        self.candidate_name = None
        self.cash_on_hand_beginning_period = None
        self.cash_on_hand_end_period = None
        self.committee_id = None
        self.committee_name = None
        self.coverage_end_date = None
        self.coverage_start_date = None
        self.debts_owed_by_committee = None
        self.debts_owed_to_committee = None
        self.document_type = None
        self.election_year = None
        self.ending_image_number = None
        self.file_number = None
        self.form_type = None
        self.house_personal_funds = None
        self.net_donations = None
        self.opposition_personal_funds = None
        self.pages = None
        self.pdf_url = None
        self.previous_file_number = None
        self.primary_general_indicator = None
        self.receipt_date = None
        self.report_type = None
        self.report_type_full = None
        self.report_year = None
        self.request_type = None
        self.senate_personal_funds = None
        self.sub_id = None
        self.total_communication_cost = None
        self.total_disbursements = None
        self.total_independent_expenditures = None
        self.total_individual_contributions = None
        self.total_receipts = None
        self.treasurer_name = None
        self.update_date = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{cid}'s #{fn} Form {ft} ({rtf})".format(fn=self.file_number,
                                                                cid=self.committee_id,
                                                                ft=self.form_type,
                                                                rtf=self.report_type_full))

    def __str__(self):
        return "{cid}'s #{fn} Form {ft} ({rtf})".format(fn=self.file_number,
                                                        cid=self.committee_id,
                                                        ft=self.form_type,
                                                        rtf=self.report_type_full)

    @utils.default_empty_list
    def select_receipts(self, **kwargs):
        return [t for t in ScheduleATransaction.fetch(
            min_image_number=self.beginning_image_number,
            max_image_number=self.ending_image_number,
            **kwargs)]

    @utils.default_empty_list
    def all_receipts(self):
        return [t for t in ScheduleATransaction.fetch(
            min_image_number=self.beginning_image_number,
            max_image_number=self.ending_image_number)]

    @utils.default_empty_list
    def select_disbursements(self, **kwargs):
        return [t for t in ScheduleBTransaction.fetch(
            min_image_number=self.beginning_image_number,
            max_image_number=self.ending_image_number,
            **kwargs)]

    @utils.default_empty_list
    def all_disbursements(self):
        return [r for r in ScheduleBTransaction.fetch(
            min_image_number=self.beginning_image_number,
            max_image_number=self.ending_image_number)]
