import pytest
from python_grammer.new_study.survey import Survey

@pytest.fixture
def language_survey():
    question = "What's your language?"
    language_survey = Survey(question)
    return language_survey

def test_single_language(language_survey):
    language_survey.store_response("English")
    assert "English" in language_survey.responses

def test_multiple_language(language_survey):
    responses = ["English","Chinese","Japanese"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
