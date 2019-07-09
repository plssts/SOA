package com.soap.ws.jaxws;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
import com.soap.ws.Attendee;

@XmlRootElement(name = "getConferenceAttendeeResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getConferenceAttendeeResponse", namespace = "http://ws.soap.com/")
public class GetConferenceAttendeeResponse {
    @XmlElement(name = "return", namespace = "")
    private Attendee _return;

    public Attendee getReturn() {
        return this._return;
    }

    public void setReturn(Attendee _return) {
        this._return = _return;
    }
}
