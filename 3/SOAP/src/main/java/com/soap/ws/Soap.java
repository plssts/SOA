/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soap.ws;
import java.util.List;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
import javax.jws.soap.SOAPBinding.Use;

@WebService
@SOAPBinding(style = Style.DOCUMENT, use=Use.LITERAL, parameterStyle= SOAPBinding.ParameterStyle.WRAPPED)
public interface Soap {
    @WebMethod Conference[] getConferences();
    @WebMethod ConferenceEMB[] getConferencesEMB();
    @WebMethod Conference getConference(@WebParam(name = "cid") Integer cid);
    @WebMethod ConferenceEMB getConferenceEMB(@WebParam(name = "cid") Integer cid);
    @WebMethod Attendee[] getConferenceAttendees(@WebParam(name = "cid") Integer cid);
    @WebMethod Attendee getConferenceAttendee(@WebParam(name = "cid") Integer cid, @WebParam(name = "email") String email);
    
    @WebMethod OutcomeConference postConference(@WebParam(name = "title") String title,
                                                @WebParam(name = "info") String info,
                                                @WebParam(name = "date") String date);
    @WebMethod OutcomeAttendee postAttendee(@WebParam(name = "cid") Integer cid,
                                            @WebParam(name = "firstName") String firstName,
                                            @WebParam(name = "lastName") String lastName,
                                            @WebParam(name = "email") String email);
    @WebMethod OutcomeSimple postAttendees(@WebParam(name = "cid") Integer cid,
                                             @WebParam(name = "all") Attendee[] all);
    
    @WebMethod OutcomeConference putConference(@WebParam(name = "cid") Integer cid,
                                               @WebParam(name = "title") String title,
                                               @WebParam(name = "info") String info,
                                               @WebParam(name = "date") String date);
    @WebMethod OutcomeAttendee putAttendee(@WebParam(name = "cid") Integer cid,
                                            @WebParam(name = "firstName") String firstName,
                                            @WebParam(name = "lastName") String lastName,
                                            @WebParam(name = "email") String email,
                                            @WebParam(name = "newEmail") String newEmail);
    
    @WebMethod OutcomeConference deleteConference(@WebParam(name = "cid") Integer cid);
    @WebMethod OutcomeAttendee deleteAttendee(@WebParam(name = "cid") Integer cid,
                                                @WebParam(name = "email") String email);
}
