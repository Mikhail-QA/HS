import requests
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterGradesInHomework
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterSubjectsInHomework
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterTypeDz
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterStatusDz
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterFormatAccess
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterWeeks
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterQuarter
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterYears
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestTrainingFormat
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterSchool
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import \
    TestFilterSubjectsInAssessmentsJournal
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import \
    TestFilterGradesInAssessmentsJournal
from API.admin_panel_filters.test_001_filter_assessments_journal_tab_home_school import TestFilterUser
from API.admin_panel_filters.test_002_filter_homework_tab_home_school import TestFilterLabels
from API.admin_panel_filters.test_003_filter_chats import TestFilterSchoolsChats
from API.admin_panel_filters.test_003_filter_chats import TestFilterGradesInChats
from API.admin_panel_filters.test_003_filter_chats import TestFilterSubjectsChats
from API.admin_panel_filters.test_003_filter_chats import TestFilterAccessChats
from API.admin_panel_filters.test_003_filter_chats import TestFilterLabelsChats
from API.admin_panel_filters.test_003_filter_chats import TestFilterUserChats


def suite():
    suite_test = requests.TestSuite()

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
    suite_test.addTest(requests.makeSuite(TestFilterLabels))
    suite_test.addTest(requests.makeSuite(TestFilterWeeks))
    suite_test.addTest(requests.makeSuite(TestFilterSchoolsChats))
    suite_test.addTest(requests.makeSuite(TestFilterGradesInChats))
    suite_test.addTest(requests.makeSuite(TestFilterSubjectsChats))
    suite_test.addTest(requests.makeSuite(TestFilterAccessChats))
    suite_test.addTest(requests.makeSuite(TestFilterLabelsChats))
    suite_test.addTest(requests.makeSuite(TestFilterUserChats))
    return suite_test
