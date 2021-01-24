FROM python:3.7

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./GRPCService /GRPCService

# Install GRPC & Motion detection dependencies
WORKDIR /GRPCService
RUN pip install -r /GRPCService/requirementsGRPC.txt
ENTRYPOINT ["python", "Server.py"]
