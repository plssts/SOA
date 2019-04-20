# General

RESTful conference data manager utilising external [user service](https://github.com/Martis467/WebServices/tree/master/Antras "Original documentation").

## Launch services

Clone this repository with ```git clone https://github.com/plssts/SOA```.

Navigate to ```SOA/2``` and execute ```./init.sh```. This will build and link all needed services. You might need to provide necessary permissions to execute the file with ```chmod +x init.sh```.

It is recommended to execute ```./cleanup.sh``` (again, make this file executable with ```chmod +x cleanup.sh``` if needed) after finishing using the service. This will stop running services, remove the dedicated network bridge and clean images.

# Working with members

## Show all members

GET /members

Status ```200``` on successfully fetching members.

Response:
```
{
    "message": "Success",
    "data": [
        {
            "firstName": "Name",
            "lastName": "Last name",
            "email": "sample@gmail.com"
        },
        {
            "firstName": "Seras",
            "lastName": "Meras",
            "email": "sir.mayor@gmail.com"
        },
        {
            "firstName": "Test",
            "lastName": "Guy",
            "email": "nomail@gmail.com"
        }
    ]
}
```
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
        "firstName": "New",
        "lastName": "Member",
        "email": "demo@gmail.com"
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

## Show a specific member

GET /members/{email}
  
Status ```200``` if there is a member with the specified email.
Response:
```
{
    "message": "User",
    "data": {
        "firstName": "Test",
        "lastName": "Guy",
        "email": "nomail@gmail.com"
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

# Working with conferences

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

# Create a new conference

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

# Show a specific conference

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

# Edit a specific conference

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

EDITING HERE AT THE MOMENT

Requesting edits for an unused email returns:
```
{
    "message": "User not found",
    "data": {}
}
```
with status ```404```.
