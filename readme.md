Info:
-----
email format needs to be:
XXXXXXXXXX@email.com
where x is the phone number without country code.


Instructions:
-------------

-build command:

docker build . -t image_name

-run container command:

sudo docker run -d -p 25:25 --restart unless-stopped image_name
