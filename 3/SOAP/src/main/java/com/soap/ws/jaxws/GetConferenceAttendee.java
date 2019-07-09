package com.soap.ws.jaxws;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement(name = "getConferenceAttendee", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getConferenceAttendee", namespace = "http://ws.soap.com/")
public class GetConferenceAttendee {
    @XmlElement(required = true, name = "cid", namespace = "")
    private Integer cid;
    @XmlElement(required = true, name = "email", namespace = "")
    private String email;

    public Integer getCid() {
        return this.cid;
    }

    public void setCid(Integer cid) {
        this.cid = cid;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
