MegWorld Website
================

This is the code for the [megworld.co.uk](https://megworld.co.uk) website.
The code is available and you're welcome to use it if you so wish. Please note
that it is under the AGPLv3 (or later) licence.

Installing
----------

To install simply run the following:
`pip install -r pip-req.txt`

Then make a config file in `~/.megworld_config.json` the only
required option is `secret` which must be a long, high entropy
string which should be kept secret at all costs. It's used to
secure the users passwords:

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


Licence
-------

MegWorld website is under the AGPLv3.

[<img src="https://www.gnu.org/graphics/agplv3-155x51.png" alt="AGPLv3">](https://www.gnu.org/licenses/agpl-3.0.html)
