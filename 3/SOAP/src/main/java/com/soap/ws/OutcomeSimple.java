/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws;

public class OutcomeSimple {
    public String message;
    
    public OutcomeSimple(){
        message = " ";
    }
    public OutcomeSimple(String msg){
        message = msg;
    }
    
    public void cat(String msg){
        message += msg;
    }
}
