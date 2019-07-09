package com.soap.ws.jaxws;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement(name = "postAttendee", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "postAttendee", namespace = "http://ws.soap.com/")
public class PostAttendee {
    @XmlElement(required = true, name = "firstName", namespace = "")
    private String firstName;
    @XmlElement(required = true, name = "lastName", namespace = "")
    private String lastName;
    @XmlElement(required = true, name = "email", namespace = "")
    private String email;
    @XmlElement(required = true, name = "cid", namespace = "")
    private Integer cid;
    
    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String lastName) {
        this.firstName = lastName;
    }
    
    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    
    public Integer getCid() {
        return cid;
    }

    public void setCid(Integer cid) {
        this.cid = cid;
    }
}
