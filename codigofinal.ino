#include <Servo.h>                
char nombre[10]= "BatCar";
char velocidad = "4";//9600
char pin[5]= "0000";

Servo servo1;                    

int izqA = 5; 
int izqB = 6; 
int derA = 9; 
int derB = 10; 
int vel = 255;            
int estado = 'c';         

int pecho = 2;           
int ptrig = 3;            
int duracion, distancia;  

const int Trigger = 3;   
const int Echo = 2;   

void setup()  { 
  Serial.begin(9600);    
  pinMode(derA, OUTPUT);
  pinMode(derB, OUTPUT);
  pinMode(izqA, OUTPUT);
  pinMode(izqB, OUTPUT);
  
  pinMode(pecho, INPUT);    
  pinMode(ptrig,OUTPUT);   
  pinMode(13,OUTPUT);

  servo1.attach(11,660,1400);    
                                 

  pinMode(Trigger, OUTPUT); 
  pinMode(Echo, INPUT);  
  digitalWrite(Trigger, LOW);                              
} 

void loop()  { 

  long t; 
  long d; 

  digitalWrite(Trigger, HIGH);
  delayMicroseconds(10);          
  digitalWrite(Trigger, LOW);
  
  t = pulseIn(Echo, HIGH); 
  d = t/59;             
  
  Serial.print("Distancia: ");
  Serial.print(d);      
  Serial.print(" cm");
  Serial.println();
  delay(100);          
  
  
  
  if(Serial.available()>0){        
    estado = Serial.read();
  }
  if(estado=='a'){           
    analogWrite(derB, 0);     
    analogWrite(izqB, 0); 
    analogWrite(derA, vel);  
    analogWrite(izqA, vel);       
  }
  if(estado=='b'){          
    analogWrite(derB, 0);     
    analogWrite(izqB, 0); 
    analogWrite(derA, 0);  
    analogWrite(izqA, vel);      
  }
  if(estado=='c'){         
    analogWrite(derB, 0);     
    analogWrite(izqB, 0); 
    analogWrite(derA, 0);    
    analogWrite(izqA, 0); 
  }
  if(estado=='d'){         
    analogWrite(derB, 0);     
    analogWrite(izqB, 0);
    analogWrite(izqA, 0);
    analogWrite(derA, vel);  
  } 

  if(estado=='e'){          
    analogWrite(derA, 0);    
    analogWrite(izqA, 0);
    analogWrite(derB, vel);  
    analogWrite(izqB, vel);      
  }
  
  if (estado =='f'){               
  
     digitalWrite(ptrig, HIGH);   
     delay(0.01);
     digitalWrite(ptrig, LOW);
     
     duracion = pulseIn(pecho, HIGH);          
     distancia = (duracion/2) / 29;            
     delay(10); 
     
     if (distancia <= 15 && distancia >=2){    
        digitalWrite(13,HIGH);                 
        
        analogWrite(derB, 0);             
        analogWrite(izqB, 0); 
        analogWrite(derA, 0);    
        analogWrite(izqA, 0); 
        delay (200);
        
        analogWrite(derB, vel);          
        analogWrite(izqB, vel); 
        delay(500);           
        
        analogWrite(derB, 0);            
        analogWrite(izqB, 0); 
        analogWrite(derA, 0);  
        analogWrite(izqA, vel);  
        delay(600);
        
        digitalWrite(13,LOW);
     }
     else{                            
         analogWrite(derB, 0);     
         analogWrite(izqB, 0); 
         analogWrite(derA, vel);  
         analogWrite(izqA, vel); 
     }
  }
  if(estado=='g'){                   
    servo1.write(30);              
    delay(1000);                    

    servo1.write(90);                 
    delay(700);                      
 
    servo1.write(150);               
    delay(700);  
  }

    if(estado=='h'){                 
    digitalWrite(13,1);        
  }
      if(estado=='m'){           
    digitalWrite(13,0);        
  }
    if(estado=='i'){           
    digitalWrite(derB,1);        
  }
    if(estado=='n'){           
    digitalWrite(derB,0);        
  }
    if(estado=='j'){           
    digitalWrite(derA,1);        
  }
    if(estado=='o'){           
    digitalWrite(derA,0);        
  }
    if(estado=='k'){           
    digitalWrite(izqB,1);        
  }
    if(estado=='p'){           
    digitalWrite(izqB,0);        
  }
    if(estado=='l'){           
    digitalWrite(izqA,1);        
  }
    if(estado=='q'){           
    digitalWrite(izqA,0);        
  }
  
}
