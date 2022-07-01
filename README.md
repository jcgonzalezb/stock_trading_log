


# Stock Trading Log REST API
> This project is an HTTP server REST API implementation



##  Environment
This project was developed on Ubuntu 20.04 LTS using python 3.8.10 with flask framework, connecting to a MySQL Database.

## File Descriptions

- ```app.py```  contains the entry point of the API.
- ```models/``` contains classes used for this project.
- ```routes/``` contains endpoints implemented for the API:
- ```routes/auth_blueprint.py``` implemented routes to create users and login.
- ```routes/index_blueprint.py``` implemented routes to test authorization and welcome the user to the API.
- ```routes/user_blueprint.py``` implemented routes to read and update users.
- ```routes/trade_blueprint.py``` implemented routes to create, read and udpate users.
- ```security/``` contains functions used to encrypt and decrypt tokens to identify users for this project.
- ```validators/``` contains functions used to validate request parameters.
- ```schemas/``` contains methods to serialize and deserialize the data. 


## API Endpoints

This is the list of available endpoints for this project.

**Index**


|Method          |Path                           |Description                  |
|----------------|-------------------------------|-----------------------------|
|GET             |```/```                        |Welcome message to the user  |
|                |```/unprotected```             |Testing user access. No token needed  |








## Installation

1. Clone this repository
```
$   git clone "https://github.com/jcgonzalezb/stock_trading_log.git"
```

2. Access the 'stock_trading_log' directory:

```
$   cd stock_trading_log
```

3. As a good practice, I suggest you create a virtual environment, e.g.

```
$   python3 -m venv myenv
```

4. Activate the new environment

```
$   source myenv/bin/activate
```

5. Install the requirements
```
$   pip install -r requirements.txt
```



6. Run the program

```
$   python3 app.py
```


## Authors

- Alejandra Hincapie Cortés <a href="https://www.linkedin.com/in/lahincapie612?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BxMhp1VYdQ2WVBGG0L%2BSNZQ%3D%3D" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
