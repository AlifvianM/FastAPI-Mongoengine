FROM python:3.9

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# # WORKDIR /code
# # COPY requirements.txt /code/
# # RUN pip install -r requirements.txt
# # COPY . /code/
# # # CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# RUN pip install "poetry==1.1.13"

# WORKDIR /code
# COPY poetry.lock pyproject.toml /code/
# RUN poetry config virtualenvs.in-project true \
#   && poetry install 
# COPY . /code/
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]