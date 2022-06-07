# fizzbuzz
Fizzbuzz REST API technical test

## OVERVIEW

This project is a simple fizz-buzz REST server.
You can read the whole description in the exercise.txt file

## Installation

This project uses Docker to run properly. Run the following command to build the Docker image:


```bash
cd fizzbuzz/
docker image build -t fizzbuzz-app:latest .
```

## Usage

Run the app:
```bash
docker run -d -p 5000:5000 fizzbuzz-app
```

You can now access the app by going to:

```bash
http://localhost:5000/
```
This guides you to the Homepage. If you want to access the actual fizzbuzz you can go to:

```bash
http://localhost:5000/fizzbuzz
```
The arguments should be passed as query parameters. Here is an example:

```bash
http://localhost:5000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz
```

This repository contains a tests.py file that you can run with:

```bash
python -m unittest tests.py
```

You can run pylint on any python file by running:

```bash
pylint tests.py
pylint fizzbuzz.py
```

## COMMENTS AND IMPROVEMENTS

To improve this project, I have a list of ideas:

Have a better file architecture.

Use Nginx which would have handled the compression of the response.

Add the bonus enpoint for the Statistics