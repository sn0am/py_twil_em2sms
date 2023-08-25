Info:
-----
email format needs to be:
XXXXXXXXXX@email.com
where x is the phone number without country code.


Instructions:
-------------

-build command:

docker build . -t user_name/image_name

-then push image to docker

-run container command:

docker pull user_name/image_name
sudo docker run -d -p 25:25 --env-file /path/to/.env --restart unless-stopped user_name/image_name
