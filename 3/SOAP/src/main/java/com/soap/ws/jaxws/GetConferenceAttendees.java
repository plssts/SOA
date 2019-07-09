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

@XmlRootElement(name = "getConferenceAttendees", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "getConferenceAttendees", namespace = "http://ws.soap.com/")
public class GetConferenceAttendees {
    @XmlElement(required = true, name = "cid", namespace = "")
    private Integer cid;

    public Integer getCid(){
        return this.cid;
    }

    public void setCid(Integer cid){
        this.cid = cid;
    }
}
