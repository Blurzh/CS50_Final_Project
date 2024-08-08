import project
import pytest

def test_missing_saving_recipe():
    with pytest.raises(ValueError):
        beer = project.Beer()
        project.choosing_recipe()

def test_wrong_quantity():
    beer = project.Beer()
    with pytest.raises(ValueError):
        beer.ingredients == ["a", "b", "c", "d"]

def test_invalid_name():
    beer = project.Beer()
    with pytest.raises(ValueError):
        beer.name == "(/&)=(/&)"