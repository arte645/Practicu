from playwright.sync_api import Page, expect

def test_wiki(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name = 'Русский').click()
    expect(page.get_by_text('Добро пожаловать в Википедию')).to_be_visible()