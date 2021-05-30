# Following https://www.jetbrains.com/pycharm/guide/tutorials/visual_pytest/setup/

1. Created NewProject CluedoFichiers
2. Created setup.py
3. Created new directory src 
4. Created new directory src/CluedoFichiers
5. Ran in terminal ```pip install -e '.[tests]'```
    NB: quotes were needed around ```.[tests]``` maybe due to update of bash?
6. Created src/CluedoFichiers/casebook.py
7. Change default test runner to PyTest
8. Create directory tests
9. Hit shift-cmd-T in casebook.py, which creates two test files
    tests/test_casebook.py with a basic test already
    tests/__init__.py empty
10. Updated first unit test with constructor of CaseBook
