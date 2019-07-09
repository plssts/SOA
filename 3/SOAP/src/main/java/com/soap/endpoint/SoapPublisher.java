/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.endpoint;
import javax.xml.ws.Endpoint;
import com.soap.ws.SoapImpl;

public class SoapPublisher {
    public static void main(String[] args) {
	Endpoint.publish("http://0.0.0.0:5006/conferences", new SoapImpl());
    }
}
