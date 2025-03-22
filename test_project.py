import project as project
import pytest


def test_valid():
    assert project.verify_mode("1") == "1"


def test_valid_error():
    with pytest.raises(ValueError):
        project.verify_mode("cat")


# Testing only the Edge Cases for easy,medium,hard functions
def test_easy():
    with pytest.raises(SystemExit):  # raises SystemExit as Input is Invalid
        project.easy(1)
    with pytest.raises(SystemExit):
        project.easy("x")


def test_medium():
    with pytest.raises(SystemExit):  # raises SystemExit as Input is Invalid
        project.medium(1)
    with pytest.raises(SystemExit):
        project.medium("x")


def test_hard():
    with pytest.raises(SystemExit):  # raises SystemExit as Input is Invalid
        project.hard(2)
    with pytest.raises(SystemExit):
        project.hard("x")
    with pytest.raises(SystemExit):
        project.hard("cat")


def test_show_scores():
    assert (
        project.show_scores("easy", 5)
        == "Impressive! You rearranged every word correctly!"
    )
    assert (
        project.show_scores("hard", 5)
        == "Impressive! You rearranged every word correctly in HARD Mode!"
    )
    assert project.show_scores("medium", 3) == "Good! You got most of them right"
    assert project.show_scores("hard", 2) == "Not bad! You're making progress."
    assert project.show_scores("hard", 0) == "Keep practicing - you'll improve!"


def test_restart():
    with pytest.raises(SystemExit):
        assert project.restart(False)
