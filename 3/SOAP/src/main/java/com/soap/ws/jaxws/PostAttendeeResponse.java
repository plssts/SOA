package com.soap.ws.jaxws;
import com.soap.ws.OutcomeAttendee;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement(name = "postAttendeeResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "postAttendeeResponse", namespace = "http://ws.soap.com/")
public class PostAttendeeResponse {
    @XmlElement(name = "return", namespace = "")
    private OutcomeAttendee _return;

    public OutcomeAttendee getReturn() {
        return this._return;
    }
    
    public void setReturn(OutcomeAttendee _return) {
        this._return = _return;
    }
}
