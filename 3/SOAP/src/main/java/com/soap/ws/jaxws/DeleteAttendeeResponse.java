/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws.jaxws;
import com.soap.ws.OutcomeAttendee;
import com.soap.ws.OutcomeConference;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
/**
 *
 * @author LAPTOPELIS
 */
@XmlRootElement(name = "deleteAttendeeResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "deleteAttendeeResponse", namespace = "http://ws.soap.com/")
public class DeleteAttendeeResponse {
    @XmlElement(name = "return", namespace = "")
    private OutcomeAttendee _return;
    public OutcomeAttendee getReturn() {
        return this._return;
    }

    public void setReturn(OutcomeAttendee _return) {
        this._return = _return;
    }
}
