package com.soap.ws;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
@XmlRootElement(name = "attendee", namespace = "http://ws.soap.com/")
@XmlType(name = "attendee", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
public class Attendee {
    @XmlElement(name = "firstName", namespace = "")
    public String firstName;
    @XmlElement(name = "lastName", namespace = "")
    public String lastName;
    @XmlElement(name = "email", namespace = "")
    public String email;
}
