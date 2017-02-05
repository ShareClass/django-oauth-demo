# Django Oauth Demo

## Package
使用 python-social-auth (django-social-auth is deprecated)

    installation:
    pip install -r requirements.txt

優點：將 Oauth User model 整合，並且要實作 account method, 修改 template 相較於 django-allauth 都很簡單。

## Configuration
在 oauth_demo/oauth_credentials.py 設定 API KEY & Client ID

## Run Demo

    1. sync database model
    $ ./manage.py migrate

    2. run server
    $ ./manage.py runserver
 
    3. access endpoint
    using browser: http://localhost:8000/accounts/login


## Endpoints
- /accounts/login
目前只支援 Oauth Login<br>

在 Facebook Login 的部分，Domain name 不可以使用 127.0.0.1:8000<br>
要改用 localhost:8000/accounts/login
Oauth 登入成功後，會導入 "localhost:8000" home page

Google Login 部分，則是使用看個人在 Google Oauth APP 的設定
一般可以設定 callback url 為 127.0.0.1:8000/path/to/google-oauth

- /accounts/logout
- /accounts/info
 console 顯示 username & user email, FB Oauth 不會取得 Email!


## Apps

- accounts
用於管理基本帳戶操作，目前只有實作 Google, Facebook 登入
