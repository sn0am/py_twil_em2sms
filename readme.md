Info:
-----
email format needs to be:
XXXXXXXXXX@domain.com
where x is the phone number without country code.

fill env.example with the proper variables before running the docker build command, the example file will be copied into the container working directory as the working .env

There is a simple webpage running at port 8090, this can be used by something like PRTG to monitor running status.

Instructions:
-------------

-build command:

docker build . -t image_name

-run container command:

sudo docker run -d -p 25:25 -p 8090:8090 --restart unless-stopped image_name
