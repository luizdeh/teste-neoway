# teste-neoway

## what is it?

A data manipulation service in *Python* that connects to a *PostgreSQL* database and persists data within it, all inside a *Docker* container.

## how does it work?

The application first checks if `base_teste.txt` or `base_teste.csv` exists in the application's **data** folder. Note that if both files exist, the script will opt for the .*csv* file and ignore the .*txt*. Then, after the file is found, it will be read and have its data manipulated (for better usage within the database) and then sent to the database.

## how do I use it?

First things first, make sure to have [Docker](https://www.docker.com/) installed on your machine.

1. Using your favorite terminal, clone the git repository.
```
git clone https://github.com/luizdeh/teste-neoway.git
```

2. Navigate to the cloned repository, which should be as easy as:
```
cd teste-neoway
```

3. Once inside, spin up the Docker container:
```
docker-compose up -d
```

4. To check if everything ran smoothly, run:
```
docker-compose logs app
```

5. The Docker container comes with **pgAdmin4**, which you can use to check the data. To access the database, open your favorite browser and go to `localhost:5050`. The login is `admin@admin.com` and the password is `root`. You need to register a server, which can be done like this:
  - Double-click *Add new server*.
  - In the General tab, name the server *db*.
  - In the Connection tab, in the *Host name/address* field, write *db*.
  - Still in the Connection tab, go to the *Password* field, type *admin* and hit the Save button.
  - Now you can go back to the top left of the screen and start going down the server tree: Servers > db > Databases > default_db > Schemas > public > Tables.
  - There should be a table there called *base_teste*. Right-click it and go to *Scripts* and select the *SELECT Script* option.
  - The top right of the screen should now have a window with the name *Query* with some sql commands inside of it. Click anywhere on it and hit the \<F5\> key.
  - You can now see the data that was imported, the data types of each column and the values contained in each row.

6. After you are done, you can just close the browser, go back to the terminal and type:
```
docker-compose down
```

