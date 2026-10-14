import random

from conftest import FakePasswordRepository

from password_manager import constants
from password_manager.application.use_cases import (
    FindPasswordEntry,
    GeneratePassword,
    SavePasswordEntry,
)
from password_manager.presentation.features.password_manager import (
    password_manager_view_model as view_model_module,
)


class FakeUi:
    """Records clipboard writes and questions, answers with a fixed choice."""

    def __init__(self, answer: bool = True) -> None:
        self.answer = answer
        self.clipboard: list[str] = []
        self.questions: list[str] = []

    def copy(self, text: str) -> None:
        self.clipboard.append(text)

    def confirm(self, message: str) -> bool:
        self.questions.append(message)
        return self.answer


def _make(
    repository: FakePasswordRepository, ui: FakeUi
) -> view_model_module.PasswordManagerViewModel:
    return view_model_module.PasswordManagerViewModel(
        SavePasswordEntry(repository),
        FindPasswordEntry(repository),
        GeneratePassword(random.Random(3)),
        ui.copy,
        ui.confirm,
    )


def test_generate_password_copies_to_clipboard(
    repository: FakePasswordRepository,
) -> None:
    ui = FakeUi()

    password = _make(repository, ui).generate_password()

    assert ui.clipboard == [password]


def test_save_stores_and_clears_fields_after_confirmation(
    repository: FakePasswordRepository,
) -> None:
    ui = FakeUi(answer=True)

    result = _make(repository, ui).save("a.com", "me@x.org", "pw")

    assert result is not None
    assert not result.is_error
    assert result.clear_fields
    assert "a.com" in repository.entries
    assert "me@x.org" in ui.questions[0]


def test_save_does_nothing_when_user_cancels(
    repository: FakePasswordRepository,
) -> None:
    result = _make(repository, FakeUi(answer=False)).save("a.com", "e", "pw")

    assert result is None
    assert repository.entries == {}


def test_save_refuses_empty_field_without_asking(
    repository: FakePasswordRepository,
) -> None:
    ui = FakeUi()

    result = _make(repository, ui).save("", "e", "pw")

    assert result is not None
    assert result.is_error
    assert result.message == constants.MESSAGE_EMPTY_FIELDS
    assert not result.clear_fields
    assert ui.questions == []


def test_find_password_found(repository: FakePasswordRepository) -> None:
    model = _make(repository, FakeUi())
    model.save("a.com", "me@x.org", "pw")

    result = model.find_password("a.com")

    assert not result.is_error
    assert result.message == constants.MESSAGE_DETAILS.format(
        email="me@x.org", password="pw"
    )


def test_find_password_website_not_present(
    repository: FakePasswordRepository,
) -> None:
    result = _make(repository, FakeUi()).find_password("b.com")

    assert result.is_error
    assert result.message == constants.MESSAGE_NO_DETAILS.format(website="b.com")


def test_find_password_no_data_file() -> None:
    model = _make(FakePasswordRepository(has_file=False), FakeUi())

    assert model.find_password("a.com").message == constants.MESSAGE_NO_DATA_FILE


def test_find_password_empty_website(repository: FakePasswordRepository) -> None:
    result = _make(repository, FakeUi()).find_password(" ")

    assert result.message == constants.MESSAGE_EMPTY_FIELDS
