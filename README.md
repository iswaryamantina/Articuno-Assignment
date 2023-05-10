# Articuno_Assignment

![ezgif com-gif-maker](https://user-images.githubusercontent.com/113454787/213131452-d53b195a-c2c0-4037-ac02-b214a74054db.gif)

command to spin up postgres db using docker :

sudo docker run  --detach      --name container-postgresdb-20     --publish 5432:5432             --env POSTGRES_USER=admin    --env POSTGRES_PASSWORD=admin     postgres:12.1 

command to start the application : python3 ./app.py 
