package com.soap.ws.jaxws;
import com.soap.ws.OutcomeConference;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement(name = "putConferenceResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "putConferenceResponse", namespace = "http://ws.soap.com/")
public class PutConferenceResponse {
    @XmlElement(name = "return", namespace = "")
    private OutcomeConference _return;

    public OutcomeConference getReturn() {
        return this._return;
    }
    public void setReturn(OutcomeConference _return) {
        this._return = _return;
    }
}
