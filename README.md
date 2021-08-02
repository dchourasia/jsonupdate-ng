JsonUpdate-NG
==========================

Introduction
------------
jsonupdate-ng provides easy and scalable way to update any json document using following ways:
* json : a head json which you can use to add/update/delete nodes from base json
* jsonpath : a jsonpath as node name along with the value to add/update/delete multiple nodes from the base json in one shot
* a mixup of json and jsonpaths

**PS -** jsonpath is a language like xpath to select single/multiple nodes from a given json. There are multiple tutorials on web to learn this.

Here are few resources to learn jsonpath:
* **jsonpath tutorial** : https://goessner.net/articles/JsonPath/index.html#e2
* **jsonpath evaluator** : https://jsonpath.com/ 

![License](https://img.shields.io/pypi/l/robotframework.svg)

Prerequisites
-------------
jsonupdate-ng has following prerequisites:
```
jsonpath-ng>=1.4.3
setuptools>=39.1.0
```
you can install all the prerequisites either one by one or using the requirements.txt provided with source code:
```
pip install -r requirements.txt
```
Installation
------------
RESTLibrary can be easily installed using pip with following command:
```
pip install jsonupdate-ng
```
Alternatively it can also be installed from the sourcecode:
```
python setup.py install
```

Major features
-----------------
### updateJson
this python function takes two arguments, base json and head json, and updates the base json based on the details provided in head.
#### Example
```
from jsonupdate_ng import jsonupdate_ng

updatedJson = jsonupdate_ng.updateJson(baseJson, headJson)
```

```
contents of base json

{
	"page": 1,
	"per_page": 6,
	"total": 12,
	"total_pages": 2,
	"data": [
		{
			"id": 1,
			"email": "george.bluth@reqres.in",
			"first_name": "George",
			"last_name": "Bluth",
			"avatar": "https://reqres.in/img/faces/1-image.jpg"
		},
		{
			"id": 2,
			"email": "janet.weaver@reqres.in",
			"first_name": "Janet",
			"last_name": "Weaver",
			"avatar": "https://reqres.in/img/faces/2-image.jpg"
		},
		{
			"id": 3,
			"email": "emma.wong@reqres.in",
			"first_name": "Emma",
			"last_name": "Wong",
			"avatar": "https://reqres.in/img/faces/3-image.jpg"
		},
		{
			"id": 4,
			"email": "eve.holt@reqres.in",
			"first_name": "Eve",
			"last_name": "Holt",
			"avatar": "https://reqres.in/img/faces/4-image.jpg"
		},
		{
			"id": 5,
			"email": "charles.morris@reqres.in",
			"first_name": "Charles",
			"last_name": "Morris",
			"avatar": "https://reqres.in/img/faces/5-image.jpg"
		},
		{
			"id": 6,
			"email": "tracey.ramos@reqres.in",
			"first_name": "Tracey",
			"last_name": "Ramos",
			"avatar": "https://reqres.in/img/faces/6-image.jpg"
		}
	]
}
```
```
contents of head json (comments are just to clarify the example, please remove them before trying it in your code)
{
    "name" : "users",                                       // this will add a name node at the root
    "per_page" : 12,                                        // this will update the per_page value
    "company" : { "name" : "anything", "office" : "anywhere" }, // this will add a new object at the root 
    "total_pages" : "<<<DELETE>>>",                             // this will delete total_pages node from the root
    "data" : [
        {
            "id": 100,                                          // this will update id of the first item in the data list
			"full_name": "deepak chourasia",                    // this will add a full_name node in the first item of the data list
        }
    ],
    "$.limit" : 6,                                              // this will add a limit node at the root
    "$.data[*].designation" : "developer",                      // this will add a designation node in all the objects inside data list
    "$.data[?(@.id > 3)].salary" : "$100,000",                    // this will add a salary node in all the objects inside data list which have id > 3
    "$.data[100]" : {                                            // this can be used to add/update an object at provided index in the data list, if index is greater than current length of the list then item will be added to the end of the list
			"id": 101,
			"email": "deepak.chourasia@gmail.com",
			"first_name": "Deepak",
			"last_name": "Chourasia"
    },
    "$.data[?(@.id > 4 & @.id < 10)].avatar" : "<<<DELETE>>>"                // this will delete avtar node from the object inside data list which has id > 4
}
```

### checkIfNodeExistsAtGivenJsonPath
this function checks if a node exists at given jsonpath in the provided json
#### Example
```
from jsonupdate_ng import jsonupdate_ng

exists = jsonupdate_ng.checkIfNodeExistsAtGivenJsonPath(baseJson, "$.data")
```
### Add_Update_Delete_Node_AtGivenJsonPath
this function can perform multiple tasks based on the situation:
* will add a node if it doesnt exist in base json
* will update the node value if node already exists in base json
* will delete the node if value is provided as <<<DELETE\>>>
```
from jsonupdate_ng import jsonupdate_ng

updatedJson = jsonupdate_ng.Add_Update_Delete_Node_AtGivenJsonPath(baseJson, "$.name", "Deepak Chourasia")
```
Contributions:
--------------
Creator and maintainer : [Deepak Chourasia](https://www.linkedin.com/in/deepak-chourasia-10767610/)

License
--------
JsonUpdate-NG is open source software provided under the [Apache License 2.0](http://apache.org/licenses/LICENSE-2.0)