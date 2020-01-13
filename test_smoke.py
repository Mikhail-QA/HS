import unittest
from Smoke.test_000_удаление_П_в_админке import RemovingUsersInAdminPanel
from Smoke.test_001_регистрация_покупка_1_класс_Cамостоятельный_1месяц_выкл_АП import  CreateAccountAndBuyLearningOneMonth
from Smoke.test_002_регистрация_покупка_7_класс_Сучителем_3месяца_с_вкл_АП_и_ПН_без_АП import CreateAccountAndBuyLearningThreeMonth
from Smoke.test_003_регистрация_покупка_10_класс_Сзачислением_9месяцев_и_ПН_с_вкл_АП import CreateAccountAndBuyLearningNineMonth
from Smoke.test_004_авторизация_купить_ЕГЭ_самостоятельный_1месяц_вкл_АП import LoginAndBuyEgeCourseOneMonth
from Smoke.test_005_авторизация_купить_ЕГЭ_онлайн_9месяцев_выкл_АП import LoginBuyEgeCourseNineMonth
from Smoke.test_006_Продлить_курс import LoginAndExtendCourseSchool
from Smoke.test_007_отключить_АП_на_курсе import LoginAndOffAutoPaymentInCourseSchool
from Smoke.test_008_отключить_АП_в_ПН import LoginAndOffAutoPaymentInPersonalMentor
from Smoke.test_009_взять_ПД import CreateAccountAndSelectTrialAccess
from Smoke.test_010_купить_курс_в_ПД import LoginAndBuyCourseInTrialAccess
from Smoke.test_011_проверка_функционала_на_страницу_Урока import LoginAndGoToLessonPageTestAllFunction
from Smoke.test_012_открыть_Выбрать_предмет import LoginAndOpenChosenSubject
from Smoke.test_013_Написать_отзыв import LoginAndWrittenReview
from Smoke.test_014_открыть_Список_всех_занятий import LoginAndGoListAllActivities
from Smoke.test_015_переход_в_Журнал_успеваемости import LoginAndGoToAcademicJournal
from Smoke.test_016_переход_в_Ленту import LoginAndGoToFeed
from Smoke.test_017_После_регистрации_проверка_соответствия_почты_пользователя import CreateAccountAndCheckEmail
from Smoke.test_018_После_авторизации_проверка_соответствия_почты_пользователя import LoginAndCheckEmailForUser
from Smoke.test_019_Проверка_выхода_из_профиля import LoginAndExitProfile
from Smoke.test_020_авторизация_через_соцсеть import RegistrationAndAuthUserInSocialNetwork
from Smoke.test_021_Пройти_Тест import PassTest
from Smoke.test_022_Пройти_Тренажер import PassTrainer
from Smoke.test_023_Проверка_плеера_ИУ import PlayVideoIu
from Smoke.test_024_Проверить_ДЗ_учителем import LoginTeacherAndCheckHomeWorks
from Smoke.test_025_проверка_отсутствия_возможности_загружить_ДЗ_тариф_Самостоятельный import LoginAndGoToLessonPageCheckHomeworkAndYaklass
from Smoke.test_026_проверка_запрета_смены_тарифа import LoginAndChangeRateCourse
from Smoke.test_027_проверка_отображения_оценки_на_страницу_урока import LoginStudentAndCheckBallInHomeWorks
from Smoke.test_028_проверка_открытия_картинки_учителем import LoginTeacherAndCheckImg

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(RemovingUsersInAdminPanel))
suite.addTest(unittest.makeSuite(CreateAccountAndBuyLearningOneMonth))
suite.addTest(unittest.makeSuite(CreateAccountAndBuyLearningThreeMonth))
suite.addTest(unittest.makeSuite(CreateAccountAndBuyLearningNineMonth))
suite.addTest(unittest.makeSuite(LoginAndBuyEgeCourseOneMonth))
suite.addTest(unittest.makeSuite(LoginBuyEgeCourseNineMonth))
suite.addTest(unittest.makeSuite(LoginAndExtendCourseSchool))
suite.addTest(unittest.makeSuite(LoginAndOffAutoPaymentInCourseSchool))
suite.addTest(unittest.makeSuite(LoginAndOffAutoPaymentInPersonalMentor))
suite.addTest(unittest.makeSuite(CreateAccountAndSelectTrialAccess))
suite.addTest(unittest.makeSuite(LoginAndBuyCourseInTrialAccess))
suite.addTest(unittest.makeSuite(LoginAndGoListAllActivities))
suite.addTest(unittest.makeSuite(LoginAndOpenChosenSubject))
suite.addTest(unittest.makeSuite(LoginAndWrittenReview))
suite.addTest(unittest.makeSuite(LoginAndGoToLessonPageTestAllFunction))
suite.addTest(unittest.makeSuite(LoginAndGoToAcademicJournal))
suite.addTest(unittest.makeSuite(LoginAndGoToFeed))
suite.addTest(unittest.makeSuite(CreateAccountAndCheckEmail))
suite.addTest(unittest.makeSuite(LoginAndCheckEmailForUser))
suite.addTest(unittest.makeSuite(LoginAndExitProfile))
suite.addTest(unittest.makeSuite(RegistrationAndAuthUserInSocialNetwork))
suite.addTest(unittest.makeSuite(PassTest))
suite.addTest(unittest.makeSuite(PassTrainer))
suite.addTest(unittest.makeSuite(PlayVideoIu))
suite.addTest(unittest.makeSuite(LoginTeacherAndCheckHomeWorks))
suite.addTest(unittest.makeSuite(LoginAndGoToLessonPageCheckHomeworkAndYaklass))
suite.addTest(unittest.makeSuite(LoginAndChangeRateCourse))
suite.addTest(unittest.makeSuite(LoginStudentAndCheckBallInHomeWorks))
suite.addTest(unittest.makeSuite(LoginTeacherAndCheckImg))



