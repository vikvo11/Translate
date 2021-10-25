FROM python:3-onbuild
COPY . /usr/src/app
COPY ./google_trans_new_fix.py /usr/local/lib/python3.6/site-packages/google_trans_new/google_trans_new.py
CMD ["python", "api.py"]
