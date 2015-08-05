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

        super(ScheduleATransaction, cls).fetch(**kwargs)

    def __unicode__(self):
        return unicode("{cid} receipt: {fn} ({t}, {d})".format(
            cid=self.committee_id,
            fn=self.file_num,
            t=self.tran_id,
            d=self.receipt_date
        ))

    def __str__(self):
        return repr("{cid} receipt: {fn} ({t}, {d})".format(
            cid=self.committee_id,
            fn=self.file_num,
            t=self.tran_id,
            d=self.receipt_date
        ))


class ScheduleBTransaction(utils.PyOpenFecApiIndexedClass):

    def __init__(self, **kwargs):
        self.amendment_indicator = None
        self.back_reference_schedule_id = None
        self.back_reference_transaction_id = None
        self.beneficiary_committee_name = None
        self.committee = None
        self.committee_id = None
        self.disbursement_amount = None
        self.disbursement_date = None
        self.disbursement_description = None
        self.disbursement_type = None
        self.election_type = None
        self.election_type_full = None
        self.entity_type = None
        self.file_number = None
        self.filing_form = None
        self.filing_type = None
        self.form_type = None
        self.image_number = None
        self.line_number = None
        self.link_id = None
        self.load_date = None
        self.memo_text = None
        self.memoed_subtotal = None
        self.national_committee_nonfederal_account = None
        self.original_sub_id = None
        self.pdf_url = None
        self.receipt_date = None
        self.recipient_city = None
        self.recipient_committee = None
        self.recipient_committee_id = None
        self.recipient_name = None
        self.recipient_state = None
        self.recipient_zip = None
        self.record_number = None
        self.report_primary_general = None
        self.report_type = None
        self.report_year = None
        self.sched_b_sk = None
        self.semi_annual_bundled_refund = None
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
            kwargs['resource'] = 'schedules/schedule_b'

        super(ScheduleBTransaction, cls).fetch(**kwargs)

    def __unicode__(self):
        return unicode("{cid} receipt: {fn} ({t}, {d})".format(
            cid=self.committee_id,
            fn=self.file_num,
            t=self.tran_id,
            d=self.disbursement_date
        ))

    def __str__(self):
        return repr("{cid} receipt: {fn} ({t}, {d})".format(
            cid=self.committee_id,
            fn=self.file_num,
            t=self.tran_id,
            d=self.disbursement_date
        ))
