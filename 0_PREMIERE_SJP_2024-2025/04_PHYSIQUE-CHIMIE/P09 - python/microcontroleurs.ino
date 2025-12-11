#include <Adafruit_MAX31865.h>

void sortie_numerique() {
  while (Serial.available() < 2) {
  }
  int pin = Serial.read();
  int etat = Serial.read(); pinMode(pin, OUTPUT);
  if (etat == 1) {
    digitalWrite(pin, HIGH);
   } else {
      digitalWrite(pin, LOW);
   }
}

void entree_numerique() {
  while (Serial.available() < 1) {
  }
  int pin = Serial.read(); 
  pinMode(pin, INPUT); 
  Serial.write(digitalRead(pin));
}

void sortie_analogique() {
  while (Serial.available() < 2) { 
  }
  int pin = Serial.read();
  int val = Serial.read(); 
  pinMode(pin, OUTPUT); 
  analogWrite(pin, val);
}

void entree_analogique() {
  while (Serial.available() < 1) { 
  }
  int pin = Serial.read();
  int val = analogRead(pin);
  Serial.write((val>>8)&0xFF); 
  Serial.write(val & 0xFF); 
}

void son() {
  while (Serial.available() < 5) {
  }
  int pin = Serial.read();
  int freq1 = Serial.read();
  int freq2 = Serial.read();
  int duree1 = Serial.read();
  int duree2 = Serial.read();
  unsigned int freq = 256*freq1 + freq2;
  unsigned int duree = 256*duree1 + duree2;
  if (freq == 0) {noTone(pin);}
  else if (duree == 0) {tone(pin,freq);}
  else {tone(pin,freq,duree);}
}

void module_us() {
  while (Serial.available() <2){
  }
  int echo = Serial.read();
  int trig = Serial.read();
  // envoie une impulsion
  pinMode(trig, OUTPUT);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  // écoute de l'écho
  pinMode(echo, INPUT);
  unsigned int duree = pulseIn(echo, HIGH);
  Serial.write((duree>>8) & 0xFF);
  Serial.write(duree & 0xFF);
}

void pt100() {
  while (Serial.available() < 4) {
  }
  int cs = Serial.read();
  int di = Serial.read();
  int doo = Serial.read();
  int clk = Serial.read();
  Adafruit_MAX31865 max = Adafruit_MAX31865(cs,di,doo,clk);
  max.begin(MAX31865_2WIRE);
  unsigned int rtd = max.readRTD();
  Serial.write((rtd>>8)&0xFF);
  Serial.write(rtd & 0xFF);
}

void setup() {
  Serial.begin(115200); // un octet transmis en 86 µs
  Serial.flush();
  Serial.write(0);
}

void loop() {
  if (Serial.available()) {
    int index = Serial.read();
    if (index == 1) {
      sortie_numerique();
      }
      else if (index == 2) { 
        entree_numerique();
      }
      else if (index == 3) {
        sortie_analogique();
      }
      else if (index == 4) {
        entree_analogique();
      }
      else if (index == 5) {
        son();
      }
      else if (index == 6) {
        module_us();
      }
      else if (index == 7) {
      pt100(); 
      }
  }
}
