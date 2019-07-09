package com.soap.ws.jaxws;
import com.soap.ws.OutcomeConference;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement(name = "deleteConferenceResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "deleteConferenceResponse", namespace = "http://ws.soap.com/")
public class DeleteConferenceResponse {
    @XmlElement(name = "return", namespace = "")
    private OutcomeConference _return;
    public OutcomeConference getReturn() {
        return this._return;
    }

    public void setReturn(OutcomeConference _return) {
        this._return = _return;
    }
}
