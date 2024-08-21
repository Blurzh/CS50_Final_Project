import mock
import project

def test_save_recipe_csv():
    mock_beer = project.Beer()
    fail = project.save_recipe_csv(mock_beer, [])
    assert fail == "\nImpossible to create the recipe, since none was entered. If you want to save one, please, select option '1.- Create Recipe'"

def test_valid_name():
    beer = project.Beer()
    with mock.patch('builtins.input', side_effect = ["!·$%&/()=?", 'Donnie']):
        beer.input_name()
    assert beer.name == 'Donnie'

def test_choosing_recipe():
    mock_beer = project.Beer()
    with mock.patch('builtins.input', return_value = '99999'):
        fail = project.choosing_recipe()
    assert fail == "That's not an available recipe. Please, select a new option\n\n"

def test_wrong_option():
    with mock.patch("builtins.input", side_effect = ['5', '0']):
        fail = project.menu()
    assert fail == "That option doesn't exist. Please, select one shown above."