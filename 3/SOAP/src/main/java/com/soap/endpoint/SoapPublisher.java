package com.soap.endpoint;
import javax.xml.ws.Endpoint;
import com.soap.ws.SoapImpl;

public class SoapPublisher {
    public static void main(String[] args) {
	Endpoint.publish("http://0.0.0.0:5006/conferences", new SoapImpl());
    }
}
