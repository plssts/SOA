# Sporto klubo narių registras
```cd .. && sudo rm -r ws_1 && git clone https://git.mif.vu.lt/krsi3832/ws_1 && cd ws_1 && sudo docker-compose up --build```
## WS Įrašymas, paleidimas ir ištrynimas

WS failų atsisiuntimas - <br />
```git clone https://git.mif.vu.lt/krsi3832/ws_1```

WS subuildinimas -<br />
```cd ws_1```<br />
```docker-compose up --build```  

WS ištrynimas -<br />
```cd ..```<br />
```rm -r ws_1```

## Naudojimas

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### Visų narių sąrašas


`GET /members`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "floor-lamp",
        "name": "Floor Lamp",
        "device_type": "switch",
        "controller_gateway": "192.1.68.0.2"
    },
    {
        "identifier": "samsung-tv",
        "name": "Living Room TV",
        "device_type": "tv",
        "controller_gateway": "192.168.0.9"
    }
]
```

### Nario registracija


`POST /members`

**Argumentai**

- `"name":string` vardas
- `"fname":string`pavardė
- `"phone":string` telefono numeris(unikalus įrašas)
- `"membership_exp":string` iki kada galioja narystė

**Užklausos pavyzdys per Postman (naudoti JSON(application/json)**

```{"name":"Kristupas","fname":"Simoncikas","phone":"37062192000","membership_exp":"22/12/19"}```

Jei toks narys jau egzistuoja(pagal telefono numerį), tai senas įrašas bus pakeistas nauju

**Response**

- `201 Created` on success

```json
{
    "identifier": "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"
}
```

## Lookup device details

`GET /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
    "identifier": "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"
}
```

## Ištrinti narį

`DELETE /members/<phone>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success
