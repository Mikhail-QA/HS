import requests
from API.admin_panel_filters.test_000_save_token import SaveToken
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterGradesInHomework
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterSubjectsInHomework
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterTypeDz
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterStatusDz
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterFormatAccess
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterQuarter
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterYears
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestTrainingFormat
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterSchool
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import \
    TestFilterSubjectsInAssessmentsJournal
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import \
    TestFilterGradesInAssessmentsJournal
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterUser


def suite():
    suite_test = requests.TestSuite()

    suite_test.addTest(requests.makeSuite(SaveToken))
    suite_test.addTest(requests.makeSuite(TestFilterGradesInHomework))
    suite_test.addTest(requests.makeSuite(TestFilterSubjectsInHomework))
    suite_test.addTest(requests.makeSuite(TestFilterTypeDz))
    suite_test.addTest(requests.makeSuite(TestFilterStatusDz))
    suite_test.addTest(requests.makeSuite(TestFilterFormatAccess))
    suite_test.addTest(requests.makeSuite(TestFilterQuarter))
    suite_test.addTest(requests.makeSuite(TestFilterYears))
    suite_test.addTest(requests.makeSuite(TestTrainingFormat))
    suite_test.addTest(requests.makeSuite(TestFilterSchool))
    suite_test.addTest(requests.makeSuite(TestFilterSubjectsInAssessmentsJournal))
    suite_test.addTest(requests.makeSuite(TestFilterGradesInAssessmentsJournal))
    suite_test.addTest(requests.makeSuite(TestFilterUser))
    return suite_test
