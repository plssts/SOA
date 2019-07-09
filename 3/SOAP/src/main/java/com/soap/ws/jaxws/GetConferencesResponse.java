package com.soap.ws.jaxws;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
import java.util.List;
import com.soap.ws.Conference;

@XmlRootElement(name = "getConferencesResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getConferencesResponse", namespace = "http://ws.soap.com/")
public class GetConferencesResponse {
    @XmlElement(name = "return", namespace = "")
    private Conference[] _return;

    public Conference[] getReturn() {
        return this._return;
    }
}
