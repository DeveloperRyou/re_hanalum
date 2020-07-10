# re_hanalum

re_hanalum is a django website to communicate with hanmin high school students & graduates 

## version

## Usage

1. fork repository `https://github.com/ryou73/re_hanalum`

2. clone your `re_hanalum` repository

```
$ git clone `https://github.com/YOUR_GITHUB_USERNAME/re_hanalum.git`
```

3. make venv & pip install 
```
$ cd re_hanalum
$ python -m venv venv
$ pip install -r requirements.txt
```

4. make secrets.json file in re_hanalum/hanalum/
```
{
    "SECRET_KEY" : "DJANGO_SECRET_KEY",
    "EMAIL_PASSWORD" : "APP_PASSWORD"
}
```

5. migrate & run server
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Contributing

### How to contribute 
1. fork repository `https://github.com/ryou73/re_hanalum`

2. clone your `re_hanalum` repository

```
$ git clone `https://github.com/YOUR_GITHUB_USERNAME/re_hanalum.git`
```

3. make venv & pip install 
```
$ cd re_hanalum
$ python -m venv venv
$ pip install -r requirements.txt
```

4. change your git branch
```
$ git checkout develop
```

5. commit, push

First, write your code. then,

```
$ git add YOUR_CODE_FILE
$ git commit -m "YOUR_COMMIT_MESSAGE"
$ git push origin develop
```

6. go to your repository & send pull request

### How to Synchronize origin repository

1. add remote url
```
$ git remote add upstream https://github.com/ryou73/re_hanalum
```

2. fetch & merge
```
$ git fetch upstream
$ git checkout BRANCH_NANE
$ git merge upstream/master
```

4. reflect your remote repository
```
$ git push origin master
```

## LICENSE
