/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import com.fasterxml.jackson.databind.ObjectMapper;

public class EnvelopeConverter {
    public static String conJSON(HttpURLConnection con) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((con.getInputStream())));
        String output = "";
        String temp;
        while ((temp = br.readLine()) != null) {
            output += temp;
        }
        br.close();
        return output;
    }
    
    public static OutcomeConference jsonToOutcomeConference(String json) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        OutcomeConference o = null;
        o = mapper.readValue(json, OutcomeConference.class);
        return o;
    }
    
    public static OutcomeAttendee jsonToOutcomeAttendee(String json) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        OutcomeAttendee o = null;
        o = mapper.readValue(json, OutcomeAttendee.class);
        return o;
    }
    
    public static Conference[] jsonToConferences(String json) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        Conference[] conf = null;
        
        System.out.println("json is: \n" + json);
        
        int start = json.indexOf("[");
        
        // POTENTIAL CRASHING POINT HERE?
        
        json = json.substring(start, json.length());
        conf = mapper.readValue(json, Conference[].class);
        System.out.println("Collected " + conf.length + " conferences.");
        return conf;
    }
    
    public static ConferenceEMB[] jsonToConferencesEMB(String json) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        ConferenceEMB[] conf = null;
        
        System.out.println("json is: \n" + json);
        
        int start = json.indexOf("\"data\":") + 7;
        json = json.substring(start, json.length());
        conf = mapper.readValue(json, ConferenceEMB[].class);
        System.out.println("Collected " + conf.length + " conferences.");
        return conf;
    }
    
    public static ConferenceEMB jsonToConferenceEMB(String json, Integer cid) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        ConferenceEMB conf = null;
        
        System.out.println("json is: \n" + json);
        
        int start = json.indexOf("{", 2);
        json = json.substring(start, json.length());
        conf = mapper.readValue(json, ConferenceEMB.class);
        //System.out.println("Collected " + conf.length + " conferences.");
        return conf;
    }
    
    public static Conference jsonToConference(String json, Integer cid) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        Conference conf = null;
        int start = json.indexOf("{", 2);
        json = json.substring(start, json.length());
        conf = mapper.readValue(json, Conference.class);
        conf.cid = cid;
        return conf;
    }
    
    public static Attendee jsonToConferenceAttendee(String json) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        Attendee at = null;
        int start = json.indexOf("{", 2);
        json = json.substring(start, json.length());
        at = mapper.readValue(json, Attendee.class);
        return at;
    }
    
    public static Attendee[] jsonToConferenceAttendees(String json, Integer cid) throws IOException
    {
        ObjectMapper mapper = new ObjectMapper();
        Attendee[] att = null;
        String normalised = "[";
        int start = json.indexOf("{", 2);
        json = json.substring(start, json.length());
        int previousAttendee = 0;
        int nextAttendee = 0;
        while(true){
            previousAttendee = json.indexOf(":") + 1;
            if (previousAttendee == 0){
                break;
            }
            nextAttendee = json.indexOf("}") + 1;
            System.out.println("Found member: " + json.substring(previousAttendee, nextAttendee));
            normalised += json.substring(previousAttendee, nextAttendee) + ",";
            if (nextAttendee == 0){
                break;
            }
            json = json.substring(nextAttendee, json.length());
        }
        if (normalised.endsWith(",")){
            normalised = normalised.substring(0, normalised.length() - 1);
        }
        normalised += "]";
        att = mapper.readValue(normalised, Attendee[].class);
        return att;
    }
}
