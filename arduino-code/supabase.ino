#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <ESP8266HTTPClient.h>
#include <DHT.h>

#define DHTPIN 5 // D1
#define DHTTYPE DHT11 

// Replace with your network credentials
const char* ssid     = "A72 2022";
const char* password = "bismillah";

// supabase credentials
String API_URL = "https://yawjhokrhegewvzqzcdh.supabase.co";
String API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inlhd2pob2tyaGVnZXd2enF6Y2RoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2ODk1MjA3MSwiZXhwIjoxOTg0NTI4MDcxfQ.o8-s-1FzfseqI6fGWUmULdWv6clZRJa8g3Y986nCyUY";
String TableName = "mlxkel6_uas";
const int httpsPort = 443;

// Sending interval of the packets in seconds
int sendinginterval = 1200; // 20 minutes
//int sendinginterval = 120; // 2 minutes'




HTTPClient https;
WiFiClientSecure client;
DHT dht(DHTPIN, DHTTYPE);

int h;
int t;
int m;

void setup() {
  // builtIn led is used to indicate when a message is being sent
//  pinMode(LED_BUILTIN, OUTPUT);
//  digitalWrite(LED_BUILTIN, HIGH); // the builtin LED is wired backwards HIGH turns it off

  // HTTPS is used without checking credentials 
  client.setInsecure();

  // Connect to the WIFI 
  Serial.begin(115200);
  dht.begin();
  
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  // Print local IP address
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {

   // If connected to the internet turn the Builtin led On and attempt to send a message to the database 
  if (WiFi.status() == WL_CONNECTED) {
//    digitalWrite(LED_BUILTIN, LOW); // LOW turns ON

    // Read all sensors
    h = dht.readHumidity();
    t = dht.readTemperature();
//    m = analogRead(A0);
    Serial.print("humi: ");
    Serial.println(h);
    Serial.print("temp: ");
    Serial.println(t);
    int prec, kec_angin, arah_angin;
    prec = random(0, 7);
    kec_angin = random(0, 4);
    arah_angin = random(0, 8);
    Serial.print("prec: ");
    Serial.println(prec);
    Serial.print("kec_angin: ");
    Serial.println(kec_angin);
    Serial.print("arah_angin: ");
    Serial.println(arah_angin);
    
    // Send the a post request to the server
    https.begin(client,API_URL+"/rest/v1/"+TableName);
    https.addHeader("Content-Type", "application/json");
    https.addHeader("Prefer", "return=representation");
    https.addHeader("apikey", API_KEY);
    https.addHeader("Authorization", "Bearer " + API_KEY);
    int httpCode = https.POST("{\"prestipasi\":" + String(prec)+ ",\"suhu\":"+ String(t)+",\"kelembapan\":"+ String(h)+",\"kecepatan_angin\":"+ String(kec_angin)+",\"arah_angin\":"+ String(arah_angin)+"}" );   //Send the request
    String payload = https.getString(); 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
    https.end();

    
//    digitalWrite(LED_BUILTIN, HIGH); // HIGH turns off
  }else{
    Serial.println("Error in WiFi connection");
  }
  delay(10000);  //wait to send the next request
  
}
