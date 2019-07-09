/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws.jaxws;

import com.soap.ws.Attendee;
import java.util.List;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElementWrapper;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


@XmlRootElement(name = "postAttendees", namespace = "http://ws.soap.com/")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "postAttendees", namespace = "http://ws.soap.com/")
public class PostAttendees {
    @XmlElementWrapper
    @XmlElement(required = true, name = "attendee", namespace = "")
    private Attendee[] all;
    
    @XmlElement(required = true, name = "cid", namespace = "")
    private Integer cid;
    
    public Integer getCid() {
        return cid;
    }

    public void setCid(Integer cid) {
        this.cid = cid;
    }
    
    /*public List<Attendee> getAll() {
        return all;
    }*/

    public void setAll(Attendee[] all) {
        this.all = all;
    }
    
    //@XmlElementWrapper
    //@XmlElement(name="attendee")
    public Attendee[] getAll() {
        return all;
    }
}
