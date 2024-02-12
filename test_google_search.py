from selene import browser, be, have


def test_search(browser_size):
    browser.open("https://google.com")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('selene: User-oriented Web UI browser tests in'))


def test_search_2(browser_size):
    browser.open("https://google.com")
    browser.element('[name="q"]').should(be.blank).type('456789099876$%&GFCJNHJVGDRTOIL').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
