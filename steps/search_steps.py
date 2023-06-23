from behave import *

@given('search: I am on home page')
def step_impl(context):
    context.search_page.navigate_to_home_page()

@when ('search: I search after "{query}"')
def step_impl(context, query):
    context.search_page.search_after(query)

@then('search: I click search button')
def step_impl(context):
    context.search_page.click_search_button()

