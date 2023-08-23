import allure
from allure_commons.types import Severity
from selene import browser, by, be

# Чистый Selene
def test_github():
    browser.open('https://github.com')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example')
    browser.element('#query-builder-test').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#81')).should(be.visible)


# Через лямбда шаги
def test_github_dynamic_steps():
    with allure.step('Открыть главную страницу'):
        browser.open('https://github.com')
    with allure.step('Найти репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example')
        browser.element('#query-builder-test').submit()
    with allure.step('Перейти по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Открыть таб Issues'):
        browser.element('#issues-tab').click()
    with allure.step('Проверить наличие Issue с номером 81'):
        browser.element(by.partial_text('#81')).should(be.visible)


# Через декоратор
def test_github_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#81')


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Поиск репозитория {repo}')
def search_for_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys(repo)
    browser.element('#query-builder-test').submit()


@allure.step('Перейти по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открыть таб Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверить наличие Issue {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)


# Через лейблы
def test_github_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Неавторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Nikolai')
@allure.feature('Задачи')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_github_decorator_labels():
    pass
