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
