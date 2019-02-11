#include "config.h"

void reciveMessage();
void sendMessage(String str);
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
    String command = Serial.readString();
    if(command.indexOf("<SEND>") != -1){
      while(Serial.available()<=0){};
      String str = Serial.readString(); 
      sendMessage(str);
    }
    if(command.indexOf("<SET_NODE_ID>") != -1){
        Serial.println(command);
        while(Serial.available()<=0){};
        NodeId = Serial.readString().toInt();
        Serial.print("<CHANGE_ID> ");
        Serial.println(NodeId);
    }
  
  }
  
  #if defined TEST_MODE
    testFunction();
  #endif
   
  delay(100);
}


void reciveMessage(){
  payload_t payload;
  radio.read(&payload,sizeof(payload_t));
  uint8_t dest = payload.data[0] - '0';
  if(!msgIdQueue.isExist(payload.Msg_id)){
    msgIdQueue.enQueue(payload.Msg_id);
    if(dest == NodeId){                                 //If it's for me - insert to PI
      Serial.println("<NEW_MSG>");
      Serial.print("<MSG_ID> ");
      Serial.println(payload.Msg_id);
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

void sendMessage(String str){
  if(str[0]-'0' != NodeId){
    radio.stopListening();
    delay(100);
    payload_t payload;
    str.toCharArray(payload.data,sizeof(payload.data));
    payload.Msg_id = millis();
    payload.src = NodeId;
    radio.write(&payload,sizeof(payload_t),1);
    delay(100);
    radio.startListening();  
  }
};



void testFunction(){
  //this massage will broadcast to all eventualy
  if(millis() - testTimer > 5000){
    testTimer = millis();
    String test = "0 <GPS: 42.12 32.43>";
    sendMessage(test);
    delay(100);
    test = "0 <BPM: 62>";
    sendMessage(test);
    delay(100);
    test = "0 <ACC: 12 13>";
    sendMessage(test);
    delay(100);
    test = "0 <EMERG: NO>";
    sendMessage(test);
  }
};
