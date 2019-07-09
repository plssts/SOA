/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws;

public class OutcomeAttendee {
    public String message;
    public Attendee data;
    
    public OutcomeAttendee(){}
    public OutcomeAttendee(String msg){
        message = msg;
    }
}
