#include "config.h"

void reciveMessage();
void sendMessage(payload_t payload);
void testFunction();



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  radio.begin();
  Serial.print("<START> ");
  Serial.println(NodeId);
  radio.openReadingPipe(1,addresses[0]);
  radio.openWritingPipe(addresses[0]); 
  radio.startListening();  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(radio.available()) reciveMessage();

  //If there is new message to send - send it
  if(Serial.available()>0){ 
    String command = Serial.readStringUntil('\n');
    if(command == "<SEND>"){
        payload_t payload;
        while(!(Serial.available()>0)){}
            payload.dest = Serial.readStringUntil('\n').substring(2).toInt();
        while(!(Serial.available()>0)){}
            payload.timestemp = Serial.readStringUntil('\n').substring(2).toInt();
        while(!(Serial.available()>0)){}
          Serial.readStringUntil('\n').substring(2).toCharArray(payload.data,sizeof(payload.data));
        payload.src = NodeId;
        payload.Msg_Id = millis()
        sendMessage(payload);
    }
//    if(command == "<SET_NODE_ID>"){
//        while(Serial.available()<=0){};
//        NodeId = command.substring(13).toInt();
//        Serial.print("<CHANGE_ID> ");
//        Serial.println(NodeId);
//    }
  
  }
  
  #if defined TEST_MODE
    testFunction();
  #endif
   
  delay(100);
}


void reciveMessage(){
  payload_t payload;
  radio.read(&payload,sizeof(payload_t));
  if(!msgIdQueue.isExist(payload.Msg_Id)){
    msgIdQueue.enQueue(payload.Msg_Id);
    if(payload.dest == NodeId){                                 //If it's for me - insert to PI
      Serial.println("<NEW_MSG>");
      Serial.print("<MSG_ID> ");
      Serial.println(payload.Msg_Id);
      Serial.print("<TIMESTEMP> ");
      Serial.println(payload.timestemp);
      Serial.print("<SRC> ");
      Serial.println(payload.src);
      Serial.print("<DATA> ");
      Serial.println(payload.data);
      Serial.println("<END_MSG>");    
    }
    else{                                             //If not - check if I allready get it - if no, broadcast the message again
      radio.stopListening();
      delay(100);
      radio.write(&payload,sizeof(payload_t),1);
      delay(100);
      radio.startListening();
    }
  }

};

void sendMessage(payload_t payload){
  Serial.println(payload.dest);
  Serial.println(payload.timestemp);
  Serial.println(payload.src);
  Serial.println(payload.data);
  if(payload.dest != NodeId){
    radio.stopListening();
    delay(100);
    radio.write(&payload,sizeof(payload_t),1);
    delay(100);
    radio.startListening();  
  }
};



//void testFunction(){
//  //this massage will broadcast to all eventualy
//  if(millis() - testTimer > 5000){
//    testTimer = millis();
//    String test = "0 <GPS: 42.12 32.43>";
//    sendMessage(test);
//    delay(100);
//    test = "0 <BPM: 62>";
//    sendMessage(test);
//    delay(100);
//    test = "0 <ACC: 12 13>";
//    sendMessage(test);
//    delay(100);
//    test = "0 <EMERG: NO>";
//    sendMessage(test);
//  }
//};
