from . import utils


class ScheduleATransaction(utils.PyOpenFecApiIndexedClass):

    def __init__(self, **kwargs):
        self.amendment_indicator = None
        self.back_reference_schedule_name = None
        self.back_reference_transaction_id = None
        self.committee = None
        self.committee_id = None
        self.contributor = None
        self.contributor_aggregate_ytd = None
        self.contributor_city = None
        self.contributor_employer = None
        self.contributor_first_name = None
        self.contributor_id = None
        self.contributor_last_name = None
        self.contributor_middle_name = None
        self.contributor_name = None
        self.contributor_occupation = None
        self.contributor_prefix = None
        self.contributor_receipt_amount = None
        self.contributor_receipt_date = None
        self.contributor_state = None
        self.contributor_suffix = None
        self.contributor_zip = None
        self.election_type = None
        self.election_type_full = None
        self.entity_type = None
        self.file_number = None
        self.filing_form = None
        self.filing_type = None
        self.form_type = None
        self.form_type_full = None
        self.image_number = None
        self.increased_limit = None
        self.line_number = None
        self.link_id = None
        self.load_date = None
        self.memo_text = None
        self.memoed_subtotal = None
        self.national_committee_nonfederal_account = None
        self.original_sub_id = None
        self.pdf_url = None
        self.receipt_date = None
        self.receipt_type = None
        self.receipt_type_full = None
        self.record_number = None
        self.report_primary_general = None
        self.report_type = None
        self.report_year = None
        self.sched_a_sk = None
        self.status = None
        self.sub_id = None
        self.tran_id = None
        self.transaction_id = None
        self.update_date = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def fetch(cls, **kwargs):
        if 'resource' not in kwargs:
            kwargs['resource'] = 'schedules/schedule_a'

        return super(ScheduleATransaction, cls).fetch(**kwargs)
