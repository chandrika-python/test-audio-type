# test-audio-type

## Setup

The first thing to do is to clone the repository:

```sh
$ git https://github.com/chandrika-python/test-audio-type.git
$ cd test-audio-type
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
# Create:
```
And navigate to `http://127.0.0.1:8000/api/create/`
```
# Sample data:
{
  "audioFileType":"song",
  "audioFileMetadata":{
      "duration":300,
      "name":"test1"
      }
}

## Get:
```
And navigate to `http://127.0.0.1:8000/api/get/song/1`
```
## Delete:
```
And navigate to `http://127.0.0.1:8000/api/delete/song/1`
```
## Update:
```
And navigate to `http://127.0.0.1:8000/api/update/song/1`
```
# Update data:
{
  "audioFileType":"song",
  "audioFileMetadata":{
      "duration":300,
      "name":"test1"
      }
}
