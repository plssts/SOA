package com.soap.ws.jaxws;
import com.soap.ws.OutcomeAttendee;
import com.soap.ws.OutcomeSimple;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;

@XmlRootElement(name = "postAttendeesResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "postAttendeesResponse", namespace = "http://ws.soap.com/")
public class PostAttendeesResponse {
    @XmlElement(name = "return", namespace = "")
    private OutcomeSimple _return;

    public OutcomeSimple getReturn() {
        return this._return;
    }
    
    public void setReturn(OutcomeSimple _return) {
        this._return = _return;
    }
}
