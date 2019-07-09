Launch with ```docker-compose up --build -d```

WSDL:

GET /conferences?wsdl

## Conferences

**List all conferences**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:getConferences xmlns:ns2="http://ws.soap.com/">
        </ns2:getConferences>
    </S:Body>
</S:Envelope>
```

**List all conferences with full attendee info**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:getConferencesEMB xmlns:ns2="http://ws.soap.com/">
        </ns2:getConferencesEMB>
    </S:Body>
</S:Envelope>
```

**List a specific conference**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:getConference xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        </ns2:getConference>
    </S:Body>
</S:Envelope>
```

**List a specific conference with full attendee info**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:getConferenceEMB xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        </ns2:getConferenceEMB>
    </S:Body>
</S:Envelope>
```

**Create a new conference**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:postConference xmlns:ns2="http://ws.soap.com/">
        	<title>conference_title</title>
        	<info>conference_info</info>
        	<date>conference_date</date>
        </ns2:postConference>
    </S:Body>
</S:Envelope>
```

**Edit an existing conference**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:putConference xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        	<title>new_title</title>
        	<info>new_info</info>
        	<date>new_date</date>
        </ns2:putConference>
    </S:Body>
</S:Envelope>
```

**Remove a conference**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:deleteConference xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        </ns2:deleteConference>
    </S:Body>
</S:Envelope>
```

## Attendees

**List all attendees under a conference**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:getConferenceAttendees xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        </ns2:getConferenceAttendees>
    </S:Body>
</S:Envelope>
```

**List a specific attendee under a conference**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:getConferenceAttendee xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        	<email>some_mail</email>
        </ns2:getConferenceAttendee>
    </S:Body>
</S:Envelope>
```

**Add a new attendee**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:postAttendee xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        	<firstName>some_fn</firstName>
        	<lastName>some_ln</lastName>
        	<email>some_mail</email>
        </ns2:postAttendee>
    </S:Body>
</S:Envelope>
```

**Edit an attendee**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:putAttendee xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        	<firstName>some_fn</firstName>
        	<lastName>some_ln</lastName>
        	<email>old_mail</email>
        	optional - <newEmail>new_mail</newEmail>
        </ns2:putAttendee>
    </S:Body>
</S:Envelope>
```

**Remove an attendee**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:deleteAttendee xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        	<email>mail</email>
        </ns2:deleteAttendee>
    </S:Body>
</S:Envelope>
```

**Add several attendees simultaneously**:

POST body:
```
<?xml version="1.0" ?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:postAttendees xmlns:ns2="http://ws.soap.com/">
        	<cid>1</cid>
        	<all>
        		<attendee>
        			<firstName>some_fn</firstName>
        			<lastName>some_ln</lastName>
        			<email>email1</email>
        		</attendee>
        		<attendee>
        			<firstName>some_fn</firstName>
        			<lastName>some_ln</lastName>
        			<email>email2</email>
        		</attendee>
        	</all>
        </ns2:postAttendees>
    </S:Body>
</S:Envelope>
```
