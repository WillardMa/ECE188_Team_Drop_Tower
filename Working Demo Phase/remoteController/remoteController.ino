#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>


HTTPClient http;
String URL = "http://172.16.0.1:8001/Control_Panel_API/command"; //API URL
//add respective parameter values.
String FGURL = URL + "?cmd=ground";
String F1URL = URL + "?cmd=floor1";
String F2URL = URL + "?cmd=floor2";
String DROPURL = URL +"?cmd=drop";

void setup()
{
  Serial.begin(9600);
//  while (!Serial.available());  //Wait Serial data to be sent to start
//  while (Serial.available())
//    Serial.read();  //flush the serial data buffer  
//    
//  Serial.println();
  Serial.println("Serial Established");
  WiFi.begin("team 7", "12345678");

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());

  attachInterrupt(digitalPinToInterrupt(D1), F2callback, FALLING);
  attachInterrupt(digitalPinToInterrupt(D2), F1callback, FALLING);
  attachInterrupt(digitalPinToInterrupt(D5), FGcallback, FALLING);
  attachInterrupt(digitalPinToInterrupt(D6), DROPcallback, FALLING);
  
}

//int httpCode;
//String payload;
//bool oneTime = false;

String button = "";
void loop() {
    if (button != "") {   // if button changed
      if (button == "floor ground") {
        http.begin(FGURL);
        sendGET();
        http.end();
      }

      else if (button == "floor 1") {
        http.begin(F1URL);
        sendGET();
        http.end();
      }

      else if (button == "floor 2") {
        http.begin(F2URL);
        sendGET();
        http.end();
      }

      else if (button == "drop") {
        http.begin(DROPURL);
        sendGET();
        http.end();
      }
      
      button = "";  //Reset for next button press
      reattachInterrupts(); //Enable button presses
      
    }
}

void sendGET() {
  int httpCode = http.GET();
  if (httpCode > 0) {
    delay(1000);
    String payload = http.getString();

    Serial.println("Get request to " + URL);
    Serial.println("Payload:");
    Serial.println(payload);
    }
    else {
      Serial.println("what");
      Serial.println(httpCode);
    }
}

void FGcallback() {
  detachInterrupts(); //Makes sure that button presses are disabled until button execution finishes
  Serial.println("Button on DIO5 Triggered");
  button = "floor ground";
}
void F1callback() {
  detachInterrupts(); //Makes sure that button presses are disabled until button execution finishes
  Serial.println("Button on DIO2 Triggered");
  button = "floor 1";
}
void F2callback() {
  detachInterrupts(); //Makes sure that button presses are disabled until button execution finishes
  Serial.println("Button on DIO1 Triggered");
  button = "floor 2";
}
void DROPcallback() {
  detachInterrupts(); //Makes sure that button presses are disabled until button execution finishes
  Serial.println("Button on DIO6 Triggered");
  button = "drop";
}

void detachInterrupts() {
  detachInterrupt(digitalPinToInterrupt(D1));
  detachInterrupt(digitalPinToInterrupt(D2));
  detachInterrupt(digitalPinToInterrupt(D5));
  detachInterrupt(digitalPinToInterrupt(D6));
  
}

void reattachInterrupts() {
  attachInterrupt(digitalPinToInterrupt(D1), FGcallback, FALLING);
  attachInterrupt(digitalPinToInterrupt(D2), F1callback, FALLING);
  attachInterrupt(digitalPinToInterrupt(D5), F2callback, FALLING);
  attachInterrupt(digitalPinToInterrupt(D6), DROPcallback, FALLING);
}

  
