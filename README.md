## Python UnitTest excercise.


## Goal

Practise writting python UT using unittest module.

## Step-by-step process:

1. Clone git repo.

    git clone git@git.epam.com:<your_login>/unittest-excercises.git

    e.g.

    git clone git@git.epam.com:michal_batyra/unittest-excercises.git

2. Create a feature branch

    git branch -b <your_login>

3. Create a new file "test_*.py" inside "tests" directory.

    e.g

    ./tests/test_weather.py

4. Code python UT using unittest module.

5. Create virtual environment:
    - python --version  # 3.X
    - pip install virtualenv
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt

6. Verify the following commands will passed localy:
    - python -m unittest discover -v
    - coverage run -m unittest discover
    - coverage report --fail-under=100 --omit=tests/*

7. Push your branch / create merge request

    https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html

8. Repeat steps 4-7 until CI/CD pipeline finish successfully.

# Good luck!
