# database_project
## python版本>=3.8
### setup
如果是Linux的作業系統的話，以下指令的python全部換成python3，以下指令的pip全部換成pip3。

1.建立虛擬環境:
`python -m venv database_project`

2.進入虛擬環境:

For Windows:
`database_project\Scripts\activate.bat`

For Linux:
`source database_project /bin/activate`

3.安裝套件:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

4.資料庫migrate:

`python manage.py migrate`

5.執行:

`python manage.py runserver`
