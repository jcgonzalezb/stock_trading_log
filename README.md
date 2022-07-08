# Stock Trading Log REST API
> This project is an HTTP server REST API implementation



##  Environment
This project was developed on Ubuntu 20.04 LTS using python 3.8.10 with flask framework, connecting to a MySQL Database.

## File Descriptions

- ```app.py```  contains the entry point of the API.
- ```config.py```  contains the configuration settings for the API.
- ```DB_stock_log_V3.sql```  contains the database configured for this project (data not included).
- ```models/``` contains classes used for this project.
- ```routes/``` contains endpoints implemented for the API:
- ```routes/auth_blueprint.py``` implemented routes to create users and login.
- ```routes/index_blueprint.py``` implemented routes to test authorization and welcome the user to the API.
- ```routes/user_blueprint.py``` implemented routes to read and update users.
- ```routes/trade_blueprint.py``` implemented routes to create, read and udpate users.
- ```security/``` contains functions used to encrypt and decrypt tokens to identify users for this project.
- ```validators/``` contains functions used to validate request parameters.
- ```schemas/``` contains methods to serialize and deserialize the data.
- ```templates/``` contains html files used to show users and trades.
- ```documentation/``` contains images used in the readme.md file.



## API Endpoints

This is the list of available endpoints for this project.

**Index**

|Method          |Path                           |Description                  |
|----------------|-------------------------------|-----------------------------|
|GET             |```/```                        |Welcome message to the user.  |
|GET             |```/unprotected```             |Test user access. No token needed.|
|GET             |```/protected```               |Test user access. JSON Web Token (JWT) is required.|
|GET             |```/all_users```               |Return all users in the database.|

**Authentication**

|Method          |Path                           |Description                  |
|----------------|-------------------------------|-----------------------------|
|POST            |```/signup```                  |Create a new user. Return a creation confirmation (JSON object). |
|POST            |```/login```             	 |Retrieve user web token. Return a JWT (JSON object) |

**User**

|Method          |Path                           |Description                  |
|----------------|-------------------------------|-----------------------------|
|GET            |```/users/profile```            |Acquire a single user data. JWT is required. Return user profile. |
|PATCH            |```/users/update```       	 |Update a single user. JWT is required. Return a update confirmation (JSON object). |

**Trade**

|Method          |Path                           |Description                  |
|----------------|-------------------------------|-----------------------------|
|POST            |```/trades/new```|Create a new trade. JWT is required. Return a creation confirmation (JSON object). |
|GET             |```/trades/<trade:id>```|Acquire a single trade data. JWT is required. Return trade profile. |
|GET             |```/trades/all```|Acquire all trade data from user. JWT is required. Return profile of all trades created by user. |
|PATCH            |```/trades/<trade_id>```|Update a single trade. JWT is required. Return an update confirmation (JSON object). |
|PATCH            |```/trades/update_status/<trade_id>```|Update the status of a single trade. PATCH is used instead of DELETE to make the trade unavailable. Return an update confirmation (JSON object). |

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

Now you are running the API and available to create requests locally and test functionality, e.g.

```
 * Serving Flask app 'config' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-635-844
```

7. To test the API, copy the IP address from your console, e.g. http://127.0.0.1:5000 and go to Usage

8. When you have done, terminate the app process with Ctrl+c and deactivate the venv.

```
$ deactivate
```
## Usage






## Authors

- Alejandra Hincapie Cortés <a href="https://www.linkedin.com/in/lahincapie612?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BxMhp1VYdQ2WVBGG0L%2BSNZQ%3D%3D" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
