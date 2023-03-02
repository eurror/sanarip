# Installation

## Installation with Docker
```bash
docker build -t my-image:1.0 .
```

```bash
docker run -p 8000:8000 my-image:1.0
```

## Installation without Docker
```bash
mkdir foo && cd foo #1
git clone https://github.com/eurror/sanarip #2
```
```bash
python3 -m venv venv #1
. venv/bin/activate
```
```bash
pip install -r requirments.txt
```
Now create .env file with these fields:
```bash
DB_NAME=
DB_USER=
DB_PASSWORD=
HOST=localhost
PORT=5432
SECRET_KEY=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

## You're almost there!
The last thing to do is just run the local server:
```bash
./manage.py runserver
```
