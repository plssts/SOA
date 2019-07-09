package com.soap.ws;
import javax.jws.WebService;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.List;

@WebService(endpointInterface = "com.soap.ws.Soap")
public class SoapImpl implements Soap {
    @Override
    public Conference[] getConferences() {
        Conference[] conf = null;
        HttpURLConnection con = null;
        try {
            URL url = new URL("http://base:5008/conferences");
            con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");
            
            if (con.getResponseCode() != 200) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            
            String json = EnvelopeConverter.conJSON(con);
            conf = EnvelopeConverter.jsonToConferences(json);
            con.disconnect();
        } catch (ProtocolException e) {
            con.disconnect();
        } catch (IOException e) {
            con.disconnect();
        }
        return conf;
    }
    
    @Override
    public ConferenceEMB[] getConferencesEMB() {
        ConferenceEMB[] conf = null;
        HttpURLConnection con = null;
        try {
            URL url = new URL("http://base:5008/conferences?embedded=attendees");
            con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");
            
            if (con.getResponseCode() != 200) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            
            String json = EnvelopeConverter.conJSON(con);
            conf = EnvelopeConverter.jsonToConferencesEMB(json);
            con.disconnect();
        } catch (ProtocolException e) {
            con.disconnect();
        } catch (IOException e) {
            con.disconnect();
        }
        return conf;
    }
    
