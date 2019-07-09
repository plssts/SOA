package com.soap.ws.jaxws;
import com.soap.ws.Conference;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement(name = "getConferenceResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getConferenceResponse", namespace = "http://ws.soap.com/")
public class GetConferenceResponse {
    @XmlElement(name = "return", namespace = "")
    private Conference _return;
    
    public Conference getReturn() {
        return this._return;
    }
    
    public void setReturn(Conference _return) {
        this._return = _return;
    }
}
