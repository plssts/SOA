package com.soap.ws;
import javax.xml.bind.annotation.XmlRootElement;
@XmlRootElement
public class ConferenceEMB {
    public String title;
    public String info;
    public String date;
    public int cid;
    public Attendee[] attendees;
}
