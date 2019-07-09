/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws.jaxws;
import com.soap.ws.Attendee;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement(name = "getConferenceAttendeesResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getConferenceAttendeesResponse", namespace = "http://ws.soap.com/")
public class GetConferenceAttendeesResponse {
    @XmlElement(name = "return", namespace = "")
    private Attendee[] _return;

    public Attendee[] getReturn() {
        return this._return;
    }
    
    public void setReturn(Attendee[] _return) {
        this._return = _return;
    }
}
