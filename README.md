Using Python 3.6.0

Using the chrome browser

1. Download the version ChromeDriver relevant to your browser on PC https://sites.google.com/a/chromium.org/chromedriver/downloads

2. Install all packages according to the \tests\requirements.txt, command "pip install -r requirements.txt"

3. To run a specific test, execute the following command "\HS\Smoke>pytest test_021_Пройти_Тест.py"

4. To run a test suite, execute the following command "\HS>pytest test_smoke.py"

## IF while running the tests you see an error "ModuleNotFoundError: No module named 'EXAMPLE'"
- you need to created file __init__.py in directories "POM, Smoke"