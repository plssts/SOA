/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class Conference {
    public String title;
    public String info;
    public String date;
    public int cid;
    //public Attendee[] attendees;
    public String[] attendees;
}
