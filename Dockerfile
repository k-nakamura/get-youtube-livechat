FROM public.ecr.aws/lambda/python:3.8

RUN pip install google-api-python-client

ARG API_KEY
ENV API_KEY=${API_KEY}

COPY app ${LAMBDA_TASK_ROOT}

CMD [ "lambda_function.lambda_handler" ]
