MegWorld Website
================

This is the code for the [megworld.co.uk](https://megworld.co.uk) website.
The code is available and you're welcome to use it if you so wish. Please note
that it is under the AGPLv3 (or later) licence.

Installing
----------

To install simply run the following commands:  
`$ virtualenv --system-site-packages .`  
`$ pip install -r pip-req.txt`  
  
Then make a config file in `~/.megworld_config.json` the only
required option is `secret` which must be a long, high entropy
string which should be kept secret at all costs. It's used to
secure the users passwords, here's an example of some of the
options:

```
{
	"database":{
		"engine": "mysql"
		"name": "table_name",
		"user: "my_user",
		"password": "MySecurePass",
		"host": "database.megworld.co.uk",
		"port": 3333
	},
	"secret": "ThisIsMySuperSecretHighEntropyStringThatIKeepSecret",
	"timezone": "Europe/London",
	"language": "cy",
}
```

Finally:  
`$ python manage.py schemamigration megworld --initial`  
`$ python manage.py migrate megworld`

Updating
--------

To update just do

`$ git pull`  
`$ python manage.py schemamigration megworld --auto`  
`$ python manage.py migrate megworld`

Running
-------

To run the website use:  
`$ python manage.py runserver`

Production
----------

You should *not* use the `runserver` showen above when trying to run the site in
production, you need to configure your webserver to execute the wsgi file found in
the `megworld` directory.


Licence
-------

MegWorld website is under the AGPLv3.

[<img src="https://www.gnu.org/graphics/agplv3-155x51.png" alt="AGPLv3">](https://www.gnu.org/licenses/agpl-3.0.html)
