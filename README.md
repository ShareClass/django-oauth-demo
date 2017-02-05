# Django Oauth Demo

## Introduction
這個 repo 記錄了使用 python-social-auth 來實作 Google, Facebook Oauth 的方式
只有單純做好串接的動作，可以辨別使用者。

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

## 心得
我們在 Share Class 的專案中會串接 Google Oauth/Facebook Oauth
基於 Django Framework, 我們 survey 了兩個 package: django-allauth, python-social-auth

django-allauth 是一個對於帳戶系統有完整支援的 package. 不論是寄信驗證，Oauth，密碼遺失以及重設密碼都有完整的實作。但是，對於修改 template 比較不容易，因為它的 template 大量使用 django template 語法。如果要擴展到 API 設計的話，就不是一種好方法

python-social-auth 原本是 django-social-auth 於去年年底更改支援到 django 外的 web framework 像是 flask. 這個套件的好處是只實作了最簡單的功能，要修改 views.py (MVC: controller) 以及 template 都很容易

但是兩者都會面臨的問題是 Oauth 時，User Profile 的創建。django-allauth 可以去修改 package source code. python-social-auth 則可以利用 Pipeline 的功能實作解決。
