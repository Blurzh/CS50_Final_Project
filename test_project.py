import mock
import project
import pytest


def test_saving_unexisting_recipe():
    mock_beer = project.Beer()
    fail = project.save_recipe_csv(mock_beer, [])
    assert fail == "\nImpossible to create the recipe, since none was entered. If you want to save one, please, select option '1.- Create Recipe'"

# def test_invalid_ingredient():
#     beer = project.Beer()
#     with mock.patch('builtins.input', return_value = 'Peanuts'):
#         fail = beer.ingredients()
#     assert fail == True

def test_valid_name():
    beer = project.Beer()
    with mock.patch('builtins.input', side_effect = ["!·$%&/()=?", 'Donnie']):
        beer.input_name()
    assert beer.name == 'Donnie'

def test_wrong_option():
    with mock.patch("builtins.input", side_effect = ['5', '0']):
        fail = project.menu()
    assert fail == "That option doesn't exist. Please, select one shown above."