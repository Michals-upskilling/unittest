## Python UnitTest excercise.


## Goal

Practise writting python UT using unittest module.

## Step-by-step process:

1. Clone git repo.

    git clone https://github.com/Michals-upskilling/unittest.git

2. Create a feature branch

    git branch -b <your_login>

3. Create a new file "test_*.py" inside "tests" directory.

    e.g

    ./tests/test_weather.py

4. Code python UT using unittest module.

5. Test your changes locally: 
    - python --version  # 3.X
    - pip install virtualenv
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=venv
    - python -m flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=venv
    - python -m unittest discover -v
    - coverage run -m unittest discover
    - coverage report --fail-under=100 --omit=tests/* # For ZSH use: coverage report --fail-under=100 --omit=tests/\\*

6. Push your branch / create pull request

    https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/working-with-your-remote-repository-on-github-or-github-enterprise/creating-an-issue-or-pull-request

7. Repeat steps 4-6 until CI pipeline finish successfully.

# Good luck!
