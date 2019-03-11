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


### Visų narių sąrašas

`GET /members`


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


### Grąžinti tam tikrą narį

`GET /members/<phone>`


### Ištrinti narį

`DELETE /members/<phone>`

