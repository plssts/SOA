# General

RESTful conference data manager utilising external [user service](https://github.com/Martis467/WebServices/tree/master/Antras "Original documentation").

Jump to:

[Working with members](#wwm):
- <sub> [Show all members](#wwm1)</sub>
- <sub> [Create a new member](#wwm2)</sub>
- <sub> [Show a specific member](#wwm3)</sub>
- <sub> [Edit a specific member](#wwm4)</sub>
- <sub> [Delete a specific member](#wwm5)</sub>

[Working with conferences](#wwc):
- <sub> [Show all conferences](#wwc1)</sub>
- <sub> [Create a new conference](#wwc2)</sub>
- <sub> [Show a specific conference](#wwc3)</sub>
- <sub> [Edit a specific conference](#wwc4)</sub>
- <sub> [Delete a specific conference](#wwc5)</sub>

[Working with conference attendees](#wwca):
- <sub> [Show all attendees](#wwca1)</sub>
- <sub> [Assign a new attendee](#wwca2)</sub>
- <sub> [Remove an attendee](#wwca3)</sub>

## Launch services

Clone this repository with ```git clone https://github.com/plssts/SOA```.

Navigate to ```SOA/2``` and execute ```./init.sh```. This will build and link all needed services. You might need to provide necessary permissions to execute the file with ```chmod +x init.sh```.

It is recommended to execute ```./cleanup.sh``` (again, make this file executable with ```chmod +x cleanup.sh``` if needed) after finishing using the service. This will stop running services, remove the dedicated network bridge and clean images.

<a name="wwm"></a>
# Working with members
<a name="wwm1"></a>
## Show all members

GET /members

Status ```200``` on successfully fetching members.

Response:

```
{
    "message": "Success",
    "data": [
        {
            "firstName": "Declan",
            "lastName": "Faherty",
            "email": "d.faherty@gmail.com"
        },
        {
            "firstName": "Arie",
            "lastName": "van Bruggen",
            "email": "windmill@gmail.com"
        },
        {
            "firstName": "Greg",
            "lastName": "Thorpe",
            "email": "oldguy@gmail.com"
        }
    ]
}
```
<a name="wwm2"></a>
## Create a new member

POST /members

Arguments:
- firstName: string       
- lastName: string
- email: string (unique)

Status ```201``` on success.
Response includes the new user with its fields:

```
{
    "message": "User created",
    "data": {
        "firstName": "Mr",
        "lastName": "Darrow",
        "email": "theranch@gmail.com"
    }
}
```

Creating a new member with an existing email returns

```
{
    "message": "Email Already Exists",
    "data": {}
}
```

with status ```409```.
<a name="wwm3"></a>
## Show a specific member

GET /members/{email}
  
Status ```200``` if there is a member with the specified email.
Response:

```
{
    "message": "User",
    "data": {
        "firstName": "Greg",
        "lastName": "Thorpe",
        "email": "oldguy@gmail.com"
    }
}
```

Status ```404``` is returned if the email was nonexistent.
Response:

```
{
    "message": "User not found",
    "data": {}
}
```
<a name="wwm4"></a>
## Edit a specific member

PUT /members/{email}

Arguments:
- firstName: string       
- lastName: string
- email: string (unique)

Successful changes return status ```202```.
Response includes the new fields:

```
{
    "message": "User updated successfully",
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
    "message": "User not found",
    "data": {}
}
```

with status ```404```.

PATCH /members/{email}

Arguments (optional):
- firstName: string       
- lastName: string
- email: string (unique)


Responds in a similar way as with the PUT requests. However, do not include the email field if you do not wish to modify it. Otherwise it triggers status ```409``` with

```
{
    "message": "Email Already Exists",
    "data": {}
}
```
<a name="wwm5"></a>
## Delete a specific member

DELETE /members/{email}

Status ```204``` is returned after the member is deleted. There is no data included with this response.

Specifying a nonexistent email returns:

```
{
    "message": "User not found",
    "data": {}
}
```

with status ```404```.
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
            "title": "NYSE Global",
            "info": "Securities operators welcome",
            "date": "20/01/20",
            "cid": "1"
        },
        {
            "title": "China International Trading",
            "info": "tickets unavailable",
            "date": "30/12/19",
            "cid": "2"
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

Status ```200``` is returned after the conference is deleted. Response includes the cid:

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
## Show all attendees

GET /conferences/{cid}/attendees

Status ```200``` is returned along with a list of attendees:

```
{
    "message": "Conference",
    "data": {
        "cid": "3",
        "attendees": [
            "panchaea@gmail.com",
            "newguy@gmail.com"
        ]
    }
}
```

When there are no attendees at the time, the response shows

```
{
    "message": "No members as of yet",
    "data": {}
}
```

with status ```404```.
<a name="wwca2"></a>
## Assign a new attendee

POST /conferences/{cid}/attendees

Arguments:
- email: string

Response includes the new attendee:

```
{
    "message": "New attendee added",
    "data": "bob.page@gmail.com"
}
```

with status ```201``` on success.

Trying to add someone who is not listed under members returns

```
{
    "message": "No such member",
    "data": "invalid@mail.com"
}
```

with status ```404```.

Status ```409``` is returned if there is an attempt to include an existing attendee. Response:

```
{
    "message": "This member is already participating",
    "data": "newguy@gmail.com"
}
```
<a name="wwca3"></a>
## Remove an attendee

DELETE /conferences/{cid}/attendees

Arguments:
- email: string

Status ```200``` on successful removal. Response:

```
{
    "message": "Attendee removed",
    "data": "haas@gmail.com"
}
```

Trying to remove someone who is already not attending a conference produces a response:

```
{
    "message": "No such member",
    "data": "hyron@gmail.com"
}
```

with status ```404```.
Trying to remove someone when there are no attendees at all gives status ```404``` with

```
{
    "message": "No members anyway",
    "data": {}
}
```
