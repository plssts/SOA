/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws.jaxws;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
import java.util.List;
import com.soap.ws.ConferenceEMB;

@XmlRootElement(name = "getConferencesEMBResponse", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getConferencesEMBResponse", namespace = "http://ws.soap.com/")
public class GetConferencesEMBResponse {
    @XmlElement(name = "return", namespace = "")
    private ConferenceEMB[] _return;

    public ConferenceEMB[] getReturn() {
        return this._return;
    }
}