    @Override
    public Conference getConference(Integer cid) {
        Conference conf = null;
        HttpURLConnection con = null;
        
        if (cid == null) {
            throw new RuntimeException("No conference CID specified");
        }
        
        try {
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid));
            con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            String json = EnvelopeConverter.conJSON(con);
            conf = EnvelopeConverter.jsonToConference(json, cid);
            con.disconnect();
        } catch (ProtocolException e) {
            con.disconnect();
        } catch (IOException e) {
            con.disconnect();
        }
        return conf;
    }
    
    @Override
    public ConferenceEMB getConferenceEMB(Integer cid) {
        ConferenceEMB conf = null;
        HttpURLConnection con = null;
        
        if (cid == null) {
            throw new RuntimeException("No conference CID specified");
        }
        
        try {
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid) + "?embedded=attendees");
            con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            String json = EnvelopeConverter.conJSON(con);
            conf = EnvelopeConverter.jsonToConferenceEMB(json, cid);
            con.disconnect();
        } catch (ProtocolException e) {
            con.disconnect();
        } catch (IOException e) {
            con.disconnect();
        }
        return conf;
    }
    
    @Override
    public Attendee[] getConferenceAttendees(Integer cid) {
        Attendee[] att = null;
        HttpURLConnection con = null;
        
        if (cid == null) {
            throw new RuntimeException("No CID specified");
        }
        
        try {
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid) + "/attendees");
            con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            String json = EnvelopeConverter.conJSON(con);
            att = EnvelopeConverter.jsonToConferenceAttendees(json, cid);
            con.disconnect();
        } catch (ProtocolException e) {
            con.disconnect();
        } catch (IOException e) {
            con.disconnect();
        }
        return att;
    }
    
    @Override
    public OutcomeConference postConference(String title, String info, String date){
        OutcomeConference outcome = null;
        try {
            String newobj = "{";
            if (title != null){
                newobj += "\"title\": \"" + title + "\",";
            }
            if (info != null){
                newobj += "\"info\": \"" + info + "\",";
            }
            if (date != null){
                newobj += "\"date\": \"" + date + "\",";
            } 

            if (newobj.endsWith(",")){
                newobj = newobj.substring(0, newobj.length() - 1);
            }
            newobj += "}";
            
            URL url = new URL("http://base:5008/conferences");
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setDoOutput(true);
            con.setRequestMethod("POST");
            con.setRequestProperty("Accept", "application/json");
            con.setRequestProperty("Content-Type", "application/json");
            OutputStreamWriter out = new OutputStreamWriter(con.getOutputStream());
            System.out.println(newobj);
            out.write(newobj);
            out.close();

            String json = EnvelopeConverter.conJSON(con);
            outcome = EnvelopeConverter.jsonToOutcomeConference(json);
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            con.disconnect();
        } catch (ProtocolException e) {
            outcome = new OutcomeConference();
        } catch (IOException e) {
            outcome = new OutcomeConference();
        }
        return outcome;
    }
    
    @Override
    public OutcomeConference putConference(Integer cid, String title, String info, String date){
        OutcomeConference outcome = null;
        if (cid == null) {
            throw new RuntimeException("No conference CID");
        }
        try {
            String newobj = "{";
            if (title != null){
                newobj += "\"title\": \"" + title + "\",";
            }

            if (info != null){
                newobj += "\"info\": \"" + info + "\",";
            }
            
            if (date != null){
                newobj += "\"date\": \"" + date + "\",";
            }

            if (newobj.endsWith(",")){
                newobj = newobj.substring(0, newobj.length() - 1);
            }
            
            newobj += "}";
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid));
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setDoOutput(true);
            con.setRequestMethod("PUT");
            con.setRequestProperty("Accept", "application/json");
            con.setRequestProperty("Content-Type", "application/json");
            OutputStreamWriter out = new OutputStreamWriter(con.getOutputStream());
            out.write(newobj);
            out.close();

            String json = EnvelopeConverter.conJSON(con);
            outcome = EnvelopeConverter.jsonToOutcomeConference(json);
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            con.disconnect();
        } catch (ProtocolException e) {
            outcome = new OutcomeConference();
        } catch (IOException e) {
            outcome = new OutcomeConference();
        }
        return outcome;
    }
    
    @Override
    public OutcomeAttendee postAttendee(Integer cid, String firstName, String lastName, String email){
        OutcomeAttendee outcome = null;
        if (cid == null || email == null) {
            throw new RuntimeException("No conference CID or attendee email");
        }
        try {
            String newobj = "{";
            if (firstName != null)
                newobj += "\"firstName\": \"" + firstName + "\",";

            if (lastName != null)
                newobj += "\"lastName\": \"" + lastName + "\",";

            if (email != null)
                newobj += "\"email\": \"" + email + "\",";

            if (newobj.endsWith(",")){
                newobj = newobj.substring(0, newobj.length() - 1);
            }

            newobj += "}";
            
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid) + "/attendees");
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setDoOutput(true);
            con.setRequestMethod("POST");
            con.setRequestProperty("Accept", "application/json");
            con.setRequestProperty("Content-Type", "application/json");
            OutputStreamWriter out = new OutputStreamWriter(con.getOutputStream());
            out.write(newobj);
            out.close();
            
            String json = EnvelopeConverter.conJSON(con);
            outcome = EnvelopeConverter.jsonToOutcomeAttendee(json);
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            con.disconnect();
        } catch (ProtocolException e) {
            outcome = new OutcomeAttendee("Something went wrong");
        } catch (IOException e) {
            outcome = new OutcomeAttendee("Incorrect parameters");
        }
        return outcome;
    }
    
    @Override
    public OutcomeSimple postAttendees(Integer cid, Attendee[] all){
        OutcomeSimple outcome = null;
        if (cid == null || all == null) {
            throw new RuntimeException("No conference CID or attendees specified");
        }
        try {
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid) + "/attendees");
            OutcomeSimple os = new OutcomeSimple();
            
            for (Attendee a : all){
                String firstName = a.firstName, lastName = a.lastName, email = a.email;
                String newobj = "{";
                if (firstName != null)
                    newobj += "\"firstName\": \"" + firstName + "\",";

                if (lastName != null)
                    newobj += "\"lastName\": \"" + lastName + "\",";

                if (email != null)
                    newobj += "\"email\": \"" + email + "\",";

                if (newobj.endsWith(",")){
                    newobj = newobj.substring(0, newobj.length() - 1);
                }
                newobj += "}";
                
                try {
                    HttpURLConnection con = (HttpURLConnection)url.openConnection();
                    con.setDoOutput(true);
                    con.setRequestMethod("POST");
                    con.setRequestProperty("Accept", "application/json");
                    con.setRequestProperty("Content-Type", "application/json");
                    OutputStreamWriter out = new OutputStreamWriter(con.getOutputStream());
                    out.write(newobj);
                    out.close();

                    String json = EnvelopeConverter.conJSON(con);
                    if (con.getResponseCode() > 300) {
                        os.cat("\nAttendee with email " + email + " could not be added.");
                    }
                    else {
                        os.cat("\nNew attendee added with email: " + email + ", first name: " + firstName + ","
                                + "last name: " + lastName);
                    }
                    con.disconnect();
                }
                catch(IOException e){
                    os.cat("\nAttendee with email " + email + " could not be added.");
                }
            }
            return os;  
            
        } catch (IOException e) {
            outcome = new OutcomeSimple("Incorrect parameters");
        }
        return outcome;
    }
    
    @Override
    public OutcomeAttendee putAttendee(Integer cid, String firstName, String lastName, String email, String newEmail){
        OutcomeAttendee outcome = null;
        if (cid == null || email == null) {
            throw new RuntimeException("No conference CID or attendee email");
        }
        try {
            String newobj = "{";
            if (firstName != null)
                newobj += "\"firstName\": \"" + firstName + "\",";

            if (lastName != null)
                newobj += "\"lastName\": \"" + lastName + "\",";

            if (newEmail != null){
                newobj += "\"email\": \"" + newEmail + "\",";
            }
            else {
                newobj += "\"email\": \"" + email + "\",";
            }

            if (newobj.endsWith(",")){
                newobj = newobj.substring(0, newobj.length() - 1);
            }

            newobj += "}";
            
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid) + "/attendees/" + email);
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setDoOutput(true);
            con.setRequestMethod("PUT");
            con.setRequestProperty("Accept", "application/json");
            con.setRequestProperty("Content-Type", "application/json");
            OutputStreamWriter out = new OutputStreamWriter(con.getOutputStream());
            out.write(newobj);
            out.close();
            
            String json = EnvelopeConverter.conJSON(con);
            outcome = EnvelopeConverter.jsonToOutcomeAttendee(json);
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            con.disconnect();
        } catch (ProtocolException e) {
            outcome = new OutcomeAttendee("Something went wrong");
        } catch (IOException e) {
            outcome = new OutcomeAttendee("Incorrect parameters");
        }
        return outcome;
    }
    
    @Override
    public Attendee getConferenceAttendee(Integer cid, String email){
        Attendee at = null;
        if (cid == null) {
            throw new RuntimeException("No conference CID specified");
        }
        if (email == null) {
            throw new RuntimeException("No attendee email specified");
        }
        try {
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid) + "/attendees/" + email);
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");
            if (con.getResponseCode() > 300) {
                throw new RuntimeException("Failed: " + con.getResponseCode());
            }
            String json = EnvelopeConverter.conJSON(con);
            at = EnvelopeConverter.jsonToConferenceAttendee(json);
            con.disconnect();
        } catch (ProtocolException e) {
            System.out.println("Something went wrong");
        } catch (IOException e) {
            System.out.println("Something went really wrong");
        }
        return at;
    }
    
    @Override
    public OutcomeConference deleteConference(Integer cid){
        OutcomeConference returnval = null;
        HttpURLConnection con = null;
        
        if (cid == null) {
            throw new RuntimeException("No conference CID specified");
        }
        
        try {
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid));
            con = (HttpURLConnection)url.openConnection();
            con.setDoOutput(true);
            con.setRequestMethod("DELETE");
            con.setRequestProperty("Accept", "application/x-www-form-urlencoded");
            con.connect();
            String json = EnvelopeConverter.conJSON(con);

            if (con.getResponseCode() == 200) {
                return new OutcomeConference("Successfully deleted conference with cid: " + cid);
            }
            if (con.getResponseCode() > 300) {
                return new OutcomeConference("No such conference with cid: " + cid);
            }
            con.disconnect();
        } catch (ProtocolException e) {
            return new OutcomeConference("No such conference with cid: " + cid);
        } catch (IOException e) {
            return new OutcomeConference("No such conference with cid: " + cid);
        }
        return returnval;
    }
    
    @Override
    public OutcomeAttendee deleteAttendee(Integer cid, String email){
        OutcomeAttendee returnval = null;
        HttpURLConnection con = null;
        
        if (cid == null || email == null) {
            throw new RuntimeException("No conference CID or attendee email specified");
        }
        
        try {
            URL url = new URL("http://base:5008/conferences/" + Integer.toString(cid) + "/attendees/" + email);
            con = (HttpURLConnection)url.openConnection();
            con.setDoOutput(true);
            con.setRequestMethod("DELETE");
            con.setRequestProperty("Accept", "application/x-www-form-urlencoded");
            con.connect();
            String json = EnvelopeConverter.conJSON(con);

            if (con.getResponseCode() == 200) {
                return new OutcomeAttendee("Successfully deleted attendee with email: " + email + " in conference cid: " + cid);
            }
            if (con.getResponseCode() > 300) {
                return new OutcomeAttendee("No such resource with cid: " + cid + " and email: " + email);
            }
            con.disconnect();
        } catch (ProtocolException e) {
            return new OutcomeAttendee("No such resource with cid: " + cid + " and email: " + email);
        } catch (IOException e) {
            return new OutcomeAttendee("No such resource with cid: " + cid + " and email: " + email);
        }
        return returnval;
    }
}
