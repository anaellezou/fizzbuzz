# fizzbuzz
Fizzbuzz REST API technical test

## OVERVIEW
```bash
Exercise: Write a simple fizz-buzz REST server. 

The original fizz-buzz consists in writing all numbers from 1 to 100, and just replacing all multiples of 3 by fizz, all multiples of 5 by buzz, and all multiples of 15 by fizzbuzz. 
The output would look like this: 1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,....

Your goal is to implement a web server that will expose a REST API endpoint that:
- Accepts five parameters: three integers int1, int2 and limit, and two strings str1 and str2.
- Returns a list of strings with numbers from 1 to limit, where: all multiples of int1 are replaced by str1, all multiples of int2 are replaced by str2, all multiples of int1 and int2 are replaced by str1str2.

 

The server needs to be:
- Ready for production
- Easy to maintain by other developers

 

Bonus: add a statistics endpoint allowing users to know what the most frequent request has been. This endpoint should:
- Accept no parameter
- Return the parameters corresponding to the most used request, as well as the number of hits for this request"
```

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