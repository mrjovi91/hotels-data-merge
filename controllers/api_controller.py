import datetime
from flask import render_template, request, session, flash, redirect, url_for, jsonify
import json
import requests
import traceback


from settings.settings import settings

# class SubmissionControllerException(Exception):
#     pass

class ApiController:
    @classmethod
    def get_client_ip(cls, request):
        if 'X-Forwarded-For' in request.headers:
            return request.headers.get('X-Forwarded-For')
        return request.remote_addr
    
    @classmethod
    def get_my_ip(cls, request):
        return jsonify({'ip': ApiController.get_client_ip(request)}), 200

    @classmethod
    def search_hotels(cls, request):
        headers = dict(request.headers)
        # headers.pop('X-Api-Key', None)
        data = request.get_json()
        print(data)
        print(headers)
        return jsonify({'ip': ApiController.get_client_ip(request)}), 200
    
    # @classmethod
    # def json_to_form(cls, data):
    #     form = None
    #     if data['form_id'] == str(ManpowerRequisitionFormSubmission.form_id):
    #         form = ManpowerRequisitionFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[ManpowerRequisitionFormSubmission.fields_to_meta['workflow_type_id']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             request_title = data[ManpowerRequisitionFormSubmission.fields_to_meta['request_title']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[ManpowerRequisitionFormSubmission.fields_to_meta['requestor']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[ManpowerRequisitionFormSubmission.fields_to_meta['request_id']]if data[ManpowerRequisitionFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             nature_of_requisition = data[ManpowerRequisitionFormSubmission.fields_to_meta['nature_of_requisition']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['nature_of_requisition']] != "" else None,
    #             justification = data[ManpowerRequisitionFormSubmission.fields_to_meta['justification']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['justification']] != "" else None,
    #             staff_name = data[ManpowerRequisitionFormSubmission.fields_to_meta['staff_name']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['staff_name']] != "" else None,
    #             position = data[ManpowerRequisitionFormSubmission.fields_to_meta['position']],
    #             department_section = data[ManpowerRequisitionFormSubmission.fields_to_meta['department_section']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['department_section']] != "" else None,
    #             employment_type = data[ManpowerRequisitionFormSubmission.fields_to_meta['employment_type']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['employment_type']] != "" else None,
    #             direct_supervisor = data[ManpowerRequisitionFormSubmission.fields_to_meta['direct_supervisor']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['direct_supervisor']] != "" else None,
    #             contract_years = data[ManpowerRequisitionFormSubmission.fields_to_meta['contract_years']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['contract_years']] != "" else None,
    #             other_info = data[ManpowerRequisitionFormSubmission.fields_to_meta['other_info']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['other_info']] != "" else None,
    #             proposed_monthly_salary = data[ManpowerRequisitionFormSubmission.fields_to_meta['proposed_monthly_salary']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['proposed_monthly_salary']] != "" else None,
    #             allowances = data[ManpowerRequisitionFormSubmission.fields_to_meta['allowances']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['allowances']] != "" else None,
    #             job_description = data[ManpowerRequisitionFormSubmission.fields_to_meta['job_description']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['job_description']] != "" else None,
    #             request_date = data[ManpowerRequisitionFormSubmission.fields_to_meta['request_date']] if data[ManpowerRequisitionFormSubmission.fields_to_meta['request_date']] != "" else None
    #         )
    #     elif data['form_id'] == str(OfferSheetFormSubmission.form_id):
    #         form = OfferSheetFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[OfferSheetFormSubmission.fields_to_meta['workflow_type_id']] if data[OfferSheetFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[OfferSheetFormSubmission.fields_to_meta['parent_entry_id']] if data[OfferSheetFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[OfferSheetFormSubmission.fields_to_meta['request_title']] if data[OfferSheetFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[OfferSheetFormSubmission.fields_to_meta['requestor']] if data[OfferSheetFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[OfferSheetFormSubmission.fields_to_meta['request_id']] if data[OfferSheetFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             candidate_name = data[OfferSheetFormSubmission.fields_to_meta['candidate_name']] if data[OfferSheetFormSubmission.fields_to_meta['candidate_name']] != "" else None,
    #             department = data[OfferSheetFormSubmission.fields_to_meta['department']] if data[OfferSheetFormSubmission.fields_to_meta['department']] != "" else None,
    #             position = data[OfferSheetFormSubmission.fields_to_meta['position']] if data[OfferSheetFormSubmission.fields_to_meta['position']] != "" else None,
    #             start_date = data[OfferSheetFormSubmission.fields_to_meta['start_date']] if data[OfferSheetFormSubmission.fields_to_meta['start_date']] != "" else None,
    #             in_singapore = data[OfferSheetFormSubmission.fields_to_meta['in_singapore']] if data[OfferSheetFormSubmission.fields_to_meta['in_singapore']] != "" else None,
    #             in_malaysia = data[OfferSheetFormSubmission.fields_to_meta['in_malaysia']] if data[OfferSheetFormSubmission.fields_to_meta['in_malaysia']] != "" else None,
    #             in_indonesia = data[OfferSheetFormSubmission.fields_to_meta['in_indonesia']] if data[OfferSheetFormSubmission.fields_to_meta['in_indonesia']] != "" else None,
    #             in_thailand = data[OfferSheetFormSubmission.fields_to_meta['in_thailand']] if data[OfferSheetFormSubmission.fields_to_meta['in_thailand']] != "" else None,
    #             in_philippines = data[OfferSheetFormSubmission.fields_to_meta['in_philippines']] if data[OfferSheetFormSubmission.fields_to_meta['in_philippines']] != "" else None,
    #             designation = data[OfferSheetFormSubmission.fields_to_meta['designation']] if data[OfferSheetFormSubmission.fields_to_meta['designation']] != "" else None,
    #             employment_type = data[OfferSheetFormSubmission.fields_to_meta['employment_type']] if data[OfferSheetFormSubmission.fields_to_meta['employment_type']] != "" else None,
    #             section_department = data[OfferSheetFormSubmission.fields_to_meta['section_department']] if data[OfferSheetFormSubmission.fields_to_meta['section_department']] != "" else None,
    #             is_manager = data[OfferSheetFormSubmission.fields_to_meta['is_manager']] if data[OfferSheetFormSubmission.fields_to_meta['is_manager']] != "" else None,
    #             shift_work = data[OfferSheetFormSubmission.fields_to_meta['shift_work']] if data[OfferSheetFormSubmission.fields_to_meta['shift_work']] != "" else None,
    #             salary = data[OfferSheetFormSubmission.fields_to_meta['salary']] if data[OfferSheetFormSubmission.fields_to_meta['salary']] != "" else None,
    #             incentive_scheme = data[OfferSheetFormSubmission.fields_to_meta['incentive_scheme']] if data[OfferSheetFormSubmission.fields_to_meta['incentive_scheme']] != "" else None,
    #             incentive_amount = data[OfferSheetFormSubmission.fields_to_meta['incentive_amount']] if data[OfferSheetFormSubmission.fields_to_meta['incentive_amount']] != "" else None,
    #             incentive_start_date = data[OfferSheetFormSubmission.fields_to_meta['incentive_start_date']] if data[OfferSheetFormSubmission.fields_to_meta['incentive_start_date']] != "" else None,
    #             has_transport_allowance = data[OfferSheetFormSubmission.fields_to_meta['has_transport_allowance']] if data[OfferSheetFormSubmission.fields_to_meta['has_transport_allowance']] != "" else None,
    #             transport_allowance_amount = data[OfferSheetFormSubmission.fields_to_meta['transport_allowance_amount']] if data[OfferSheetFormSubmission.fields_to_meta['transport_allowance_amount']] != "" else None,
    #             has_mobile_allowance = data[OfferSheetFormSubmission.fields_to_meta['has_mobile_allowance']] if data[OfferSheetFormSubmission.fields_to_meta['has_mobile_allowance']] != "" else None,
    #             mobile_allowance_amount = data[OfferSheetFormSubmission.fields_to_meta['mobile_allowance_amount']] if data[OfferSheetFormSubmission.fields_to_meta['mobile_allowance_amount']] != "" else None,
    #             has_standby_allowance = data[OfferSheetFormSubmission.fields_to_meta['has_standby_allowance']] if data[OfferSheetFormSubmission.fields_to_meta['has_standby_allowance']] != "" else None,
    #             standby_allowance_amount = data[OfferSheetFormSubmission.fields_to_meta['standby_allowance_amount']] if data[OfferSheetFormSubmission.fields_to_meta['standby_allowance_amount']] != "" else None,
    #             has_other_allowance = data[OfferSheetFormSubmission.fields_to_meta['has_other_allowance']] if data[OfferSheetFormSubmission.fields_to_meta['has_other_allowance']] != "" else None,
    #             other_allowance_amount = data[OfferSheetFormSubmission.fields_to_meta['other_allowance_amount']] if data[OfferSheetFormSubmission.fields_to_meta['other_allowance_amount']] != "" else None,
    #             other_terms = data[OfferSheetFormSubmission.fields_to_meta['other_terms']] if data[OfferSheetFormSubmission.fields_to_meta['other_terms']] != "" else None
    #         )
    #     elif data['form_id'] == str(InterviewEvaluationFormSubmission.form_id):
    #         form = InterviewEvaluationFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[InterviewEvaluationFormSubmission.fields_to_meta['workflow_type_id']] if data[InterviewEvaluationFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[InterviewEvaluationFormSubmission.fields_to_meta['parent_entry_id']] if data[InterviewEvaluationFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[InterviewEvaluationFormSubmission.fields_to_meta['request_title']] if data[InterviewEvaluationFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[InterviewEvaluationFormSubmission.fields_to_meta['requestor']] if data[InterviewEvaluationFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[InterviewEvaluationFormSubmission.fields_to_meta['request_id']] if data[InterviewEvaluationFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             candidate_name = data[InterviewEvaluationFormSubmission.fields_to_meta['candidate_name']] if data[InterviewEvaluationFormSubmission.fields_to_meta['candidate_name']] != "" else None,
    #             position_applied = data[InterviewEvaluationFormSubmission.fields_to_meta['position_applied']] if data[InterviewEvaluationFormSubmission.fields_to_meta['position_applied']] != "" else None,
    #             department_applied = data[InterviewEvaluationFormSubmission.fields_to_meta['department_applied']] if data[InterviewEvaluationFormSubmission.fields_to_meta['department_applied']] != "" else None,
    #             notice_period = data[InterviewEvaluationFormSubmission.fields_to_meta['notice_period']] if data[InterviewEvaluationFormSubmission.fields_to_meta['notice_period']] != "" else None,
    #             educational_background_1 = data[InterviewEvaluationFormSubmission.fields_to_meta['educational_background_1']] if data[InterviewEvaluationFormSubmission.fields_to_meta['educational_background_1']] != "" else None,
    #             skill_set_competencies_1 = data[InterviewEvaluationFormSubmission.fields_to_meta['skill_set_competencies_1']] if data[InterviewEvaluationFormSubmission.fields_to_meta['skill_set_competencies_1']] != "" else None,
    #             work_experience_1 = data[InterviewEvaluationFormSubmission.fields_to_meta['work_experience_1']] if data[InterviewEvaluationFormSubmission.fields_to_meta['work_experience_1']] != "" else None,
    #             communication_skill_1 = data[InterviewEvaluationFormSubmission.fields_to_meta['communication_skill_1']] if data[InterviewEvaluationFormSubmission.fields_to_meta['communication_skill_1']] != "" else None,
    #             teambuilding_interpersonal_skills_1 = data[InterviewEvaluationFormSubmission.fields_to_meta['teambuilding_interpersonal_skills_1']] if data[InterviewEvaluationFormSubmission.fields_to_meta['teambuilding_interpersonal_skills_1']] != "" else None,
    #             enthusiasm_1 = data[InterviewEvaluationFormSubmission.fields_to_meta['enthusiasm_1']] if data[InterviewEvaluationFormSubmission.fields_to_meta['enthusiasm_1']] != "" else None,
    #             interview_1_comments = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_comments']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_comments']] != "" else None,
    #             interview_1_result = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_result']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_result']] != "" else None,
    #             interview_1_interviewer_1_name = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_1_name']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_1_name']] != "" else None,
    #             interview_1_interviewer_1_designation = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_1_designation']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_1_designation']] != "" else None,
    #             interview_1_interviewer_1_date = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_1_date']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_1_date']] != "" else None,
    #             interview_1_interviewer_2_name = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_2_name']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_2_name']] != "" else None,
    #             interview_1_interviewer_2_designation = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_2_designation']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_2_designation']] != "" else None,
    #             interview_1_interviewer_2_date = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_2_date']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_1_interviewer_2_date']] != "" else None,
    #             interview_2_comments = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_comments']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_comments']] != "" else None,
    #             interview_2_result = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_result']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_result']] != "" else None,
    #             interview_2_interviewer_1_name = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_1_name']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_1_name']] != "" else None,
    #             interview_2_interviewer_1_designation = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_1_designation']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_1_designation']] != "" else None,
    #             interview_2_interviewer_1_date = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_1_date']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_1_date']] != "" else None,
    #             interview_2_interviewer_2_name = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_2_name']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_2_name']] != "" else None,
    #             interview_2_interviewer_2_designation = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_2_designation']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_2_designation']] != "" else None,
    #             interview_2_interviewer_2_date = data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_2_date']] if data[InterviewEvaluationFormSubmission.fields_to_meta['interview_2_interviewer_2_date']] != "" else None
    #     )
    #     elif data['form_id'] == str(CandidateResponseFormSubmission.form_id):
    #         form = CandidateResponseFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[CandidateResponseFormSubmission.fields_to_meta['workflow_type_id']] if data[CandidateResponseFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[CandidateResponseFormSubmission.fields_to_meta['parent_entry_id']] if data[CandidateResponseFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[CandidateResponseFormSubmission.fields_to_meta['request_title']] if data[CandidateResponseFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[CandidateResponseFormSubmission.fields_to_meta['requestor']] if data[CandidateResponseFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[CandidateResponseFormSubmission.fields_to_meta['request_id']] if data[CandidateResponseFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             candidate_name = data[CandidateResponseFormSubmission.fields_to_meta['candidate_name']] if data[CandidateResponseFormSubmission.fields_to_meta['candidate_name']] != "" else None,
    #             position_offered = data[CandidateResponseFormSubmission.fields_to_meta['position_offered']] if data[CandidateResponseFormSubmission.fields_to_meta['position_offered']] != "" else None,
    #             department = data[CandidateResponseFormSubmission.fields_to_meta['department']] if data[CandidateResponseFormSubmission.fields_to_meta['department']] != "" else None,
    #             accepted_job_offer = data[CandidateResponseFormSubmission.fields_to_meta['accepted_job_offer']] if data[CandidateResponseFormSubmission.fields_to_meta['accepted_job_offer']] != "" else None,
    #             response_date = data[CandidateResponseFormSubmission.fields_to_meta['response_date']] if data[CandidateResponseFormSubmission.fields_to_meta['response_date']] != "" else None,
    #         )
    #     elif data['form_id'] == str(JobApplicationFormSubmission.form_id):
    #         form = JobApplicationFormSubmission(
    #         entry_id = data['id'],
    #         workflow_type_id = data[JobApplicationFormSubmission.fields_to_meta['workflow_type_id']] if data[JobApplicationFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #         parent_entry_id = data[JobApplicationFormSubmission.fields_to_meta['parent_entry_id']] if data[JobApplicationFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #         request_title = data[JobApplicationFormSubmission.fields_to_meta['request_title']] if data[JobApplicationFormSubmission.fields_to_meta['request_title']] != "" else None,
    #         requestor = data[JobApplicationFormSubmission.fields_to_meta['requestor']] if data[JobApplicationFormSubmission.fields_to_meta['requestor']] != "" else None,
    #         request_id = data[JobApplicationFormSubmission.fields_to_meta['request_id']] if data[JobApplicationFormSubmission.fields_to_meta['request_id']] != "" else None,
    #         position_applied = data[JobApplicationFormSubmission.fields_to_meta['position_applied']] if data[JobApplicationFormSubmission.fields_to_meta['position_applied']] != "" else None,
    #         employment_type = data[JobApplicationFormSubmission.fields_to_meta['employment_type']] if data[JobApplicationFormSubmission.fields_to_meta['employment_type']] != "" else None,
    #         applicant_full_name = data[JobApplicationFormSubmission.fields_to_meta['applicant_full_name']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_full_name']] != "" else None,
    #         applicant_chinese_name = data[JobApplicationFormSubmission.fields_to_meta['applicant_chinese_name']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_chinese_name']] != "" else None,
    #         applicant_residential_address = data[JobApplicationFormSubmission.fields_to_meta['applicant_residential_address']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_residential_address']] != "" else None,
    #         applicant_mobile_number = data[JobApplicationFormSubmission.fields_to_meta['applicant_mobile_number']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_mobile_number']] != "" else None,
    #         applicant_email = data[JobApplicationFormSubmission.fields_to_meta['applicant_email']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_email']] != "" else None,
    #         applicant_citizenship = data[JobApplicationFormSubmission.fields_to_meta['applicant_citizenship']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_citizenship']] != "" else None,
    #         applicant_work_pass_holder = data[JobApplicationFormSubmission.fields_to_meta['applicant_work_pass_holder']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_work_pass_holder']] != "" else None,
    #         applicant_other_citizenship_type = data[JobApplicationFormSubmission.fields_to_meta['applicant_other_citizenship_type']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_other_citizenship_type']] != "" else None,
    #         applicant_drivers_license = data[JobApplicationFormSubmission.fields_to_meta['applicant_drivers_license']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_drivers_license']] != "" else None,
    #         applicant_drivers_license_class = data[JobApplicationFormSubmission.fields_to_meta['applicant_drivers_license_class']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_drivers_license_class']] != "" else None,
    #         applicant_expected_basic_monthly_salary = data[JobApplicationFormSubmission.fields_to_meta['applicant_expected_basic_monthly_salary']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_expected_basic_monthly_salary']] != "" else None,
    #         applicant_notice_period = data[JobApplicationFormSubmission.fields_to_meta['applicant_notice_period']] if data[JobApplicationFormSubmission.fields_to_meta['applicant_notice_period']] != "" else None,
    #         educational_qualifications_1_institution_name = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_institution_name']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_institution_name']] != "" else None,
    #         educational_qualifications_1_from_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_from_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_from_date']] != "" else None,
    #         educational_qualifications_1_to_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_to_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_to_date']] != "" else None,
    #         educational_qualifications_1_qualification_obtained = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_qualification_obtained']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_1_qualification_obtained']] != "" else None,
    #         educational_qualifications_2_institution_name = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_institution_name']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_institution_name']] != "" else None,
    #         educational_qualifications_2_from_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_from_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_from_date']] != "" else None,
    #         educational_qualifications_2_to_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_to_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_to_date']] != "" else None,
    #         educational_qualifications_2_qualification_obtained = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_qualification_obtained']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_2_qualification_obtained']] != "" else None,
    #         educational_qualifications_3_institution_name = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_institution_name']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_institution_name']] != "" else None,
    #         educational_qualifications_3_from_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_from_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_from_date']] != "" else None,
    #         educational_qualifications_3_to_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_to_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_to_date']] != "" else None,
    #         educational_qualifications_3_qualification_obtained = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_qualification_obtained']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_3_qualification_obtained']] != "" else None,
    #         educational_qualifications_4_institution_name = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_institution_name']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_institution_name']] != "" else None,
    #         educational_qualifications_4_from_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_from_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_from_date']] != "" else None,
    #         educational_qualifications_4_to_date = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_to_date']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_to_date']] != "" else None,
    #         educational_qualifications_4_qualification_obtained = data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_qualification_obtained']] if data[JobApplicationFormSubmission.fields_to_meta['educational_qualifications_4_qualification_obtained']] != "" else None,
    #         employment_history_1_company_name = data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_company_name']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_company_name']] != "" else None,
    #         employment_history_1_from_date = data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_from_date']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_from_date']] != "" else None,
    #         employment_history_1_to_date = data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_to_date']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_to_date']] != "" else None,
    #         employment_history_1_basic_salary = data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_basic_salary']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_basic_salary']] != "" else None,
    #         employment_history_1_allowance_bonus = data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_allowance_bonus']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_allowance_bonus']] != "" else None,
    #         employment_history_1_reason_for_leaving = data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_reason_for_leaving']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_1_reason_for_leaving']] != "" else None,
    #         employment_history_2_company_name = data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_company_name']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_company_name']] != "" else None,
    #         employment_history_2_from_date = data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_from_date']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_from_date']] != "" else None,
    #         employment_history_2_to_date = data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_to_date']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_to_date']] != "" else None,
    #         employment_history_2_basic_salary = data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_basic_salary']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_basic_salary']] != "" else None,
    #         employment_history_2_allowance_bonus = data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_allowance_bonus']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_allowance_bonus']] != "" else None,
    #         employment_history_2_reason_for_leaving = data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_reason_for_leaving']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_2_reason_for_leaving']] != "" else None,
    #         employment_history_3_company_name = data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_company_name']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_company_name']] != "" else None,
    #         employment_history_3_from_date = data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_from_date']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_from_date']] != "" else None,
    #         employment_history_3_to_date = data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_to_date']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_to_date']] != "" else None,
    #         employment_history_3_basic_salary = data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_basic_salary']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_basic_salary']] != "" else None,
    #         employment_history_3_allowance_bonus = data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_allowance_bonus']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_allowance_bonus']] != "" else None,
    #         employment_history_3_reason_for_leaving = data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_reason_for_leaving']] if data[JobApplicationFormSubmission.fields_to_meta['employment_history_3_reason_for_leaving']] != "" else None,
    #         declaration_1 = data[JobApplicationFormSubmission.fields_to_meta['declaration_1']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_1']] != "" else None,
    #         declaration_1_details = data[JobApplicationFormSubmission.fields_to_meta['declaration_1_details']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_1_details']] != "" else None,
    #         declaration_2 = data[JobApplicationFormSubmission.fields_to_meta['declaration_2']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_2']] != "" else None,
    #         declaration_2_details = data[JobApplicationFormSubmission.fields_to_meta['declaration_2_details']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_2_details']] != "" else None,
    #         declaration_3 = data[JobApplicationFormSubmission.fields_to_meta['declaration_3']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_3']] != "" else None,
    #         declaration_4 = data[JobApplicationFormSubmission.fields_to_meta['declaration_4']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_4']] != "" else None,
    #         declaration_4_details = data[JobApplicationFormSubmission.fields_to_meta['declaration_4_details']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_4_details']] != "" else None,
    #         declaration_5 = data[JobApplicationFormSubmission.fields_to_meta['declaration_5']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_5']] != "" else None,
    #         declaration_5_details = data[JobApplicationFormSubmission.fields_to_meta['declaration_5_details']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_5_details']] != "" else None,
    #         declaration_acceptance = data[JobApplicationFormSubmission.fields_to_meta['declaration_acceptance']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_acceptance']] != "" else None,
    #         declaration_date = data[JobApplicationFormSubmission.fields_to_meta['declaration_date']] if data[JobApplicationFormSubmission.fields_to_meta['declaration_date']] != "" else None,
    #         employment_references_1_name = data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_name']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_name']] != "" else None,
    #         employment_references_1_company = data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_company']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_company']] != "" else None,
    #         employment_references_1_designation = data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_designation']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_designation']] != "" else None,
    #         employment_references_1_relationship = data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_relationship']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_relationship']] != "" else None,
    #         employment_references_1_contact = data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_contact']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_1_contact']] != "" else None,
    #         employment_references_2_name = data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_name']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_name']] != "" else None,
    #         employment_references_2_company = data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_company']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_company']] != "" else None,
    #         employment_references_2_designation = data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_designation']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_designation']] != "" else None,
    #         employment_references_2_relationship = data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_relationship']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_relationship']] != "" else None,
    #         employment_references_2_contact = data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_contact']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_2_contact']] != "" else None,
    #         employment_references_3_name = data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_name']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_name']] != "" else None,
    #         employment_references_3_company = data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_company']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_company']] != "" else None,
    #         employment_references_3_designation = data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_designation']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_designation']] != "" else None,
    #         employment_references_3_relationship = data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_relationship']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_relationship']] != "" else None,
    #         employment_references_3_contact = data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_contact']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_3_contact']] != "" else None,
    #         employment_references_check_authorisation = data[JobApplicationFormSubmission.fields_to_meta['employment_references_check_authorisation']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_check_authorisation']] != "" else None,
    #         employment_references_check_authorisation_date = data[JobApplicationFormSubmission.fields_to_meta['employment_references_check_authorisation_date']] if data[JobApplicationFormSubmission.fields_to_meta['employment_references_check_authorisation_date']] != "" else None
    #     )
    #     elif data['form_id'] == str(EmployeeDataFormSubmission.form_id):
    #         form = EmployeeDataFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[EmployeeDataFormSubmission.fields_to_meta['workflow_type_id']] if data[EmployeeDataFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[EmployeeDataFormSubmission.fields_to_meta['parent_entry_id']] if data[EmployeeDataFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[EmployeeDataFormSubmission.fields_to_meta['request_title']] if data[EmployeeDataFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[EmployeeDataFormSubmission.fields_to_meta['requestor']] if data[EmployeeDataFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[EmployeeDataFormSubmission.fields_to_meta['request_id']] if data[EmployeeDataFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             employee_name = data[EmployeeDataFormSubmission.fields_to_meta['employee_name']] if data[EmployeeDataFormSubmission.fields_to_meta['employee_name']] != "" else None,
    #             employee_identification_no = data[EmployeeDataFormSubmission.fields_to_meta['employee_identification_no']] if data[EmployeeDataFormSubmission.fields_to_meta['employee_identification_no']] != "" else None,
    #             employee_designation = data[EmployeeDataFormSubmission.fields_to_meta['employee_designation']] if data[EmployeeDataFormSubmission.fields_to_meta['employee_designation']] != "" else None,
    #             employee_department = data[EmployeeDataFormSubmission.fields_to_meta['employee_department']] if data[EmployeeDataFormSubmission.fields_to_meta['employee_department']] != "" else None,
    #             employee_religion = data[EmployeeDataFormSubmission.fields_to_meta['employee_religion']] if data[EmployeeDataFormSubmission.fields_to_meta['employee_religion']] != "" else None,
    #             employee_marital_status = data[EmployeeDataFormSubmission.fields_to_meta['employee_marital_status']] if data[EmployeeDataFormSubmission.fields_to_meta['employee_marital_status']] != "" else None,
    #             emergency_1_name = data[EmployeeDataFormSubmission.fields_to_meta['emergency_1_name']] if data[EmployeeDataFormSubmission.fields_to_meta['emergency_1_name']] != "" else None,
    #             emergency_1_relationship = data[EmployeeDataFormSubmission.fields_to_meta['emergency_1_relationship']] if data[EmployeeDataFormSubmission.fields_to_meta['emergency_1_relationship']] != "" else None,
    #             emergency_1_contact = data[EmployeeDataFormSubmission.fields_to_meta['emergency_1_contact']] if data[EmployeeDataFormSubmission.fields_to_meta['emergency_1_contact']] != "" else None,
    #             emergency_2_name = data[EmployeeDataFormSubmission.fields_to_meta['emergency_2_name']] if data[EmployeeDataFormSubmission.fields_to_meta['emergency_2_name']] != "" else None,
    #             emergency_2_relationship = data[EmployeeDataFormSubmission.fields_to_meta['emergency_2_relationship']] if data[EmployeeDataFormSubmission.fields_to_meta['emergency_2_relationship']] != "" else None,
    #             emergency_2_contact = data[EmployeeDataFormSubmission.fields_to_meta['emergency_2_contact']] if data[EmployeeDataFormSubmission.fields_to_meta['emergency_2_contact']] != "" else None,
    #             bank_name = data[EmployeeDataFormSubmission.fields_to_meta['bank_name']] if data[EmployeeDataFormSubmission.fields_to_meta['bank_name']] != "" else None,
    #             bank_branch = data[EmployeeDataFormSubmission.fields_to_meta['bank_branch']] if data[EmployeeDataFormSubmission.fields_to_meta['bank_branch']] != "" else None,
    #             bank_account_name = data[EmployeeDataFormSubmission.fields_to_meta['bank_account_name']] if data[EmployeeDataFormSubmission.fields_to_meta['bank_account_name']] != "" else None,
    #             bank_account_number = data[EmployeeDataFormSubmission.fields_to_meta['bank_account_number']] if data[EmployeeDataFormSubmission.fields_to_meta['bank_account_number']] != "" else None,
    #             acknowledgement = data[EmployeeDataFormSubmission.fields_to_meta['acknowledgement']] if data[EmployeeDataFormSubmission.fields_to_meta['acknowledgement']] != "" else None
    #         )
    #     elif data['form_id'] == str(EmployeeDeclarationFormSubmission.form_id):
    #         form = EmployeeDeclarationFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[EmployeeDeclarationFormSubmission.fields_to_meta['workflow_type_id']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[EmployeeDeclarationFormSubmission.fields_to_meta['parent_entry_id']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[EmployeeDeclarationFormSubmission.fields_to_meta['request_title']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[EmployeeDeclarationFormSubmission.fields_to_meta['requestor']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[EmployeeDeclarationFormSubmission.fields_to_meta['request_id']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             code_of_conduct_acknowledgement = data[EmployeeDeclarationFormSubmission.fields_to_meta['code_of_conduct_acknowledgement']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['code_of_conduct_acknowledgement']] != "" else None,
    #             organisation_1_name = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_name']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_name']] != "" else None,
    #             organisation_1_relationship = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_relationship']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_relationship']] != "" else None,
    #             organisation_1_financial_interest = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_financial_interest']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_financial_interest']] != "" else None,
    #             organisation_1_financial_interest_value = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_financial_interest_value']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_financial_interest_value']] != "" else None,
    #             organisation_1_persons_involved = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_persons_involved']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_1_persons_involved']] != "" else None,
    #             organisation_2_name = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_name']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_name']] != "" else None,
    #             organisation_2_relationship = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_relationship']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_relationship']] != "" else None,
    #             organisation_2_financial_interest = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_financial_interest']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_financial_interest']] != "" else None,
    #             organisation_2_financial_interest_value = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_financial_interest_value']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_financial_interest_value']] != "" else None,
    #             organisation_2_persons_involved = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_persons_involved']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_2_persons_involved']] != "" else None,
    #             organisation_3_name = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_name']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_name']] != "" else None,
    #             organisation_3_relationship = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_relationship']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_relationship']] != "" else None,
    #             organisation_3_financial_interest = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_financial_interest']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_financial_interest']] != "" else None,
    #             organisation_3_financial_interest_value = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_financial_interest_value']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_financial_interest_value']] != "" else None,
    #             organisation_3_persons_involved = data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_persons_involved']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['organisation_3_persons_involved']] != "" else None,
    #             sanctions_confirmation = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_confirmation']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_confirmation']] != "" else None,
    #             sanctions_1_country = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_1_country']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_1_country']] != "" else None,
    #             sanctions_1_details = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_1_details']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_1_details']] != "" else None,
    #             sanctions_1_amount = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_1_amount']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_1_amount']] != "" else None,
    #             sanctions_2_country = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_2_country']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_2_country']] != "" else None,
    #             sanctions_2_details = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_2_details']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_2_details']] != "" else None,
    #             sanctions_2_amount = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_2_amount']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_2_amount']] != "" else None,
    #             sanctions_3_country = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_3_country']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_3_country']] != "" else None,
    #             sanctions_3_details = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_3_details']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_3_details']] != "" else None,
    #             sanctions_3_amount = data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_3_amount']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['sanctions_3_amount']] != "" else None,
    #             final_acknowledgement = data[EmployeeDeclarationFormSubmission.fields_to_meta['final_acknowledgement']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['final_acknowledgement']] != "" else None,
    #             employee_name = data[EmployeeDeclarationFormSubmission.fields_to_meta['employee_name']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['employee_name']] != "" else None,
    #             employee_designation = data[EmployeeDeclarationFormSubmission.fields_to_meta['employee_designation']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['employee_designation']] != "" else None,
    #             date_of_confirmation = data[EmployeeDeclarationFormSubmission.fields_to_meta['date_of_confirmation']] if data[EmployeeDeclarationFormSubmission.fields_to_meta['date_of_confirmation']] != "" else None
    #         )
    #     elif data['form_id'] == str(StaffOnboardingFormSubmission.form_id):
    #         form = StaffOnboardingFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[StaffOnboardingFormSubmission.fields_to_meta['workflow_type_id']] if data[StaffOnboardingFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[StaffOnboardingFormSubmission.fields_to_meta['parent_entry_id']] if data[StaffOnboardingFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[StaffOnboardingFormSubmission.fields_to_meta['request_title']] if data[StaffOnboardingFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[StaffOnboardingFormSubmission.fields_to_meta['requestor']] if data[StaffOnboardingFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[StaffOnboardingFormSubmission.fields_to_meta['request_id']] if data[StaffOnboardingFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             employee_name = data[StaffOnboardingFormSubmission.fields_to_meta['employee_name']] if data[StaffOnboardingFormSubmission.fields_to_meta['employee_name']] != "" else None,
    #             department = data[StaffOnboardingFormSubmission.fields_to_meta['department']] if data[StaffOnboardingFormSubmission.fields_to_meta['department']] != "" else None,
    #             job_title = data[StaffOnboardingFormSubmission.fields_to_meta['job_title']] if data[StaffOnboardingFormSubmission.fields_to_meta['job_title']] != "" else None,
    #             manager = data[StaffOnboardingFormSubmission.fields_to_meta['manager']] if data[StaffOnboardingFormSubmission.fields_to_meta['manager']] != "" else None,
    #             employment_status = data[StaffOnboardingFormSubmission.fields_to_meta['employment_status']] if data[StaffOnboardingFormSubmission.fields_to_meta['employment_status']] != "" else None,
    #             start_date = data[StaffOnboardingFormSubmission.fields_to_meta['start_date']] if data[StaffOnboardingFormSubmission.fields_to_meta['start_date']] != "" else None,
    #             end_date = data[StaffOnboardingFormSubmission.fields_to_meta['end_date']] if data[StaffOnboardingFormSubmission.fields_to_meta['end_date']] != "" else None,
    #             location = data[StaffOnboardingFormSubmission.fields_to_meta['location']] if data[StaffOnboardingFormSubmission.fields_to_meta['location']] != "" else None,
    #             require_computer = data[StaffOnboardingFormSubmission.fields_to_meta['require_computer']] if data[StaffOnboardingFormSubmission.fields_to_meta['require_computer']] != "" else None,
    #             previous_computer_user = data[StaffOnboardingFormSubmission.fields_to_meta['previous_computer_user']] if data[StaffOnboardingFormSubmission.fields_to_meta['previous_computer_user']] != "" else None,
    #             new_computer_required = data[StaffOnboardingFormSubmission.fields_to_meta['new_computer_required']] if data[StaffOnboardingFormSubmission.fields_to_meta['new_computer_required']] != "" else None,
    #             computer_operating_system = data[StaffOnboardingFormSubmission.fields_to_meta['computer_operating_system']] if data[StaffOnboardingFormSubmission.fields_to_meta['computer_operating_system']] != "" else None,
    #             email = data[StaffOnboardingFormSubmission.fields_to_meta['email']] if data[StaffOnboardingFormSubmission.fields_to_meta['email']] != "" else None,
    #             ats_sg_all_staff_distribution_group = data[StaffOnboardingFormSubmission.fields_to_meta['ats_sg_all_staff_distribution_group']] if data[StaffOnboardingFormSubmission.fields_to_meta['ats_sg_all_staff_distribution_group']] != "" else None,
    #             ats_my_all_staff_distribution_group = data[StaffOnboardingFormSubmission.fields_to_meta['ats_my_all_staff_distribution_group']] if data[StaffOnboardingFormSubmission.fields_to_meta['ats_my_all_staff_distribution_group']] != "" else None,
    #             pisg_all_staff_distribution_group = data[StaffOnboardingFormSubmission.fields_to_meta['pisg_all_staff_distribution_group']] if data[StaffOnboardingFormSubmission.fields_to_meta['pisg_all_staff_distribution_group']] != "" else None,
    #             piid_all_staff_distribution_group = data[StaffOnboardingFormSubmission.fields_to_meta['piid_all_staff_distribution_group']] if data[StaffOnboardingFormSubmission.fields_to_meta['piid_all_staff_distribution_group']] != "" else None,
    #             pith_all_staff_distribution_group = data[StaffOnboardingFormSubmission.fields_to_meta['pith_all_staff_distribution_group']] if data[StaffOnboardingFormSubmission.fields_to_meta['pith_all_staff_distribution_group']] != "" else None,
    #             other_email_distribution_groups = data[StaffOnboardingFormSubmission.fields_to_meta['other_email_distribution_groups']] if data[StaffOnboardingFormSubmission.fields_to_meta['other_email_distribution_groups']] != "" else None,
    #             shared_mailboxes = data[StaffOnboardingFormSubmission.fields_to_meta['shared_mailboxes']] if data[StaffOnboardingFormSubmission.fields_to_meta['shared_mailboxes']] != "" else None,
    #             ms_office_2016 = data[StaffOnboardingFormSubmission.fields_to_meta['ms_office_2016']] if data[StaffOnboardingFormSubmission.fields_to_meta['ms_office_2016']] != "" else None,
    #             forticlient = data[StaffOnboardingFormSubmission.fields_to_meta['forticlient']] if data[StaffOnboardingFormSubmission.fields_to_meta['forticlient']] != "" else None,
    #             ms_visio = data[StaffOnboardingFormSubmission.fields_to_meta['ms_visio']] if data[StaffOnboardingFormSubmission.fields_to_meta['ms_visio']] != "" else None,
    #             ms_project = data[StaffOnboardingFormSubmission.fields_to_meta['ms_project']] if data[StaffOnboardingFormSubmission.fields_to_meta['ms_project']] != "" else None,
    #             other_software_required = data[StaffOnboardingFormSubmission.fields_to_meta['other_software_required']] if data[StaffOnboardingFormSubmission.fields_to_meta['other_software_required']] != "" else None,
    #             sap_access = data[StaffOnboardingFormSubmission.fields_to_meta['sap_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['sap_access']] != "" else None,
    #             accpac_access = data[StaffOnboardingFormSubmission.fields_to_meta['accpac_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['accpac_access']] != "" else None,
    #             servicedesk_access = data[StaffOnboardingFormSubmission.fields_to_meta['servicedesk_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['servicedesk_access']] != "" else None,
    #             servicenow_access = data[StaffOnboardingFormSubmission.fields_to_meta['servicenow_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['servicenow_access']] != "" else None,
    #             sales_force_access = data[StaffOnboardingFormSubmission.fields_to_meta['sales_force_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['sales_force_access']] != "" else None,
    #             phone_required = data[StaffOnboardingFormSubmission.fields_to_meta['phone_required']] if data[StaffOnboardingFormSubmission.fields_to_meta['phone_required']] != "" else None,
    #             existing_phone_extension = data[StaffOnboardingFormSubmission.fields_to_meta['existing_phone_extension']] if data[StaffOnboardingFormSubmission.fields_to_meta['existing_phone_extension']] != "" else None,
    #             voicemail_required = data[StaffOnboardingFormSubmission.fields_to_meta['voicemail_required']] if data[StaffOnboardingFormSubmission.fields_to_meta['voicemail_required']] != "" else None,
    #             door_access_card_required = data[StaffOnboardingFormSubmission.fields_to_meta['door_access_card_required']] if data[StaffOnboardingFormSubmission.fields_to_meta['door_access_card_required']] != "" else None,
    #             door_access_card_location = data[StaffOnboardingFormSubmission.fields_to_meta['door_access_card_location']] if data[StaffOnboardingFormSubmission.fields_to_meta['door_access_card_location']] != "" else None,
    #             drs_work_area_access = data[StaffOnboardingFormSubmission.fields_to_meta['drs_work_area_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['drs_work_area_access']] != "" else None,
    #             acclivis_staging_area_access = data[StaffOnboardingFormSubmission.fields_to_meta['acclivis_staging_area_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['acclivis_staging_area_access']] != "" else None,
    #             service_desk_area_access = data[StaffOnboardingFormSubmission.fields_to_meta['service_desk_area_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['service_desk_area_access']] != "" else None,
    #             server_room_access = data[StaffOnboardingFormSubmission.fields_to_meta['server_room_access']] if data[StaffOnboardingFormSubmission.fields_to_meta['server_room_access']] != "" else None,
    #             door_access_card_other_clearance = data[StaffOnboardingFormSubmission.fields_to_meta['door_access_card_other_clearance']] if data[StaffOnboardingFormSubmission.fields_to_meta['door_access_card_other_clearance']] != "" else None,
    #             dc_access_required = data[StaffOnboardingFormSubmission.fields_to_meta['dc_access_required']] if data[StaffOnboardingFormSubmission.fields_to_meta['dc_access_required']] != "" else None,
    #             tata_dc = data[StaffOnboardingFormSubmission.fields_to_meta['tata_dc']] if data[StaffOnboardingFormSubmission.fields_to_meta['tata_dc']] != "" else None,
    #             telin_dc = data[StaffOnboardingFormSubmission.fields_to_meta['telin_dc']] if data[StaffOnboardingFormSubmission.fields_to_meta['telin_dc']] != "" else None,
    #             telstra_dc = data[StaffOnboardingFormSubmission.fields_to_meta['telstra_dc']] if data[StaffOnboardingFormSubmission.fields_to_meta['telstra_dc']] != "" else None,
    #             equinix_dc = data[StaffOnboardingFormSubmission.fields_to_meta['equinix_dc']] if data[StaffOnboardingFormSubmission.fields_to_meta['equinix_dc']] != "" else None,
    #             name_card_required = data[StaffOnboardingFormSubmission.fields_to_meta['name_card_required']] if data[StaffOnboardingFormSubmission.fields_to_meta['name_card_required']] != "" else None,
    #             name_card_company = data[StaffOnboardingFormSubmission.fields_to_meta['name_card_company']] if data[StaffOnboardingFormSubmission.fields_to_meta['name_card_company']] != "" else None,
    #             name_card_name = data[StaffOnboardingFormSubmission.fields_to_meta['name_card_name']] if data[StaffOnboardingFormSubmission.fields_to_meta['name_card_name']] != "" else None,
    #             name_card_email = data[StaffOnboardingFormSubmission.fields_to_meta['name_card_email']] if data[StaffOnboardingFormSubmission.fields_to_meta['name_card_email']] != "" else None,
    #             name_card_job_title = data[StaffOnboardingFormSubmission.fields_to_meta['name_card_job_title']] if data[StaffOnboardingFormSubmission.fields_to_meta['name_card_job_title']] != "" else None,
    #             name_card_mobile_number = data[StaffOnboardingFormSubmission.fields_to_meta['name_card_mobile_number']] if data[StaffOnboardingFormSubmission.fields_to_meta['name_card_mobile_number']] != "" else None,
    #             name_card_did = data[StaffOnboardingFormSubmission.fields_to_meta['name_card_did']] if data[StaffOnboardingFormSubmission.fields_to_meta['name_card_did']] != "" else None,
    #             requesting_manager = data[StaffOnboardingFormSubmission.fields_to_meta['requesting_manager']] if data[StaffOnboardingFormSubmission.fields_to_meta['requesting_manager']] != "" else None,
    #             request_date = data[StaffOnboardingFormSubmission.fields_to_meta['request_date']] if data[StaffOnboardingFormSubmission.fields_to_meta['request_date']] != "" else None
    #         )
    #     elif data['form_id'] == str(ProbationEvaluationFormSubmission.form_id):
    #         form = ProbationEvaluationFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[ProbationEvaluationFormSubmission.fields_to_meta['workflow_type_id']] if data[ProbationEvaluationFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[ProbationEvaluationFormSubmission.fields_to_meta['parent_entry_id']] if data[ProbationEvaluationFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[ProbationEvaluationFormSubmission.fields_to_meta['request_title']] if data[ProbationEvaluationFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[ProbationEvaluationFormSubmission.fields_to_meta['requestor']] if data[ProbationEvaluationFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[ProbationEvaluationFormSubmission.fields_to_meta['request_id']] if data[ProbationEvaluationFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             employee_id = data[ProbationEvaluationFormSubmission.fields_to_meta['employee_id']] if data[ProbationEvaluationFormSubmission.fields_to_meta['employee_id']] != "" else None,
    #             employee_name = data[ProbationEvaluationFormSubmission.fields_to_meta['employee_name']] if data[ProbationEvaluationFormSubmission.fields_to_meta['employee_name']] != "" else None,
    #             designation_department = data[ProbationEvaluationFormSubmission.fields_to_meta['designation_department']] if data[ProbationEvaluationFormSubmission.fields_to_meta['designation_department']] != "" else None,
    #             join_date = data[ProbationEvaluationFormSubmission.fields_to_meta['join_date']] if data[ProbationEvaluationFormSubmission.fields_to_meta['join_date']] != "" else None,
    #             key_competencies_1 = data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_1']] if data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_1']] != "" else None,
    #             key_competencies_2 = data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_2']] if data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_2']] != "" else None,
    #             key_competencies_3 = data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_3']] if data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_3']] != "" else None,
    #             key_competencies_4 = data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_4']] if data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_4']] != "" else None,
    #             key_competencies_5 = data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_5']] if data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_5']] != "" else None,
    #             key_competencies_6 = data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_6']] if data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_6']] != "" else None,
    #             key_competencies_7 = data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_7']] if data[ProbationEvaluationFormSubmission.fields_to_meta['key_competencies_7']] != "" else None,
    #             kpi_1_deliverable = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_1_deliverable']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_1_deliverable']] != "" else None,
    #             kpi_1_self_assessment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_1_self_assessment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_1_self_assessment']] != "" else None,
    #             kpi_1_supervisor_comment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_1_supervisor_comment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_1_supervisor_comment']] != "" else None,
    #             kpi_2_deliverable = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_2_deliverable']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_2_deliverable']] != "" else None,
    #             kpi_2_self_assessment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_2_self_assessment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_2_self_assessment']] != "" else None,
    #             kpi_2_supervisor_comment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_2_supervisor_comment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_2_supervisor_comment']] != "" else None,
    #             kpi_3_deliverable = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_3_deliverable']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_3_deliverable']] != "" else None,
    #             kpi_3_self_assessment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_3_self_assessment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_3_self_assessment']] != "" else None,
    #             kpi_3_supervisor_comment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_3_supervisor_comment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_3_supervisor_comment']] != "" else None,
    #             kpi_4_deliverable = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_4_deliverable']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_4_deliverable']] != "" else None,
    #             kpi_4_self_assessment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_4_self_assessment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_4_self_assessment']] != "" else None,
    #             kpi_4_supervisor_comment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_4_supervisor_comment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_4_supervisor_comment']] != "" else None,
    #             kpi_5_deliverable = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_5_deliverable']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_5_deliverable']] != "" else None,
    #             kpi_5_self_assessment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_5_self_assessment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_5_self_assessment']] != "" else None,
    #             kpi_5_supervisor_comment = data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_5_supervisor_comment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['kpi_5_supervisor_comment']] != "" else None,
    #             overall_assessment = data[ProbationEvaluationFormSubmission.fields_to_meta['overall_assessment']] if data[ProbationEvaluationFormSubmission.fields_to_meta['overall_assessment']] != "" else None,
    #             recommendation = data[ProbationEvaluationFormSubmission.fields_to_meta['recommendation']] if data[ProbationEvaluationFormSubmission.fields_to_meta['recommendation']] != "" else None,
    #             probation_extension_in_months = data[ProbationEvaluationFormSubmission.fields_to_meta['probation_extension_in_months']] if data[ProbationEvaluationFormSubmission.fields_to_meta['probation_extension_in_months']] != "" else None,
    #             salary_review = data[ProbationEvaluationFormSubmission.fields_to_meta['salary_review']] if data[ProbationEvaluationFormSubmission.fields_to_meta['salary_review']] != "" else None,
    #             others = data[ProbationEvaluationFormSubmission.fields_to_meta['others']] if data[ProbationEvaluationFormSubmission.fields_to_meta['others']] != "" else None,
    #             supervisor_overall_comments = data[ProbationEvaluationFormSubmission.fields_to_meta['supervisor_overall_comments']] if data[ProbationEvaluationFormSubmission.fields_to_meta['supervisor_overall_comments']] != "" else None,
    #             supervisor_recommendation_date = data[ProbationEvaluationFormSubmission.fields_to_meta['supervisor_recommendation_date']] if data[ProbationEvaluationFormSubmission.fields_to_meta['supervisor_recommendation_date']] != "" else None,
    #             employee_comments = data[ProbationEvaluationFormSubmission.fields_to_meta['employee_comments']] if data[ProbationEvaluationFormSubmission.fields_to_meta['employee_comments']] != "" else None,
    #             employee_acknowledgement_date = data[ProbationEvaluationFormSubmission.fields_to_meta['employee_acknowledgement_date']] if data[ProbationEvaluationFormSubmission.fields_to_meta['employee_acknowledgement_date']] != "" else None,
    #         )
    #     elif data['form_id'] == str(StaffOnboardingHrCreationFormSubmission.form_id):
    #         form = StaffOnboardingHrCreationFormSubmission(
    #             entry_id = data['id'],
    #             workflow_type_id = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['workflow_type_id']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['workflow_type_id']] != "" else None,
    #             parent_entry_id = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['parent_entry_id']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['parent_entry_id']] != "" else None,
    #             request_title = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['request_title']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['request_title']] != "" else None,
    #             requestor = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['requestor']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['requestor']] != "" else None,
    #             request_id = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['request_id']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['request_id']] != "" else None,
    #             staff_name = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['staff_name']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['staff_name']] != "" else None,
    #             department = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['department']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['department']] != "" else None,
    #             job_title = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['job_title']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['job_title']] != "" else None,
    #             manager_supervisor = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['manager_supervisor']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['manager_supervisor']] != "" else None,
    #             staff_email = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['staff_email']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['staff_email']] != "" else None,
    #             username = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['username']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['username']] != "" else None,
    #             issued_items = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['issued_items']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['issued_items']] != "" else None,
    #             completed_by = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['completed_by']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['completed_by']] != "" else None,
    #             completed_at = data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['completed_at']] if data[StaffOnboardingHrCreationFormSubmission.fields_to_meta['completed_at']] != "" else None
    #         )
    #     else:
    #         raise SubmissionControllerException("Invalid form")
    #     return form
    
    # @classmethod
    # def post_gravity_form(cls, form):
    #     data = form.generate_post_data()
    #     response = requests.post(settings['gravity_forms_base_url'] + "/entries", auth=(settings['gravity_forms_user'], settings['gravity_forms_pass']), json=data)
        
    #     if response.status_code != 201:
    #         raise SubmissionControllerException("Error during posting of data to gravity forms")
        
    #     data  = response.json()
    #     return data['id']
    
    # @classmethod
    # def get_next_form(cls, current_form, log=None, log_status=None, log_description=None):
    #     next_forms = current_form.generate_next_form()
    #     if next_forms is not None:
    #         next_form_entry_ids = []
    #         for next_form in next_forms:
    #             next_form_entry_ids.append(str(SubmissionController.post_gravity_form(next_form)))
    #         response = {'message': f'Data stored successfully and created forms {",".join(next_form_entry_ids)}', 'result': 'success'}
    #     else:
    #         response = {'message': 'Data stored successfully', 'result': 'success'}
    #     if log is not None and log_description is not None and log_status is not None:
    #         LogController.handle_log(log, log_status, response, log_description)
    #     return jsonify(response)
    
    # @classmethod
    # def reject(cls, request):
    #     try:
    #         headers = dict(request.headers)
    #         headers.pop('X-Api-Key', None)
    #         log = APILog.create(
    #             source_ip = str(AuthenticationController.get_client_ip(request)),
    #             request_type = str(request.method),
    #             request_url = str(request.url),
    #             headers = json.dumps(headers),
    #             received_at = datetime.datetime.now(),
    #             status = "processing"
    #         )
    #         if not AuthenticationController.is_authenticated(request):
    #             response = {'message': 'Unauthorized', 'result': 'failed'}
    #             LogController.handle_log(log, "unauthenticated", response, "API key authentication failure")
    #             return jsonify(response), 401
            
    #         data = request.get_json()
            
    #         log.data = str(data)
    #         log.save()
            
    #         current_form = SubmissionController.json_to_form(data)
    #         voided_form_entries = []
            
    #         while True:
    #             if current_form is None:
    #                 raise SubmissionControllerException("Error during form voiding. Current form is None.")
                
    #             if current_form.is_break_point:
    #                 current_form.voiding = True
    #                 break
    #             next_form_id = current_form.void()
    #             if next_form_id is None:
    #                 raise SubmissionControllerException("Error during form voiding. Next form id is None.")
    #             current_form = SubmissionController.json_to_form(get_gravity_form(next_form_id))
                
    #         return SubmissionController.get_next_form(
    #             current_form = current_form,
    #             log = log,
    #             log_status = "voided",
    #             log_description = "Form voiding triggered successfully"
    #         )
            
    #     except:
    #         ex = traceback.format_exc()
    #         SubmissionController.error_notification.load(
    #             error_msg = f'Error on /reject, details below:\n\n{ex}',
    #         )
    #         SubmissionController.error_notification.send()
        
    
    # @classmethod
    # def store(cls, request):
    #     try:
    #         headers = dict(request.headers)
    #         headers.pop('X-Api-Key', None)
    #         log = APILog.create(
    #             source_ip = str(AuthenticationController.get_client_ip(request)),
    #             request_type = str(request.method),
    #             request_url = str(request.url),
    #             headers = json.dumps(headers),
    #             received_at = datetime.datetime.now(),
    #             status = "processing"
    #         )
    #         if not AuthenticationController.is_authenticated(request):
    #             response = {'message': 'Unauthorized', 'result': 'failed'}
    #             LogController.handle_log(log, "unauthenticated", response, "API key authentication failure")
    #             return jsonify(response), 401
            
    #         data = request.get_json()
            
    #         log.data = str(data)
    #         log.save()
            
    #         current_form = SubmissionController.json_to_form(data)
            
    #         if current_form == None:
    #             raise SubmissionControllerException('Invalid Form')
    #         current_form.save()
    #         current_form.actions()
    #         return SubmissionController.get_next_form(
    #             current_form = current_form,
    #             log = log,
    #             log_status = "success",
    #             log_description = "Data stored successfully!"
    #         )
        
    #     except:
    #         ex = traceback.format_exc()
    #         SubmissionController.error_notification.load(
    #             error_msg = f'Error on /submit, details below:\n\n{ex}',
    #         )
    #         SubmissionController.error_notification.send()
            
    # @classmethod
    # def debug(cls, request):
    #     try:
    #         headers = dict(request.headers)
    #         headers.pop('X-Api-Key', None)
    #         log = APILog.create(
    #             source_ip = str(AuthenticationController.get_client_ip(request)),
    #             request_type = str(request.method),
    #             request_url = str(request.url),
    #             headers = json.dumps(headers),
    #             received_at = datetime.datetime.now(),
    #             status = "processing"
    #         )
            
    #         # if not AuthenticationController.is_authenticated(request):
    #         #     response = {'message': 'Unauthorized', 'result': 'failed'}
    #         #     LogController.handle_log(log, "unauthenticated", response, "API key authentication failure")
    #         #     return jsonify(response), 401
            
    #         print('reached')
    #         data = request.get_json()
    #         print(data)
    #         log.data = str(data)
    #         log.save()
            
    #         response = {'message': "Data stored successfully", 'result': 'success'}
    #         LogController.handle_log(log, "success", response, f"[Test] Data stored successfully.")
    #         return jsonify(response)
    #     except:
    #         ex = traceback.format_exc()
    #         SubmissionController.error_notification.load(
    #             error_msg = f'Error on /debug, details below:\n\n{ex}',
    #         )
    #         SubmissionController.error_notification.send()