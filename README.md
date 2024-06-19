# CodeClauseInternship_ColorDetection
Lora Sender:
#include<LoRa.h>
#defineSS15
#defineRST16
#defineDIO02
String data = "Subscribe Tech Vegan";
voidsetup()
{
  Serial.begin(9600);
  while(!Serial);
  Serial.println("Sender Host");
  LoRa.setPins(SS, RST, DIO0);
  if(!LoRa.begin(433E6)){
    Serial.println("LoRa Error");
    delay(100);
    while(1);
  }
}
voidloop()
{
  Serial.print("Sending Data: ");
  Serial.println(data);
  LoRa.beginPacket();
  LoRa.print(data);
  LoRa.endPacket();
  delay(3000);
}


LORA Receiver code:
#include<LoRa.h>
#defineSS15
#defineRST16
#defineDIO02
voidsetup(){
  Serial.begin(9600);
  while(!Serial);
  Serial.println("Receiver Host");
  LoRa.setPins(SS, RST, DIO0);
  if(!LoRa.begin(433E6)){
    Serial.println("LoRa Error");
    while(1);
  }
}
voidloop(){
  int packetSize = LoRa.parsePacket();
  if(packetSize){
    Serial.print("Receiving Data: ");
    while(LoRa.available()){
      String data = LoRa.readString();
      Serial.println(data);
    }
  }
}



Color detection refers to a process of identifying the colors of objects or images using computer vision and other technologies.
Some applications: Image editing, robotics, and object recognition, etc.

This project is very simple. It uses OpenCV and Pandas modules of Python.

We analyze the color information in an image's pixels. The representation used in this project is an RGB color model which uses the intensity of the primary colors.

In Computer, a color value lies between 0 to 255.
That's 255 x 255 x 255 = 16581375 ways to define a color. 

We use pandas to read the data from the dataset and we use simple concepts of OpenCV to deal with images.

IDE: Python 3.12

Language: Python

Dataset: https://www.kaggle.com/code/mohammedlahsaini/color-detection-using-opencv/input?select=colors.csv
