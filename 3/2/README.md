# General

RESTful conference data manager utilising external [user service](https://github.com/Martis467/WebServices/tree/master/Pirmas "Original documentation").

Jump to:

[Working with conferences](#wwc):
- <sub> [Show all conferences](#wwc1)</sub>
- <sub> [Create a new conference](#wwc2)</sub>
- <sub> [Show a specific conference](#wwc3)</sub>
- <sub> [Edit a specific conference](#wwc4)</sub>
- <sub> [Delete a specific conference](#wwc5)</sub>

[Working with conference attendees](#wwca):
- <sub> [Show all attendees under a conference](#wwca1)</sub>
- <sub> [Assign a new attendee to a conference](#wwca2)</sub>
- <sub> [Show a specific attendee](#wwca3)</sub>
- <sub> [Edit a specific attendee](#wwca4)</sub>
- <sub> [Delete a specific attendee](#wwca5)</sub>

# Launch services

Clone this repository with ```git clone https://github.com/plssts/SOA```.

Navigate to ```SOA/2``` and execute ```docker-compose up --build```.

It is recommended to execute ```./cleanup.sh``` (make this file executable with ```chmod +x cleanup.sh``` if needed) after finishing using the service. This will stop running services, remove the containers and clean images.

<a name="wwc"></a>
# Working with conferences
<a name="wwc1"></a>
## Show all conferences

GET /conferences

Response:

```
{
    "message": "Conferences",
    "data": [
        {
            "title": "NYSE Securities Operators Annual",
            "info": "Register through [website] with your corporate email",
            "date": "20-04-20",
            "cid": "1",
            "attendees": [
                "td@mail.com",
                "larry@mail.com"
            ]
        },
        {
            "title": "China Global Trading",
            "info": "Information here",
            "date": "TBD",
            "cid": "2",
            "attendees": [
                "larry@mail.com",
                "hyron@mail.com"
            ]
        }
    ]
}
```

while requesting  ```/conferences?embedded=attendees``` gives:

```
{
    "message": "Conferences",
    "data": [
        {
            "title": "NYSE Securities Operators Annual",
            "info": "Register through [website] with your corporate email",
            "date": "20-04-20",
            "cid": "1",
            "attendees": [
                {
                    "firstName": "Thomas",
                    "lastName": "Danforth",
                    "email": "td@mail.com"
                },
                {
                    "firstName": "Larry",
                    "lastName": "Simmons",
                    "email": "larry@mail.com"
                }
            ]
        },
        {
            "title": "China Global Trading",
            "info": "Information here",
            "date": "TBD",
            "cid": "2",
            "attendees": [
                {
                    "firstName": "Larry",
                    "lastName": "Simmons",
                    "email": "larry@mail.com"
                },
                {
                    "firstName": "Penelope",
                    "lastName": "Hyron",
                    "email": "hyron@mail.com"
                }
            ]
        }
    ]
}
```

with status ```200```.
<a name="wwc2"></a>
## Create a new conference

POST /conferences

Arguments:
- title: string
- info: string
- date: string

Responds with the new resource and its fields:

```
{
    "message": "New conference created",
    "data": {
        "title": "California Firefighters",
        "info": "Register through [website] with your corporate email",
        "date": "21-04-19",
        "cid": "3"
    }
}
```

with status ```201```. Conference IDs are managed automatically.
<a name="wwc3"></a>
## Show a specific conference

GET /conferences/{cid}

Status ```200``` if there is a conference with the specified cid.
Response:

```
{
    "message": "Conference",
    "data": {
        "title": "NYSE Global",
        "info": "Securities operators welcome",
        "date": "20/01/20",
        "cid": "1"
    }
}
```

It is also possible to request ```/conferences/1?embedded=attendees```and get:
```
{
    "message": "Conference",
    "data": {
        "title": "NYSE Securities Operators Annual",
        "info": "Register through [website] with your corporate email",
        "date": "20-04-20",
        "cid": "1",
        "attendees": [
            {
                "firstName": "Thomas",
                "lastName": "Danforth",
                "email": "td@mail.com"
            },
            {
                "firstName": "Larry",
                "lastName": "Simmons",
                "email": "larry@mail.com"
            }
        ]
    }
}
```

Requesting with incorrect cid returns

```
{
    "message": "No such conference",
    "data": {}
}
```

with status ```404```.
<a name="wwc4"></a>
## Edit a specific conference

PUT /conferences/{cid}

Arguments:
- title: string
- info: string
- date: string

Successful changes return status ```200```.
Response includes the new fields:

```
{
    "message": "Conference updated",
    "data": {
        "title": "China International Trading - day 5",
        "info": "Tickets available for a limited time only!",
        "date": "04/01/20",
        "cid": "2"
    }
}
```

Trying to edit a nonexistent conference returns

```
{
    "message": "No such conference",
    "data": {}
}
```

with status ```404```.
<a name="wwc5"></a>
## Delete a specific conference

DELETE /conferences/{cid}

Status ```200``` is returned after the conference is deleted. All members under the conference are deleted as well. Response includes the cid:

```
{
    "message": "Conference removed",
    "data": "1"
}
```

Specifying a nonexistent cid returns:

```
{
    "message": "No such conference",
    "data": {}
}
```

with status ```404```.

<a name="wwca"></a>
# Working with conference attendees
<a name="wwca1"></a>
## Show all attendees under a conference

GET /conferences/{cid}/attendees

Status ```200``` is returned along with a list of attendees:

```
{
    "message": "Attendees",
    "data": {
        "td@mail.com": {
            "firstName": "Thomas",
            "lastName": "Danforth",
            "email": "td@mail.com"
        },
        "larry@mail.com": {
            "firstName": "Larry",
            "lastName": "Simmons",
            "email": "larry@mail.com"
        }
    }
}
```

When there are no attendees at the time, the response shows

```
{
    "message": "No attendees",
    "data": {}
}
```

with status ```404```.
<a name="wwca2"></a>
## Assign a new attendee to a conference

POST /conferences/{cid}/attendees

Arguments:
- firstName: string
- lastName: string
- email: string

Response includes the new attendee:

```
{
    "message": "Attendee created",
    "data": {
        "firstName": "Penelope",
        "lastName": "Hyron",
        "email": "hyron@mail.com"
    }
}
```

with status ```201``` on success.

Status ```409``` is returned if there is an attempt to include an existing attendee. Response:

```
{
    "message": "Email Already Exists",
    "data": {}
}
```

<a name="wwca3"></a>
## Show a specific attendee
GET /conference/{cid}/attendees/{email}
  
Status ```200``` if there is a member with the specified email.
Response:

```
{
    "message": "Attendee",
    "data": {
        "firstName": "Penelope",
        "lastName": "Hyron",
        "email": "hyron@mail.com"
    }
}
```

Status ```404``` is returned if the email was nonexistent.
Response:

```
{
    "message": "Attendee not found",
    "data": {}
}
```
<a name="wwca4"></a>
## Edit a specific attendee

PUT /conferences/{cid}/attendees/{email}

Arguments:
- firstName: string       
- lastName: string
- email: string

Successful changes return status ```202```.
Response includes the new fields:

```
{
    "message": "Attendee updated successfully",
    "data": {
        "firstName": "newname",
        "lastName": "newlastname",
        "email": "newmail@gmail.com"
    }
}
```

Trying to specify a new email when it is already used returns:

```
{
    "message": "Email Already Exists",
    "data": {}
}
```

with status ```409```.
Requesting edits for an unused email returns:

```
{
    "message": "Attendee not found",
    "data": {}
}
```

with status ```404```.

PATCH /conferences/{cid}/attendees/{email}

Arguments (optional):
- firstName: string       
- lastName: string
- email: string


Responds in a similar way as with the PUT requests. However, do not include the email field if you do not wish to modify it. Otherwise it triggers status ```409``` with

```
{
    "message": "Email Already Exists",
    "data": {}
}
```
<a name="wwca5"></a>
## Delete a specific attendee

DELETE /conferences/{cid}/attendees/{email}

Status ```204``` is returned after the member is deleted. There is no data included with this response.

Specifying a nonexistent email returns:

```
{
    "message": "Attendee not found",
    "data": {}
}
```

with status ```404```.
